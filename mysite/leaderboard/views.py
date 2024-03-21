from django.shortcuts import render
from db.models import CompleteTask

def leaderboard(request):
    entries = CompleteTask.objects.all()

    faculty_entries = {}
    for entry in entries:
        faculty = entry.user.faculty
        if faculty not in faculty_entries:
            faculty_entries[faculty] = []
        faculty_entries[faculty].append(entry)
        faculty_entries[faculty].sort(key=lambda x: x.score, reverse=True)

    overall_entries = [entry for faculty_entries_list in faculty_entries.values() for entry in faculty_entries_list]
    overall_entries.sort(key=lambda x: x.score, reverse=True)
    overall_winner = overall_entries[0] if overall_entries else None
        
    context = { 
        'faculty_entries': faculty_entries,
        'overall_winner': overall_winner,
    }
    return render(request, 'leaderboard.html', context)