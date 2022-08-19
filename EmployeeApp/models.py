from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Departments(models.Model):
    department_name = models.CharField(max_length=20)

    #
    def __str__(self):
        return str(self.department_name)


class Employees(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, )
    emp_name = models.CharField(max_length=20)
    age = models.IntegerField()
    department = models.ForeignKey(Departments, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.emp_name)
