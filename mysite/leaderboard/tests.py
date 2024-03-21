from django.test import TestCase

from db.models import LeaderboardEntry, User
#TODO: Add tests for the leaderboard app + fix the failing tests.
class LeaderboardEntryTest(TestCase):
    def setUp(self):

        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.assertTrue(User.objects.filter(username='testuser').exists())
'''        self.entry = LeaderboardEntry.objects.create(user=self.user, score=100)

    def test_leaderboard_entry_creation(self):
         self.assertEqual(self.entry.score, 100)
         self.assertEqual(self.entry.user, self.user)

    def test_leaderboard_entry_str(self):
         self.assertEqual(str(self.entry), f"LeaderboardEntry {self.entry.id}")
'''