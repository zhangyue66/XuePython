#Selection sort

alist = [54,226,93,17,77,31,44,55,20]
"""index:0  1   2  3  4  5  6  7  8   """

# def selection_sort(list):
#     n = len(list)
#
#     for j in range(n-1):
#         """j is starting index """
#         min_index = j
#         for i in range(j+1,n):
#             """i should be the element next to j so i = j+1"""
#             if list[min_index] > list[i]:
#                 min_index = i
#
#         alist[j],alist[min_index] = alist[min_index],alist[j]


# def bubble_sort(list):
#     n = len(list)
#     for j in range(n-1):
#         for i in range(n-1-j):
#             if list[i] > list[i+1]:
#                 list[i],list[i+1] = list[i+1],list[i]


def selection_sort(list):
    n = len(list)
    for j in range(n-1):

        min_index = j
        for i in range(j+1,n):

            if list[min_index] > list[i]:
                min_index = i
            list[min_index],list[j] = list[j],list[min_index]



print(alist)

selection_sort(alist)

#bubble_sort(alist)

print(alist)





