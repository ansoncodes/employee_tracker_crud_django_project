from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_form, name='employee_insert'),  # GET and POST for insert
    path('<int:id>/', views.employee_form, name='employee_update'),  # GET and POST for update
    path('delete/<int:id>/', views.employee_delete, name='employee_delete'),  # ✅ DELETE route added
    path('list/', views.employee_list, name='employee_list'),  # GET for read
]
