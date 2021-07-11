# we are going to convert month name to abbreviation
'''

month_Dic = {
    "Jan":"January",
    "Feb":"February",
    "Mar":"March",
    "Apr":"April",
    "May":"MayMay",
    "Nov":"November",
    "Dec":"December",
}

print(month_Dic.get("Nasd","Not a valid key"))
print(month_Dic)

'''


#while loop
'''
i = 1.0
while i <=10:
    print(i)
    i += 1.2

'''

#building guess game
def guess_game():
 secret_word = 'giraffe'
 user_guess = ''
 guess_count = 0
 out_of_guess = False
 guess_limit = 3

 while user_guess != secret_word and out_of_guess == False:
    if guess_count < guess_limit:
        user_guess = input("Please enter you guess here: ")
        guess_count += 1

    else:
        out_of_guess = True

 if out_of_guess == False:
    print("You Win! The answer is "+ user_guess)
 else:
    print("You lose! You are out of guess!")



#guess_game()



#For loop
for letter in "Yue Zhang is handsome and tall.He love big tits":
    print(letter)
NBA_league =["duncan","wallace","tony","kobe"]
for player in NBA_league:
    print(player)


for index in range(5):
    if index == 0:
        print("this is first element")
    else:
        print("Continue")

#exponent Function
def raise_to_power(base_num,power_num):
    result = 1
    for index in range(power_num):
       result = result * base_num
    return result
#print(raise_to_power(7,3))

#2D list and nested loops

number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

print(number_grid[3][0])

#print(int(number_grid.row))

for row in number_grid:
    print(row)
    for col in row:
        print(col)


