def get_database():
  
  # Add a condition here:
  # If in dev environment run the usual stuff
  # If in test environment use a test db
  
  import pymongo
  from pymongo import MongoClient
  import certifi
  

  MONGODB_URI = "mongodb+srv://noah:noah@cluster0.3msix.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

  client = MongoClient(MONGODB_URI, tlsCAFile=certifi.where())

  return client["en_croissant"]

if __name__ == "__main__":
  import json
  database = get_database()
  
  user_collection = database['users']
  user_file = open("user_data.json")
  user_data = json.load(user_file)
  user_collection.insert_many(user_data)

# After importing the json files generate a schema in Atlas
