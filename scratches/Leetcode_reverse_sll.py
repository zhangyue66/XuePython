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
        pre = None
        current = self._head
        while current != None:
            if current.item == item:
                "if deleting first node. it will have mistakes"
                if current == self._head:
                    self._head = current.next
                    break
                else:
                    pre.next = current.next
                    break
            else:
                pre = current
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

    def delete_duplicates(self):
        if self._head == None:
            print("empty list.")
        else:
            current = self._head
            #anchor = current.item
            while current != None and current.next !=None:

                if current.item == current.next.item:
                    self.remove(current.next.item)
                current = current.next

    def rev_list(self):

        prev = None
        current = self._head
        while (current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next

            #current.next,prev,current = prev,current,current.next
        self._head = prev



    def get_elem(self,position):
        """this is get the value on position x"""
        count = 1
        current = self._head
        while count < position:
            count += 1
            current = current.next
        return current.item


    def rev_list_yz(self):
        prev = None
        current = self._head
        while current != None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self._head = prev






sorted_list = SingleLinkedList()
sorted_list.add(5)
sorted_list.append(5)
sorted_list.append(5)
sorted_list.append(6)
sorted_list.append(7)
sorted_list.append(8)
sorted_list.append(9)
sorted_list.append(9)



sorted_list.travel()
#sorted_list.delete_duplicates()
sorted_list.travel()


#print(sorted_list.get_elem(5))

#reverse list
# reverse_list = SingleLinkedList()
# yzs = sorted_list.length()
# for yz in range(yzs,0,-1):
#     reverse_item = sorted_list.get_elem(yz)
#
#     reverse_list.append(reverse_item)
#
#
# reverse_list.travel()

# sorted_list.rev_list()
#
# sorted_list.travel()

sorted_list.rev_list_yz()

sorted_list.travel()










