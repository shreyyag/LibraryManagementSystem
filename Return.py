import Splitlist
import date

def Bookreturn():
    
    name = input("Enter name of borrower: ")
    a = "Borrow-"+name+".txt"
    try:
        with open(a,"r") as f:
            lines = f.readlines()
            lines = [a.strip("$") for a in lines]
    
        with open(a,"r") as f:
            data = f.read()
            print(data)
    except:
        print("Record not found. The name of the borrower must be incorrect.")
        Bookreturn()

    b = "Return-"+name+".txt"
    with open(b,"w+")as f:
        f.write("      ------>Library Management System<----- \n")
        f.write("               Returned By: "+ name+"\n")
        f.write("    Date: " + date.Bdate()+"    Time:"+ date.Btime()+"\n")
        f.write("S.N.\t\t\tBook's name\t\t\t Cost\n")

    total = 0.0
    for i in range(4):
        if Splitlist.booksname[i] in data:
            with open(b,"a") as f:
                f.write(str(i+1)+"\t\t\t"+Splitlist.booksname[i]+"\t\t$"+Splitlist.borrowprice[i]+"\n")
                Splitlist.quantity[i] = int(Splitlist.quantity[i])+1
            total+=float(Splitlist.borrowprice[i])
            
    print("\t\t\t\t\t"+"$"+str(total))
    print("Are you returning the book after expiry date(10 days from borrowing)?")
    typed = input("Type 'Y' for YES and 'N' for NO: ")
    if(typed.upper()=="Y"):
        d = int(input("How many days late are you returning the book?: "))
        fine = 2*d
        with open(b,"a")as f:
            f.write("\t\t\t\tFine: $"+ str(fine)+"\n")
        total = total + fine
    

    print("Total Price: "+ "$"+str(total))
    with open(b,"a")as f:
        f.write("\t\t\t\tTotal: $"+ str(total))
       
    with open("data.txt","w+") as f:
            for i in range(10):
                f.write(Splitlist.sn[i]+","+Splitlist.booksname[i]+","+Splitlist.author[i]+","+str(Splitlist.quantity[i])+","+"$"+Splitlist.borrowprice[i]+"\n")

