from abc import ABCMeta,abstractmethod
from random import randint,randrange


class Fighter(object,metaclass=ABCMeta):

    __slots__ = ("_name","_hp")

    def __init__(self,name,hp):
        self._name = name
        self._hp = hp



    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp


    @hp.setter
    def hp(self,hp):
        self._hp = hp if hp >=0 else 0
        #if hp >0 :
            #self._hp = hp
        #else:
            #hp =0
    '''
    @property
     def is_alive(self):
        return True
    '''

    @property
    def alive(self):
        return self._hp >0

    @abstractmethod
        # define a attack method
    def attack(self,other):
        #other can be another object of fighter.
        #hp will decrease based on different value in Class Automan or Monster
        pass


class Automan(Fighter):
    #Automan has attack damage (15,25)
    __slots__ = ("_name","_hp","_mp")


    def __init__(self,name,hp,mp):
        super().__init__(name,hp)
        self._mp = mp

    def attack(self,other):
        other.hp -= randint(15,25)
        return other.hp

    # attack damage random from (45,75) if mp >50 , mp increase by 10 every round, start value is 10
    def huge_attack(self,other):
        if self._mp >= 50:
            self._mp -= 50
            attack_damage = randint(45,75)
            if attack_damage >= self._hp*(3/4):

                attack_damage = attack_damage
            else:
                attack_damage = 50
            other.hp -= attack_damage
            return True
        else:
            #trigger a normal attack if mp is not bigger than 50
            self.attack(other)

            return False


    #maigc attack is multi attack. it can attack all monsters . attack_damage is small (10,15) range.
    def magic_attack(self,others):
        if self._mp >= 20:
            self._mp -= 20
            for other in others:
                if other.alive:
                    other.hp -= randint(10,15)
                return True
        else:
            return False


    def heal(self):
        self._mp += 10
        return self._mp


    def __str__(self):
        # +\ code is too long. use this to start another line
        return "~~~%sAutoman~~~\n" % self._name + \
            "HP : %d\n" % self._hp + \
            "MP : %d\n" % self._mp


class Monster(Fighter):

    __slots__ = ("_name","_hp")

    '''
    # no need to init varaiable if son class is having same variable as super class
        def __init__(self,name,hp):
        super().__init__()
    '''

    def attack(self,other):
        attack_damage = randint(10,15)
        other.hp -= attack_damage

    def __str__(self):
        return "~~~%sMonster~~~\n" % self._name + \
            "HP : %d \n" % self._hp

def is_any_alive(monsters):
    for monster in monsters:
        #if monster.alive > 0:
            #return True
    #return False
        if monster.alive >0:
            return True
        else:
            return False

def select_alive_one(monsters):
    monsters_len = len(monsters)
    while True:
        index = randrange(monsters_len)
        monster = monsters[index]
        if monster.alive >0 :
            return monster

def disply_info(automan,monsters):
    print(automan)
    for monster in monsters:
        print(monster,end="")




def main():
    u =Automan("Yue Zhang",600,10)

    m1 = Monster("Tina",200)
    m2 = Monster("Minshan",400)
    m3 = Monster("Yuri",188)

    monsters = [m1,m2,m3]

    fight_round = 1

    while u.alive and is_any_alive(monsters):
        print('========第%02d Round========' % fight_round)
        monster = select_alive_one(monsters)

        # 60% attack, 30% huge attack, 10% magic attack
        skill = randint(1,10)

        if skill <= 6:
            print('%s使用普通攻击打了%s.' % (u.name, monster.name))
            u.attack(monster)
            print('%s的魔法值恢复了%d点.' % (u.name, u.heal()))
        elif skill <=9 :
            if u.magic_attack(monsters):
                print("%s 使用魔法成功！" % u.name)
            else:
                print("%s 使用魔法失败！" % u.name)
        else:
            if u.huge_attack(monster):
                print("%s 使用必杀击打了 %s" % (u.name,monster.name))
            else:
                print("%s 使用普通击打了 %s" % (u.name,monster.name))
                print("%s 的魔法恢复了 %d 点！" %(u.name,u.heal()))
        if monster.alive > 0:
            print("%s回击了%s" % (monster.name,u.name))
            monster.attack(u)
        disply_info(u,monsters)
        fight_round += 1
    print("====回合结束！=====")
    if u.alive > 0:
        print("奥特曼胜利！")
    else:
        print("怪兽胜利！")



if __name__ == "__main__":
    main()


