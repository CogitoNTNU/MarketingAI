import pymongo as db
from src.config import Config


# print(Config().MONGO_DB_API_KEY)
# db_client = db.MongoClient("mongodb+srv://sverre:cogito@cogitontnupropagandaai.zy5j9mf.mongodb.net/?retryWrites=true&w=majority")


from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://sverre:cogito@cogitontnupropagandaai.zy5j9mf.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# print(db_client.list_database_names())
# # db = db_client[]
# # collection = db.create_collection("test")
# # collection.insert_one({"test": "test"})

# db_client.close()
