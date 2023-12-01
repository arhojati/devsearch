from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def login_user(request):
    if request.user.is_authenticated:
        return redirect("profiles")
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Username does not exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("profiles")
        else:
            messages.error(request, "Username or Password is incorrect")
    return render(request, "users/login_register.html")


def logout_user(request):
    logout(request)
    messages.info(request, "User logged out")
    return redirect("login")


def register_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'User account created!')
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'An error occurred during registration!')

    page = 'register'
    form = CustomUserCreationForm()
    context = {'page': page, 'form': form}
    return render(request, 'users/login_register.html', context)


def profiles(requests):
    profiles = Profile.objects.all()
    context = {"profiles": profiles}
    return render(requests, "users/profiles.html", context)


def user_profile(requests, pk):
    profile = Profile.objects.get(id=pk)
    top_skills = profile.skill_set.exclude(description__exact="")
    other_skills = profile.skill_set.filter(description="")

    context = {
        "profile": profile,
        "top_skills": top_skills,
        "other_skills": other_skills,
    }
    return render(requests, "users/user-profile.html", context)

@login_required(login_url='login')
def user_account(request):
    profile = request.user.profile
    skills = profile.skill_set.all()
    projects = profile.project_set.all()
    context = {
        "profile": profile,
        "skills": skills,
        "projects": projects,
    }
    return render(request, 'users/account.html', context)