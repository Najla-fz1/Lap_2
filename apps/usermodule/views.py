from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from .models import Address, Student
from django.db.models import Count

# def create_sample_data(request):
#     Address.objects.all().delete()
#     Student.objects.all().delete()
#     return HttpResponse("Sample data has been created!")

def student_count_by_city(request):
    city_counts = Address.objects.annotate(student_count=Count('student'))
    return render(request, 'students_per_city.html', {'city_counts': city_counts})


from .forms import StudentForm

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students_list.html', {'students': students})

def student_add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})

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

def student_delete(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'confirm_delete.html', {'student': student})

#--------------------------------------------------------------------- task 2 

from .models import Student2
from .forms import Student2Form

def student2_list(request):
    students = Student2.objects.all()
    return render(request, 'student2_list.html', {'students': students})


def student2_add(request):
    if request.method == 'POST':
        form = Student2Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student2_list')
    else:
        form = Student2Form()
    return render(request, 'student2_form.html', {'form': form, 'title': 'Add Student'})

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

def student2_delete(request, student_id):
    student = get_object_or_404(Student2, pk=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('student2_list')
    return render(request, 'student2_confirm_delete.html', {'student': student})

from .forms import StudentProfileForm


from .models import StudentProfile

def add_student_profile(request):
    if request.method == 'POST':
        form = StudentProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_student_profile')  
    else:
        form = StudentProfileForm()
    return render(request, 'add_student_profile.html', {'form': form})

def list_student_profiles(request):
    profiles = StudentProfile.objects.all()
    return render(request, 'list_student_profiles.html', {'profiles': profiles})