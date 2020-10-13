import os
import pymongo
from dotenv import load_dotenv


load_dotenv()


def connect(db_name='autodl'):
    """Connecting the MongoDB."""
    client = pymongo.MongoClient(os.getenv("Mongo"))
    db = client[db_name]
    print("MongoDB connected")
    return db


if __name__ == "__main__":
    db = connect()
