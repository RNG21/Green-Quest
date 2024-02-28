import json
from typing import Iterable

from django.shortcuts import render
from django.http import HttpRequest
from django.conf import settings

from db.models import Task


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
        "center": json.dumps(settings.MAPS_CENTER_COORDINATES)
    }
    return render(request, "challenges/map.html", context=context)

    