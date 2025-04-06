from django.urls import path
from . import views

urlpatterns = [
    path('data/', views.create_sample_data),
    path('students-per-city/', views.students_per_city),
]