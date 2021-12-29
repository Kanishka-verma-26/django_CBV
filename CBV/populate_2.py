import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','CBV.settings')

import django
django.setup()

## fake pop script
import random
from cbv_app.models import School, Student
from faker import Faker
from random import randint


fakegen = Faker()
skl = ['Delhi Public School','Nutan Vidya Mandir','Green Fields','Green Way','Kendra Vidyalaya', 'St. Jones']

# def add_topic():
#     print('random choice:- ',random.choice(skl))
#     t=School.objects.get_or_create(name=random.choice(skl))[0]
#     t.save()
#     return t

# def populate(N=5):
#     for entry in range(N):
#         try:
#             top = add_topic()
#         except Exception as er:
#             print("exception:- ",er)
#
#         #creating fake data for the netry
#         fake_pname = fakegen.name()
#         fake_loc = fakegen.address()
#         fake_name = fakegen.name()
#         fake_age = randint(30, 70)
#         # fake_school = fakegen.company()
#
#
#         school = School.objects.get_or_create(principle=fake_pname, name=top, location=fake_loc)[0]
#
#         student = Student.objects.get_or_create(age=fake_age, school=school, name=fake_name)[0]
#

def school_add(N=6):
    for i in range(6):
        fake_pname = fakegen.name()
        fake_loc = fakegen.address()
        fake_name = skl[i]
        school = School.objects.get_or_create(principle=fake_pname, name=fake_name, location=fake_loc)

def student_add():
    for i in range(40):
        fake_name = fakegen.name()
        fake_age = randint(10,20)
        fake_sname = School.objects.get_or_create(name=random.choice(skl))[0]
        fake_sname.save()
        student = Student.objects.get_or_create(age=fake_age, school=fake_sname, name=fake_name)[0]


if __name__=='__main__':
    print("populating script!")
    student_add()
    print("populating complete!")