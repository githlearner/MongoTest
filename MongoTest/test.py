from pymongo import MongoClient

# client = MongoClient("mongodb://127.0.0.1:27017/Orchestrator")
# dbname = client.mydb
# coll = dbname.addr
#
# # mydict = [{'Name':'Githin','Age':29},{'Name':'Nighisha','Age':28},{'Name':'Diya','Age':0}]
# res = coll.find({'Name'})
# print(list(res))


client = MongoClient("mongodb://127.0.0.1:27017/Orchestrator")
displaydata = client.Orchestrator.tasks.find()

the_last = client.Orchestrator.tasks.find().sort('_id',-1).limit(1)
s = [ d for d in the_last]
print(s)

# data = [data for data in displaydata]
# print(data[0]['firstname'])

