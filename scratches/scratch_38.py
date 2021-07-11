from threading import Thread
from time import time,sleep
from random import randint
from os import getpid,getppid


class DownloadTask(Thread):

    def __init__(self,filename):
        super().__init__()
        self._filename = filename



    def run(self):
        print("Start downloading file %s now! \n" % (self._filename))
        time_cost = randint(5, 10)
       # print("PID is %d! \n" %getpid())
        #print("PPID is %d! \n" % getppid())
        sleep(time_cost)
        print("Download completed. Cost time %d ! \n" % (time_cost))




def main():
           start_time = time()
           t1 = DownloadTask("Wo Ai Lingzi")
           t1.start()

           t2 = DownloadTask("Wo Cao Lingzi Ju Ru!")
           t2.start()

           t1.join()
           t2.join()

           end_time = time()

           print("She le ,Lingzi! total time is %.3f" %(end_time-start_time))



if __name__ == "__main__":
    main()