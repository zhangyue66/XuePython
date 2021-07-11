import re
from packaging.version import parse as parse_version

version_list = ['v1_3_11','v1_3_9','v1_3_8','v1_3_10']
b_list = []
for item in version_list:
    new_item = re.sub(r"v",'',item)
    b_list.append(new_item)
    print(new_item)

print(b_list)

x_list =[]



for version in b_list:
    c_item = re.sub('_', '', version)
    x_list.append(c_item)



def version_sort(list):
    #use bubble sort and parse_version to do sorting
    n = len(list)

    for i in range(n):
        for j in range(0,n-i-1):
            if parse_version(list[j]) > parse_version(list[j+1]):
                list[j],list[j+1] = list[j+1],list[j]

version_sort(x_list)

print(x_list)











