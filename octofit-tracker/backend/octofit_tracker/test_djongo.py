from octofit_tracker.models import User

# Test querying the database using Djongo
try:
    users = User.objects.all()
    print(f"Number of users in the database: {users.count()}")
    for user in users:
        print(f"User: {user.username}, Email: {user.email}")
except Exception as e:
    print("Error querying the database with Djongo:", e)
