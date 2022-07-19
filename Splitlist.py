def listSplit():
    global sn
    global booksname
    global author
    global quantity
    global borrowprice

    sn = []
    booksname = []
    author = []
    quantity = []
    borrowprice = []
    with open("data.txt","r") as f:   
        lines = f.readlines()
        lines =[x.strip('\n') for x in lines]
        for i in range(len(lines)):
            index =0
            for a in lines[i].split(','):
                if(index==0):
                    sn.append(a)
                elif(index==1):
                    booksname.append(a)
                elif(index==2):
                    author.append(a)
                elif(index == 3):
                    quantity.append(a)    
                elif(index==4):
                    borrowprice.append(a.strip("$"))   
                index = index + 1
