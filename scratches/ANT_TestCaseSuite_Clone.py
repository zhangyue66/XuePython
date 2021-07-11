from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import json
import copy
from bson.objectid import ObjectId


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



with client and target_client:

    db = MongoClient(uri).get_database()
    #print(db.name)
    #print(client)

    collection = db["ANT_TestSuite"]
    yz = collection.count_documents({})
    #"testcase_name":"213409_S1HO_woSGW_Data_IMS_V4_V6
    #Target label  "label" : [ "BF_P1"]
    #label_query = {"label" : ["sanity"]}
    label_query= {"label":{ "$in" : ["Sanity"]}}
    #label_query = {"testcase_name":"213409_S1HO_woSGW_Data_IMS_V4_V6"}
    #db.getCollection('ANT_TestSuite').find({"labels":{$elemMatch:{"sanity","Sanity"}}})
    orin_file = open("orin.json","w")
    orin_list = []
    # target file to save the test cases in new zone
    new_file = open("target.json", "w")
    new_list = []

    for x in collection.find(label_query):
        orin_list.append(x)

        y = copy.deepcopy(x) # deepcopy a new json file for the new test case so modification on y dooes not impact x

        # if "_id" not in y:
        #         #     print("error:can not see _id for test case")
        #         #     break
        #         # else:
        #         #     case_id = y.pop("_id") # delete the _id for new test case
        #         #     print("delete case id is : %s" %case_id)
        #         #
        #         # if "DUT" not in y:
        #         #     print("error: DUT is empty")
        #         #     break
        #         # else:
        #         #     # "DUT": {
        #         #     #     "type": "Zone",
        #         #     #     "networkElement": [
        #         #     #         "rdm56E_CP"
        #         #     #     ],
        #         #     #     "value": "RDM56E_BlackFox"
        #         #     # }
        #         #     y["DUT"]["networkElement"][0] = "rdm56D_CP"
        #         #     y["DUT"]["value"] = "RDM56D_BlackFox"

        if "label" not in y:
            print("error: label is empty")
            break
        else:
           y["label"].append("yz")

        # change is done. y is new dictionary . mongo insert this new y
        new_list.append(y)


    orin_dict = {"testcases":orin_list}
    json.dump(orin_dict,orin_file)
    orin_file.close()

    new_dict = {"testcases":new_list}
    json.dump(new_dict,new_file)
    new_file.close()

    # now time to insert each y into ANT_TestCase collection
    # f  = open("target.json")
    #
    # data = json.load(f)
    #
    # for testcase in data["testcases"] :  # {"testcases":[y1,y2,y3....]}
    #     if "_id" not in testcase:
    #         id = ObjectId()
    #         testcase["_id"] = str(id)
    #     collection.insert_one(testcase)
    #     print("Done!")
    #
    # f.close()

    # now import the data to target client mongo
    target_db = MongoClient(target_uri).get_database()
    target_collection = target_db["ANT_TestSuite"]
    old_testsuite_count = target_collection.count_documents({})

    # f  = open("target.json")
    #
    # data = json.load(f)
    #
    # for testcase in data["testcases"] :  # {"testcases":[y1,y2,y3....]}
    #     target_collection.insert_one(testcase)
    #     print("Done!")
    #
    # new_testsuite_count = target_collection.count_documents({})
    #
    # print("previously test suite count is " + old_testsuite_count)
    # print("now test suite count is " + new_testsuite_count)
    #
    # f.close()






