#O(nlogn) ~O(n2)

# nums = [ 13 14 94 33 82 25 59 94 65 23 45 27 73 25 39 10 ]



def shell_sort(alist):
    n = len(alist)
    gap = n // 2

    while gap > 0:
        for j in range(gap,n):
            i = j
            while i >= gap:
                if alist[i] < alist[i-gap]:
                    alist[i],alist[i-gap] = alist[i-gap],alist[i]
                    i -= gap
                else:
                    break

        gap = gap //2


alist = [54,26,93,17,77,31,44,55,20]
shell_sort(alist)
print(alist)


