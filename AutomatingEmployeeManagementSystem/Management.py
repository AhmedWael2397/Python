def Menu():
    print("\t\t=== SharksMart ===")
    print("1. Add Employee")
    print("2. Update Employee")
    print("3. Departements Guide")
    print("4. Employees Report")
    print("5. Exit\n")
    print("================================")

SharksDepartements=[]
salaries=[]


def Add_Employee(E):
    EmployeeID=len(E)+1                                        #0
    name = input("Enter Employee's Name: ")                    #1               #2
    Departement= input("Enter Employee's Departement: ")     #2
    SharksDepartements.append(Departement)    
    Salary= int(input("Enter Employee's Salary: "))            #3
    while Salary <=0:
        print("Error Entering Salary, Please Enter a valid value \n") 
        Salary= int(input("Enter Employee's Salary: "))     
        salaries.append(Salary)                   #4
    E.append([EmployeeID,name,Departement,Salary])


def Update_Employee(E):
    TempID=int(input(("Please enter Employee ID \n==> ")))
    for Employee in E:
        if Employee[0]==TempID:
            print("ID found , Displaying Employee Data")
            print("Name: ",Employee[1])
            print("A.Departement: ",Employee[2])
            print("B.Salary: ",Employee[3])
            print("What to update ?")
            userInput=input("==> ")
            if userInput =='A':
               Departement = input("Enter Employee's Departement: ")
               Employee[2]=Departement
            elif userInput =='B':
                Salary= int(input("Enter Employee's Salary: "))
                Employee[3]=Salary
            print("Employee data updated ")
    print("ID not Found, check with Manager")          

def DepartmentGuide():
    print(set(SharksDepartements))
    userinput=input("which Department ? \n==>")
    for department in SharksDepartements:
       if userinput== department:
        EmployeeCount=SharksDepartements.count(department)
    print(department,"Has: ",EmployeeCount, " Employees")

       
   

def Reporter(E):
    print("\t ==== OUR EMPLOYEES ==== ")
    for Employee in E:
        print("Name:\t\t",Employee[1])
        print("ID: \t\t",Employee[0])
        print("Departement: \t",Employee[2])
        print("Salary: \t",Employee[3])
        print("\t ==========================\n")
    user_filters=input("A. Filter by Departement \t B. Main Menu \n==> " )
    print("========================================================================")
    if user_filters=='A':
        filter=input("Enter which departement to show\n==>")
        for Employee in E:
            if filter == Employee[2]:
                print("Name:\t\t",Employee[1])
                print("ID: \t\t",Employee[0])
                print("Salary: \t",Employee[3])
                print("\t ==========================\n")
    elif user_filters =='B':
        pass
    


