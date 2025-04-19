from django.shortcuts import render
from .models import Student

# Create your views here.

def home(request):
    return render(request,'landing.html')


def home1(request,pk):
    userdata = Student.objects.get(id=pk)
    userdta = {
                    "id":userdata.id,
                    "name":userdata.Student_name,
                    "contact":userdata.Student_contact,
                    "dis":userdata.Student_description,
                    "dob":userdata.Student_DOB,
                    "email":userdata.Student_email,
                    "image":userdata.Student_Image,
                    "file":userdata.Student_Resume,
                    "education":userdata.Student_Education,
                    "password":userdata.Student_Password,
                }
    return render(request,'home.html',{'userdata':userdata})


def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def ragi(request):
    return render(request,'ragistion.html')

def log(request):
    return render(request,'login.html')
   

def register(request):

    # print('register page')
    # print(request.method)
    # print(request.POST)
    # print(request.FILES)
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
    # print(username,email,detail,phone,dob,subscribe,gender,password,cpassword,profile,resume)

    u=Student.objects.filter(Student_email=email)
    if u:
        msg='Email already exist'
        return render(request,'ragistion.html',{'key':msg})
    else:
        if password==cpassword:
            Student.objects.create(Student_name=username,Student_email=email,Student_contact=phone,Student_description=detail,Student_DOB=dob,Student_Education=subscribe,Student_Gender=gender,Student_Image=profile,Student_Resume=resume,Student_Password=password )
            msg='gegistration done'
            return render(request,'login.html',{'keyy':msg})
        else:
            msg1='pssword and cpssword not match'
            return render(request,'ragistion.html',{'key':msg1})
        


    # Student.objects.create(Student_name=username,Student_email=email,Student_contact=phone,Student_description=detail,Student_DOB=dob,Student_Education=subscribe,Student_Gender=gender,Student_Image=profile,Student_Resume=resume,Student_Password=password )
      

def logindata(request):
    if request.method=='POST':
        email=request.POST.get('email')
        passw=request.POST.get('password')
        user=Student.objects.filter(Student_email=email)
        if user:
            userdata=Student.objects.get(Student_email=email)
            print(userdata.Student_name)
            print(userdata.Student_email)
            pass1=userdata.Student_Password
            if passw==pass1:
                msg='welcom to dashbord'
                userdata = {
                    "id":userdata.id,
                    "name":userdata.Student_name,
                    "contact":userdata.Student_contact,
                    "dis":userdata.Student_description,
                    "dob":userdata.Student_DOB,
                    "email":userdata.Student_email,
                    "image":userdata.Student_Image,
                    "file":userdata.Student_Resume,
                    "education":userdata.Student_Education,
                    "password":userdata.Student_Password,
                }
                return render(request,'dashboard.html',{'userdata':userdata})
            else:
                msg='email & password not match'
                return render(request,'login.html',{'msg':msg,'email':email})
        else:
            msg='email not registard'
            return render(request,'login.html',{'msg':msg})
    else:
        return render(request,'login.html')
    
