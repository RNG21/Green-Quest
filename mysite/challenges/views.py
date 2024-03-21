import json
from typing import Iterable

from django.shortcuts import render
from django.http import HttpRequest
from django.conf import settings

from db.models import Task, User, TaskType, Location

def task_view(request, task_id):
    # method used to send task data to html
    task = Task.objects.get(id=task_id)  # 获取特定任务
    context = {'task': task}
    return render(request, 'myapp/Task_chinese.html', context)

def add_challenge(request: HttpRequest) -> None:
    task_name, task_des, location_name = request.POST["task_name"], request.POST["task_des"], request.POST["location"]
    
    location = Location.objects.get(name=location_name)
    TaskType(task_name, task_des, location).save()


def render_map(request: HttpRequest, tasks: Iterable[Task]=...):
    tasks = Task.objects.all()
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
        "center": json.dumps(settings.MAPS_CENTER_COORDINATES),
        "is_admin": True
    }
    return render(request, "challenges/map.html", context=context)
