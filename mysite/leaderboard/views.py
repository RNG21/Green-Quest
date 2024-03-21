from typing import Dict

from django.shortcuts import render
from django.http import HttpRequest

from db.models import CompleteTask

def sort_dict_by_value(dict: Dict, max_len: int=10):
    return {k: v for i, (k, v) in enumerate(sorted(dict.items(), reverse=True, key=lambda item: item[1])) if i<max_len}

def leaderboard(request: HttpRequest):
    entries = CompleteTask.objects.all()

    # Sum scores by user and faculty
    user_scores = {}
    faculty_scores = {}
    for entry in entries:
        user = entry.user

        # Add key if not already exist
        if not user_scores.get(user.username):
            user_scores[user.username] = 0
        if not faculty_scores.get(user.faculty):
            faculty_scores[user.faculty] = 0
        
        # Sum scores
        user_scores[user.username] += entry.score
        faculty_scores[user.faculty] += entry.score

    user_scores = sort_dict_by_value(user_scores)
    faculty_scores = sort_dict_by_value(faculty_scores)

    try:
        first = next(iter(faculty_scores))
    except:
        first = ""

    context = { 
        "student_entries": user_scores,
        'faculty_entries': faculty_scores,
        'overall_winner': first,
    }
    return render(request, 'leaderboard.html', context)