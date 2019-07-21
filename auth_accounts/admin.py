from django.contrib import admin
from .models import CustomerSession, Customer, Referral


# Now register for Customer Session
admin.site.register(CustomerSession)
# Register for Customer
admin.site.register(Customer)
# Register for Referral
admin.site.register(Referral)
