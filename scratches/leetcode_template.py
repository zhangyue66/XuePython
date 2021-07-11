#Find Prime
class Solution:
    def isPrime(self,num):
        if num <= 1:
            return False
        for i in range(2,int(num**0.5)+1):
            if num % i == 0:
                return False

        return True

#Binary Search Tree
class Node(object):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def search(self, data, parent=None):
        if data < self.data:
            if self.left is None:
                return None, None
            return self.left.search(data, self)
        elif data > self.data:
            if self.right is None:
                return None, None
            return self.right.search(data, self)
        else:
            return self, parent

#KMP
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle: return 0
        # build next
        next = [0]*len(needle)
        l, r = 0, 1
        while r < len(needle):
            if needle[l] == needle[r]:
                next[r] = l+1
                l, r = l+1, r+1
            elif l: l = next[l-1]
            else: r += 1
        # find idx
        l, r = 0, 0
        while r < len(haystack):
            if needle[l] == haystack[r]:
                if l == len(needle)-1:
                    return r-l
                l, r = l+1, r+1
            elif l: l = next[l-1]
            else: r += 1
        return -1

# Reverse Linked List
class Solution:
    def reverseList(self, head):
        cur, prev = head, None
        while cur:
            cur.next, cur, prev = prev, cur.next, cur  # standard reversing
        return prev

#Merge Sorted Linked List
class Solution(object):
    def merge(self, h1, h2):
        dummy = tail = ListNode(None)
        while h1 and h2:
            if h1.val < h2.val:
                tail.next, tail, h1 = h1, h1, h1.next
            else:
                tail.next, tail, h2 = h2, h2, h2.next

        tail.next = h1 or h2
        return dummy.next

    def sortList(self, head):
        if not head or not head.next:
            return head

        pre, slow, fast = None, head, head
        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next
        pre.next = None

        return self.merge(self.sortList(head), self.sortList(slow))

# Binary Search Value
def bisec(array,val):
    l,r = 0,len(array)-1

    while l <= r :
        mid = l +(r-l)//2
        if array[mid] == val:
            array.pop(mid)
            return True
        elif array[mid] > val:
            r = mid - 1
        else:
            l = mid + 1

    return False

#bisect_left
def bisect_left(a, x, lo=0, hi=None):
    lo, hi = 0, n
    while lo < hi:
        mid = (lo+hi)//2
        if a[mid] < x:
            lo = mid+1  # disgard equals part
        else:
            hi = mid
    return lo

# BACKTRACK
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []

        def backtrack(nums,start,end,res,length):
            if  len(res) == length:
                self.ans.append(res[:])
                return
            # if start == len(nums):
            #     self.ans.append(res[:])
            #     return

            for i in range(start,end):
                if nums[i] not in res:
                    res.append(nums[i])
                    backtrack(nums,i+1,end,res,length)
                    res.pop()

        for i in range(len(nums)+1):

            backtrack(nums,0,len(nums),[],i)

        return self.ans
# Tree
class Tree(object):
    def __init__(self):
        self.root = None


    def add(self,item):
        node = Node(item)
        if self.root == None:
            self.root = node
            return

        else:
            queue = [self.root]
            while queue is not None:
                cur_node = queue.pop(0)
                if cur_node.lchild is None:
                    cur_node.lchild = node
                    return
                else:
                    queue.append(cur_node.lchild)
                if cur_node.rchild is None:
                    cur_node.rchild = node
                    return
                else:
                    queue.append(cur_node.rchild)

#permu of string
def toString(List):
    return ''.join(List)

# Function to print permutations of string
# This function takes three parameters:
# 1. String
# 2. Starting index of the string
# 3. Ending index of the string.
def permute(a, l, r):
    if l==r:
        print toString(a)
    else:
        for i in range(l,r+1):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l] # backtrack


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#quick Sort
def partition(nums, lo, hi):
    i, x = lo, nums[hi]
    for j in range(lo, hi):
        if nums[j] <= x:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[i], nums[hi] = nums[hi], nums[i]
    return i

def quick_select(nums, lo, hi, k):
    while lo < hi:
        mid = partition(nums, lo, hi)
        if mid == k:
            return nums[k]
        elif mid < k:
            lo = mid+1
        else:
            hi = mid-1

nums = [54, 26, 93, 17, 77, 31, 44, 55, 20]
for i in range(len(nums)):
    print(quick_select(nums, 0, len(nums)-1, i))

#Union find
class Solution:
    def makeConnected(self, n: int, connections):
        if len(connections)<n-1:
            return -1

        self.parent = [i for i in range(n)]

        def find(a):
            if self.parent[a] == a:
                return a
            return find(self.parent[a])

        def union(a,b):
            pa = find(a)
            pb = find(b)
            if pa != pb:
                self.parent[pa] = pb

        ans=n-1 # if n nodes all connected, we just need n-1 vertic

        for a,b in connections:
            parent_a = find(a)
            parent_b = find(b)
            if parent_a != parent_b :
                union(a,b)
                ans -= 1
        return ans
