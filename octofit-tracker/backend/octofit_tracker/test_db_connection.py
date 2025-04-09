from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

# Test database connection with detailed error handling
try:
    client = MongoClient('localhost', 27018)
    db = client['octofit_db']
    collections = db.list_collection_names()
    print("Collections in octofit_db:", collections)
    
    # Test direct insertion into MongoDB
    try:
        db.users.insert_one({"_id": "test_user", "username": "test", "email": "test@example.com", "password": "test123"})
        print("Inserted test user into users collection.")
        collections = db.list_collection_names()
        print("Collections after insertion:", collections)
    except Exception as e:
        print("Error during direct insertion:", e)
except ConnectionFailure as cf:
    print("Connection failed:", cf)
except Exception as e:
    print("An error occurred:", e)
