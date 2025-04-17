from django.db import models

# Create your models here.
class Student(models.Model):
    Student_name=models.CharField(max_length=50)
    Student_email=models.EmailField()
    Student_contact=models.IntegerField()
    Student_description=models.CharField(max_length=211)
    Student_DOB=models.DateField()
    Student_Education=models.CharField(max_length=40)
    Student_Gender=models.CharField(max_length=50)
    Student_Image=models.ImageField(upload_to='image/')
    Student_Resume=models.FileField(upload_to='file/')
    Student_Password=models.CharField(max_length=50)
