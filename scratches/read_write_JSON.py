import json


"""
def main():
    my_dic = {
    "name": "骆昊",
    "age": 38,
    "qq": 957658,
    "friends": ["王大锤", "白元芳"],
    "cars": [
        {"brand": "BYD", "max_speed": 180},
        {"brand": "Audi", "max_speed": 280},
        {"brand": "Benz", "max_speed": 320}
            ]
             }


    with open("my_dic.json","w",encoding="utf-8") as fs:
        js = json.dumps(my_dic)
        fs.write(js)
        print("write Json successful!")
    print("Try again!")
"""
# Deserialization

def main():
    my_dic=[]
    fs = open("my_dic.json", "r", encoding="utf-8")
    content = fs.read()
    lingzi = json.loads(content)
    print(lingzi)
    fs.close()



if __name__ =="__main__":
    main()