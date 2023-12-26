'''
    Name: Meghan Brinkmann
    Date: February 11, 2023
    Class: CIS-108-M02 - Programming Fundamentals
    Program name: Average
    Description: a program to accept two tests, finds the
                average and prints the average.
'''

#       Input Section
name = input("Enter Your name please: ")
test1 = int(input("Your Score on the first test is? "))
test2 = int(input("Your Score on the second test is? "))

#       Processing Section
average = (test1 + test2) / 2

#       Output Section
print ("Hello", name, "Your Average is ", average)
