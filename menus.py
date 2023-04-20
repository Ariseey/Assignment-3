
from grade import Grade

students = []

def addStudents():
    while True:
        print()
        id = input('Enter id: ')
        lastName = input('Enter last name: ')
        firstName = input('Enter first name: ')
        middleName = input('Enter middle name: ')
        type = input('Enter type: ')
        course = input('Enter Course: ')
        year = input('Enter year: ')
        section = input('Enter section: ')
        print('----------------------------')
        filipino = input('Grade filipino: ')
        math = input('Grade math: ')
        science = input('Grade science: ')
        english = input('Grade english: ')

        stud = Grade(filipino, math, science, english)
        stud.id = id
        stud.last_name = lastName
        stud.first_name = firstName
        stud.middle_name = middleName
        stud.type = type
        stud.course = course
        stud.year = year
        stud.section = section

        students.append(stud)

        print()
        ans = input('Enter another? [y/n]: ')

        if (ans != 'y'):
            break

    menu()

def deleteRecord():
    i = int(input('Enter index: '))
    students.pop(i)

    menu()

def searchRecord():
    i = int(input('Enter index: '))
    print(f'{i} \t {students[i].getName()} \t | {students[i].getYrCourseSec()} \t | {students[i].getAverage()}')

    menu()

def displayRecords():
    print()
    print('-------------------------------------------------------------------------------')
    i = 0
    for s in students:
        print(f'{i} \t | {s.getName()} \t | {s.getYrCourseSec()} \t | {s.getAverage()}')
        i += 1
    print('-------------------------------------------------------------------------------')

    menu()

def menu():
    print()
    print()
    print('::Menu::')
    print('D - delete record        S - search record')
    print('A - add record           M - display all')
    print()
    choice = input('Enter a function: ')
    if (choice == 'D'):
        deleteRecord()
    elif (choice == 'A'):
        addStudents()
    elif(choice == 'S'):
        searchRecord()
    elif (choice == 'M'):
        displayRecords()

    print()

menu()