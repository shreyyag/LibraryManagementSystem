import Splitlist
import date
def Bookborrow():
    ifBorrowed = False
    while(True):
        fName = input("Enter first name of the borrower: ")
        if fName.isalpha():
            break
        print("Error! Please input the name in alphabet.")
    while(True):
        lName = input("Enter last name of the borrower: ")
        if lName.isalpha():
            break
        print("Error! Please input last name in alphabet.\n")
            
    n ="Borrow-"+fName+".txt"
    with open(n,"w+") as f:
        f.write("           ---->Bookaholics Library Management System<----   \n")
        f.write("             Borrowed By: "+ fName+" "  +lName+"\n")
        f.write("    Issued Date: " + date.Bdate()+"    Issued time:"+ date.Btime()+"\n\n")
        f.write("S.N. \t\t Book borrowed \t\t\t\t  Author \n" )
    
    while (ifBorrowed == False):
        print("Please select an option for the required book:")
        for i in range(len(Splitlist.booksname)):
            print("-> To borrow", Splitlist.booksname[i],", please Enter", i)
    
        try:   
            a = int(input("Input the code: "))
            try:
                if(int(Splitlist.quantity[a])>0):
                    print("Book is available. You can borrow it.")
                    with open(n,"a") as f:
                        f.write("1. \t\t"+ Splitlist.booksname[a]+"\t\t\t  "+Splitlist.author[a]+"\n")

                    Splitlist.quantity[a] = int(Splitlist.quantity[a])-1
                    with open("data.txt","w+") as f:
                        for i in range(10):
                            f.write(Splitlist.sn[i]+","+Splitlist.booksname[i]+","+Splitlist.author[i]+","+str(Splitlist.quantity[i])+","+"$"+Splitlist.borrowprice[i]+"\n")


                    #multiple book borrowing code
                    loop = True
                    count = 1
                    while (loop == True):
                        choice = str(input("Do you want to borrow any other book?.Reminder: You cannot boorow the same book twice. Press 'y' for YES and 'n' for NO."))
                        if(choice.upper()=="Y"):
                            count = count + 1
                            print("Please select an option for the required book:")
                            for i in range(len(Splitlist.booksname)):
                                print("->To borrow", Splitlist.booksname[i],", please Enter", i)
                            a = int(input("Input the code: "))
                            if(int(Splitlist.quantity[a])>0):
                                print("Book is available. You can borrow it.")
                                with open(n,"a") as f:
                                    f.write(str(count) +". \t\t"+ Splitlist.booksname[a]+"\t\t  "+Splitlist.author[a]+"\n")

                                Splitlist.quantity[a]=int(Splitlist.quantity[a])-1
                                with open("data.txt","w+") as f:
                                    for i in range(10):
                                        f.write(Splitlist.sn[i]+","+Splitlist.booksname[i]+","+Splitlist.author[i]+","+str(Splitlist.quantity[i])+","+"$"+Splitlist.borrowprice[i]+"\n")
                                        ifBorrowed = False
                            else:
                                loop = False
                                break
                        elif (choice.upper()=="N"):
                            print ("Thank you for borrowing a book from us. ")
                            print("")
                            loop = False
                            ifBorrowed = True
                        else:
                            print("Please follow the instructions.\n")
                        
                else:
                    print("Book is not available.")
                    Bookborrow()
                    ifBorrowed = False
            except IndexError:
                print("")
                print("Please choose the correct number for the book as specified.")
        except ValueError:
            print("")
            print("Please choose as specified.")