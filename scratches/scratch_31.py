from multiprocessing import Process
from random import randint
from time import time,sleep
from os import getpid,getppid


def download(filename):
    print("Start downloading %s" %filename)
    time_cost = randint(5,10)
    print("ProcessID is %d" %getpid())
    print("Parent ProcessID is %d" % getppid() )
    sleep(time_cost)
    print("Download is finished. Cost %d seconds" %time_cost)

def main():
    p1 = Process(target=download,args=("Lingzi is beautiful!",))
    p1.start()
    time1 = time()

    p2 = Process(target=download,args=("Lingzi juru!",))
    p2.start()


    p1.join()
    p2.join()

    time2 = time()

    cost = time2-time1
    print("all process is doen! cost time is %d" %cost)

if __name__ == "__main__":
    main()


