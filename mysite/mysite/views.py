#Author: Fred Westhead
from django.shortcuts import render
from django.http import HttpResponse
# Can add more views here. I think these are all the ones the navbar links to ? 
def home(request):
    return render(request, 'home.html')
def base(request):
    return render(request, 'mysite/base.html')
def settings(request):
    return render(request, 'settings.html')
def leaderboard(request):
    return render(request, 'leaderboard.html')
def challenges(request):
    return render(request, 'challenges.html')
def login(request):
    return render(request, 'login.html')