from django.urls import path
from . import views

urlpatterns = [
    # path('data/', views.create_sample_data),
    path('students-per-city/', views.student_count_by_city),
]