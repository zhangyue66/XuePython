
class Classy():
    def __init__(self):
        self.items = ["yue"]
        print("the list value is " + str(self.items))

    def addItem(self,additem):
        self.additem = additem
        self.items.append(additem)
        print (self.items)
    """
    def getClassiness(self):
        point = 0
        for x in self.items:
            if "tophat" in self.items:
                point += 2
            elif "bowtie" in self.items:
                point += 4
            elif "monocle" in self.items:
                point += 5
            else:
                print("nothing need to change")

            print ("the fanciness point is " + str(point))
    """
    def getClassiness(self):
        point = 0
        for self.additem in self.items:
           if self.additem == "tophat":
            point += 2
           elif self.additem == "bowtie":
            point += 4
           elif self.additem == "monocle":
            point += 5
           else:
            print("nothing need to change")

        print("the fanciness point is " + str(point))



# Test cases
me = Classy()


print (me.getClassiness())

me.addItem("tophat")
print (me.getClassiness())


me.addItem("bowtie")
me.addItem("jacket")
me.addItem("monocle")

print (me.getClassiness())


