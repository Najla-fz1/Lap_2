from django.db import models

class Address(models.Model):
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.city
    
class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.ForeignKey('Address', on_delete=models.CASCADE)


class Address2(models.Model):
    city = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.city}"

class Student2(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    addresses = models.ManyToManyField(Address2, related_name='students')

    def __str__(self):
        return self.name
    
class StudentProfile(models.Model):
    student = models.OneToOneField('Student2', on_delete=models.CASCADE, related_name='profile')
    profile_image = models.ImageField(upload_to='profile_images/')

    def __str__(self):
        return f"Profile of {self.student.name}"
