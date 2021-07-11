# import re
# from packaging.version import parse as parse_version

version_list = ['','1_3_9','1_3_8','1_3_10']

def is_bigger(src, dest, seperator):
    src_list = src.split(seperator)
    dest_list = dest.split(seperator)
    length = max(len(src_list), len(dest_list))

    for i in range(0, length):
        try:
            if int(src_list[i]) > int(dest_list[i]):
                return True
            elif int(src_list[i]) == int(dest_list[i]):
                continue
            else:
                return False
        except Exception as e:
            if len(src_list) > len(dest_list):
                return True
            else:
                return False
    return False

def version_sort(version_list):
    #use bubble sort and parse_version to do sorting
    n = len(version_list)

    for i in range(n):
        for j in range(0,n-i-1):
            if is_bigger(version_list[j],version_list[j+1],"_"):
                version_list[j],version_list[j+1] = version_list[j+1],version_list[j]
    return version_list


a=version_sort(version_list)

print(a)

