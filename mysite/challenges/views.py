import json
from typing import Iterable
import datetime

from django.shortcuts import render
from django.http import HttpRequest
from django.conf import settings

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

    loc_tasks = {}
    positions = []
    for task in tasks:
        if task.location is None:
            task.location = Location()
            task.location.locationName = "Extras"
            task.location.longtitude = None
            task.location.latitude = None

        if str(task.location) not in loc_tasks:
            loc_tasks[str(task.location)] = []
        loc_tasks[str(task.location)].append(task)

        positions.append(
            {
                "lat": task.location.latitude,
                "lng": task.location.longtitude,
                "location_name": str(task.location)
            }
        )

    context = {
        "API_KEY": settings.MAPS_API_KEY,
        "tasks": loc_tasks,
        "positions": json.dumps(positions),
        "center": json.dumps(settings.MAPS_CENTER_COORDINATES),
    }
    return render(request, "challenges/map.html", context=context)
