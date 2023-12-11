from django.db import models
from django_currentuser.middleware import get_current_user, get_current_authenticated_user
# Create your models here.

class CLUB(models.Model):
    club_name = models.CharField(max_length=30, blank=True)
    domain = models.CharField(max_length=20, blank=True)
    head_of_club = models.CharField(max_length=30, blank=True)
    contactNo = models.CharField(max_length=10, blank=True)
    email = models.EmailField(blank=True)
    registration_cerificate_Trust_Society = models.FileField(upload_to='verification', blank=True)
    certificate_12A = models.FileField(upload_to='verification', blank=True)
    beneficiary_profiles = models.FileField(upload_to='verification', blank=True)
    verification_status = models.BooleanField(default=None, blank=True, null=True)
    ngo_current_user = models.CharField(default=get_current_authenticated_user, blank=True, max_length=40)

    def verification_true(self):
        self.verification_status=True        
        self.save()

    def verification_false(self):
        self.verification_status = False
        self.save()

    def get_user(self,user):
        self.club_user = user
        self.save()

    def __str__(self):
        return self.ngo_name


class donation_request(models.Model):

    donation_description = models.TextField(blank=True,default=None)
    donation_amount = models.CharField(default=None,blank=True,max_length=15)
    donation_request_user = models.CharField(blank=True,default=get_current_authenticated_user,max_length=30)

    def __str__(self):
        return self.donation_amount

class donation_request_view(models.Model):
    club_name = models.CharField(default=None,max_length=50,blank=False,primary_key=True)
    domain = models.CharField(default=None,max_length=50,blank=False)
    head_of_club = models.CharField(default=None,max_length=50,blank=False)
    contactNo = models.CharField(default=None,max_length=10,blank=False)
    email = models.EmailField(blank=False,default=None)
    donation_description = models.TextField(default=None,blank=False)
    donation_amount = models.CharField(default=None,max_length=10,blank=False)

    def __str__(self):
        return self.club_name

    class Meta:
        managed = False
        db_table = 'post_request'    