import Splitlist
import Return
import Borrow
import date

def starts():
    while(True):

        print(" <------ Welcome to the Bookaholics Library management system----->     ")
        print("....................................................................")
        print("Display Books: ENTER 1")
        print("Borrow a Book: ENTER 2")
        print("Return a Book: ENTER 3")
        print("To Exit: ENTER 4")
        try:
            x = int(input("Select a number from above: "))

            print()
            if(x == 1):
                with open("data.txt","r") as f:
                    lines = f.read()
                    print(lines)
                    print ()
            elif(x == 2):
                Splitlist.listSplit()
                Borrow.Bookborrow()
            elif(x == 3):
                Splitlist.listSplit()
                Return.Bookreturn()
            elif(x == 4):
                print("Thanks alot for choosing Bookaholics Library Management System. Have a great day!")
                break
            else:
                print("Please enter a valid choice from 1-4")
        except ValueError:
            print("Please input as suggested.")
starts()
