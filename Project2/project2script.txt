'''
    Name: Meghan Brinkmann
    Due Date: March 16, 2023
    Date: March 10, 2023
    Course: CIS 108 M02
    Project: Tuition
    Description: This program takes the student's name, ID number,
                 and number of credits, calculates the total tuition
                 as well as its breakdown, and gives the
                 information in an organized format.
'''

# constant
COST_PER_CREDIT = float(177.00)
GEN_COST_PER_CREDIT = float(23.50)
ACT_FEE_PER_CREDIT = float(2.90)
ATH_FEE_PER_CREDIT = float(6.60)
TECH_FEE_PER_CREDIT = float(22.00)

REG_FEE_PER_SEMESTER =  float(50.00)

# import
import random

def main():

    # input
    name = input("Student's Name: ")
    ID = int(input("Student's ID#: "))
    credit = float(input ("Number of Credits: "))

    # processing
    CreditCharge = (credit * COST_PER_CREDIT)
    GenColFee = (credit * GEN_COST_PER_CREDIT)
    StudActFee = (credit * ACT_FEE_PER_CREDIT)
    AthFee = (credit * ATH_FEE_PER_CREDIT)
    TechFee = (credit * TECH_FEE_PER_CREDIT)

    Total = (CreditCharge + GenColFee + StudActFee + AthFee + TechFee + REG_FEE_PER_SEMESTER)

    # output
    print("\n\n\t\tPassaic County Community College")
    print("\nName: ",name,"\t\tID#: ",ID,"\t\tInvoice #: ",random.randint(1000,10000))
    print("Number of Credits: ",credit,"\tCost Per Credit: \t$",format(COST_PER_CREDIT,"<5.2f"))
    print("\n\t\tCredit Charges: \t$",format(CreditCharge,"<10.2f"))
    print("\t\tGeneral College Fees: \t$",format(GenColFee,"<10.2f"))
    print("\t\tStudent Activity Fees: \t$",format(StudActFee,"<10.2f"))
    print("\t\tAthletic Fees: \t\t$",format(AthFee,"<10.2f"))
    print("\t\tTechnology Fees: \t$",format(TechFee,"<10.2f"))
    print("\t\tRegistration Fee: \t$",format(REG_FEE_PER_SEMESTER,"<10.2f"))
    print("\n\tTotal Charges for Semester: \t$",format(Total,"<10.2f"))
    print("\n\n\t\t",name,", Enjoy Your Semester!",sep='')


main()
input("\n\n\nPress Enter to Continue")
