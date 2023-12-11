from django import forms
from .models import CLUB, donation_request


class CLUB_form(forms.ModelForm):
    class Meta:
        model = CLUB
        fields = ('club_name', 'domain', 'head_of_club', 'contactNo', 'email', 'registration_cerificate_Trust_Society',
                  'certificate_12A', 'beneficiary_profiles')


class donation_form(forms.ModelForm):
    class Meta:
        model = donation_request
        fields = ('donation_description', 'donation_amount')
