#Family name: Prabh Simran Singh Badwal
# Student number: 300057572
# Course: IT1 1120
# Assignment Number 3 Part 2


import random

def main():
              
       deck = [] # deck of cards
       suits = ['Hearts','Diamonds','Spades','Clubs']
       ranks = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
       
       # create a list of 52 cards
       # each card is a list of (suit,rank)
       for i in range(len(suits)):
           
              for j in range(len(ranks)):

                             deck.append([suits[i],ranks[j]])
       # shuffle the deck
       for i in range(len(deck)//2):
           
              ind1 = random.randint(0,len(deck)-1)
              ind2 = random.randint(0,len(deck)-1)
              
              if ind1 != ind2:
                 card1 = deck[ind1]
                 card2 = deck[ind2]
                 
                 if ind1 > ind2:
                    del deck[ind1]
                    del deck[ind2]
                    deck.insert(ind2,card1)
                    deck.insert(ind1,card2)
                    
                 else:
                    del deck[ind2]
                    del deck[ind1]
                    deck.insert(ind1,card2)
                    deck.insert(ind2,card1)  
       
       picks = 0
       spade_card = ""
       diamond_card = ""
       heart_card=""
       club_card = ""
       
       while(len(spade_card) == 0 or len(diamond_card) == 0 or len(heart_card) == 0 or len(club_card) == 0):
          ind = random.randint(0,len(deck)-1) # randomly pick a card
          if(deck[ind][0].lower() == 'hearts'):
                         heart_card = deck[ind][1] + ' of ' + deck[ind][0]
          elif(deck[ind][0].lower() == 'spades'):
                         spade_card = deck[ind][1] + ' of ' + deck[ind][0]
          elif(deck[ind][0].lower() == 'diamonds'):
                         diamond_card = deck[ind][1] + ' of ' + deck[ind][0]
          else:
               club_card = deck[ind][1] + ' of ' + deck[ind][0]
          picks = picks + 1

      

       #output
       print(spade_card)
       print(diamond_card)
       print(heart_card)
       print(club_card)

       print('Number of picks : %d' %(picks))

main() 
