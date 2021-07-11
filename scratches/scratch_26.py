#Test module
'''
class Car(object):

    def __init__(self,name,hp,mp):
        self._name = name
        self._hp = hp
        self._mp = mp

    def __str__(self):
        return '~~~%s Automan~~~\n' % self._name + \
               'Life %d\n' % self._hp + \
               'Magic: %d\n' % self._mp




yue = Car("YueZhang",2000,1000)

print(yue)

'''

#1 what is being returned.->same result

hp1 =0
hp2= 0
hp3 =0

h = [hp1,hp2,hp3]

def is_alive():

    for hp in h:
        if hp > 0:
            return True
        else:
            return  False


print(is_alive())



def is_alive_1():

    for hp in h:
        if hp > 0 :
            return True
    return False

print("what?",is_alive_1())


# return hp

hphp = 0

def alive():
    if hphp >0:
        return hphp
    return False

print(alive())


def alive1():

        return hphp >0

print(alive1())


# Exercise 3 generate 52 cards

class Card(object):
    def __init__(self,suite,face):
        self.suite = suite
        self.face = face

    def __str__(self):
        return "%s%s" %(self.suite,self.face)

    def __repr__(self):
        return self.__str__()

card = [ Card(suite,face) for suite in "ABCD"  for face in range(1,14)]


print(type(card))

print(card)


