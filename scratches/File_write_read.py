"""
def main():
    try:
        file_open = open("test.txt","r",encoding = "utf-8")
        print(file_open.read())
    except FileNotFoundError:
        print("Can not find files!")
    except LookupError:
        print("Can not find correct encoding!")
    finally:
        file_open.close()







if __name__ == "__main__":
    main()

"""

"""
import time

def main():

    #with open("test.txt","r",encoding="utf-8") as f :
        #print(f.read())

    #with open("test.txt",mode="r") as f :
        #for line in f:
            #print(line,end ='')
            #time.sleep(1)

        f=open("test.txt","r+")
        a = f.readlines()
        a.sort()
        print(a)
        #print(type(a))
        #b = a.sort(reverse=True)
        #print(b)



if __name__ == "__main__":
    main()

"""
"""
from math import sqrt


def is_prime(n):
    assert n >0
    for factor in range(2,int(sqrt(n))+1):
        if (n%factor ==0):
            return False
    return True if n!=1 else False


def main():
    #file_names = ["a.txt","b.txt","c.txt"]
    a_file = open("a.txt","a",encoding="utf-8")
    b_file = open("b.txt","a",encoding="utf-8")
    c_file = open("c.txt", "a", encoding="utf-8")
    for number in range(1,10000):
        if is_prime(number) and number<100:
            a_file.write("%d \n" %number)
        if is_prime(number) and number< 999:
            b_file.write("%d \n" %number)
        if is_prime(number) and number <10000:
            c_file.write("%d \n" %number)
    a_file.close()
    b_file.close()
    c_file.close()
    print("write prime done!")

if __name__ == "__main__":
    main()
"""

#read binary file



def main():
    try:
        with open("Lingzi.jpg", "rb") as fs1:
            data_ori=fs1.read()
            print("The type of oringinal data is : " + str(type(data_ori)))
        with open("Lingzi_juru.jpg", "ab") as fs2:
            fs2.write(data_ori)
    except AssertionError:
        print("try again!")
    except IOError as err:
        print("IO is wrong!" + str(err))


if __name__ == "__main__":
    main()



