from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'address']


from .models import Student2, Address2

class Student2Form(forms.ModelForm):
    class Meta:
        model = Student2
        fields = ['name','age','addresses']
        widgets = {
            'addresses': forms.CheckboxSelectMultiple(), 
        }

class Address2Form(forms.ModelForm):
    class Meta:
        model = Address2
        fields = ['city']

from .models import StudentProfile

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['student', 'profile_image']



