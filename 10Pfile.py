F1=open("Story1.txt",'r')
F2=open("New.txt",'w')
S=F1.readlines()
for i in S:
    if i[0]=='A' or i[0]=='a':
        F2.write(i)
print("Written Successfully")
F1.close()
F2.close()
