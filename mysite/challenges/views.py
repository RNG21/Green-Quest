import json
from typing import Iterable

from django.shortcuts import render
from django.http import HttpRequest
from django.conf import settings

from leaderboard.models import LeaderboardEntry
from db.models import Task, User, TaskType, Location

def completed_challenge(request: HttpRequest) -> None:
    username = request.POST["username"]
    score = request.POST["score"]

    user = User.objects.get(username=username)
    LeaderboardEntry(user=user, score=score).save()

def add_challenge(request: HttpRequest) -> None:
    task_name, task_des, location_name = request.POST["task_name"], request.POST["task_des"], request.POST["location"]
    
    location = Location.objects.get(name=location_name)
    TaskType(task_name, task_des, location).save()


def render_map(request: HttpRequest, tasks: Iterable[Task]=...):
    tasks = Task.objects.all()
    positions = [
        {
            "lat": task.taskType.location.longitude,
            "lng": task.taskType.location.latitude
        } for task in tasks
    ]
    context = {
        "menu_items": tasks,
        "API_KEY": settings.MAPS_API_KEY,
        "positions": json.dumps(positions),
        "center": json.dumps(settings.MAPS_CENTER_COORDINATES),
        "is_admin": True
    }
    return render(request, "challenges/map.html", context=context)

    