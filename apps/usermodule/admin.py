from django.contrib import admin

from .models import Student
from .models import Address

admin.site.register(Student)
admin.site.register(Address)
