# employees/models.py
from django.db import models

class Department(models.Model):
    department_name = models.CharField(max_length=255)

    def __str__(self):
        return self.department_name

class Employee(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    city_id = models.IntegerField()
    email = models.EmailField(max_length=255)
    employment_start = models.DateField()
    job_title_id = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class DepartmentHistory(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.employee} - {self.department}"
