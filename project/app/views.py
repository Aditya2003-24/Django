from django.shortcuts import render
from .models import Student

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

def register(request):
    print('register page')
    print(request.method)
    print(request.POST)
    print(request.FILES)
    username=request.POST.get('username')
    email=request.POST.get('email')
    detail=request.POST.get('detail')
    phone=request.POST.get('phone')
    dob=request.POST.get('dob')
    subscribe=request.POST.getlist('subscribe')
    gender=request.POST.get('gender')
    password=request.POST.get('password')
    cpassword=request.POST.get('cpassword')
    profile=request.FILES.get('profile-pic')
    resume=request.FILES.get('resume')
    print(username,email,detail,phone,dob,subscribe,gender,password,cpassword,profile,resume)
    Student.objects.create(Student_name=username,Student_email=email,Student_contact=phone,Student_description=detail,Student_DOB=dob,Student_Education=subscribe,Student_Gender=gender,Student_Image=profile,Student_Resume=resume,Student_Password=password )
      

