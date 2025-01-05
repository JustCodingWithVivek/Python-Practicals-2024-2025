First=0
Second=1
choice=int(input("How many Fibonacci numbers you want to display: "))
if choice<=0:
    print("Please Enter Positive Integer")
else:
    print(First)
    print(Second)
    for i in range(2,choice):
        Third=First+Second
        First=Second
        Second=Third
        print(Third)
