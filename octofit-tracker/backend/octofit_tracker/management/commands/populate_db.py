from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        self.stdout.write("Starting database population...")

        # Clear existing data
        self.stdout.write("Clearing existing data...")
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        self.stdout.write("Creating users...")
        users = [
            User(_id=ObjectId(), username='john_doe', email='john@example.com', password='password123'),
            User(_id=ObjectId(), username='jane_smith', email='jane@example.com', password='password123'),
            User(_id=ObjectId(), username='alice_wonder', email='alice@example.com', password='password123'),
        ]
        User.objects.bulk_create(users)
        self.stdout.write(f"Created {len(users)} users.")

        # Create teams
        self.stdout.write("Creating teams...")
        team1 = Team(_id=ObjectId(), name='Team Alpha')
        team2 = Team(_id=ObjectId(), name='Team Beta')
        team1.save()
        team2.save()
        team1.members.add(users[0], users[1])
        team2.members.add(users[2])
        self.stdout.write("Teams created and members added.")

        # Create activities
        self.stdout.write("Creating activities...")
        activities = [
            Activity(_id=ObjectId(), user=users[0], activity_type='Running', duration=timedelta(minutes=30)),
            Activity(_id=ObjectId(), user=users[1], activity_type='Cycling', duration=timedelta(minutes=45)),
            Activity(_id=ObjectId(), user=users[2], activity_type='Swimming', duration=timedelta(minutes=60)),
        ]
        Activity.objects.bulk_create(activities)
        self.stdout.write(f"Created {len(activities)} activities.")

        # Create leaderboard entries
        self.stdout.write("Creating leaderboard entries...")
        leaderboard_entries = [
            Leaderboard(_id=ObjectId(), user=users[0], score=100),
            Leaderboard(_id=ObjectId(), user=users[1], score=90),
            Leaderboard(_id=ObjectId(), user=users[2], score=80),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)
        self.stdout.write(f"Created {len(leaderboard_entries)} leaderboard entries.")

        # Create workouts
        self.stdout.write("Creating workouts...")
        workouts = [
            Workout(_id=ObjectId(), name='Morning Run', description='A quick morning run to start the day'),
            Workout(_id=ObjectId(), name='Evening Cycle', description='Cycling in the evening to relax'),
            Workout(_id=ObjectId(), name='Swimming Session', description='An hour of swimming practice'),
        ]
        Workout.objects.bulk_create(workouts)
        self.stdout.write(f"Created {len(workouts)} workouts.")

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
