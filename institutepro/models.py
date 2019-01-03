from django.db import models
from multiselectfield import MultiSelectField
from .porter import *


class RegistrationData(models.Model):
    username = models.TextField(max_length=20, unique=True)
    email = models.EmailField(max_length=30)
    password1 = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)
    mobile  = models.BigIntegerField()
    # dob =models.DateField()
    def __str__(self):
        return self.password1



class ApplicantData(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    mobile = models.BigIntegerField()
    courses = MultiSelectField(max_length=100, choices=COURSE__CHOICES)
    startdate = models.DateField()
    timings = MultiSelectField(max_length= 100 , choices=TIMING__CHOICES)



class FeedbackData(models.Model):
    name = models.CharField(max_length= 20)
    rating = models.IntegerField()
    datetime = models.DateTimeField()
    feedback = models.CharField(max_length=2000)




class Page(models.Model):
    title = models.CharField(max_length=20)
    permalink = models.CharField(unique=True ,max_length=20)
    update_date = models.DateTimeField('last_updated')

    def __str__(self):
        return  self.title



class CompanyAddress(models.Model):
    company_name= 'Zulfiqar'
    plot_no = models.CharField(max_length=30)
    block_name = models.CharField(max_length=30)
    street_name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    district= models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country =models.CharField(max_length=30)

    def __str__(self):
        return  self.city




