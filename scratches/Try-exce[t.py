



'''
try:
    number = int(input("Enter a number : "))
    print(number)
except:
    print("invalid input")
'''

employee_file = open("employees.txt", "r")

#print(employee_file.readable())

#print(employee_file.read())

#print(employee_file.readlines()[1])

for employee in employee_file.readlines():
    print(employee)




employee_file.close()