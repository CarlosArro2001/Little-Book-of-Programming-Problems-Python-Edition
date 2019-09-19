#...

#Aim:   Make a game of rock , papers , scissors against the computer 
#       Tell the user to enter either rock , paper or scissors.
#       Get the response.
#       Generate a random number from 1 to 3.
#       (1 = rock , 2 = paper , 3 = scissors)
#       Compare user selection and computer selection
#       Display who wins.


#Author : Carlos Raniel Ariate Arro.
#Date   : 10-09-2019.

#...

#   1 = rock 
#   2 = paper
#   3 = scissors 

userChoice = int(input('''
Rock, Paper, Scissors Game
======================
  Make your choice:
  1 - Rock
  2 - Paper
  3 - Scissors
'''))

# get the computer generated value
computerChoice = randint(1, 3)

if userChoice == computerChoice :
    print("The computer chose the same as you so it is a draw\n")
elif userChoice == rock :
    if computerChoice == paper :
        print("The computer chose paper so you lose\n")
    else :
        print("The computer chose scissors so you win\n")
elif userChoice == paper :
    if computerChoice == scissors :
        print("The computer chose scissors so you lose\n")
    else :
        print("The computer chose rock so you win\n")
elif userChoice == scissors :
    if computerChoice == rock :
        print("The computer chose rock so you lose\n")
    else :
        print("The computer chose paper so y1ou win\n")
else :
    print("Error incorrect input!")