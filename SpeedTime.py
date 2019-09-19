#...

#Aim:   Write a program that will work out the distance travelled if the user enters in the speed and time.

#Author: Carlos Raniel Ariate Arro 
#Date:  06-09-2019

#...

#Asking user to input the speed and speed
speed = int(input("What is the speed of the car : "))
time = int(input("What is  the time taken for the car to travel " ))

#calculating the distance
distance = speed * time

#
print("The distance travelled is {} multiplied by {} which is {} km" .format(speed ,time,distance))