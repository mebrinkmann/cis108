'''
    Name: Meghan Brinkmann
    Date: April 24, 2023
    Due Date: May 2, 2023
    Project: GPA Loops
    Description: This program takes the name, ID number, number of courses,
                 course ID, credits and grade for each course, calculates
                 the grade point average and displays the name, ID number,
                 total credits and points, and GPA.
'''
#constants
GRADE_A = 4
GRADE_B = 3
GRADE_C = 2
GRADE_D = 1
GRADE_F = 0

#imported

def main():
    #input
    total_points = 0 #accumulator for points
    total_credits = 0 #accumulator for credits
    Name = input("Student's Name: ")
    Id = int(input("Student's ID#: "))
    if(Id not in range(0,9999)):
        Id = int(input("Wrong ID#, Re-Enter Student's ID#: "))
    Class = int(input('Number of Courses: '))
    for Class in range(Class):
        Course = input("Course ID: ")
        Credits = int(input("Number of Credits for Course: "))
        total_credits += Credits
        Grade = input("Enter Grade for Course: ")[0].upper()     
        while(Grade != 'A' and Grade != 'B' and Grade != 'C' and Grade != 'D' and Grade != 'F'):
            Grade = input("Not a grade, Re-enter Grade: ")[0].upper()
        if(Grade == 'A'):
            Points = GRADE_A * Credits
            total_points += Points
        elif(Grade == 'B'):
            Points = GRADE_B * Credits
            total_points += Points
        elif(Grade == 'C'):
            Points = GRADE_C * Credits
            total_points += Points
        elif(Grade == 'D'):
            Points = GRADE_D * Credits
            total_points += Points
        elif(Grade == 'F'):
            Points = GRADE_F * Credits
            total_points += Points

    #processing
    GPA = total_points / total_credits
    
    #output
    print('\n\nGPA Calculator')
    print('Name: ',Name,sep='')
    print('ID#: ',Id,sep='')
    print('Total Credits: ',total_credits,sep='')
    print('Total Points: ',total_points, sep='')
    print('GPA for the Semester: ',round(GPA,2),sep='')

main()

input("Press Enter to Continue")
