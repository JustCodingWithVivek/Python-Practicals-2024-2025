def Push():  
    Doc_ID=int(input("Enter the Doctor ID:"))  
    Doc_Name=input("Enter the Name of the Doctor:")  
    Mob=int(input("Enter the Mobile Number of the Doctor:"))  
    Special=input("Enter the Specialization:")  
    if Special=='ENT' or 'Ent':  
        Stack.append([Doc_ID,Doc_Name])  

def Pop():  
    if Stack==[]:  
        print("Stack is empty")  
    else:  
        print("The deleted doctor detail is:", Stack.pop())  

def Peek():  
    if Stack==[]:  
        print("Stack is empty")  
    else:  
        top=len(Stack)-1  
        print("The top of the stack is:", Stack[top])  
def Disp():  
    if Stack==[]:  
        print("Stack is empty")  
    else:  
        top=len(Stack)-1  
        for i in range(top,-1,-1):  
            print(Stack[i])
Stack=[]
ch='y'
print("Performing Stack Operations Using List\n")
while ch=='y' or ch=='Y':
    print()
    print("1.PUSH")
    print("2.POP")
    print("3.PEEK")
    print("4.Disp")
    opt=int(input("Enter your choice:"))
    if opt==1:
        Push()
    elif opt==2:
        Pop()
    elif opt==3:
        Peek()
    elif opt==4:
        Disp()
    else:
        print("Invalid Choice, Try Again!!!")
    ch=input("\nDo you want to Perform another operation(y/n):")
