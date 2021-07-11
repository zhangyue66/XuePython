"""using python list (linear) to achieve Queue """



class Queue(object):


    def __init__(self):
        self.__list = []

    def enqueue(self,item):
        self.__list.append(item)

    def dequeue(self):
        if self.__list :
            return self.__list.pop(0)
        else:
            return None


    def is_empty(self):
        return self.__list == []


    def size(self):
        return len(self.__list)


if __name__ == "__main__":

    queue_yz = Queue()

    queue_yz.enqueue(1)
    queue_yz.enqueue(11)
    queue_yz.enqueue(23)
    queue_yz.enqueue(99)
    print(queue_yz.dequeue())
    print("queue length is %d"%(queue_yz.size()))
    print(queue_yz.dequeue())
    print(queue_yz.dequeue())
    print(queue_yz.dequeue())
    print(queue_yz.is_empty())
    print(queue_yz.size())
