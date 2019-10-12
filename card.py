# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 18:59:22 2019

@author: User
"""

import random

class card:
    def __init__(self,suit='',value=0):
        self.suit=suit
        self.value=value
    
    
    def card_test(self):
        print(self.suit)
        print(self.value)
    

    

def card_sorted(cards,flag):
    card_vals =[]
    sorted_cards=[]
    for card in cards:
        temp_suit=suits.index(card.suit)
        temp_val = values.index(card.value)
        
        card_vals.append((temp_val,temp_suit))
    pass1= [i[0] for i in sorted(enumerate(card_vals),key=lambda x:x[1],reverse=flag)] 
    for idx in pass1:
        sorted_cards.append(cards[idx])
        
    return sorted_cards

def output(card):
    
    print(card.value)
    print(card.suit)
    print("\n")

suits = ["Hearts","Spades","Clubs","Diamonds"] #precedence encoded in index
values = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"] # precedence encoded in index
queen_spades =card(suit="Spades",value="Q")
cards = []
flag = False
i=0
print("Enter Y/y for ascending order."+
      "Enter N/n for descending order")
choice = str(input()).lower()
if(choice == 'y'):
    flag = False
elif(choice=='n'):
    flag = True
else:
    print("wrong option entered.Proceeding with ascending order")

#for creating random pack of 10 cards
while i<10:
    rand_suit = suits[random.randint(0,3)]
    rand_val = values[random.randint(0,12)]
    rand_card = card(suit=rand_suit,value=rand_val)
    cards.append(rand_card)
    i+=1
sorted_cards = card_sorted(cards,flag)
idx=0
for card in sorted_cards:
    print("Card "+str(idx+1)+":"+"\n")
    output(card)
    idx+=1


   
        