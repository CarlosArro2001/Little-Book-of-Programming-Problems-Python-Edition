#... 

#Aim    :  Write a program that will generate a random playing cards , when the return return is pressed. 
#          Rather than generate a random number from 1 to 52 . Create two random numbers - one for the suit and one for the card.

#Author : Carlos Raniel Ariate Arro
#Date   : 09-09-2019

#...

#imports
import random
#Array for the suits 
suits = ["Hearts","Spades","Clubs","Diamonds"]
#Array for the numbers 
numbers = ["Ace","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","King","Queen","Jack"]

#press enter to output a random card 
input()

#two variables for storing the randomly generated , one for the suit and one for the numbers 


randSuit = random.choice(suits)
randNum  = random.choice(numbers)
cardName = randSuit + " of " + randNum

if cardName != randSuit + " of " + "King" or cardName != randSuit + " of " + "Queen" or cardName != randSuit + " of " + "Jack" : 
    print(cardName)
else:
    randSuit = random.choice(Suits)
    randNum  = random.choice(numbers)
    cardName = randSuit + " of " + randNum

#Extension - put it into a loop. 