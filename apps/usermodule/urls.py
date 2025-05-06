from django.urls import path
from . import views

urlpatterns = [
    # path('data/', views.create_sample_data),
    path('students-per-city/', views.student_count_by_city),
    path('students/', views.student_list, name='student_list'),
    path('students/add/', views.student_add, name='student_add'),
    path('students/<int:student_id>/edit/', views.student_edit, name='student_edit'),
    path('students/<int:student_id>/delete/', views.student_delete, name='student_delete'),
    #task 2 
    path('students2/', views.student2_list, name='student2_list'),                
    path('students2/add/', views.student2_add, name='student2_add'),
    path('students2/<int:student_id>/edit/', views.student2_edit, name='student2_edit'),
    path('students2/<int:student_id>/delete/', views.student2_delete, name='student2_delete'),
    #-----------------------------------------------------------------------------------------
    path('profile/add/', views.add_student_profile, name='add_student_profile'),
    path('profile/list/', views.list_student_profiles, name='list_student_profiles'),
    #----------------- lab 12 --------------------------------
    path('register/',views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home, name='home'),
]
