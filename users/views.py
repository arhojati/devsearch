from django.shortcuts import render
from .models import Profile

# Create your views here.
def profiles(requests):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(requests, 'users/profiles.html', context)

def user_profile(requests, pk):
    profile = Profile.objects.get(id=pk)
    top_skills = profile.skill_set.exclude(description__exact="")
    other_skills = profile.skill_set.filter(description="")

    context = {'profile':  profile,
               'top_skills': top_skills,
               'other_skills': other_skills}
    return render(requests, 'users/user-profile.html', context)