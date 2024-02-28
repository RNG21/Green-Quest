from django.shortcuts import render
from django.http import HttpRequest
from django.conf import settings
import json

def challenge_page(request):
    context = {
        "menu_items": [1,2,3,4]
    }
    return render(request, "sidebar.html", context=context)

def render_map(request: HttpRequest):
    context = {
        "API_KEY": settings.MAPS_API_KEY,
        "positions": json.dumps([
            {"lat": -25.344, "lng": 131.031},
            {"lat": -29.344, "lng": 132.031}
            ])
    }
    return render(request, "map.html", context=context)

    