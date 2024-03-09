from django.db import models

# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=100)
    

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subjects = models.ManyToManyField('Subject',related_name='teachers')

class Class(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField('Student',related_name='classes')
    subject = models.ForeignKey('Subject',on_delete=models.CASCADE,related_name='classes')
    teacher = models.ForeignKey('Teacher',on_delete=models.CASCADE,related_name='classes')
    
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    
    
class Schedule_cell(models.Model):
    class Day(models.TextChoices):
        monday = "monday", "monday"
        tuesday = "tuesday", "monday"
        wednsday = "wednsday", "monday"
        thursday = 'thursday', 'wednsday'
        friday =  'friday', 'friday'

    room = models.IntegerField()
    day_of_week = models.CharField(choices=Day.choices,max_length=100)
    time = models.TimeField()
    class_number = models.IntegerField()
    _class = models.ForeignKey('Class',on_delete=models.CASCADE ,related_name='schedule_cells')
    
    
    