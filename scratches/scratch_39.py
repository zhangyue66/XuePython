from time import time,sleep
from threading import Thread
from threading import Lock



class Account(object):
    def __init__(self):
        self._balance = 0
        self._lock =Lock()

    def deposit(self,money):
        self._lock.acquire()
        new_balance = self._balance+ money
        sleep(0.01)
        print("Deposit money done!")
        self._balance = new_balance
        self._lock.release()

    @property
    def balance(self):
        return self._balance



class AddMoney(Thread):
    def __init__(self,account,money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)



def main():

    account = Account()
    threads = []

    for customer in range(100):
        t = AddMoney(account,1)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

    print("This account has money: %d Dollar!" %(account.balance))


if __name__ == "__main__":
    main()