"""  
    Name: Meghan Brinkmann
    Class: CIS 108
    Date:05/09/2023
    Program Name: Hotel Statement (functions)
    Description: This program takes the customer's name, room number, days
                 stayed, and their internet and tv usage, calculates their
                 totals for each charge item, and displays the information
                 in an organized invoice statement using functions.
"""

#imports
from random import randint

#constants
SINGLE = 225.0
FAMILY= 325.0
SUITE = 550.0
INTERNET_WIFI = 9.95
INTERNET_WIRED = 5.95
CABLE_TV = 9.95
BASIC_TV = 2.95
LOCAL_TAX = 0.035
FMT = "<12,.2f"
INVOICE = randint(100,999)

#this function accepts the name, days, and room
def setdata():
    name = input('Enter Name: ')
    days = int(input('Enter Number of Days Stayed: '))
    room = int(input('Enter Room Number: '))
    return name, days, room

#this function calculates the room type and charges
def setroom(room,days):
    if(room%100 <= 9):
        roomcharges=(SINGLE * days)
        roomtype = str('in a Single Room')
    elif(room%100 <= 19):
        roomcharges=(FAMILY * days)
        roomtype = str('in a Family Room')
    elif(room%100 <= 29):
        roomcharges=(SUITE * days)
        roomtype = str('in a Suite')
    elif(room%100 >= 30):
        roomtype = str('You did not stay here')
        quit()
    return roomtype, roomcharges

#this function calculates the net type and charges
def setnet(days):
    internet = input('Did you use the internet? : ')
    if(internet == 'Y' or internet == 'y'):
        print('\n\t\tInternet Access Usage\n\t\t---------------------')
        print('\t\t1--(W)iFi Connection')
        print('\t\t2--(w)ired Connection')
        internet = input('\tEnter Choice: ')
        if(internet == '1'):
            netcharges = (INTERNET_WIFI * days)
            nettype = str('Wifi')
        elif(internet == '2'):
            netcharges = (INTERNET_WIRED * days)
            nettype = str('Wired')
    elif(internet == 'N' or internet == 'n'):
        netcharges = 0
        nettype = str('None')
    return nettype, netcharges

#this function calculates the tv type and charges
def settv(days):
    tv = input('Did you watch television? : ')
    if(tv == 'Y' or tv == 'y'):
        print('\n\t\tTV Usage\n\t\t---------------------')
        print('\t\t1--(C)able Channels')
        print('\t\t2--(B)asic Channels')
        tv = input('\tEnter Choice: ')
        if(tv == '1'):
            tvcharges = (CABLE_TV * days)
            tvtype = str('Cable')
        elif(tv == '2'):
            tvcharges = (BASIC_TV * days)
            tvtype = str('Basic')
    elif(tv == 'N' or tv == 'n'):
        tvcharges = 0
        tvtype = str('None')
    return tvtype, tvcharges

#this function calculates the total charges
def findtotal(roomcharges, netcharges, tvcharges):        
    totalcharges = (roomcharges + netcharges + tvcharges)
    return totalcharges

#this function formats the name, room, day, and room type
def heading(name, room, days, roomtype): 
    print('\n\n\n\t\t\tPCCC Palace Hotel')
    print('\n',name,'\'s Billing Statement','\t\t\tInvoice#: ',INVOICE,sep='')
    print('\n\tNumber of Days in Hotel: ',days,'\t',roomtype,sep='')

#this function formats the types and totals of charges
def output(roomcharges, netcharges, nettype, tvcharges, tvtype):
    print('\n\tRoom Charges\t\t\t\t$',format(roomcharges,FMT),sep='')
    print('\n\tInternet Charges\t',nettype,'\t\t$',format(netcharges,FMT),sep='')
    print('\n\tTelevision Charges\t',tvtype,'\t\t$',format(tvcharges,FMT),sep='')

#this function calculates the taxes and grand total and formats the total charges output
def footing(totalcharges): 
    taxes = (totalcharges * LOCAL_TAX)
    grandtotal = (totalcharges + taxes)
    print('\n\tTotal Charges\t\t\t\t$',format(totalcharges,FMT),sep='')
    print('\n\tLocal Taxes\t\t\t\t$',format(taxes,FMT),sep='')
    print('\n\t\tTotal Due\t\t$',format(grandtotal,FMT),sep='')
    print('\n\n\tThank you for visiting PCCC Palace Hotel!\n\t\tHope to see you again!')

def main():
    name, days, room = setdata()
    roomtype, roomcharges = setroom(room,days)
    nettype, netcharges = setnet(days)
    tvtype, tvcharges = settv(days)
    totalcharges = findtotal(roomcharges, netcharges, tvcharges)
    heading(name, room, days, roomtype)
    output(roomcharges, netcharges, nettype, tvcharges, tvtype)
    footing(totalcharges)
    
main()
input("\n\nPress Enter to Continue") 
