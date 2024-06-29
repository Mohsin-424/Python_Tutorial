import random
suits = {  'Hearts' , 'Diamonds' , 'Spades' , 'Clubs' }
ranks = { 'Two' , 'Three' , 'Four' , 'Five' , 'Six' , 'Seven' , 'Eight' , 'Nine' , 'Ten'}
values = {
    'Two':2 , 'Three':3 , 'Four':4 , 'Five':5 , 'Six':6 , 'Seven':7 , 'Eight':8 , 'Nine':9 , 'Ten':10 , 'Jack': 11 , 'Queen': 12 , "King":13 , "Ace":14  }

# Card Class
class Card():
    def __init__(self , suit , rank ):
        self.suit = suit 
        self.rank = rank 
        
    def __str__( self ):
        return self.rank + "  of  " + self.suit
# Class Deck 
class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in suits:
                self.deck.append(Card(suit,rank))
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return 'The deck has:' + deck_comp
    def shuffle(self):
        random.shuffle(self.deck)
    def deal(self):
        single_card = self.deck.pop()
        return single_card
    
        
test_deck = Deck()
test_deck.shuffle()

print(test_deck)

# Hand Class 
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    def add_card( self , card ):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
        
        
    def adjust_for_ace(self):
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1
            
    
zero = 0
one = 1
two = 2

if 1:
    print('TRUE')
    
test_deck = Deck()
test_deck.shuffle()
# Player 
test_player = Hand()
# Deal 1 card from the deck CARD (suit , rank)

pulled_card = test_deck.deal()

print( pulled_card)
test_player.add_card(pulled_card)

print(test_player.value)


# Class Chip
class Chips:
    def __init__(self , total = 1000 ):
        self.total = total 
        self.bet = 0
    def win_bet(self):
        self.total += self.bet
    def lose_bet(self):
        self.total -= self.bet
         
#  WWrite a funin for taking bets
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('How many chips would you like to be '))
        except:
            print("Sory Please provide an integer")
        else:
            if chips.bet > chips.totals:
                print("Sorry, you do not have engough chips! YUo have: ")
            else:
                break
# Hit class
def hit(deck , hand):
    single_card = deck.deal()
    hand.add_cacrd(single_card)
    hand.adjust_for_ace()
    
# HIT_oR Stand functions
def hit_or_stand( deck , hand ):
    global playing 
    while True:
        x = input('Hit os Stand? Enter  h or s')
        if x[0].lower() == 'h':
            hit(deck , hand)
        elif x[0].lower() == 's':
            print("Player stands Dealers Turn")
            playing = False
        else:
            print("Sorry! , I did not undersatnd oly!")
            
            
def player_busts(player, dealer , chips):
    print('BUS PLAYER!')
    chips.lose_bet()
    
def player_wins(player, dealer , chips):
    print('PLAYER! Wins')
    chips.win_bet()
    
def dealer_busts(player, dealer , chips):
    print('BUS PLAYER! Dealer Busted.')
    chips.win_bet()
    
def dealer_busts(player, dealer , chips):
    print('BUS PLAYER!')
    chips.lose_bet()
    
    
def push(player, dealer):
    print('Dealer and Player Tie!  Push.')
    
# Step 11
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except:
            print("Sorry you provide an interger")
        else:
            if chips.bet > chips.total:
                print("Sorry , you do not have enough chips! Yo have have : {}" .format(chips.total()))
            else:
                break
            
            # Will be continued furhter tommorrow.....
            
            
            
            
            



    
        
            
        
            
            
     
        



    
    