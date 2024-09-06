from django.contrib import admin
from myapp0.models import Employee
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['e_no','e_name','id']


admin.site.register(Employee,EmployeeAdmin)
