def quick_sort(alist,start,end):

    #the condition to exit recursion
    if start >= end:
        return

    #n = len(alist)
    mid_value = alist[start]
    low = start
    high = end

    while low < high:
        # high pointer move left
        # while low < high and alist[high] >= mid_value:
        #
        #         high -= 1
        # alist[low] = alist[high]
        #
        # #low pointer move to right
        # while low < high and  alist[low] < mid_value:
        #
        #         low += 1
        #
        # alist[high] = alist[low]
        # high -= 1
        while low < high:
            if alist[high] >= mid_value:
                high -= 1
            else:
                break
        alist[low] = alist[high]

        while low <high:
            if alist[low] < mid_value:
                low +=1
            else:
                break
        alist[high] = alist[low]

    alist[low] = mid_value

    quick_sort(alist,start,low-1)
    quick_sort(alist,low+1,end)



alist = [54,26,93,17,77,31,44,55,20]
print(alist)
quick_sort(alist,0,len(alist)-1)
print(alist)









