import mysql.connector as connections


con = connections.connect(host="localhost",username="root",database="vivekrawat")
cursor = con.cursor()

cursor.execute("use vivekrawat")


def add():                
        print("{:>55}".format("-->> Add Employee Details <<--"))
        addid = int(input("Enter the Employee Id: "))
        if checkid(addid):
                print("Id is already exists")
                add()
        addname = input("Enter the Employee Name: ")
        addage = int(input("Enter the Employee age: "))
        addemail = input("Enter the Employee email: ")
        addaddress = input("Enter the employeeaddress: ")
        addsalary = int(input("Enter the Employee addsalary: "))
      
        cursor.execute(f'''insert into employe(id,employee_name,employee_age,employee_email,employee_address,
                       employee_salary ) values({addid},"{addname}",{addage},"{addemail}","{addaddress}",{addsalary})  ''')
        con.commit()  
        print("Details as been added")  
        input("Press any key to quit: ")
        details()

def checkid(id):
     cursor.execute(f'select * from employe where id={id}')
     data = cursor.fetchall()
     if len(data) > 0:
          return True
     


def display():
     print("{:>55}".format("-->> Employee Details <<--"))
     cursor.execute(f'''select * from employe ''')   
     data = cursor.fetchall()    
     for i in data:
          print(i)                                                         
     input("Press any key to quit: ")
     details()

def update():
        addid = int(input("Enter the Employee Id: "))
        print("{:>55}".format("-->> Update Employee Details <<--"))
        addname = input("Enter the Employee Name: ")
        addage = int(input("Enter the Employee age: "))
        addemail = input("Enter the Employee email: ")
        addaddress = input("Enter the employeeaddress: ")
        addsalary = int(input("Enter the Employee addsalary: "))
        
        cursor.execute(f'''update employe set employee_name="{addname}", employee_age={addage}, employee_email="{addemail}",
                            employee_address="{addaddress}",employee_salary={addsalary} where id={addid}''')        
        con.commit()
        print("Employee Details as been update")
        input("Press any key to quit: ")
        details()   

def remove():
     print("{:>55}".format("-->> Remove Employee Details <<--"))
     addid = int(input("Enter Employee id :"))
     cursor.execute(f'''delete from employe where id={addid}''')
     con.commit()
     print("Employee Details as been remove")
     input("Press any key to quit: ")
     details()


def search():
     print("{:>55}".format("-->>Search Employee Details <<--"))
     addid = int(input("Enter employee id: "))
     cursor.execute(f'''select * from employe where id={addid} ''')
     data = cursor.fetchall()    
     for i in data:
          print(i) 
     input("Press any key to quit: ")
     details()

def details():
    print("{:>60}".format("************************************"))
    print("{:>60}".format("-->> Employee Management System <<--"))
    print("{:>60}".format("************************************"))
    print("1.Add Employee Details")
    print("2.Display Employee Record")
    print("3.Update Employee Record")
    print("4.Remove Employee Record")
    print("5.Search Employee Record")
    print("{:>55}".format("Choice Option:(1,2,3,4,5,6)"))
    userinput = int(input("Enter The Number :"))
    if(userinput == 1):
        add()
    elif(userinput == 2):
        display() 
    elif(userinput == 3):
         update()
    elif(userinput == 4):
          remove()
    elif(userinput == 5):
          search()
    

details()