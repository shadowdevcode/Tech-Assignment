from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import CustomerSession, Customer
from .serializer import SendOtpDao, ConfirmOtpDao, CustomerDto, UpdateCustomerDao
import requests
import random
import datetime
from .middleware import CustomerPermission


# Create your views here.


def send_otp(phone):
    phone = int(phone)
    if phone:
        key = str(random.randint(999, 9999))
        link = "https://2factor.in/API/R1/?module=TRANS_SMS&apikey=45b0c18b-a7dd-11e9-ade6-0200cd936042&to={}&from=SMSHMJ&templatename=SMSFAMPAY&var1=&var2={}".format(
            phone, key
        )
        requests.get(link)
        return key


class SendOtpView(APIView):
    def post(self, request):
        attributes = SendOtpDao(data=request.data)
        if not attributes.is_valid():
            return Response(attributes.errors, status=status.HTTP_400_BAD_REQUEST)

        customer = Customer.objects.filter(
            phone_number=attributes.validated_data["phone_number"],
            country_code=attributes.validated_data["country_code"],
        ).first()
        if not customer:
            customer = Customer.objects.create(**attributes.validated_data)

        otp = send_otp(customer.phone_number)
        customer.otp = otp
        customer.otp_send_on = datetime.datetime.utcnow()
        customer.save()

        return Response({"message": "otp sent successfully"})


class ConfirmOtpView(APIView):
    def post(self, request):
        attributes = ConfirmOtpDao(data=request.data)
        if not attributes.is_valid():
            return Response(attributes.errors, status=status.HTTP_400_BAD_REQUEST)

        customer = Customer.objects.filter(
            phone_number=attributes.validated_data["phone_number"],
            country_code=attributes.validated_data["country_code"],
        ).first()
        if not customer:
            return Response({"message": "invalid customer"})

        if customer.otp != attributes.validated_data["otp"]:
            return Response({"message": "invalid otp"})

        if customer.otp_send_on <= (
            datetime.datetime.utcnow() - datetime.timedelta(seconds=120)
        ):
            return Response({"message": "otp expired"})

        session = CustomerSession.objects.create(customer_id=customer.id)

        data = {"customer": CustomerDto(customer).data, "token": session.token}
        return Response({"message": "otp sent successfully", "data": data})


class CustomerView(APIView):
    permission_classes = (CustomerPermission,)

    def put(self, request):
        attributes = UpdateCustomerDao(data=request.data)
        if not attributes.is_valid():
            return Response(attributes.errors, status=status.HTTP_400_BAD_REQUEST)

        Customer.objects.filter(id=request.customer_id).update(
            **attributes.validated_data
        )

        return Response({"message": "customer updated successfully"})


class CustomerLogoutView(APIView):
    permission_classes = (CustomerPermission,)

    def delete(self, request):
        CustomerSession.objects.filter(token=request.token).delete()
        return Response({"message": "session deleted successfully"})
