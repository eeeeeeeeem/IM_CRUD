# employees/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Employee URLs
    path('employees/', views.employee_list, name='employee_list'),
    path('employees/new/', views.employee_create, name='employee_create'),
    path('employees/<int:pk>/edit/', views.employee_update, name='employee_update'),
    path('employees/<int:pk>/delete/', views.employee_delete, name='employee_delete'),

    # Department URLs
    path('departments/', views.department_list, name='department_list'),
    path('departments/new/', views.department_create, name='department_create'),
    path('departments/<int:pk>/edit/', views.department_update, name='department_update'),
    path('departments/<int:pk>/delete/', views.department_delete, name='department_delete'),

    # Department History URLs
    path('department_history/', views.department_history_list, name='department_history_list'),
    path('department_history/new/', views.department_history_create, name='department_history_create'),
    path('department_history/<int:pk>/edit/', views.department_history_update, name='department_history_update'),
    path('department_history/<int:pk>/delete/', views.department_history_delete, name='department_history_delete'),

]
