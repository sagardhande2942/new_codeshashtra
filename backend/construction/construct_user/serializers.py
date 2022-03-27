from dataclasses import field
from .models import Worker, Contractor, Owner
from rest_framework import serializers

class WorkerRegister(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = ['first_name','last_name', 'mob','pwd', 'role', 'wid']

class ContractorRegister(serializers.ModelSerializer):
    class Meta:
        model = Contractor
        fields = ['first_name','last_name', 'mob','pwd', 'role', 'cid']
        

class OwnerRegister(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ['first_name','last_name', 'mob','pwd', 'role', 'oid']

class WorkerEdit(serializers.ModelSerializer):

    class Meta:
        model = Worker
        fields = ['wid', 'first_name', 'last_name', 'pwd', 'mob', 'dob', 
        'aadhar_card_photo', 'email', 'photo_url', 'aadhar_number', 'sex',
        'address_line1', 'address_line2', 'address_line3', 'role']

class ContractorEdit(serializers.ModelSerializer):

    class Meta:
        model = Contractor
        fields = ['cid', 'first_name', 'last_name', 'pwd', 'mob', 'dob', 
        'aadhar_card_photo', 'email', 'photo_url', 'aadhar_number', 'sex',
        'address_line1', 'address_line2', 'address_line3', 'role']


class OwnerEdit(serializers.ModelSerializer):

    class Meta:
        model = Owner
        fields = ['oid', 'mob', 'first_name', 'pwd', 'last_name', 'role']