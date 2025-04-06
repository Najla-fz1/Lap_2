from django.shortcuts import render
from django.http import HttpResponse
from .models import Address, Student
from django.db.models import Count

def create_sample_data(request):
    Address.objects.all().delete()
    Student.objects.all().delete()

    # Create addresses
    Address.objects.bulk_create([
        Address(city="New York"),
        Address(city="Los Angeles"),
        Address(city="Chicago"),
        Address(city="Houston"),
        Address(city="Phoenix"),
    ])

    addresses = Address.objects.all()
    
    # Create students
    Student.objects.bulk_create([
        Student(name="Alice Johnson", age=20, address=addresses[0]),
        Student(name="Bob Smith", age=22, address=addresses[1]),
        Student(name="Charlie Brown", age=21, address=addresses[2]),
        Student(name="Diana Prince", age=19, address=addresses[3]),
        Student(name="Ethan Hunt", age=23, address=addresses[4]),
        Student(name="Bob Smith", age=22, address=addresses[1]),
        Student(name="Charlie Brown", age=21, address=addresses[2]),
        Student(name="Diana Prince", age=19, address=addresses[3]),
        Student(name="Ethan Hunt", age=23, address=addresses[4]),
        
    ])

    return HttpResponse("Sample data has been created!")

def students_per_city(request):
    city_counts = Address.objects.annotate(student_count=Count('student'))
    return render(request, 'students_per_city.html', {'city_counts': city_counts})