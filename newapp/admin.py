from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.

@admin.register(bullratio)
@admin.register(nyse)
@admin.register(feargreed)
@admin.register(putcall)
@admin.register(riskapp)
class userdata(ImportExportModelAdmin):
    pass