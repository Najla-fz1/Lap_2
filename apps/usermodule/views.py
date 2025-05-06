from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from .models import Address, Student
from django.db.models import Count
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

from django.contrib.auth.decorators import login_required

# def create_sample_data(request):
#     Address.objects.all().delete()
#     Student.objects.all().delete()
#     return HttpResponse("Sample data has been created!")

@login_required(login_url='/users/login')
def student_count_by_city(request):
    city_counts = Address.objects.annotate(student_count=Count('student'))
    return render(request, 'students_per_city.html', {'city_counts': city_counts})


from .forms import StudentForm

@login_required(login_url='/users/login')
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students_list.html', {'students': students})

@login_required(login_url='/users/login')
def student_add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})

@login_required(login_url='/users/login')
def student_edit(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_form.html', {'form': form})

@login_required(login_url='/users/login')
def student_delete(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'confirm_delete.html', {'student': student})

#--------------------------------------------------------------------- task 2 

from .models import Student2
from .forms import Student2Form

@login_required(login_url='/users/login')
def student2_list(request):
    students = Student2.objects.all()
    return render(request, 'student2_list.html', {'students': students})


@login_required(login_url='/users/login')
def student2_add(request):
    if request.method == 'POST':
        form = Student2Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student2_list')
    else:
        form = Student2Form()
    return render(request, 'student2_form.html', {'form': form, 'title': 'Add Student'})

@login_required(login_url='/users/login')
def student2_edit(request, student_id):
    student = get_object_or_404(Student2, pk=student_id)
    if request.method == 'POST':
        form = Student2Form(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student2_list')
    else:
        form = Student2Form(instance=student)
    return render(request, 'student2_form.html', {'form': form, 'title': 'Edit Student'})

@login_required(login_url='/users/login')
def student2_delete(request, student_id):
    student = get_object_or_404(Student2, pk=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('student2_list')
    return render(request, 'student2_confirm_delete.html', {'student': student})

from .forms import StudentProfileForm


from .models import StudentProfile

@login_required(login_url='/users/login')
def add_student_profile(request):
    if request.method == 'POST':
        form = StudentProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_student_profile')  
    else:
        form = StudentProfileForm()
    return render(request, 'add_student_profile.html', {'form': form})

@login_required(login_url='/users/login')
def list_student_profiles(request):
    profiles = StudentProfile.objects.all()
    return render(request, 'list_student_profiles.html', {'profiles': profiles})

#--------------------------------- lap 12


# users/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required


# Register View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully registered!')
            return redirect('/users/login') 
        else:
            messages.error(request, 'Registration failed. Please try again.')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


from django.contrib import messages

# Login View
def login_view(request):
    list(messages.get_messages(request))  
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, 'Login successfully!')
            return redirect('/users/home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Logout View
def logout_view(request):
    auth_logout(request)
    list(messages.get_messages(request))  
    messages.success(request, 'You have been logged out.')
    return redirect('/users/login')




# Home View
@login_required(login_url='/users/login')
def home(request):
    return render(request, 'home.html')



