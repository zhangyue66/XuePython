from threading import Thread
from time import time,sleep
from random import randint


def download_file(file_name):
    print("Start downloading file %s now!" %(file_name))
    time_cost = randint(5,10)
    sleep(time_cost)
    print("Download completed. Cost time %d" %time_cost)




def main():

    start_time = time()

    t1 = Thread(target=download_file,args=("Lingzi Wo Ai",))

    t1.start()

    t2 = Thread(target=download_file,args=("Lingzi Mei Ru",))

    t2.start()


    t1.join()
    t2.join()

    end_time = time()

    print("Download finish! Totally taking %.3f" %(end_time-start_time))



if __name__ == "__main__":
    main()
