'''
    Name: Meghan Brinkmann
    Class: CIS 108 M02
    Date: February 28, 2023
    Prject Name: Hexagon
    Description: This program will take the name of the user
                 and length of one side of a hexagon, calculate
                 the area of the hexagon, and then say "Hello"
                 to the user and tell them the area of the hexagon.
'''

#constants

#imported modules
from math import sqrt

#input section
name = input("What is your name? ")
side = float(input("What is the length of the side? "))

#processing section
area = round(3/2 * sqrt(3) * side ** 2,2)
        
#output section
print('\nHello', name)
print('The area of the hexagon with')
print('Side =', side)
print('Is =', area)

input("\nPress Enter to Continue")
