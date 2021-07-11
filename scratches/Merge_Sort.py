def merge_sort(alist):
    # Recursiong is needed

    n = len(alist)
    if n <=1 :
        return alist
    mid = n //2
    alist[:mid]
    alist[mid:]
    left_list = merge_sort(alist[:mid])
    right_list =merge_sort(alist[mid:])

    left_pointer,right_pointer = 0,0
    result = []

    while left_pointer < len(left_list) and right_pointer < len(right_list):
        if left_list[left_pointer] < right_list[right_pointer]:
            result.append(left_list[left_pointer])
            left_pointer += 1
        else:
            result.append(right_list[right_pointer])
            right_pointer += 1

    result += left_list[left_pointer:]
    result += right_list[right_pointer:]


    #merge(left_list,right_list)
    return result



alist = [54,26,93,17,77,31,44,55,20]
print(alist)
print(merge_sort(alist))
print(alist)