from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'base.html')

def Home1(request):
    return render(request,'landing.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def ragi(request):
    return render(request,'ragistion.html')

def log(request):
    return render(request,'login.html')


