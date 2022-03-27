from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Worker)
admin.site.register(Contractor)
admin.site.register(Owner)
admin.site.register(Site)
admin.site.register(Attendance)
admin.site.register(Safety_Violation) 
admin.site.register(WOSMap)   
admin.site.register(ContractorSite) 
admin.site.register(AttendanceSheet)  