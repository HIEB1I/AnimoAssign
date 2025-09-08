from pymongo import MongoClient

uri = "mongodb+srv://rafaeldebelen:animo123@cluster0.yjavtx7.mongodb.net/"
client = MongoClient(uri)

try:
    client.admin.command("ping")
    print("Connected successfully")

    for i in client.list_database_names():
        print(i)

    client.close()
except Exception as e:
    raise Exception("The following error occurred: ", e)