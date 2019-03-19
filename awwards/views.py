from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

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

def index(request):
    projects = Project.objects.all()
    return render(request, 'index.html', {"date": date,"projects": projects})
