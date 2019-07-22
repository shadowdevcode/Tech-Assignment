from django.urls import path
from .views import (
    SendOtpView,
    ConfirmOtpView,
    CustomerView,
    CustomerLogoutView,
    VerifyReferralCodeView,
)

app_name = "auth_accounts"
urlpatterns = [
    path("send/otp", SendOtpView.as_view(), name="send_otp"),
    path("verify/otp", ConfirmOtpView.as_view(), name="confirm_otp"),
    path("customer", CustomerView.as_view(), name="customer_view"),
    path("customer/logout", CustomerLogoutView.as_view(),
         name="customer_logout_view"),
    path("verify/referral", VerifyReferralCodeView.as_view(), name="verify_referral"),
]
