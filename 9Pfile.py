def Disp():
    F=open("Poem.txt")
    S=F.read()
    W=S.split()
    print("The follwoing words are less than 5 characters")
    for i in W:
        if len(i)<5:
            print(i,end=' ')
    F.close()
Disp()
