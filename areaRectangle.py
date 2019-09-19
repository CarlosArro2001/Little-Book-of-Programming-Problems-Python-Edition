#...

#Aim:   Write a program to work out the areas of a rectangle. Collect the width and height of the rectangle from the keyboard, calculate the area and display the result.

#Author : Carlos Raniel Ariate Arro
#Date   : 06-09-2019

#...

#Asking the user the length and width.
length = int(input("What is the length of the rectangle? "))
width = int(input("What is the height of the rectangle? "))

#Calculate the area of the rectangle.
area =  length * width



#Displaying the area as well as  the dimensions involved.
print("The area of a recntalge with dimensions {} by {} is {}".format(length,width,area)) #.format allows you to output whats inside variables in a string.