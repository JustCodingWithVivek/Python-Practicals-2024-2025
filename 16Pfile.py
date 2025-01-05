import mysql.connector  
def Create_DB():  
    Con=mysql.connector.connect(host='localhost', user='root', password='root')  
    try:  
        if Con.is_connected():  
            cur=Con.cursor()
            Q="CREATE DATABASE employees"  
            cur.execute(Q)  
            print("Employees database created sucessfully")  
    except:  
        print("Database name already exists")  
        Con.close()  
def Create_Table():  
    Con=mysql.connector.connect(host='localhost', user='root', password='root', database='employees')  
    if Con.is_connected():  
        cur=Con.cursor()  
        Q="CREATE TABLE EMP(ENO INT PRIMARY KEY,ENAME VARCHAR(20), GENDER VARCHAR(3), SALARY INT)"  
        cur.execute(Q)  
        print("Emp Table created sucessfully")
    else:
        print("Table Name already exists")  
        Con.close()  
ch='y'  
while ch=='y' or ch=='Y':  
    print("\nInterfacing Python with Mysql")  
    print("1. To Create Database")  
    print("2. To Create Table")  
    opt=int(input("Enter your choice:"))  
    if opt==1:  
        Create_DB()  
    elif opt==2:  
        Create_Table()  
    else:  
        print("Invalid Choice")  
    opt=input("Do you want to perform another operation(y/n);")
