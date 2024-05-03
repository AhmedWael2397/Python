import Management
Employee=[]
EmployeeNo=0
while True:
    Management.Menu()
    userInput=input("==> ")
    if userInput =='1':
        Management.Add_Employee(Employee)
        EmployeeNo+=1
        print("===============================")
        print("Employee added to Sharks-Mart system successfuly\n")
        print("===============================")
    elif userInput =='2':
        if EmployeeNo==0:
            print("Error , No Employees in database yet")
        else:
            Management.Update_Employee(Employee)
            print("===============================")
    elif userInput =='3':
        if EmployeeNo==0:
            print("Error , No Employees in database yet")
        else:
            Management.DepartmentGuide()
    elif userInput =='4':
        if EmployeeNo==0:
            print("Error , No Employees in database yet")
        else:
            Management.Reporter(Employee)
            print("===============================")
    elif userInput =='5':
        exit()
        
