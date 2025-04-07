from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'base.html')

def Home1(request):
    return render(request,'landing.html')


