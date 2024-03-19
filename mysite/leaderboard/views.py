from django.shortcuts import render
from models import LeaderboardEntry

def leaderboard(request):
    return render(request, 'leaderboard.html')
