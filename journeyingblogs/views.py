from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from .models import Chamber, Topic, Message
from .form import ChamberForm, UserForm
# Create your views here.


# view for our login page
def ourLoginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('homepage')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does nor exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            messages.error(request, "Username OR Password doesn't exist")

    context = {'page': page}
    return render(request, 'journeyingblogs/login_register.html', context)

#view for logging a user out
def logoutUser(request):
    logout(request)
    return redirect('homepage')

#registration view
def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('homepage')
        else:
            messages.error(request, 'An error occured during registration')
    return render(request, 'journeyingblogs/login_register.html', {'form': form})

#our homepage view
def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    chambers = Chamber.objects.filter(
                                      Q(topic__name__icontains=q) | 
                                      Q(name__icontains=q) | 
                                      Q(description__icontains=q)
                                      )
    topics = Topic.objects.all()[0:4]
    chamber_count = chambers.count()
    chamber_reactions = Message.objects.filter(Q(chamber__topic__name__icontains=q))
    
    context = {'chambers': chambers, 'topics': topics,
               'chamber_count': chamber_count, 'chamber_reactions':chamber_reactions}
    return render(request, 'journeyingblogs/home.html', context)

#our chamber method view 
def chamber(request, pk):
    chamber = Chamber.objects.get(id=pk)
    chamber_messages = chamber.message_set.all()
    techiesspace = chamber.techiesspace.all()

    if request.method == 'POST':
        message = Message.objects.create(
            user=request.user,
            chamber=chamber,
            body=request.POST.get('body')
        )
        chamber.techiesspace.add(request.user)
        return redirect('chamber', pk=chamber.id)

    context = {'chamber': chamber, 'chamber_messages': chamber_messages,'techiesspace':techiesspace}
    return render(request, 'journeyingblogs/chamber.html', context)

#the user profile view
def userProfile(request, pk):
    user = User.objects.get(id=pk)
    chambers = user.chamber_set.all()
    chamber_messages = user.message_set.all()
    topics = Topic.objects.all()
    context = {'user': user, 'chambers': chambers, 'chamber_messages': chamber_messages,
               'topics': topics}
    return render(request, 'journeyingblogs/userprofile.html', context)

#creating chamber view with a decorator
@login_required(login_url='loginpage')
def createChamber(request):
    form = ChamberForm()
    topics = Topic.objects.all()
    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)

        Chamber.objects.create(
            host=request.user,
            topic=topic,
            name=request.POST.get('name'),
            description=request.POST.get('description'),            
        )
        return redirect('homepage')
    context = {'form': form, 'topics': topics}
    return render(request, 'journeyingblogs/chamber_form.html', context)

# the updating chamber view with a login required decorator
@login_required(login_url='loginpage')
def updateChamber(request, pk):
    chamber = Chamber.objects.get(id=pk)
    form = ChamberForm(instance=chamber)
    topics = Topic.objects.all()

    if request.user != chamber.host:
            return HttpResponse("You are not allowed here!")

    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)
        form = ChamberForm(request.POST, instance=chamber)
        chamber.name = request.POST.get('name')
        chamber.topic = topic
        chamber.description = request.POST.get('description')
        chamber.save()
        return redirect('homepage')
    context = {'form': form, 'topics': topics, 'chamber': chamber}
    return render(request, 'journeyingblogs/chamber_form.html', context)

#deleting chamber view
@login_required(login_url='loginpage')
def deleteChamber(request,pk):
    chamber = Chamber.objects.get(id=pk)

    if request.user != chamber.host:
            return HttpResponse("You are not allowed here!")

    if request.method == 'POST':
        chamber.delete()
        return redirect('homepage')    
    return render(request, 'journeyingblogs/delete.html', {'obj':chamber})

#deleting a message view
@login_required(login_url='loginpage')
def deleteMessage(request,pk):
    message = Message.objects.get(id=pk)

    if request.user != message.user:
            return HttpResponse("You are not allowed here!")

    if request.method == 'POST':
        message.delete()
        return redirect('homepage')    
    return render(request, 'journeyingblogs/delete.html', {'obj':message})

#updating a user view
@login_required(login_url='login')
def updateUser(request):
    user = request.user
    form = UserForm(instance=user)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user-profile', pk=user.id)
    context = {'form': form}

    return render(request, 'journeyingblogs/update-user.html', context)

#this is a view of search for topics
def topicPage(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    topics = Topic.objects.filter(name__icontains=q)
    return render(request, 'journeyingblogs/topic.html', {'topics': topics})

#this is a view of search for blog reactions
def ReactionPage(request):
    chamber_messages = Message.objects.all()
    return render(request, 'journeyingblogs/reaction.html', {'chamber_messages':chamber_messages})