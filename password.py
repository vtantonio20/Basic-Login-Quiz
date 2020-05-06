import random

def setNewPassword(set_pw):
    file = open('file.txt', 'w')
    file.write(set_pw)
    file.close()
    print("Your new password is: " + str(set_pw) + "\n")

def verify_password(check_pw):
    file = open('file.txt', 'r')
    if check_pw == file.readline():
        print("correct password\n")
        exec(open('CountryCapitalQuiz.py').read())
    else:
        print("incorrect password\n")


run = True
while run:
    inp = input("Type A to set a new password. \nType B to login using password.\nType C to quit program and reset password").lower()
    if inp == "a":
        inp = input("Type in your new password: ")
        setNewPassword(inp)
    elif inp == 'b':
        inp = input("Enter your password: ")
        verify_password(inp)
    elif inp == 'c':
        setNewPassword("")
        print("Thanks for playing.")
        run = False
    else:
        print("please type a valid input!\n")
