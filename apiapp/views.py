from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def employee_data(request):
    employee_data={"ename":1,"sal":200,"eaddr":300,"eloc":"chennai"}
    return JsonResponse(employee_data)
