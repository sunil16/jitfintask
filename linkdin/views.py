from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
def home(request):
    return JsonResponse({"key":"value"})

def fun(request):
    print(request.readlines())
    return JsonResponse({"key":request.readlines()})
