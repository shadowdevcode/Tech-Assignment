from rest_framework import serializers
from .models import Customer


class SendOtpDao(serializers.Serializer):
    phone_number = serializers.CharField(max_length=14)
    country_code = serializers.IntegerField()


class ConfirmOtpDao(serializers.Serializer):
    phone_number = serializers.CharField(max_length=14)
    country_code = serializers.IntegerField()
    otp = serializers.IntegerField()
    ref_code = serializers.CharField(max_length=50, allow_null=True)


class UpdateCustomerDao(serializers.Serializer):
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    birth_date = serializers.DateField()
    you_are = serializers.CharField(max_length=20)


class VerifyReferralCodeDao(serializers.Serializer):
    ref_code = serializers.CharField(max_length=50)


class CustomerDto(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = (
            "phone_number",
            "country_code",
            "first_name",
            "last_name",
            "birth_date",
            "you_are",
            'ref_code',
        )
