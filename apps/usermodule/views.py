from django.shortcuts import render
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