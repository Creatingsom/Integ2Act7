from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_students),
    path('dashboard/', views.student_data),
    path('form/', views.add_student_form),
]