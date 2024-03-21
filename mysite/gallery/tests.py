import json
from django.http import HttpRequest
from django.test import TestCase
from django.contrib.auth.models import User
from db.models import Like, CompleteTask
from .views import render_gallery

class RenderGalleryTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.task = CompleteTask.objects.create(user=self.user, score=1, image='images/test.jpg')

    def test_render_gallery_post_with_authenticated_user(self):
        request = HttpRequest()
        request.method = 'POST'
        request.user = self.user
        request.POST['like'] = self.task.id

        response = render_gallery(request)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"total_likes": 1, "is_liked": True, "status": "ok"})

    def test_render_gallery_post_with_unauthenticated_user(self):
        request = HttpRequest()
        request.method = 'POST'
        request.user = User()
        request.POST['like'] = self.task.id

        response = render_gallery(request)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"total_likes": 0, "is_liked": False, "status": "ok"})

    def test_render_gallery_post_with_existing_like(self):
        Like.objects.create(CompleteTask=self.task, user=self.user)

        request = HttpRequest()
        request.method = 'POST'
        request.user = self.user
        request.POST['like'] = self.task.id

        response = render_gallery(request)