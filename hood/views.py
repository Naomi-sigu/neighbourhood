from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages
from .models import Profile , Neighbourhood

# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    current_user = request.user
    hoods = Neighbourhood.get_all_hoods()
    return render (request, 'home.html', {"hoods":hoods})

@login_required
def profile(request):
  current_user = request.user
  return render(request,'profile.html') 


@login_required(login_url='/accounts/login/')
def update_profile(request):
    current_user=request.user
    if request.method=="POST":
        instance = Profile.objects.get(user=current_user)
        form =UpdateProfile(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            profile = form.save(commit = False)
            profile.user = current_user
            profile.save()

        return redirect('/')

    elif Profile.objects.get(user=current_user):
        profile = Profile.objects.get(user=current_user)
        form = UpdateProfile(instance=profile)
    else:
        form = UpdateProfile()

    return render(request,'update_profile.html',{"form":form}) 
 
@login_required(login_url='/accounts/login/')
def businesses(request):
    current_user=request.user
    profile=Profile.objects.get(user=current_user)
    businesses = Business.objects.filter(neighbourhood=profile.neighbourhood)

    return render(request,'businesses.html',{"businesses":businesses}) 