from django.shortcuts import render
from models import LeaderboardEntry

def leaderboard(request):
    entries = LeaderboardEntry.objects.order_by('-score')[:10]  # Get top 10 entries
    return render(request, 'leaderboard/leaderboard.html', {'entries': entries})
