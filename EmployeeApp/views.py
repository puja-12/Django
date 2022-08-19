from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import json

from EmployeeApp.models import Employees, Departments


# Create your views here.


def department_api(request):
    print(dir(request))
    if request.method == 'GET':
        employee = Employees.objects.all()
        print(employee)

        count = employee.count()
        if count == 0:
            return JsonResponse({'message': 'data not found'})

        return JsonResponse({'message': f'{count} data found'})

    elif request.method == 'POST':

        data = json.loads(request.body)

        emp = Employees.objects.create(user_id=data.get('user'), emp_name=data.get('emp_name'), age=data.get('age'),
                                       department_id=data.get('department'))

        print(emp)

        return JsonResponse({'message': 'added successfully'})
    elif request.method == 'PUT':
        data = json.loads(request.body)
        emp = Employees.objects.get(user_id=data.get('user'))
        print(emp)
        if not emp:
            return JsonResponse({'message': 'data not found'})

        emp.emp_name = data.get('emp_name')
        emp.age = data.get('age')
        emp.department_id = data.get('department')

        emp.save()

        return JsonResponse({'message': 'updated successfully'})

    elif request.method == 'DELETE':
        data = json.loads(request.body)
        department = Employees.objects.get(user_id=data.get('user'))
        print(department)
        if not department:
            return JsonResponse({'message': 'data not found'})

        department.delete()
        return JsonResponse({'message': 'delete successfully'})



def user_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = User.objects.create_user(**data)
        return JsonResponse({'message': f"{user.username} is created"})
    return JsonResponse({'message': "method not allowed"})
