from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import json
import copy
from bson.objectid import ObjectId


# This is used to migrate test case and test suite from ANT24


uri = "mongodb://m02128:044a23cadb567653eb51d4eb40acaa88@localhost:27017/pronghorn?authSource=admin"
try:
    client = MongoClient(uri)
except ConnectionFailure as err:
    print("you are facing a connection error :" + err)


with client:

    db = MongoClient(uri).get_database()
    #print(db.name)
    #print(client)

    collection = db["ANT_TestCase"]
    yz = collection.count_documents({})
    #"testcase_name":"213409_S1HO_woSGW_Data_IMS_V4_V6
    #Target label  "label" : [ "BF_P1"]

    label_query = {"testcase_name":"mini_enhancedphone_MRC5G_310784_HTTP80_NCL_IPv4_SyGy"}
    #label_query = {"testcase_name":"213409_S1HO_woSGW_Data_IMS_V4_V6"}
    orin_file = open("orin.json","w")
    orin_list = []
    # target file to save the test cases in new zone
    new_file = open("target.json", "w")
    new_list = []

    for x in collection.find(label_query):
        orin_list.append(x)

        y = copy.deepcopy(x) # deepcopy a new json file for the new test case so modification on y dooes not impact x

        if "_id" not in y:
            print("error:can not see _id for test case")
            break
        else:
            case_id = y.pop("_id") # delete the _id for new test case
            print("delete case id is : %s" %case_id)

        if "DUT" not in y:
            print("error: DUT is empty")
            break
        else:
            # "DUT": {
            #     "type": "Zone",
            #     "networkElement": [
            #         "rdm56E_CP"
            #     ],
            #     "value": "RDM56E_BlackFox"
            # }
            y["DUT"]["networkElement"][0] = "RDM56CCP1"
            y["DUT"]["networkElement"].append("RDM54ACP2")
            y["DUT"]["value"] = "BB_56CCP_Consumer"
            #y["ui_Columns"]["Scenario"]["MCC"]["value"] = "8989898"

        if "label" not in y:
            print("error: label is empty")
            break
        # else:
        #    y["label"].append("yz")



        # change is done. y is new dictionary . mongo insert this new y
        new_list.append(y)


    orin_dict = {"testcases":orin_list}
    json.dump(orin_dict,orin_file)
    orin_file.close()

    new_dict = {"testcases":new_list}
    json.dump(new_dict,new_file)
    new_file.close()

    # now time to insert each y into ANT_TestCase collection
    f  = open("target.json")

    data = json.load(f)

    for testcase in data["testcases"] :  # {"testcases":[y1,y2,y3....]}
        if "_id" not in testcase:
            id = ObjectId()
            testcase["_id"] = str(id)
        collection.insert_one(testcase)
        print("Done!")

    f.close()






