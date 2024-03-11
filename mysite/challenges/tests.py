import json
from django.http import HttpRequest
from django.test import TestCase
from django.conf import settings
from django.test import Client
from challenges.views import render_map

class RenderMapTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_render_map_with_tasks(self):
        self.client.cookies = {"location": "Forums", "task_name": "Task 1", "task_des": "Description 1"}

        response = self.client.get("/challenges/map.html")

        self.assertEqual(response.status_code, 200)
       # self.assertEqual(response.template_name, "challenges/map.html")
        self.assertEqual(response.context["menu_items"]["name"], "Task 1")
        self.assertEqual(response.context["menu_items"]["description"], "Description 1")
        self.assertEqual(response.context["menu_items"]["location"], "Forums")
        self.assertEqual(response.context["API_KEY"], settings.MAPS_API_KEY)
        self.assertEqual(response.context["positions"], json.dumps([{"lat": 50.735259873632835, "lng": -3.5336820973566327}]))
        self.assertEqual(response.context["center"], json.dumps(settings.MAPS_CENTER_COORDINATES))
        self.assertEqual(response.context["is_admin"], True)

    def test_render_map_without_tasks(self):
        self.client.cookies = {}
        response = self.client.get("/challenges/")

        self.assertEqual(response.status_code, 200)
        #self.assertEqual(response.template_name, "challenges/map.html")
        self.assertEqual(response.context["menu_items"], {})
        self.assertEqual(response.context["API_KEY"], settings.MAPS_API_KEY)
        self.assertEqual(response.context["positions"], json.dumps([]))
        self.assertEqual(response.context["center"], json.dumps(settings.MAPS_CENTER_COORDINATES))
        self.assertEqual(response.context["is_admin"], True)