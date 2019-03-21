from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http  import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .forms import  *
from .models import *

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login')

    else:
        form = UserCreationForm()
    return render(request,'signup.html',{
        "form": form
    })

def login(request):
    return render(request, 'login.html')

def home(request):
    projects = Projects.objects.all()
    return render(request, 'home.html', {"projects": projects})

def profile(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            return redirect('profile')
            return render(request, 'profile.html')
    else:
        form = ProjectsForm()

        my_profile = Profile.objects.all()
    return render(request,'profile.html', locals())

@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'username' in request.GET and request.GET["username"]:
        search_term = request.GET.get("username")
        searched_users = User.objects.filter(username=search_term)
        message = f"{search_term}"
        profiles=  Profile.objects.all( )

        return render(request, 'search.html',{"message":message,"users": searched_users,'profiles':profiles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-posts/search.html',{"message":message})


def new_projects(request):
    current_user = request.user
    profile = Profile.objects.get(user=current_user)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = current_user
            project.profile = profile
            project.save()
        return redirect('index')

    else:
        form = ProjectsForm()
    return render(request, 'new_project.html', {"form": form})
