try:
    employee_file = open("employees123.txt", "w")
    employee_file.write("\nToby - Human Resource")
    employee_file.write("\nKelly - Fucker")

except:
    print("error is happening")


# w->write a-> append r->read r+ -> read and write