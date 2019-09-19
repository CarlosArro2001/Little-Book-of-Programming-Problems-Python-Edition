#...

#Aim : Write a program that will accept someones date of birth and work out whether they can voite (i.e Are they 18?)

#Author : Carlos Raniel Ariate Arro
#Date   : 07-09-2019


#...

import datetime


# Constants
year = datetime.timedelta(days=365)
voteAge = 18 * year

#	Get the users date of birth
year = input("\nIn which year were you born? ")
month = input("In which month were you born? ")
date = input("On what date were you born? ")
dateOfBirth = datetime.date(int(year), int(month), int(date))

# Work out the date when user can vote
dateOfVote = datetime.date(int(year)+18, int(month), int(date))

# Get the date today
dateToday = datetime.date.today()

# Check if today is after the date of voting
if dateOfVote <= dateToday :
	print("\nCongratulations, you can vote.\n")
else :
	print("\nI am sorry you are not old enough to vote.\n")