from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#our homepage view
def home(request):
    return render(request, 'home.html')

#our chamber method view 
def chamber(request):
    return render(request, 'chamber.html')
