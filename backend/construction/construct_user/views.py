from asyncio.windows_events import NULL
from cgitb import lookup
from os import set_inheritable
from pydoc import resolve
from unittest import installHandler
import urllib.request
from django.http import Http404, HttpResponse, QueryDict
from django.shortcuts import render
from grpc import Status
from .serializers import ContractorEdit, OwnerEdit, WorkerEdit, WorkerRegister, ContractorRegister, OwnerRegister
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .models import Attendance, ContractorSite, Safety_Violation, Worker, Contractor, Owner, WOSMap, Site
import cv2
import dlib
import face_recognition
from datetime import datetime, timedelta
from .firebase_authentication import bucket
from construct_user import firebase_authentication
import urllib.request
import requests
import shutil
from safety_detection import yolo3image
from construct_user import aadhar_OCR

def download_image(url, file_path, file_name):
    file_path = "construct_user/" + file_path + file_name + ".jpg"
    req = urllib.request.Request(url, headers={'User-Agent': 'mozilla'})
    res = urllib.request.urlopen(req)
    assert res.status == 200
    with open(file_path, 'wb') as out:
        shutil.copyfileobj(res, out)

# Create your views here.
def index(request):
    return HttpResponse("HII")


# register fname, lname, mno, pwd, roles

roles = ['Worker', 'Contractor', 'Owner']
detector = dlib.get_frontal_face_detector()
base_url = 'https://firebasestorage.googleapis.com/v0/b/construction-5054c.appspot.com/o/'

@api_view(['GET', 'POST'])
def register_user(request, *args, **kwargs):
    if request.method == "POST": 
        if request.data['role'] == '0': 
            my_dict = dict(request.data) 
            my_dict['role'] = roles[int(request.data['role'])]
            user_qs = Worker.objects.filter(mob__exact = my_dict['mob'])
            if user_qs.exists():
                return HttpResponse("Mobile Number Already Exists", status = 404)
            serializer = WorkerRegister(data = my_dict)
            if serializer.is_valid(raise_exception=True):
                instance = serializer.save()     
                qs1 = Worker.objects.get(id = instance.id)
                qs1.wid = f'w{qs1.id}'
                qs1.save()
            print(serializer)
        if request.data['role'] == '1': 
            my_dict = dict(request.data) 
            my_dict['role'] = roles[int(request.data['role'])]
            user_qs = Contractor.objects.filter(mob__exact = my_dict['mob'])
            if user_qs.exists():
                return HttpResponse("Mobile Number Already Exists", status = 404)
            serializer = ContractorRegister(data = my_dict)
            if serializer.is_valid(raise_exception=True):
                instance = serializer.save()
                qs1 = Contractor.objects.get(id = instance.id)
                qs1.cid = f'c{qs1.id}'
                qs1.save()    
            print(serializer)
        if request.data['role'] == '2': 
            my_dict = dict(request.data) 
            my_dict['role'] = roles[int(request.data['role'])] 
            user_qs = Owner.objects.filter(mob__exact = my_dict['mob'])
            if user_qs.exists():
                return HttpResponse("Mobile Number Already Exists", status = 404) 
            serializer = OwnerRegister(data = my_dict)
            if serializer.is_valid(raise_exception=True):
                instance = serializer.save()  
                qs1 = Owner.objects.get(id = instance.id)
                qs1.oid = f'c{qs1.id}'
                qs1.save()  
            print(serializer)
        
        return Response(request.data)   

@api_view(['POST'])
def login_user(request, *args, **kwargs):
    if request.method == 'POST':
        if request.data['role'] == '0':
            try:
                worker_qs = Worker.objects.get(mob = request.data['mob'])
            except: 
                return HttpResponse(request.data, status=404)
            if request.data['pwd'] == worker_qs.pwd:
                pass
            else:
                return HttpResponse(request.data, status=404)
        
        if request.data['role'] == '1':
            try:
                contractor_qs = Contractor.objects.get(mob = request.data['mob']) 
            except: 
                return HttpResponse(request.data, status=404)
            if request.data['pwd'] == contractor_qs.pwd:
                pass
            else:
                return HttpResponse(request.data, status=404)
        
        if request.data['role'] == '2':
            try:
                owner_qs = Owner.objects.get(mob = request.data['mob'])
            except: 
                return HttpResponse(request.data, status=404)
            if request.data['pwd'] == owner_qs.pwd:
                pass
            else:
                return HttpResponse(request.data, status=404)
        return Response(request.data)


