import random
def random_int_list(start, stop, length):
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    length = int(abs(length)) if length else 0
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list
class MinStack:
    def __init__(self,stack):
        self.stack = []
        self.mini = float("inf") # record minimum number using greedy
        #self.minus = 0



    def push(self,n):
        if len(self.stack) == 0:
            self.mini = n
            self.stack.append(0)
        self.stack.append(n-self.mini)
        if n < self.mini:
            self.mini = n

    def pop(self):
        val = self.stack[-1]
        if val >= 0:
            return self.stack.pop()+self.mini
        else: # val < self.mini need to recover
            yz = self.stack.pop()

            self.mini -= yz
            return self.mini





    def getMin(self):
        return self.mini
input_list = random_int_list(-100, 100, 50)
print(input_list)

time_to_pop = random.randint(1,50)

a = MinStack([])
for i in range(len(input_list)):
    a.push(input_list[i])
for i in range(time_to_pop):
    print("int to be popped is {}".format(a.pop()))
    print("int did be popped is {}".format(input_list.pop()))

print("list after {} pop operation - {}".format(time_to_pop,input_list))
print(a.getMin())
print(min(input_list))