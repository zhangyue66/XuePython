"""
from multiprocessing import Process
from time import sleep

counter = 0


def sub_task(string):
    global counter
    while counter < 10:
        print(string, end='', flush=True)
        counter += 1
        sleep(0.01)


def main():
    p1=Process(target=sub_task, args=('Ping',))
    p2=Process(target=sub_task, args=('Pong',))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
if __name__ == '__main__':
    main()
"""

'''
from multiprocessing import Queue,Process
from time import sleep
counter = 0
def insert_word(word,q):
    global counter
    while counter <10:
        q.put(word)
        counter += 1
        sleep(0.1)
        print("inserting!")


def show_queue(q):
    for number in range(0,10):
        print(q.get())


def main():
    q = Queue()

    p1 = Process(target=insert_word,args=("PING",q,))
    p2 = Process(target=insert_word,args=("PONG",q,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()


    show_queue(q)



if __name__ == "__main__":
    main()

'''
