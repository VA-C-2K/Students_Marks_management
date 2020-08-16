import os
import time

def upload():

    file_name = input("Enter the file name: ")
    no_stud = int(input("Enter the number students: "))
    print(f'\nYou are entering data for student {1}')
    student_id = input("\nEnter the student id: ")
    marks= input("Enter the marks: ")
    with open(file_name+'.txt','w') as file:
        file.write('\t'*2+'ID'+'\t'*4+'Marks'+'\n')
        file.write('\t'*2+student_id+'\t'*4+marks+'\n')
    for i in range(no_stud-1):
        print(f'\nYou are entering data  for student {i+2}\n')
        student_id = input("\nEnter the student id: ")
        marks= input("Enter the marks: ")
        with open(file_name+'.txt','a') as file:
            file.write('\t'*2+student_id+'\t'*4+marks+'\n')
    print("\n Data uploaded")

def update():
    file_name = input("Enter the file name: ")
    no_stud = int(input("Enter the number students to be added: "))
    for i in range(no_stud):
        print(f'\nYou are entering data  for student {i+1}\n')
        student_id = input("\nEnter the student id: ")
        marks= input("Enter the marks: ")
        with open(file_name+'.txt','a') as file:
            file.write('\t'*2+student_id+'\t'*4+marks+'\n')
    print("\n Data uploaded")


def view():

    print("\n You have created following file:  \n")
    directories = os.listdir(r"D:\python\python_Projects")
    for i in directories:
        print(i)
    try:
        file = input("\n Enter the file name:")
        with open(file+'.txt','r') as vfile:
            data=vfile.read()
            print('\n'+data+'\n')
        time.sleep(30)
    except FileNotFoundError:
        print("\nError:No such file found\n")

def menu():
    print("Enter the operation you want to Perform: Upload")
    print(f"{' '*len('Enter the operation you want to perform')} Update")
    print(f"{' '*len('Enter the operation you want to perform')} view---->",end=" ")
    option = input().lower()
    if option == 'update':
        update()
    elif option == 'upload':
        upload()
    elif option == 'view':
        view()
    else:
        print("\n WRong Input\n")

menu()
time.sleep(30)

