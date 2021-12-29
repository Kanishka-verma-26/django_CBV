from django.db import models
from django.urls import reverse


# Create your models here.
class School(models.Model):
    # id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=255)
    principle = models.CharField(max_length=256)
    location = models.CharField(max_length = 256)

    def __str__(self):
        # return str(self.id) + " " + str(self.name)
        return str(self.name)

    def get_absolute_url(self):
        return reverse("cbv_app:detail", kwargs={'pk':self.pk})


class Student(models.Model):
    # id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()

    # # if we pass the related_name like we did in the below LOC then we will call it as "school_detail.xyz.all" , refere school_details.html template.
    #
    # school = models.ForeignKey(School,related_name = 'xyz',on_delete=models.CASCADE)

    # if we don't pass the related_name like we did in the below LOC then we will call it as "school_detail.student_set.all" , refere school_details.html template.

    school = models.ForeignKey(School,on_delete=models.CASCADE)


    def __str__(self):
        # return str(self.id) + " " + str(self.name)
        return str(self.name)

