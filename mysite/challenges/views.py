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
    cookies = request.COOKIES
    tasks = cookies.get("location")
    if tasks is not None:
        tasks = {
            "name": cookies["task_name"],
            "description": cookies["task_des"],
            "location": "Forums"
        }

        positions = [
            {
                "lat": 50.735259873632835,
                "lng": -3.5336820973566327
            }
        ]

    else:
        positions = []

    context = {
        "menu_items": tasks,
        "API_KEY": settings.MAPS_API_KEY,
        "positions": json.dumps(positions),
        "center": json.dumps(settings.MAPS_CENTER_COORDINATES),
        "is_admin": True
    }
    return render(request, "challenges/map.html", context=context)

    