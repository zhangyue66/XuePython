#useful tools in python

import random

i = 0
while i<10 :
 random_number = random.randrange(0,101,2)
 i +=1
 print(random_number)
 print("this is the " + str(i) + "times to roll a dice!")



