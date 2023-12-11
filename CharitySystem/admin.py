from django.contrib import admin
from .models import CLUB, donation_request , donation_request_view

# Register your models here.

admin.site.register(CLUB)

admin.site.register(donation_request)

admin.site.register(donation_request_view)