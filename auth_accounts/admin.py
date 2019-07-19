from django.contrib import admin
from .models import CustomerSession, Customer


# Now register for Customer Session
admin.site.register(CustomerSession)
# Register for Customer
admin.site.register(Customer)
