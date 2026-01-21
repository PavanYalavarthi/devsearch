from django.shortcuts import render

from .models import Profile

# Create your views here.
def profiles(request):
    users = Profile.objects.all()
    return render(request, 'profiles.html', {'users': users})

def userProfile(request, pk):
    userObj = Profile.objects.get(id=pk)
    return render(request, 'profile.html', {'user': userObj })