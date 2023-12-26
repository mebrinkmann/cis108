'''
    Name: Meghan Brinkmann
    Date: April 10, 2023
    Due Date: April 13, 2023
    Project: Hotel Statement
    Description: This program takes the customer's name, room number, days
                 stayed, and their internet and tv usage, calculates their
                 totals for each charge item, and displays the information
                 in an oprganized invoice statement.
'''
#import
import random

#constants
SINGLE = 225.0
FAMILY= 325.0
SUITE = 550.0
INTERNET_WIFI = 9.95
INTERNET_WIRED = 5.95
NO_INTERNET = 0
CABLE_TV = 9.95
BASIC_TV = 2.95
NO_TV = 0
LOCAL_TAX = 0.035
FMT = "<12,.2f"
INVOICE = random.randint(100,999)

def main():

    #input
    name = input('Enter Name: ')
    days = int(input('Enter Number of Days Stayed: '))
    room = int(input('Enter Room Number: '))
    if(room%100 <= 9):
        room_style = str('in a Single Room')
        room_charge=(SINGLE * days)
    elif(room%100 <= 19):
        room_style = str('in a Family Room')
        room_charge=(FAMILY * days)
    elif(room%100 <= 29):
        room_style = str('in a Suite')
        room_charge=(SUITE * days)
    elif(room%100 >= 30):
        print('You did not stay here')
        quit()
        
    print('\n\t\tInternet Access Usage\n\t\t---------------------')
    print('\t\t1--WiFi Connection')
    print('\t\t2--Wired Connection')
    print('\t\t3--No Internet Used')
    Internet=input('\tEnter Choice 1, 2, or 3: ')

    print('\n\t\tTV Usage\n\t\t---------------------')
    print('\t\t1--Cable Channels')
    print('\t\t2--Basic Channels')
    print('\t\t3--No TV Used')
    Tv=input('\tEnter Choice 1, 2, or 3: ')
        

    #processing
    if(Internet == '1'):
        wifi_charge = (INTERNET_WIFI * days)
        wifi_access = str('Wifi')
    if(Internet == '2'):
        wifi_charge = (INTERNET_WIRED * days)
        wifi_access = str('Wired')
    if(Internet == '3'):
        wifi_charge = (NO_INTERNET * days)
        wifi_access = str('None')

    if(Tv == '1'):
        tv_charge=(CABLE_TV * days)
        tv_access = str('Cable')
    if(Tv == '2'):
        tv_charge=(BASIC_TV * days)
        tv_access = str('Basic')
    if(Tv == '3'):
        tv_charge = (NO_TV * days)
        tv_access = str('None')

    total_charge = (room_charge + wifi_charge + tv_charge)
    taxes = (total_charge * LOCAL_TAX)
    grand_total = (total_charge + taxes)
    
    #output
    print('\n\n\t\t\tPCCC Palace Hotel')
    print('\n',name,'\'s Billing Statement','\t\t\tInvoice#: ',INVOICE,sep='')
    print('\n\tNumber of Days in Hotel: ',days,'\t',room_style,sep='')
    print('\n\tRoom Charges\t\t\t\t$',format(room_charge,FMT),sep='')
    print('\n\tInternet Charges\t',wifi_access,'\t\t$',format(wifi_charge,FMT),sep='')
    print('\n\tTelevision Charges\t',tv_access,'\t\t$',format(tv_charge,FMT),sep='')
    print('\n\tTotal Charges\t\t\t\t$',format(total_charge,FMT),sep='')
    print('\n\tLocal Taxes\t\t\t\t$',format(taxes,FMT),sep='')
    print('\n\t\tTotal Due\t\t$',format(grand_total,FMT),sep='')
    print('\n\n\tThank you for visiting PCCC Palace Hotel!\n\t\tHope to see you again!')
    
main()
input('\n\nPress Enter to Continue')
