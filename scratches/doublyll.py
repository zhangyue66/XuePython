# is_empty() 链表是否为空
# length() 链表长度
# travel() 遍历链表
# add(item) 链表头部添加
# append(item) 链表尾部添加
# insert(pos, item) 指定位置添加
# remove(item) 删除节点
# search(item) 查找节点位置 （改进SLL）

#from linkedlist import SingleLinkedList ->how to do

class Node(object):
    """node forward backward """
    def __init__(self,item):
        self.item = item
        self.prev = None
        self.next = None

class DoublyLinkedList(object):
    """double linked list """

    def __init__(self,node=None):

        self._head = node

    def is_empty(self) :
        if self._head is None:
            return True
        else:
            return False

    def length(self) :
        current = self._head
        count = 0
        while current != None:
            #yue write current.ite not None -> wrong!
            count +=1
            current = current.next
        return count

    def travel(self) :
        current = self._head
        while current is not None:
            print(current.item,end=" ")
            current = current.next
        print("")

    def add(self,item):
        node = Node(item)
        if self.is_empty() is True:
            self._head = node
        else:
            # node.next = self._head
            # self._head = node
            # node.next.prev = node
            node.next = self._head
            node.next.prev = node
            self._head = node

    def append(self,item):
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            current = self._head
            while current.next != None:
                current = current.next
            current.next = node
            node.prev = current


    def insert(self,position,item):
        if position <= 0:
            self.add(item)
        elif position >= self.length():
            self.append(item)
        else:

            counter = 0
            current = self._head
            while counter < position:
                current = current.next
                counter += 1

            node = Node(item)

            # node.next = current.next
            # current.next.prev = node
            # current.next = node

            node.next = current
            node.prev = current.prev
            current.prev = node
            node.prev.next = node

    def remove(self,item):
        current = self._head
        #
        # while current != None:
        #     if current.item == item:
        #         if current == self._head:
        #
        #             self._head = current.next
        #             current.next.prev = None
        #         else:
        #             current.prev.next = current.next
        #             current.next.prev = current.prev
        #
        #     else:
        #         prev = current
        #         current = current.next
        while current != None:
            if current.item == item:
                if current == self._head:
                    self._head = current.next
                    if current.next != None:
                        '''if there is only one node. None will not have prev.'''
                        current.next.prev = None
                    break
                else:
                    current.prev.next = current.next
                    if current.next != None:
                        current.next.prev = current.prev
                    break
            else:
                current = current.next






    def search(self,item):
        current = self._head

        count = 0

        # if current != None :
        #     is_found = False
        #     while current is not None:
        #         count += 1
        #         if current.item == item:
        #             is_found = True
        #             break
        #         else:
        #
        #
        #             current = current.next
        #     if is_found == True:
        #         return count
        #     else:
        #         return -1
        #
        #
        # else:
        #     return False

        if current == None:
            return False

        while current.item != item:
            count +=1
            current = current.next
            if current is None:
                return -1
        return count


if __name__ == "__main__":
    doublyll_obj = DoublyLinkedList()
    print(doublyll_obj.is_empty())
    print(doublyll_obj.length())
    doublyll_obj.travel()
    doublyll_obj.add(1)
    doublyll_obj.add(2)
    doublyll_obj.travel()
    doublyll_obj.append(3)
    doublyll_obj.travel()
    print(doublyll_obj.length())
    doublyll_obj.insert(2,88888)
    doublyll_obj.travel()
    print(doublyll_obj.search(99))
    doublyll_obj.append(3)
    doublyll_obj.append(3)
    doublyll_obj.append(78)
    doublyll_obj.add(789)
    doublyll_obj.remove(88888)
    doublyll_obj.travel()
