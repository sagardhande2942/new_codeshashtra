from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [ 
    path('', views.index),
    path('register/', views.register_user),
    path('login/', views.login_user),
    path('delete/worker/<int:pk>', views.DestroyWorkerAPI.as_view()),
    path('delete/contractor/<int:pk>', views.DestroyContractorAPI.as_view()),
    path('delete/owner/<int:pk>', views.DestroyOwnerAPI.as_view()),
    path('edit/worker/<str:wid>', views.UpdateWorkerAPI.as_view()),
    path('edit/contractor/<int:pk>', views.UpdateContractorAPI.as_view()),
    path('edit/owner/<int:pk>', views.UpdateOwnerAPI.as_view()),
    path('get/worker/<str:mob>', views.WorkerRetrieveAPI.as_view()),
    path('get/contractor/<str:mob>', views.ContractorRetrieveAPI.as_view()),
    path('get/owner/<str:mob>', views.OwnerRetrieveAPI.as_view()),
    path('detect/contractor/<str:cid>', views.CheckContractorPhoto),
    path('detect/worker/<str:wid>', views.CheckWorkerPhoto),
    path('safetydetect/<str:wid>', views.SafetyIdentification),
    path('mapload/<str:cid>', views.MapLoadAPI),
    path('workerundercontractor/<str:cid>', views.WorkerUnderContractorList),
    path('workersnotassigned/', views.WorkersNotAssignedAPI),
    path('workertocontractor/<str:cid>', views.WorkerToContractor),
    path('worker/aadharlink/<str:wid>',views.WorkerAadhaarLinkAPI),
]