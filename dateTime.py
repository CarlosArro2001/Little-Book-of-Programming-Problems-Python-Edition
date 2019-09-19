#...

#Aim:   Write a program to work out how many days you have lived for.
#       Enter the date of birth
#       Get today's date
#       Get the difference in days between the two dates
#       Display result

#Author: Carlos Raniel Ariate Arro
#Date: 06-09-2019


#...

#imports 
import datetime #used to import classes for manipulating date and time in both complex and simple ways.

#Get the users date of birth
year  = int(input("In what year were you born"))
month = int(input("In what month is your birthday (write as a two-digit number)"))
day = int(input("What is the day of your birthday"))

#Convert to datetime format 
birthdate = datetime.date(year , month , day)

#Get today 
today = datetime.date.today()

#Work out how many days since birthday 
daysAlive = (today - birthdate).days

#Display how many days since birthday
print("You have been alive for {} days .".format(daysAlive))