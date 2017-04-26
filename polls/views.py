from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


#this is the index veiw this is the main site will show the polls.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")