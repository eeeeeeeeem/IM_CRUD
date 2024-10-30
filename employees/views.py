# employees/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee, Department, DepartmentHistory
from .forms import EmployeeForm, DepartmentForm, DepartmentHistoryForm

# Employee Views
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees/employee_list.html', {'employees': employees})

def employee_create(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employees/employee_form.html', {'form': form})

def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employees/employee_form.html', {'form': form})

def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == "POST":
        employee.delete()
        return redirect('employee_list')
    return render(request, 'employees/employee_confirm_delete.html', {'employee': employee})

# Department Views
def department_list(request):
    departments = Department.objects.all()
    return render(request, 'employees/department_list.html', {'departments': departments})

def department_create(request):
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm()
    return render(request, 'employees/department_form.html', {'form': form})

def department_update(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == "POST":
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'employees/department_form.html', {'form': form})

def department_delete(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == "POST":
        department.delete()
        return redirect('department_list')
    return render(request, 'employees/department_confirm_delete.html', {'department': department})

# Department History Views
def department_history_list(request):
    history = DepartmentHistory.objects.all()
    return render(request, 'employees/department_history_list.html', {'history': history})

def department_history_create(request):
    if request.method == "POST":
        form = DepartmentHistoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department_history_list')
    else:
        form = DepartmentHistoryForm()
    return render(request, 'employees/department_history_form.html', {'form': form})

def department_history_update(request, pk):
    history = get_object_or_404(DepartmentHistory, pk=pk)
    if request.method == "POST":
        form = DepartmentHistoryForm(request.POST, instance=history)
        if form.is_valid():
            form.save()
            return redirect('department_history_list')
    else:
        form = DepartmentHistoryForm(instance=history)
    return render(request, 'employees/department_history_form.html', {'form': form})

def department_history_delete(request, pk):
    history = get_object_or_404(DepartmentHistory, pk=pk)
    if request.method == "POST":
        history.delete()
        return redirect('department_history_list')
    return render(request, 'employees/department_history_confirm_delete.html', {'history': history})
