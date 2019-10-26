from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages
from .models import Profile

# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    current_user = request.user
    return render (request, 'home.html')

@login_required
def profile(request):
  current_user = request.user
  return render(request,'profile.html') 


@login_required(login_url='/accounts/login/')
def update_profile(request):
  if request.method == 'POST':
    u_form = UpdateUser(request.POST,instance=request.user)
    p_form = UpdateProfile(request.POST,request.FILES,instance=request.user.profile)
    if u_form.is_valid() and p_form.is_valid():
      u_form.save()
      p_form.save()
      messages.success(request,'Your Profile account has been updated successfully')
      return redirect('profile')
  else:
    u_form = UpdateUser(instance=request.user)
    p_form = UpdateProfile(instance=request.user.profile) 
    
  params = {
    'u_form':u_form,
    'p_form':p_form
  }
  return render(request,'update_profile.html', params)
  
 
 