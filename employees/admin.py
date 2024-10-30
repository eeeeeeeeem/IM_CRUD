# employees/admin.py
from django.contrib import admin
from .models import Department, Employee, DepartmentHistory

admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(DepartmentHistory)
