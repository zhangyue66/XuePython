import csv

csv_file_directory = r"C:\Users\yz632h\Documents\Zoom\wvs.csv"

fields = []

rows = []

with open(csv_file_directory,"r") as csvfile:
    csvreader = csv.reader(csvfile)

    for row in csvreader:
        rows.append(row)

    #print(len(rows))
    #this will be your dictionary . each element will be an independent dictionary for example : v4 = {}  , v204 = {}
    new_row_zero =  rows[0][0].split("\t")
    # Remember to split("\t") for every row. otherwise values will be messed

    #get the index of "v204" . you will use this index for every row -> rows[1][0][index] to get the data
    for i in range(len(new_row_zero)):
        if new_row_zero[i] == "V204":
            target_index = i

    print(new_row_zero)

    #print(target_index)  # 228 is your target index. you need to get the value on index 228 on every row



    #now i am going to get all the values for V204 and form a list
    values = []

    #now i am going to make a dictionary for every row[i][0][index]
    # you dictionary should be like this { -5: XXX , -4 :XXXX ,-3:XXXX,-2:XXX  , -1:XX ,1 :XXX, .... 10:xxxx}
    # xxx is the counters  ( you can use collections.counters to enum  or you can for your own dictionary )

    V204_dic = {}

    #print(rows[1])