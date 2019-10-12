# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 19:25:27 2019

@author: User
"""

import card as cs
import random

suits = ["Hearts","Spades","Clubs","Diamonds"] #precedence encoded in index
values = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"] # precedence encoded in index
queen_spades = cs.card(suit="Spades",value="Q")
cards = []
i=0
#for creating random pack of 10 cards
while i<10:
    rand_suit = suits[random.randint(0,3)]
    rand_val = values[random.randint(0,12)]
    card = cs.card(suit=rand_suit,value=rand_val)
    cards.append(card)
    i+=1
    

def card_sorted(cards):
    card_vals =[]
    sorted_cards=[]
    for card in cards:
        temp_suit=suits.index(card.suit)
        temp_val = values.index(card.value)
        
        card_vals.append((temp_val,temp_suit))
    pass1= [i[0] for i in sorted(enumerate(card_vals),key=lambda x:x[1])] 
    #pass2 = [i for i  in sorted(pass1,key=lambda x:x[0])]
    for idx in pass1:
        sorted_cards.append(cards[idx])
        
    return sorted_cards

def output(card):
    
    print(card.value)
    print(card.suit)
    print("\n")
sorted_cards = card_sorted(cards)
idx=0
for card in sorted_cards:
    print("Card "+str(idx+1)+":"+"\n")
    output(card)
    idx+=1

