import json
from typing import Iterable
import datetime

from django.shortcuts import render
from django.http import HttpRequest
from django.conf import settings

from leaderboard.models import LeaderboardEntry
from db.models import Task, User, TaskType, Location, CompleteTask

def task_view(request, task_id):
    # method used to send task data to html
    task = Task.objects.get(id=task_id)
    context = {'task': task}
    return render(request, 'myapp/Task_chinese.html', context)


def completed_challenge(request: HttpRequest) -> None:
    CompleteTask(
        user=request.user, 
        task=Task.objects.get(id=request.POST["task_id"]), 
        image=request.POST["image"],
        latitude=request.POST["lat"],
        longtitude=request.POST["lng"],
        completion_date=datetime.datetime.now()
    ).save()


def render_map(request: HttpRequest, tasks: Iterable[Task]=Task.objects.all()):
    if request.method == "POST":
        completed_challenge(request)

    positions = [
        {
            "lat": task.location.longtitude,
            "lng": task.location.latitude
        } for task in tasks
    ]

    context = {
        "menu_items": tasks,
        "API_KEY": settings.MAPS_API_KEY,
        "positions": json.dumps(positions),
        "center": json.dumps(settings.MAPS_CENTER_COORDINATES)
    }
    return render(request, "challenges/map.html", context=context)
