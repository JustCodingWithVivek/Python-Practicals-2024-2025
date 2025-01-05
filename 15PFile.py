def Push(Stk,D):  
    for i in D:  
        if D[i]>70:  
            Stk.append(i)  
def Pop(Stk):  
    if Stk==[ ]:  
        return "Stack is Empty"  
    else:  
        print("The deleted element is:",end=' ')  
        return Stk.pop()  
def Disp():  
    if Stk==[ ]:  
        print("Stack is empty")  
    else:  
        top=len(Stk)-1  
        for i in range(top,-1,-1):  
            print(Stk[i])  

ch='y'  
D={}  
Stk=[]  
print("Performing Stack Operations Using Dictionary\n")  
while ch=='y' or ch=='Y':  
    print()  
    print("1.PUSH")  
    print("2.POP")  
    print("3.Disp")  
    opt=int(input("Enter your choice:"))  
    if opt==1:  
        D['Arun']=int(input("Enter the Mark of Arun:"))  
        D['Anu']=int(input("Enter the Mark of Anu:"))  
        D['Vishal']=int(input("Enter the Mark of Vishal:"))  
        D['Priya']=int(input("Enter the Mark of Priya:"))  
        D['Mano']=int(input("Enter the Mark of Mano:"))  
        Push(Stk,D)  
    elif opt==2:  
        r=Pop(Stk)  
        print(r)  
    elif opt==3:  
        Disp()  
    opt=input("Do you want to perform another operation(y/n):")
