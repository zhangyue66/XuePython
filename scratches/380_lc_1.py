import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        self.rand = []



    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.dict:
            self.dict[val] = val
            self.rand.append(val)
            return True
        else:
            return False


    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.dict:
            self.dict.pop(val)
            self.rand.remove(val)
            return True

        else:
            return False


    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """

        if len(self.rand) == 0:
            return
        else:
            tmp = random.randrange(0,len(self.rand),1)

            return self.rand[tmp]



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()