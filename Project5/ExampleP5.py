"""
Name: Christopher Mora
class: cis 108
profesor: Atshan
project: this project will help you understand how to make a program usung functions. 
It will accept an input for name, length, width and price per square foot. process everything and print it out
in a nice customer recipt. 
"""
#project 5 using fuctions
from random import randint
from math import ceil

#constants
tax_rate = .0685

#this function accepts a name input 
def name_input():
    name = input("What is the name of the customer? :")
    return name

#this function accepts a data number entry as a float
def set_data():
    unit = float(input("\t\t\t\t:"))
    return unit

#this function will make a random number between 100 and 1000       
def recipt():
    number = randint(100,1000)
    return number
#this function finds the area of two numbers using ceiling
def find_area(l,w):  
    area = l *w
    return ceil(area)  
#this function find the product of two numbers
def find_product(num1, num2):
    product = num1 * num2
    return product
    
def main():
    #input
    name = name_input()
    print("what is the length of the carpet?")
    length = set_data()
    print("what is the width of the carpet?")
    width = set_data()
    print("what is the price per square foot?")
    price_per_foot = set_data()

    area = find_area(length, width)
    subtotal =  find_product(price_per_foot,area)
    sales_tax = find_product(subtotal,tax_rate)
    total = find_product(subtotal,sales_tax)

    print("Welcome to the PASSAIC COUNTY CARPETING COMPANY")
    print("-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-")  
    print("\nCustomer Information :")  
    print("\nCustomer number order:\t\t#",recipt())
    print("\n\tCustomer Name :",name)
    print("\tCarpet Size :",area,"Square Feet")
    print("\nCharges")
    print("\tCarpet Cost :\t\t","$"+ str(format(subtotal,".2f")))
    print("\tTaxes:\t\t\t","$"+str(format(sales_tax,".2f")))
    print("\t\t\t\t__________")
    print("Total Cost:\t\t\t", "$"+str(format(total,".2f")))
    print("\n", name,",Thank You for using PCCCC")
main()  
main()
main()  

input("\npress enter")
"""
Welcome to the PASSAIC COUNTY CARPETING COMPANY  
-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-

Customer Information :

Customer number order:          # 793

        Customer Name : chris
        Carpet Size : 557 Square Feet

Charges
        Carpet Cost :            $10165.25
        Taxes:                   $696.32
                                __________
Total Cost:                      $7078263.07

 chris ,Thank You for using PCCCC

press enter
"""
