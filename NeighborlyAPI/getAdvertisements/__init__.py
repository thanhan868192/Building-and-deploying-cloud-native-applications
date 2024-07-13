import os
import azure.functions as func
import pymongo
import json
from bson.json_util import dumps

def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        url = os.getenv("MONGO_CONNECTION_STRING", "")  # TODO: Update with appropriate MongoDB connection information
        client = pymongo.MongoClient(url)
        database = client[os.getenv("MONGO_DB_NAME", "")]
        collection = database['advertisements']


        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except:
        print("could not connect to mongodb")
        return func.HttpResponse("could not connect to mongodb",
                                 status_code=400)

