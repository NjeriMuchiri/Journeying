from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

rooms = [
    {'id': 1, 'name': 'my software engineering journey'},
    {'id': 2, 'name': 'my graphic designing journey'},
    {'id': 3, 'name': 'my entry job journey'},
]
#our homepage view
def home(request):
    context = {'rooms': rooms}
    return render(request, 'journeyingblogs/home.html', context)

#our chamber method view 
def chamber(request):
    return render(request, 'journeyingblogs/chamber.html')
