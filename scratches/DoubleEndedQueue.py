"""Double Ended Queue"""

class Deque(object):

    def __init__(self):
        self.__list = []

    def add_front(self,item):
        self.__list.insert(0,item)

    def add_rear(self,item):
        self.__list.append(item)

    def pop_front(self):
        if self.__list :
            return self.__list.pop(0)
        else:
            return None

    def pop_rear(self):
        if self.__list:
            return self.__list.pop()
        else:
            return None

    def is_empty(self):
        return self.__list == []


    def size(self):
        return len(self.__list)


if __name__ == "__main__":
    deque = Deque()
    deque.add_front(1)
    deque.add_front(2)
    deque.add_rear(3)
    deque.add_rear(4)
    print( deque.size())
    print (deque.pop_front())
    print (deque.pop_front())
    print (deque.pop_rear())
    print (deque.pop_rear())
    print(deque.pop_rear())