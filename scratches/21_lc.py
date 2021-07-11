# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        # create l3 head
        #l1 1-2-4
        #12 1-3-4
        cur = dummy = ListNode(0)

        #while l1 and l2 :
        if l1.value <= l2.value:
            dummy.next = l1
            l1 = l1.next
        else:
            dummy.next = l2
            l2 = l2.next
            #dummy = dummy.next

        #dummy.next = l1 or l2
        return cur.next


