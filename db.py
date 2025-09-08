from pymongo import MongoClient

uri = "mongodb+srv://rafaeldebelen:animo123@cluster0.yjavtx7.mongodb.net/"
client = MongoClient(uri)

try:
    client.admin.command("ping")
    print("Connected successfully")

    for i in client.list_database_names():
        print(i)

    db = client['animoAssigndb']

    print("\nanimoAssigndb Collections:")
    for collection_name in db.list_collection_names():
        print(collection_name)

    client.close()
except Exception as e:
    raise Exception("The following error occurred: ", e)