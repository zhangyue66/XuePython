from pymongo import MongoClient
from pymongo.errors import ConnectionFailure,DuplicateKeyError
import json
#import copy
#from bson.objectid import ObjectId

# this script will do:
# 1. query ANT_TestCase  and ANT_TestSuite with label_query on Portal #1, save the test cases to target.json file.
#2. migrate all the queried test cases and insert to Portal #2



#make sure you give URL for primary ATE mongo. if ATE mongo is secondary . it might fail  -> enhance to replicaset rsantadb
# mongo authentication password can be found in ANT portal VM . give this command  cat /apps/ant/pronghorn/properties.json
# command to find proper FQDN   hostname -f on ATE01,ATE02,ATE03
uri = "mongodb://m02128:25db67c5657914454081c6a18e93d6dd@ant24ate01.ttve.mobilephone.net:27017/pronghorn?authSource=admin"
target_uri = "mongodb://m02128:044a23cadb567653eb51d4eb40acaa88@ant19-ate02.atve.mobilephone.net/pronghorn?authSource=admin"
try:
    client = MongoClient(host=uri)

except ConnectionFailure as err:
    print("you are facing a connection error :" + err)

try:
    target_client = MongoClient(host=target_uri)
except ConnectionFailure as err1:
    print("target client can not be connected " + err1)


with target_client and client:
    # 1st get all the test case id in test suite and save it to testcase_list = []# {"testcases":[y1,y2,y3....]}
    testcase_list,testsuite_list = [],[]
    #f  = open("target.json")
    #data = json.load(f)

    #here you define your query label (same as mongo shell)
    label_query = {"DUT.value":{"$in":["RDM56E_BlackFox","RDM56D_BlackFox"]}}
    suite_query = {"DUT.value":{"$in":["RDM56E_BlackFox","RDM56D_BlackFox"]}}
    #Now get original portal ready
    db = MongoClient(uri).get_database(name="pronghorn")
    # change to any collection name per your requirement
    collection = db["ANT_TestCase"]
    suite_collection = db["ANT_TestSuite"]

    new_file = open("target.json", "w")


    #Now get target portal ready
    target_db = MongoClient(target_uri).get_database(name="pronghorn")
    target_collection = target_db["ANT_TestCase"]
    target_suite_collection = target_db["ANT_TestSuite"]

    cnt = 0
    for x in collection.find(label_query):
        testcase_list.append(x)
        try:
            target_collection.insert_one(x)
            cnt+=1
        except DuplicateKeyError:
            continue

    for _ in suite_collection.find(suite_query):
        testsuite_list.append(_)
        try:
            target_suite_collection.insert_one(_)
            cnt += 1
        except DuplicateKeyError:
            continue

    new_dict = {"testcases":testcase_list}
    new_dict["testsuites"] = testsuite_list
    json.dump(new_dict,new_file)
    new_file.close()

    print("We have transfer %d cases and suites!",cnt)





