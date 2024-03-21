from django.test import TestCase, Client
from .views import leaderboard

class LeaderboardTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_leaderboard(self):
        response = self.client.get('/leaderboard/')

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Assert that the response contains the expected keys in the context
        self.assertIn('student_entries', response.context)
        self.assertIn('faculty_entries', response.context)
        self.assertIn('overall_winner', response.context)

        # Assert that the response context values are of the expected types
        self.assertIsInstance(response.context['student_entries'], dict)
        self.assertIsInstance(response.context['faculty_entries'], dict)
        self.assertIsInstance(response.context['overall_winner'], str)
