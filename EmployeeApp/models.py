from django.db import models


# Create your models here.


# Create your models here.
class Departments(models.Model):
    department_name = models.CharField(max_length=20)

    def __str__(self):
        return str(self.id)


class Employees(models.Model):
    employee_name = models.CharField(max_length=200)
    Department = models.CharField(max_length=500)
    date_of_join = models.DateField()
