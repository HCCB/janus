from django.contrib import admin

from models import Patient, Physician, Staff


admin.site.register([Patient, Physician, Staff])
