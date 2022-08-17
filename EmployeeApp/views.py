from django.shortcuts import render
from django.http import JsonResponse
import json
from rest_framework.parsers import JSONParser

from EmployeeApp.models import Departments


# Create your views here.


def department_api(request):
    # print(dir(request))
    if request.method == 'GET':
        departments = Departments.objects.all()
        print(departments)
        count = departments.count()
        if count == 0:
            return JsonResponse({'message': 'data not found'})

        return JsonResponse({'message': f'{count} data found'})

    elif request.method == 'POST':
        data = json.loads(request.body)
        department = Departments.objects.create(department_name=data.get('name'))
        print(department)

        # return JsonResponse("Added Successfully")
        return JsonResponse({'message': 'added successfully'})
    elif request.method == 'PUT':
        data = json.loads(request.body)
        department = Departments.objects.get(id=data.get('key_id'))
        print(department)
        if not department:
            return JsonResponse({'message': 'data not found'})

        department.department_name = data.get('name')
        department.save()

        return JsonResponse({'message': 'updated successfully'})

    elif request.method == 'DELETE':
        data = json.loads(request.body)
        department = Departments.objects.get(id=data.get('key_id'))
        print(department)
        if not department:
            return JsonResponse({'message': 'data not found'})

        department.delete()
        return JsonResponse({'message': 'delete successfully'})

