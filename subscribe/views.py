from typing import final
from django.http.response import HttpResponse
from django.shortcuts import render
from django import forms
from .forms import Subscribe
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
# Create your views here.

def subscribe_email(request):
    sub =Subscribe()
    if request.method == "POST":
        sub = Subscribe(request.POST)
        subject1 = 'Welcome to Django app'
        message1 = 'Hope you are enjoying your Django Tutorials'
        recepient = request.POST["email"]
        # print(recepient)
        final_mail_list = None
        if "," in recepient:
            final_mail_list = recepient.split(",")
        else:
            final_mail_list = [recepient]
        if final_mail_list:
            mail = EmailMessage(subject=subject1 , body=message1, from_email = settings.EMAIL_HOST_USER, to=final_mail_list)
            mail.attach_file(r"C:\Users\Ashish\Desktop\TestFileForMail.txt")
            mail.send(fail_silently=False)
        # send_mail(subject=subject1 , message=message1, from_email = settings.EMAIL_HOST_USER, recipient_list=[recepient],fail_silently = False)
        return render(request, "success.html", context= {'recepient': recepient})

    return render(request, "index.html", context= {'form1': sub})