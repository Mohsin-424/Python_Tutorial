# A card War Game
# Step 1 
# Card , Suit , Rank , Value

import random
suits = {  'Hearts' , 'Diamonds' , 'Spades' , 'Clubs' }
ranks = { 'Two' , 'Three' , 'Four' , 'Five' , 'Six' , 'Seven' , 'Eight' , 'Nine' , 'Ten'}
values = {
    'Two':2 , 'Three':3 , 'Four':4 , 'Five':5 , 'Six':6 , 'Seven':7 , 'Eight':8 , 'Nine':9 , 'Ten':10 , 'Jack': 11 , 'Queen': 12 , "King":13 , "Ace":14  }

#  Defining a Card class

class Card:
    def __init__(self , suit , rank ):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    def __str__(self):
        return self.rank + "  of  " + self.suit
    
# Calling back to class

three_of_clubs = Card("Clubs" , 'Three')
result = Card("Hearts" , 'Two')
print(result.value)
print(three_of_clubs)
print(three_of_clubs.rank)
print(three_of_clubs.suit)

# Step2 Deck Class....

class Deck:
    def __init__(self):
        self.all_cards = [ ]
        
        for suit in suits:
            for rank in ranks:
                # Creating here Card Object.
                created_card = Card( suit , rank )
                self.all_cards.append( created_card )
                
    def shuffle( self ):
        random.shuffle( self.all_cards )
    def deal_one( self ):
        
        # return self.all_cards.append("One")
        return self.all_cards.append("Two")
        # return self.all_cards.pop()
    
# calling back function..
new_card = Deck()
cards = new_card.all_cards
print( cards )

for card_object in new_card.all_cards:
    print(card_object)
# Access Bottom card
bottom_card = new_card.all_cards[-1]
print(f' Last Card is : {bottom_card}')
# Deal one card access
mycard = new_card.deal_one()
print(f'My deal card is :   {mycard}')
 
#  Step 3:  Player Class Going on here........

class Player:
    def __init__( self , name ):
        self.name = name
        self.all_cards = []
    def remove_one( self ):
        return self.all_cards.pop()
    def add_cards( self , new_carrds ):
        if type(new_card) == type([]):
            # List of all multiple card objects
            self.all_cards.extend(new_carrds)
        else:
            self.all_cards.append(new_carrds)
    def __str__(self):
        return f'Player { self.name} has  { len (self.all_cards ) } cards.'
# Calling back class

new_player = Player('Mohsin')
print(new_player)

print(new_player.add_cards(mycard))
print(new_player.all_cards[0])

print(new_player.add_cards([mycard , mycard , mycard]))
print(new_player)

# Game logic part 1 ........
# Game Setup ......

player_one = Player('One')
player_two = Player('Two')

new_deck = Deck()
new_deck.shuffle()



for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True
round_num = 0
while game_on:
    round_num += 1
    print(f'Round {round_num}')
    
    if (len(player_one.all_cards)) ==0:
        print('Player one out of cards ! Player 2 wins!')
        game_on = False
        break
        
    if (len(player_two.all_cards)) ==0:
        print('Player two out of cards ! Player 1 wins!')
        game_on = False
        break
    
    # Starting New Round
    player_one_cards = [ ]
    player_one_cards.append(player_one.remove_one())
    
    player_two_cards = [ ]
    player_two_cards.append(player_two.remove_one())
       
       
    #    At war Round
    at_war = True
    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one_cards(player_one_cards)
            player_two_cards(player_two_cards)
            at_war = False
            
        elif player_one_cards[-1].value > player_two_cards[-1].value:
            player_one_cards(player_one_cards)
            player_two_cards(player_two_cards)
            at_war = False
        else:
            print('WAR!')
            if len(player_one.all_cards) < 3:
                print('Player one unable to declare war')
                print('Player Two Wins')
                game_on = False
                break
            elif len(player_one.all_cards) < 3:
                print('Player Two unable to declare war')
                print('Player One Wins')
                game_on = False
                break
            else:
                for num in range(3):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
                
                


    