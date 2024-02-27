from django.shortcuts import render
from django.http import HttpRequest
from django.conf import settings
import json

# Create your views here.
def render_map(request: HttpRequest):
    context = {
        "API_KEY": settings.MAPS_API_KEY,
        "positions": json.dumps([
            {"lat": -25.344, "lng": 131.031},
            {"lat": -29.344, "lng": 132.031}
            ])
    }
    return render(request, "map.html", context=context)

    