# @api_view(['POST','GET'])
class UpdateWorkerAPI(generics.UpdateAPIView):
    queryset = Worker.objects.all()
    lookup_field = 'wid'
    serializer_class = WorkerEdit

# @api_view(['POST','GET'])
class UpdateContractorAPI(generics.UpdateAPIView):
    queryset = Contractor.objects.all()
    lookup_field = 'cid'
    serializer_class = ContractorEdit

# @api_view(['POST','GET'])
class UpdateOwnerAPI(generics.UpdateAPIView):
    queryset = Owner.objects.all()
    lookup_field = 'oid'
    serializer_class = OwnerEdit


# @api_view(['POST','GET'])

class DestroyWorkerAPI(generics.DestroyAPIView):
    queryset = Worker.objects.all()
    serialzier_class = WorkerEdit

# @api_view(['POST','GET'])
class DestroyContractorAPI(generics.DestroyAPIView):
    queryset = Contractor.objects.all()
    serializer_class = ContractorEdit

# @api_view(['POST','GET'])
class DestroyOwnerAPI(generics.DestroyAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerEdit


@api_view(['POST', 'GET'])
def MapLoadAPI(request, cid=None, *args, **kwargs):
    if cid == None:
        return HttpResponse("CID invalid", status=404)

    if request.method == "GET": 
        qs = ContractorSite.objects.filter(cid = cid)
        if not qs.exists():
            return Response("{}")
        outer_dict = []
        counter = 0
        for value in qs:
            counter += 1
            sid = value.sid
            qs1 = Site.objects.get(sid = sid) 
            name = qs1.location
            lat = qs1.latitude
            lon = qs1.longitude
            inner_dict = {
                "id": counter,
                "name":name,
                "lat":lat,
                "lon":lon
            }
            outer_dict.append(inner_dict)
        
        return Response(outer_dict)

    if request.method == "POST":
        s_instance = Site(location = request.data['name'], latitude = request.data['lat'], longitude = request.data['lon']).save()
        s_instance = Site.objects.last()
        s_instance = Site.objects.get(id = s_instance.id)
        sid = s_instance.sid
        s_instance.sid = f's{s_instance.id}'
        s_instance.save()
        
        cs_instance = ContractorSite(cid = cid, sid=sid).save()
        cs_instance = ContractorSite.objects.last()
        cs_instance1 = Contractor.objects.get(cid = cs_instance.cid)
        cs_instance.csid = f'cs{cs_instance.id}'
        cs_instance.save()

        return HttpResponse("Success", status = 200)

@api_view(['POST', 'GET'])
def CheckContractorPhoto(request, cid=None, *args, **kwargs):
    if cid == None:
        return HttpResponse("Invalid CID", status = 404)

    if request.method == "POST":
        # print(instance.photo_url)
        instance = Contractor.objects.get(cid = cid) 
        if instance.photo_url == None:
            instance.photo_url = request.data['image_url'] 
            instance.save()
            blob = bucket.blob("contractor/"+cid+".jpg")
            x = blob.generate_signed_url(timedelta(seconds=300), method='GET') 
            download_image(x, 'contractor/', cid)
            a_is = Attendance(uid = f'c{cid}', is_present=True, start_time=datetime.now()).save()
            return HttpResponse("Successfully uploaded", status = 200)
        else:
            #
            #   Photo Checking FROM drowsiness project
            #
            blob = bucket.blob("trash/contractor/"+cid+".jpg")
            x = blob.generate_signed_url(timedelta(seconds=300), method='GET') 
            download_image(x, 'trash/contractor/', cid)
            user_image_location = face_recognition.load_image_file(
            '{}.jpg'.format(f'construct_user/trash/contractor/{cid}'))
            user_image_encoding = face_recognition.face_encodings(user_image_location)[0]

            db_face_locations = face_recognition.load_image_file(
                '{}.jpg'.format(f'construct_user/contractor/{cid}'))
            db_face_encodings = face_recognition.face_encodings(db_face_locations)[0]

            match = face_recognition.face_distance( [user_image_encoding], db_face_encodings)
            match = match[0]
            print(match)
            if match < 0.4:
                a_is = Attendance(uid = f'c{cid}', is_present=True, start_time=datetime.now()).save()
                return HttpResponse("Success", status = 200)
            else:
                return HttpResponse("Face not match", status = 404)

@api_view(['POST', 'GET'])
def CheckWorkerPhoto(request, wid=None, *args, **kwargs):
    if wid == None:
        return HttpResponse("Invalid WID", status = 404)

    if request.method == "POST":
        # print(instance.photo_url)
        instance = Worker.objects.get(wid = wid) 
        if instance.photo_url == None:
            instance.photo_url = request.data['image_url'] 
            instance.save()
            blob = bucket.blob("worker/"+wid+".jpg")
            x = blob.generate_signed_url(timedelta(seconds=300), method='GET') 
            download_image(x, 'worker/', wid)
            a_is = Attendance(uid = f'w{wid}', is_present=True, start_time=datetime.now()).save()
            return HttpResponse("Successfully uploaded", status = 200)
        else:
            #
            #   Photo Checking FROM drowsiness project
            #
            blob = bucket.blob("trash/worker/"+wid+".jpg")
            x = blob.generate_signed_url(timedelta(seconds=300), method='GET') 
            download_image(x, 'trash/worker/', wid)
            user_image_location = face_recognition.load_image_file(
            '{}.jpg'.format(f'construct_user/trash/worker/{wid}'))
            user_image_encoding = face_recognition.face_encodings(user_image_location)[0]

            db_face_locations = face_recognition.load_image_file(
                '{}.jpg'.format(f'construct_user/worker/{wid}'))
            db_face_encodings = face_recognition.face_encodings(db_face_locations)[0]

            match = face_recognition.face_distance( [user_image_encoding], db_face_encodings)
            match = match[0]
            print(match)
            if match < 0.4:
                a_is = Attendance(uid = f'w{wid}', is_present=True, start_time=datetime.now()).save()
                return HttpResponse("Success", status = 200)
            else:
                return HttpResponse("Face not match", status = 404)



@api_view(['POST', 'GET'])
def AttendanceSheetAPI(request, cid=None, *args, **kwargs):
    if request.method == "POST":
        #
        # Attendance sheet logic
        #
        pass


class WorkerRetrieveAPI(generics.RetrieveAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerEdit
    lookup_field = 'mob'

class ContractorRetrieveAPI(generics.RetrieveAPIView):
    queryset = Contractor.objects.all()
    serializer_class = ContractorEdit
    lookup_field = 'mob'

class OwnerRetrieveAPI(generics.RetrieveAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerEdit
    lookup_field = 'mob'


@api_view(['POST', 'GET'])
def WorkerUnderContractorList(request, cid = None, *args, **kwargs):
    if cid == None:
        return HttpResponse("Cid invalid", status = 404)

    if request.method == "GET":
        qs = WOSMap.objects.all()
        my_dict = {}
        for value in qs:
            try:
                w_is = Worker.objects.get(wid = value.wid)
                i_d = {
                    "wid":value.wid,
                    "mob":w_is.mob,
                    "first_name":w_is.first_name,
                    "last_name":w_is.last_name
                }
                my_dict[value.cid].append(i_d)
            except:
                my_dict[value.cid] = []
                w_is = Worker.objects.get(wid = value.wid)
                i_d = {
                    "wid":value.wid,
                    "mob":w_is.mob,
                    "first_name":w_is.first_name,
                    "last_name":w_is.last_name
                }
                my_dict[value.cid].append(i_d)
            
        return Response(my_dict)


# @api_view(['POST', 'GET'])



# list of workers not assigned

@api_view(['POST', 'GET'])

def WorkersNotAssignedAPI(request, *args, **kwargs):
    if request.method == "GET":
        w_qs = Worker.objects.all()
        w_nassign = []
        for value in w_qs: 
            a_qs = WOSMap.objects.filter(wid = value.wid)
            if not a_qs.exists(): 
                # a_qs = a_qs.first()
                i_dict = {
                    "wid":value.wid,
                    "first_name":value.first_name,
                    "last_name":value.last_name,
                    "mob":value.mob,
                }
                w_nassign.append(i_dict)
        
        s_qs = Site.objects.all()
        s_list = []
        for value in s_qs:
            i_dict = {
                "sid":value.sid,
                "name":value.location,
                "lat":value.latitude,
                "lon":value.longitude
            }
            s_list.append(i_dict)
        final_dict = {"unassigned_workers":w_nassign, "all_sites":s_list}

        return Response(final_dict)



@api_view(['POST','GET'])
def WorkerToContractor(request, cid = None, *args, **kwargs):
    if cid == None:
        return HttpResponse("Invalid CID", status = 404)
    
    if request.method == "POST":
        my_list = request.data[cid]
        print(my_list)
        for value in my_list:
            print(value)
            WOSMap(wid=value['wid'], cid=cid, sid=value['sid'], status=0).save()
    
    return HttpResponse("Success", status=200)


@api_view(['POST', 'GET'])
def SafetyIdentification(request, wid = None, *args, **kwargs):
    if wid == None:
        return HttpResponse("WID invalid", status=404)
    
    if request.method == "POST":
        # yolo3image.yolo3("image2.jpg")
        vidcap = cv2.VideoCapture('construct_user/My_video.mp4')
        count = 0
        success = True
        fps = int(vidcap.get(cv2.CAP_PROP_FPS))
        print(fps)
        while success:
            im_path = ""
            success,image = vidcap.read()
            print('read a new frame:',success)
            if count == 0:
                cv2.imwrite('safety_detection/frame%d.jpg'%count,image)
                im_path = 'safety_detection/frame%d.jpg'%count
                print('successfully written 10th frame')
                yolo3image.yolo3(im_path)
                user_image_location = face_recognition.load_image_file(
                '{}.jpg'.format(f'construct_user/trash/worker/{wid}'))
                user_image_encoding = face_recognition.face_encodings(user_image_location)[0]

                w_qs = Worker.objects.all()
                for value in w_qs:
                    db_face_locations = face_recognition.load_image_file(
                    '{}.jpg'.format(f'construct_user/worker/{value.wid}'))
                    db_face_encodings = face_recognition.face_encodings(db_face_locations)[0]

                    match = face_recognition.face_distance( [user_image_encoding], db_face_encodings)
                    match = match[0]
                    print(match)
                    if match < 0.4:
                        imageBlob = bucket.blob("/safety_violation/")
                        imagePath = "safety_detection/frame0.jpg"  # Replace with your own path
                        imageBlob = bucket.blob("frame0.jpg")
                        imageBlob.upload_from_filename(imagePath)
                        imageBlob.make_public()
                        image_url = imageBlob.public_url
                        wos_qs = WOSMap.objects.filter(wid = wid).first()
                        site_qs = Site.objects.filter(sid = wos_qs.sid).first()
                        Safety_Violation(uid=value.wid, photo_url = image_url, latitude=site_qs.longitude, longitude=site_qs.latitude).save()

            count+=1
            if count > 2*fps + 1: 
                count = 0
            print(count)


    return HttpResponse("success", status=200)

@api_view(['POST','GET'])
def WorkerAadhaarLinkAPI(request, wid = None, *args, **kwargs):
    if wid == None:
        return HttpResponse("WID invalid", status=404)
    
    if request.method == "POST":
        photo_url = request.data['photo_url']
        blob = bucket.blob("aadhaar/worker/"+wid+".jpg")
        # x = blob.generate_signed_url(timedelta(seconds=300), method='GET') 
        download_image(photo_url, 'aadhaar/worker/', wid)
        details = aadhar_OCR.mfun(f'construct_user/aadhaar/worker/{wid}.jpg')
        date = details[0]
        number = details[1]
        gender = details[2]

        w_ins = Worker.objects.get(wid = wid)
        w_ins.aadhar_number = number
        w_ins.gender = gender
        w_ins.save()    

        # return HttpResponse("hi")

        return Response({"aadhar number" : number, "gender":gender})
