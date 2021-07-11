comp = lambda x,y: x<y

print(comp(5,8))

list = {"google":299.20,"facebook":199,"baidu":178}
list2 = {key: value for key,value in list.items() if value > 100}
print(list2)

from random import randint

names = ["Shion","Yue","Lingzi","Ruri","Fakuta"]
courses = ["Chinese","Maths","English"]

#Record score of three course for 5 people. So you can grep them any time.

#Dictionary1 which key:value is courses : scores

# scores = [randint(50,100),randint(46,90),randint(70,100)]
# score_dic=dict(zip(courses,scores))
# print(score_dic)

for name in names:
    #print(name)

        scores = [randint(50, 100), randint(46, 90), randint(70, 100)]
        score_dic = dict(zip(courses,scores))
        print(score_dic)
    #print(score_dic["Yue"])
    #dic = dict(zip(name,score_dic))
    # dic ={}
    # dic[name] ={}
    # dic[name][course]=scores

#print(dic)