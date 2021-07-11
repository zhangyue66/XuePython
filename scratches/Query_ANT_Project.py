from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import json
import copy
from bson.objectid import ObjectId

uri = "mongodb://m02128:044a23cadb567653eb51d4eb40acaa88@ant19-ate02.atve.mobilephone.net:27017/pronghorn?authSource=admin"
try:
    client = MongoClient(host=uri,replicaset="rsantdb")
except ConnectionFailure as err:
    print("you are facing a connection error :" + err)


with client:

    db = MongoClient(uri).get_database("execution_mgmt")
    collection = db['ATE_Test_Execution_Metadata']
    yz = collection.count_documents({})
    #"testcase_name":"213409_S1HO_woSGW_Data_IMS_V4_V6
    #Target label  "label" : [ "BF_P1"]
    #execution between 2019.1.1 and 2020.1.1
    label_query = {"start_time":{"$gt":1546300800000},"start_time":{"$lte":1577836800000}}
    #label_query = {"testcase_name":"213409_S1HO_woSGW_Data_IMS_V4_V6"}

    project_dict= {}

    vnf_dict = {}

    project = ["Neo","Sundance","FirstNet","BlackFox","BlackBird"]
    vnf = ["Navigation_MCC_Proxy","Browsing","Application"]

    new_file1 = open("project.json","w")
    new_list = []  # each element is an dictionary
    new_file2 = open("vnf.json","w")

    for x in collection.find(label_query):
        if "parameter_list" in x:
            new_list.append(x["parameter_list"])

    for parameter in new_list:
        for _ in parameter:
            pro = _.get("value")
            if pro and pro in project:
                if pro not in project_dict:
                    project_dict[pro] = 1
                else:
                    project_dict[pro] +=1

            vnf_node = _.get("value")
            if vnf_node and vnf_node in vnf:
                if vnf_node not in vnf_dict:
                    vnf_dict[vnf_node] = 1
                else:
                    vnf_dict[vnf_node] += 1

    json.dump(project_dict,new_file1)
    json.dump(vnf_dict,new_file2)

    new_file1.close()
    new_file2.close()
    print("Done!")









