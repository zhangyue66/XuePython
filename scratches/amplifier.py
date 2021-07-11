"""

import re

username="123aaaaaaaaaaaa_"

if re.match("^\w{6,20}$",username):
    print("you are good!")
    print("length is %d" %(len(username)))
else:
    print("no match!")
    print("length is %d" % (len(username)))


pattern = re.compile(r"123")
match_list = re.findall(pattern,username)
print(match_list)

"""

import re

sentence = '你丫是傻叉吗? 我操你大爷的. Fuck you.'

pattern = re.compile(r"[傻操]|fuck|Fuck")

match_list = re.findall(pattern,sentence)


after_hexie = re.sub(pattern,"+",sentence)

print(after_hexie)









