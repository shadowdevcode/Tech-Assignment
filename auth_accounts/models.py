from django.db import models
import os
import hashlib
import string
import random

# Create your models here.


class Customer(models.Model):
    """Implementing Customer Model"""

    phone_number = models.CharField(max_length=255)
    country_code = models.IntegerField(default=0)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    birth_date = models.DateField(default=None, null=True)
    you_are = models.CharField(max_length=20, default=None, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    otp = models.IntegerField(default=0)
    last_login_on = models.DateTimeField(default=None, null=True)
    otp_send_on = models.DateTimeField(default=None, null=True)
    # Reference Code Logic Implementation
    # TODO : Declare reference code | ref_code & reference bonus | ref_bonus
    ref_code = models.CharField(max_length=255, blank=True, unique=True)
    ref_bonus = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.ref_code = "".join(
                random.choices(string.ascii_uppercase + string.digits, k=5)
            )
        super(Customer, self).save(*args, **kwargs)

    def __str__(self):
        return (
            self.first_name
            + " "
            + self.last_name
            + " used referral code = {} ".format(self.ref_code)
        )


class Referral(models.Model):
    referrer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="referrer"
    )
    referee = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="referee"
    )
    create_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.referee, self.referrer


class CustomerSession(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    token = models.CharField(max_length=64, default=None)
    created_on = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        token = str(hashlib.sha1(os.urandom(128)).hexdigest())
        self.token = token
        super(CustomerSession, self).save(*args, **kwargs)

    def __str__(self):
        return self.token + " " + "created on = {}".format(self.created_on)
