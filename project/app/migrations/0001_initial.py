# Generated by Django 5.2 on 2025-04-15 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student_name', models.CharField(max_length=50)),
                ('Student_email', models.EmailField(max_length=254)),
                ('Student_contact', models.IntegerField()),
                ('Student_description', models.CharField(max_length=201)),
                ('Student_DOB', models.DateField()),
                ('Student_Education', models.CharField(max_length=50)),
                ('Student_Gender', models.CharField(max_length=50)),
                ('Student_Image', models.ImageField(upload_to='image/')),
                ('Student_Resume', models.FileField(upload_to='file/')),
                ('Student_Password', models.CharField(max_length=50)),
            ],
        ),
    ]
