from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Chamber, Topic
from .form import ChamberForm
# Create your views here.

# chambers = [
#     {'id': 1, 'name': 'my software engineering journey'},
#     {'id': 2, 'name': 'my graphic designing journey'},
#     {'id': 3, 'name': 'my entry job journey'},
# ]
#our homepage view
def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    chambers = Chamber.objects.filter(
                                      Q(topic__name__icontains=q) | 
                                      Q(name__icontains=q) | 
                                      Q(description__icontains=q)
                                      )
    topics = Topic.objects.all()
    context = {'chambers': chambers, 'topics': topics}
    return render(request, 'journeyingblogs/home.html', context)

#our chamber method view 
def chamber(request, pk):
    chamber = Chamber.objects.get(id=pk)
    context = {'chamber': chamber}
    return render(request, 'journeyingblogs/chamber.html', context)

def createChamber(request):
    form = ChamberForm()
    if request.method == 'POST':
        form = ChamberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    context = {'form': form}
    return render(request, 'journeyingblogs/chamber_form.html', context)

def updateChamber(request, pk):
    chamber = Chamber.objects.get(id=pk)
    form = ChamberForm(instance=chamber)
    if request.method == 'POST':
        form = ChamberForm(request.POST, instance=chamber)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    context = {'form': form}
    return render(request, 'journeyingblogs/chamber_form.html', context)

def deleteChamber(request,pk):
    chamber = Chamber.objects.get(id=pk)
    if request.method == 'POST':
        chamber.delete()
        return redirect('homepage')    
    return render(request, 'journeyingblogs/delete.html', {'obj':chamber})
