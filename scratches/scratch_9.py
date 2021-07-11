'''
for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%d' % (i, j, i * j), end='\t')
    print()
'''

'''
from itertools import islice

a = islice("ABCDEFG",2)

print(str(a))
'''

'''
x = int(input('x = '))
y = int(input('y = '))
# 如果x大于y就交换x和y的值
if x > y:
    # 通过下面的操作将y的值赋给x, 将x的值赋给y
    x, y = y, x
# 从两个数中较的数开始做递减的循环
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('%d和%d的最大公约数是%d' % (x, y, factor))
        print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
        break
'''
# Looking for Narcissitc Number
'''
for hundred in range(1,10):
    for ten in range (0,10):
        for single in range (0,10):
            num = hundred*100+ten*10+single
            if num == hundred**3+ten**3+single**3:
                print(num)
'''


# reversing a number rev(346) = 643
'''
def rev(number):
    if number ==0:
        return number
    else:
        rev_number = str(number)[::-1]
        return int(rev_number)

print(rev(43563463465))
'''

'''
for x in range(0,21):
    for y in range(0,34):
        for z in range(0,301):
            if x+y+z == 100 and 5*x+3*y+(1/3)*z == 100:
                print("man chicken is %d, woman chikcen is %d and small chicken is %d!" %(x,y,z))
'''

#CRAPS Roll dice for once

from random import randint


def craps():
    first_roll = randint(1, 6)
    second_roll = randint(1, 6)
    third_roll = 0
    fourth_roll = 0
    print("player first roll is %d !" %(first_roll+second_roll))

    win_counter = 0
    loss_counter = 0

    if first_roll+second_roll == 7 or first_roll+second_roll == 11:
        win_counter += 1
        print("Player rolled %d !" %(first_roll+second_roll) )
        print("Player Wins")
        print("you lost counter is " + str(loss_counter))
        print("you win counter is " + str(win_counter))
    elif first_roll+second_roll ==2 or first_roll+second_roll==3 or first_roll+second_roll == 12:
        loss_counter += 1
        print("Player rolled %d !"  %(first_roll + second_roll))
        print("Host Wins")
        print("you lost counter is " + str(loss_counter))
        print("you win counter is " + str(win_counter))
    else:
        third_roll = randint(1, 6)
        fourth_roll = randint(1, 6)
        print("Roll continue...")
        print("new roll is %d" %(third_roll+fourth_roll))
        while third_roll+fourth_roll != first_roll+second_roll:
            print("reroll not same as first one!")
            third_roll = randint(1,6)
            fourth_roll = randint(1,6)
            loss_counter +=1

            print("fucking roll is %d" % (third_roll + fourth_roll))
            if third_roll+fourth_roll ==7:
                #print("new roll is %d" % (third_roll + fourth_roll))
                print("host wins!")

            else:
                #print("new roll is %d" % (third_roll + fourth_roll))

                print("Continue!")
        print("you lost counter is " + str(loss_counter))
        print("you win counter is " + str(win_counter))



    return loss_counter


craps()


#print(" Your loss counter is " + str(craps().loss_counter))


#money = 1000
#bet = int(input("Enter you bet:"))







