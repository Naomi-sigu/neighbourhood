from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    current_user = request.user
    return render (request, 'home.html')

@login_required
def profile(request):
  current_user = request.user
  return render(request,'profile.html') 
 