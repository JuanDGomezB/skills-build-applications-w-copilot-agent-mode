from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        marvel = Team.objects.create(name='Team Marvel')
        dc = Team.objects.create(name='Team DC')
        tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel)
        Activity.objects.create(user=tony, type='Run', duration=30)
        Workout.objects.create(name='Avengers HIIT', description='High intensity')
        Leaderboard.objects.create(user=tony, score=100)

    def test_user(self):
        self.assertEqual(User.objects.count(), 1)

    def test_team(self):
        self.assertEqual(Team.objects.count(), 2)

    def test_activity(self):
        self.assertEqual(Activity.objects.count(), 1)

    def test_workout(self):
        self.assertEqual(Workout.objects.count(), 1)

    def test_leaderboard(self):
        self.assertEqual(Leaderboard.objects.count(), 1)
