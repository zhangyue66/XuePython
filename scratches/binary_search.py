#binary search must be used in a sorted and async list !

def binary_search(alist,target):
    #return True or False

    n = len(alist)

    if n >= 1:
    #     pivot = alist[n//2]
    #
    #     if target < pivot:
    #         return binary_search(alist[:pivot],target)
    #
    #     elif target > pivot:
    #
    #         return binary_search(alist[pivot+1:],target)
    #
    #     else:
    #         return True
    # else:
    #     return False
        mid = n//2
        if  alist[mid] == target:
            return True
        elif             target < alist[mid]:
                return binary_search(alist[:mid],target)

        else:
            return binary_search(alist[mid+1:],target)
    return False


alist =[14,17, 20, 26, 31, 44, 54, 55, 77, 93]
target =999
print(binary_search(alist,target))