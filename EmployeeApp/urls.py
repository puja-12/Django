from django.template.defaulttags import url
from django.urls import path

from . import views

urlpatterns = [
    path('department_api/', views.department_api,name="department_api"),
    path('createuser/',views.user_api,name="createuser")

]
