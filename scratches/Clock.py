# Exercise 1 Define a Class of Clock

import time

class Clock(object):
    def __init__(self,hour,minute,second,brand):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.brand = brand


    def run(self):
        self.second +=1
        if self.second ==60:
            self.second =0
            self.minute += 1
            if self.minute == 60:
                self.minute =0
                self.hour += 1
                if self.hour ==24:
                    self.hour =0


    def show(self):
        #while True:
            print("%02d:%02d:%02d" %(self.hour,self.minute,self.second))

    def show_brand(self):
        print("this clock brand is %s" %(self.brand))



rolex = Clock(23,59,40,"Rolex")
rolex.show_brand()
while True:
    rolex.run()
    time.sleep(1)
    rolex.show()





