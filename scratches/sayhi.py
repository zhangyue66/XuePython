def say_hi(name,age,place):
    print("Hello User!" + name +"!" ," you are " + str(age) ,"you live in" + place)


say_hi("yue",30,"seattle")
say_hi("lin",31,"los_agneles")
say_hi("hui",32,"Brues")


def cube_number(number):
    return number **3
    #return number

print(cube_number(3))



#def if_stat(condition):


is_male = True
is_tall = False

if is_male == 1 and is_tall:
    print("you are a male with power tall!")
elif is_male == False and is_tall :
    print("you are a female with tall!")
elif is_male == True and is_tall == False:
    print("You are male with not tall")
else:
    print("you are a female but not tall")


# more if and comparison

# take three numbers and compare

def max_num(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
       return num1
    elif num1 >= num2 and num1 <=num3:
       return num3
    elif num1 < num2 and num2 >= num3:
        return num2
    elif num1 < num2 and num2 < num3:
        return num3

print(max_num(38.1,8.2,38.7))

#buiding calculator

num1 = float(input("Enter the first number:"))
op = input("Enter the operator you want to do: ")
num2 = float(input("Enter the 2nd number:"))

def cal(num1,op,num2):
    if op == "+":
        return num1+num2
    elif op == "-":
        return num1-num2
    elif op == "*":
        return num1*num2
    elif op == "/":
        return num1/num2
    else:
        print("sorry no supported")

print(cal(num1,op,num2))