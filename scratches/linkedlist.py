# is_empty() 链表是否为空
# length() 链表长度
# travel() 遍历整个链表
# add(item) 链表头部添加元素
# append(item) 链表尾部添加元素
# insert(pos, item) 指定位置添加元素
# remove(item) 删除节点
# search(item) 查找节点是否存在

class Node(object):
    def __init__(self,item):
        self.item = item
        self.next = None
        #python variable reality a,b = b,a

# node = Node(2)
# node2 = Node(788)

class SingleLinkedList(object):
    """single direction linked list"""
    def __init__(self,node=None):
        self._head = node

    def is_empty(self):
        if self._head == None:
            return True
        else:
            return False


    def length(self):
        #current used to travel list and count
        current = self._head
        count = 0
        while current != None:
            count += 1
            current = current.next

        return count


    def travel(self):
        current = self._head
        while current != None:
            print(current.item,end=" ")

            current = current.next
        print('\n')



    def add(self,item):
        """头插法"""
        node = Node(item)
        #add nodes in head/first
        node.next = self._head
        self._head = node
        '''can handle list if it is empty'''


    def append(self,item):
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            current = self._head

            while current.next != None:
                current = current.next
            current.next = node




    def insert(self,position,item):
        node = Node(item)
        pre= self._head
        counter = 0
        if position <=0:
            self.add(item)
        elif position > self.length():
            self.append(item)
        else:
            while counter < (position-1):
                counter += 1
                pre = pre.next
            node.next = pre.next
            pre.next = node


    def remove(self,item):
        """delete item. if there is duplicate, delete first one.use two anchors PRE and CURRENT"""
        # pre = None
        # current = self._head
        # while current != None:
        #     if current.item == item:
        #         "if deleting first node. it will have mistakes"
        #         if current == self._head:
        #             self._head = current.next
        #             break
        #         else:
        #             pre.next = current.next
        #             break
        #     else:
        #         pre = current
        #         current = current.next

        current = self._head
        prev = None

        while current != None :
            if current.item == item:
                if current == self._head:
                    self._head = current.next
                    break
                else:
                    prev.next = current.next
                    break

            else:
                prev = current
                current = current.next





    def search(self,item):
        """search item in list or not. (node.item)"""
        current = self._head
        while current != None:
            if current.item == item:
                return True
            else:
                current = current.next
        return False


"""link list must have a head node"""
if __name__ == "__main__":
    single_obj=SingleLinkedList()
    print(single_obj.is_empty())
    single_obj.add(89)
    print(single_obj.length())
    single_obj.append(100)
    single_obj.append(101)
    single_obj.append(102)
    single_obj.append(1)
    single_obj.add(89)
    single_obj.add(1999)
    print(single_obj.length())
    # print(single_obj.is_empty())
    single_obj.travel()
    single_obj.insert(1,55)
    single_obj.travel()
    print(single_obj.search(67))
    single_obj.remove(55)
    single_obj.travel()
    #print(single_obj.travel()) there is one more None being printed
    #single_obj.add()   #add an item into head node
