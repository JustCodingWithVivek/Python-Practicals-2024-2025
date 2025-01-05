
def Check(no1,no2):
    if (no1%10)<(no2%10):
        return no1
    else:
        return no2
    
a=int(input("Enter the First number:"))
b=int(input("Enter the Second number:"))
r=Check(a,b)
print("The Number that has minimum one's digit is:",r)
