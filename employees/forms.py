# employees/forms.py
from django import forms
from .models import Employee, Department, DepartmentHistory

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'

class DepartmentHistoryForm(forms.ModelForm):
    class Meta:
        model = DepartmentHistory
        fields = '__all__'
