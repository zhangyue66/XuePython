from random import randint

names = ["Shion","Yue","Lingzi","Ruri","Fakuta"]



courses = ["Chinese","Maths","English"]



score1 = [randint(50, 100), randint(46, 90), randint(70, 100)]
score2 = [randint(50, 100), randint(46, 90), randint(70, 100)]
score3 = [randint(50, 100), randint(46, 90), randint(70, 100)]


score_dic1 = dict(zip(courses,score1))

score_dic2 = dict(zip(courses,score2))

score_dic3 = dict(zip(courses,score3))

scores = [score_dic1,score_dic2,score_dic3]

#score_dics = [score_dic1,score_dic2,score_dic3]
score_list = [score for score in scores]

dic = dict(zip(names,score_list))


print(dic)


