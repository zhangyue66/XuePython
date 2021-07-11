import random

class Card(object):
        #one card 1-k, 2joker,4 color

    def __init__(self,suite,face):
        self._suite = suite
        self._face = face


    @property
    def suite(self):
        return self._suite

    @property
    def face(self):
        return self._face

    def __str__(self):
        if self._face == 1:
            face_str = "A"
        elif self._face == 11:
            face_str = "J"
        elif self._face == 12:
            face_str= "Q"
        elif self._face == 13:
            face_str = "K"
        else:
            face_str = str(self._face)
        return "%s%s" %(self._suite,face_str)

    def __repr__(self):
        return self.__str__()



class Poker(object):
    #54 card#
    def __init__(self):
        self._cards = [Card(suite,face) for suite in "ABCD" for face in range(1,14)]
        self._current = 0

    @property
    def cards(self):
        return self._cards

    @property
    def suite(self):
        return self._suite


    def shuffle(self):
        # ramdom select one card from cards
        self._current = 0
        new_card = random.shuffle(self._cards)
        #random.shuffle(self._cards)


    @property
    def next(self):
        # give only one card
        card = self._cards[self._current]
        self._current += 1
        return card

    @property
    def has_next(self):
        if self._current <52:
            return True
        return False
        #return self._current < len(self._cards)

class Player(object):
    #player who play card. Here lets assume we have three players. Yue,Tina,Lingzi

    def __init__(self,name):
        self._name = name
        self._cards_on_hand = []

    @property
    def name(self):
        return self._name

    @property
    def cards_on_hand(self):
        return self._cards_on_hand

    #Player get a card
    def get_card(self,card):
        self._cards_on_hand.append(card)
        return "Player get a card successfully!"

    #sort card

    def sort_card(self):
        self._cards_on_hand.sort(key=lambda card : (card.suite,card.face))


# sorting rules -suite then face
#list.sort(key=)  ->https://www.programiz.com/python-programming/methods/list/sort
#def card_key(yue):
    #return (card.suite,card.face)
    #return len(card)

    #return yue.suite,yue.face
#AttributeError: 'Card' object has no attribute 'a'



def main():
    p = Poker()
    p.shuffle()

    P1 = Player("YUE")
    P2 = Player("Tina")
    P3 = Player("Lingzi")
    P4 = Player("xxJess")
    player_list = [P1,P2,P3,P4]

    #we have 3 players . so we can have 52/4 =13 round of next cards

    for round in range(13):
        for player in player_list:
            player.get_card(p.next)
    #yz_card = Card("ABCD",range(1,14))
    for player in player_list:
        print(player.name + ':', end=' ')

        player.sort_card()
        print(player.cards_on_hand)

if __name__ == "__main__":
    main()


