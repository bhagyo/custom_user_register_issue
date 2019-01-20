from django.contrib import admin

# Register your models here.
from .models import Profile, Doctor, Patient, Doctor_1, Patient_1

admin.site.register(Profile)
admin.site.register(Doctor)
admin.site.register(Doctor_1)
admin.site.register(Patient)
admin.site.register(Patient_1)
