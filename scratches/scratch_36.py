from multiprocessing import Process,Pipe
from time import  time,sleep

def sender(word,conn):
    conn.send(word)
    conn.send("TESTTESTYUE")
    print("Sent the message: {}".format(word))
    conn.close()

def receiver(conn):
    msg = conn.recv()
    print("Received the message: {}".format(msg))

if __name__ == "__main__":
    word = ["First_word","2nd_word"]

    conn1,conn2 = Pipe()

    p1 = Process(target=sender,args=(word,conn1,))
    p2 = Process(target=receiver,args=(conn2,))

    p1.start()
    p2.start()

    p1.join()
    p1.join()

    p3 = Process(target=receiver,args=(conn2,))
    p3.start()
    p3.join()







