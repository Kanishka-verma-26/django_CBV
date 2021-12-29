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

# def add_topic():
#     t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]
#     t.save()
#     return t

def populating(N=5):
    for entry in range(N):
        # top = add_topic()

        #creating fake data for the netry
        fake_pname = fakegen.name()
        # print(fakegen.__init__())
        fake_loc = fakegen.address()
        fake_name = fakegen.name()
        fake_age = randint(30,70)
        fake_school  = fakegen.company()

        # create a fake record for that school
        try:
            school = School.objects.get_or_create(principle=fake_pname, name=fake_school, location=fake_loc)[0]
            print(school)
            print("Type of school",type(school))
        except Exception as er:
            print(er)

        #create the new student entry
        try:
            student = Student.objects.get_or_create(age=fake_age,school=school,name=fake_name)[0]
        except Exception as e:
            print("Err while creating student:- ",e)


if __name__=='__main__':
    print("populating script!")
    populating(20)
    print("populating complete!")
