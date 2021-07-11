# Guess a random number
#import random
#answer = random.randint(1,100)
#answer = 88
#guess_count = 0
'''

if guess_count < 5 :
    guess_number = input(" Please enter a integer number: ")
    if int(guess_number) == answer:
     print("you are correct! Answer is "+ str(answer) + "!")
    elif int(guess_number) > answer:
     print("your guess is bigger")
     guess_count += 1
    else:
     print("your guess is smaller")
     guess_count += 1

else:
    print("you are done!")

'''


'''
while  guess_count < 5:
    guess_number = input("Give a number: ")
    guess_count += 1

    if int(guess_number) == answer:
        print("Good! you are using " + str(guess_count) + " times of guesses!")
        break
    elif int(guess_number) > answer:
        print("you number is bigger")
    else:
        print("you number is smaller")

else:
    print("you are running out of chances")





'''

# Judge is a number is a prime number

from math import sqrt

number = int(input("Please input an integer!"))
com = int(sqrt(number))
is_prime = True

if number < 4:
    is_prime = False
    print("this is not a prime number!")

else:
    for deno in range(2,com+1):
        if number % deno ==0:
           is_prime = False

       # else:
            #print("lets see")

if is_prime == True:
    print("Prime!")

else:
    print("NOT prime!")