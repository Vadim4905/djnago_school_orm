import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_school_orm.settings")
django.setup()

from home import models

def add_subject(name:str):
    models.Subject(name=name).save()
    
def add_teacher(name:str):
    models.Teacher(name=name).save()
    
def add_subject_to_teacher(subject,teacher):
    teacher.subjects.add(subject)
    
def add_class(name:str,subject:models.Subject,teacher:models.Teacher):
    models.Class(name=name, subject=subject, teacher=teacher).save()
    
def add_student(name:str,age:int):
    models.Student(name=name, age=age).save()
    
def add_student_to_class(student,_class):
    _class.add(student)
    
def add_schedule_cell(room:int,day_of_week:str,time:str,class_number:int,_class:models.Class):
    models.Student(room=room, day_of_week=day_of_week, time=time, class_number=class_number, _class=_class ).save()
    

def main():
    while 1:
        print("""
              1 - add subject
              2 - add teacher
              3 - add subject to teacher
              4 - add class
              5 - add student to class
              6 - add student
              7 - add schedule cell
              8 - get teacher schedule
              9 - get student schedule
              10 - get room schedule
              0 - exit
              """)
        ans = int(input(': '))
        match ans:
            case 1:
                name = input('name: ')
                add_subject(name)
            case 2:
                name = input('name: ')
                add_teacher(name)
            case 3:
                subject = models.Subject.objects.get(id=int(input('subject id: ')))
                teacher = models.Teacher.objects.get(id=int(input('teacher id: ')))
                add_subject_to_teacher(subject,teacher)
            case 4:
                name = input('name: ')
                subject = models.Subject.objects.get(id=int(input('subject id: ')))
                teacher = models.Teacher.objects.get(id=int(input('teacher id: ')))
                add_class(name,subject,teacher)
            case 5:
                student = models.Student.objects.get(id=int(input('student id: ')))
                _class = models.Class.objects.get(id=int(input('class id: ')))
                add_student_to_class(student,_class)
            case 6:
                name = input('name: ')
                age = input('age: ')
                add_student(name,age)
            case 7:
                room = int(input('room: '))
                day_of_week = input('day of week MON-FRI: ')
                time = input('time: ')
                class_number = int(input('class number: '))
                _class = models.Class.objects.get(id=int(input('class id: ')))
                add_schedule_cell(room,day_of_week,time,class_number,_class)
            case 8:
                pass
            case 9:
                pass
            case 10:
                pass
            case 0:
                break


if __name__=='__main__':
    main()