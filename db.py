from pymongo import MongoClient
URL= "mongodb+srv://tj:tejthedevil@cluster0.7pqnko2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client= MongoClient(URL)

db= client['CDC']
collection= db['datas']
