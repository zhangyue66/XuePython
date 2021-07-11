#define a insertion_sort
alist = [54,26,93,17,77,31,44,55,20]

# def insertion_sort(alist):
#     n = len(alist)
#     # i = 1
#     # if alist[i] < alist[i-1]:
#     #     alist[i],alist[i-1] = alist[i-1],alist[i]
#     #
#     # i = 2
#     # if alist[i] < alist[i-1]:
#     #     alist[i],alist[i-1] = alist[i-1],alist[i]
#     #
#     #
#     # i = 3
#     # if alist[i] < alist[i-1]:
#     #     alist[i],alist[i-1] = alist[i-1],alist[i]
#     #     i -= 1
#     #     if alist[i] < alist[i - 1]:
#     #         alist[i], alist[i - 1] = alist[i - 1], alist[i]
#     #         """......."""
#     for j in range(1,n):
#         i = j
#         while i > 0:
#             if alist[i] < alist[i - 1]:
#                 alist[i], alist[i - 1] = alist[i - 1], alist[i]
#                 i -= 1
#             else:
#                 break
def insertion_sort(alist):
    n = len(alist)

    for j in range(1,n):
        for i in range(j,0,-1):
            if alist[i] < alist[i-1]:
                alist[i],alist[i-1] = alist[i-1],alist[i]

print(alist)

insertion_sort(alist)

print(alist)


