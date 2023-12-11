from django.shortcuts import render, redirect, get_object_or_404
from .forms import CLUB_form , donation_form
from .models import CLUB, donation_request , donation_request_view
from django.contrib import messages
from django.core.mail import send_mail
import stripe
# Create your views here.
stripe.api_key = 'sk_test_TjwJ8KIE4pM0zUDkkubD4kvV00PipgfR59'

def header(request):
    return render(request, 'CharitySystem\header.html')


def about(request):
    return render(request, 'CharitySystem\self.html')

def club(request):
    if request.method == 'POST':
        form = CLUB_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/')
    else:
        form = CLUB_form()

    return render(request,"CharitySystem\get_verified.html",{'form':form})


def not_verified(request):
    return render(request, "CharitySystem\\not_verified.html")

def verify_from_admin(request):
    data = CLUB.objects.all()
    return render(request, "CharitySystem\\verify_from_admin.html", {'ngo':data})

def Verification_Status_True(request, pk):
    club = get_object_or_404(CLUB, pk=pk)
    club.verification_true()

    send_mail(
    'SaathiHaathBadhana | Verification Status',
    'Our admins have deemed your verification to be right.',
    'aman_22@outlook.com',
    ['heroup534@gmail.com'],
    fail_silently=False,
)

    return redirect("/mail_Y/")

def Verification_Status_False(request, pk):
    club = get_object_or_404(CLUB, pk=pk)
    club.verification_false()

    send_mail(
    'SaathiHaathBadhana | Verification Status',
    'Our admins have deemed your verification to be wrong.',
    'abascharlesbenard@gmail.com',
    ['heroup534@gmail.com'],
    fail_silently=False,
)
    return redirect("/mail_N/")

def mail_Y(request):
    return render(request, "CharitySystem\mail_Y.html")

def mail_N(request):
    return render(request, "CharitySystem\mail_N.html")

def donation(request):
    if request.method == 'POST':
        form = donation_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = donation_form()

    return render(request, "CharitySystem\\request_form.html",{'form':form})

    
def post_request(request):
    data = donation_request_view.objects.all()
    return render(request, "CharitySystem\post_request.html",{'data':data})

def payment(request):
    return render(request, 'CharitySystem\payment.html')    

def charge(request):
    if request.method == 'POST':

        cus_name = request.POST["cus_name"]
        amount = request.POST["amount"]
        donation_message = request.POST["message"]
        mail = request.POST["mail"]

        customer = stripe.Customer.create(
            email = mail,
            name = cus_name,
            source = request.POST["stripeToken"]
        )

        charge = stripe.Charge.create (
            customer = customer,
            amount = int(amount)*100,
            currency = 'INR',
            description = donation_message
        )

        return render(request, 'CharitySystem\success_payment.html',{'amount':amount})