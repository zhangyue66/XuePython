from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import json
import copy
from bson.objectid import ObjectId

#make sure you give URL for primary ATE mongo. if ATE mongo is secondary . it might fail
uri = "mongodb://m02128:b24d516bb65a5a58079f0f3526c87c57@ant31ate03.ttve.mobilephone.net:27017/pronghorn?authSource=admin"
target_uri = "mongodb://m02128:1aa48fc4880bb0c9b8a3bf979d3b917e@ant32ate02.ttve.mobilephone.net:27017/pronghorn?authSource=admin"
try:
    client = MongoClient(uri)

except ConnectionFailure as err:
    print("you are facing a connection error :" + err)

try:
    target_client = MongoClient(target_uri)
except ConnectionFailure as err1:
    print("target client can not be connected " + err1)


with target_client and client:
    # 1st get all the test case id in test suite and save it to testcase_list = []
    testcase_list = []

    f  = open("target.json")

    data = json.load(f)

    testcase_cnt = 0
    for testcase in data["testcases"] :  # {"testcases":[y1,y2,y3....]}
        if "testcase_id" in testcase and len(testcase["testcase_id"]) != 0:
            for id in testcase["testcase_id"]:
                testcase_list.append(id)
                testcase_cnt += 1
        else:
            print("id not available , test case _id is %s " + testcase["_id"])

    print("Total test case count is %s" + str(testcase_cnt))

    # we got all the testcase id and now open client and insert to target client
    if len(testcase_list) != 0:
        yz_cnt = 0
        db = MongoClient(uri).get_database()
        collection = db["ANT_TestCase"]
        yz_temp = collection.count_documents({})

        target_db = MongoClient(target_uri).get_database()
        target_collection = target_db["ANT_TestCase"]

        for id in testcase_list:
            query ={"_id":id}
            yz = collection.find_one(query)

            dup = target_collection.find_one(query)
            if dup is None:
                target_collection.insert_one(yz)
                yz_cnt += 1
                print("Done!")

        print("total insert documents are %s " + str(yz_cnt))

    f.close()





