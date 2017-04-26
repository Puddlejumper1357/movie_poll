from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


#this is the index were the 
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")