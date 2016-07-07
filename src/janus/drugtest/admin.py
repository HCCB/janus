from django.contrib import admin

from models import Patient, Physician, Staff
from models import TestCategory, Analysis
# from models import ResultMaster, ResultDetail


class AnalysisAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_name', 'category')
    list_filter = ('category', 'profiles',)


admin.site.register([Patient, Physician, Staff])
admin.site.register([TestCategory, ])

admin.site.register(Analysis, AnalysisAdmin)
