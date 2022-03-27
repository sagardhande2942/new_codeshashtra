from msilib.schema import Class
from operator import truediv
from statistics import mode
from tkinter import Widget
from django.db import models
from datetime import datetime

# Create your models here.

roles = [
    ('Worker', 'Worker'),
    ('Contractor', 'Contractor'),
    ('Owner', 'Owner')
]

class Worker(models.Model):
    id = models.AutoField(primary_key=True)
    wid = models.CharField(max_length=200, null=True)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    pwd = models.CharField(max_length=200, null=True)
    mob = models.CharField(max_length=10, null=True)
    dob = models.DateField(null=True)
    aadhar_card_photo = models.CharField(max_length = 200, null=True)
    email = models.EmailField(null = True)
    photo_url = models.CharField(max_length=200, null = True)
    aadhar_number = models.CharField(max_length=200, null=True)
    sex = models.CharField(max_length=1,null=True)
    address_line1 = models.CharField(max_length=200, null = True)
    address_line2 = models.CharField(max_length=200, null=True)
    address_line3 = models.CharField(max_length=200, null=True)
    role = models.CharField(max_length=50, choices=roles)

    def __str__(self):
        return str(self.first_name + " " + str(self.wid))

class Contractor(models.Model):
    id = models.AutoField(primary_key=True)
    cid = models.CharField(max_length=200, null=True)
    first_name = models.CharField(max_length=200, null=True)
    mob = models.CharField(max_length=10, null=True)
    pwd = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    dob = models.DateField(null=True)
    aadhar_card_photo = models.CharField(max_length=200, null=True)
    email = models.EmailField(null = True)
    photo_url = models.CharField(max_length=200, null = True)
    aadhar_number = models.CharField(max_length=200, null=True)
    sex = models.CharField(max_length=1,null=True)
    address_line1 = models.CharField(max_length=200, null = True)
    address_line2 = models.CharField(max_length=200, null=True)
    address_line3 = models.CharField(max_length=200, null=True)
    role = models.CharField(max_length=50, choices=roles)

    def __str__(self):
        return str(self.first_name + " " + self.cid)

class Owner(models.Model):
    id = models.AutoField(primary_key=True)
    oid = models.CharField(max_length=200, null=True)
    mob = models.CharField(max_length=10, null=True)
    first_name = models.CharField(max_length=200, null=True)
    pwd = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    role = models.CharField(max_length=50, choices=roles)

    def __str__(self):
        return str(self.first_name + " " + str(self.oid))


class Site(models.Model):
    id = models.AutoField(primary_key=True)
    sid = models.CharField(max_length=200, null=True)
    latitude = models.CharField(max_length=200, null=True)
    longitude = models.CharField(max_length=200, null=True)
    location = models.CharField(max_length=200, null=True, default="Location")

    def __str__(self):
        return str(self.location + " " + str(self.sid))

class WOSMap(models.Model):
    id = models.AutoField(primary_key=True)
    wid = models.CharField(max_length=200, null=True)
    cid = models.CharField(max_length=200, null=True)
    sid = models.CharField(max_length=200, null=True)
    oid = models.CharField(max_length=200, null=True)
    status = models.BooleanField(default=0, null=True)

    def __str__(self):
        return self.wid

class Attendance(models.Model):
    id = models.AutoField(primary_key=True)
    uid = models.CharField(max_length=200, null=False)
    date = models.DateField(auto_now_add=datetime.now())
    is_present = models.BooleanField(default=1, null=True)
    start_time = models.DateTimeField(auto_now_add=datetime.now(), null=True)
    end_time = models.DateTimeField(auto_now_add=datetime.now(), null=True)
    hours = models.DecimalField(max_digits=10, decimal_places=3, default=0, null=True)

    def __str__(self):
        return self.uid

class Safety_Violation(models.Model):
    id = models.AutoField(primary_key=True)
    uid = models.CharField(max_length=200, null=False)
    timestamp = models.DateTimeField(auto_now_add=datetime.now())
    photo_url = models.CharField(max_length=200, null=True)
    latitude = models.CharField(max_length=200, null=True)
    longitude = models.CharField(max_length= 200, null=True)
    message = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.uid

class ContractorSite(models.Model):
    id = models.AutoField(primary_key=True)
    csid = models.CharField(max_length=200, null=True)
    cid = models.CharField(max_length=200, null=True)
    sid = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.csid)


class AttendanceSheet(models.Model):
    id = models.AutoField(primary_key=True)
    aid = models.CharField(max_length=200, null=True)
    photo_url = models.CharField(max_length=200, null = False)
    date = models.DateField(auto_now=datetime.now())

    def __str__(self):
        return self.aid
