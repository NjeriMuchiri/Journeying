from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#our homepage view
def home(request):
    return HttpResponse('This is our homepage')

#our chamber method view 
def chamber(request):
    return HttpResponse('This is our chamber of blogging')