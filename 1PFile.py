print("Welcome to my user defined Calculator")
print("1. Adddition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
op=int(input("Enter your choice:"))
a=int(input("Enter the First Number:"))
b=int(input("Enter the Second Number:"))

if op==1:
    c=a+b
    print("The Addition of two number is: ",c)
    
elif op==2:
    c=a-b
    print("The Subtraction of two number is:",c)
    
elif op==3:
    c=a*b
    print("The Multiplication of two number is: ",c)

elif op==4:
    if b==0:
        print("Enter any other number other than 0")
    else:
        c=a/b
        print("The Division of two number is:",c)
else:
    print("Invalid Option")
