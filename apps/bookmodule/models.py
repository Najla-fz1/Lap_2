from django.db import models
from django import forms

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.FloatField(default=0.0)
    edition = models.SmallIntegerField(default=1)

class Department(models.Model):
    name = models.CharField(max_length=50)

class Course(models.Model):
    title = models.CharField(max_length=50)
    code = models.CharField(max_length=500)

class Card(models.Model):
    card_number = models.CharField(max_length=20 , unique=True)
    
class Student11(models.Model):
    name = models.CharField(max_length=50)
    student_Card = models.OneToOneField(Card, on_delete=models.PROTECT)
    student_Department = models.ForeignKey(Department, on_delete=models.CASCADE)
    student_Course = models.ManyToManyField(Course)
