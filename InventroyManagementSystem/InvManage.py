
import Manager as M

ItemID=0
TotalR=0
TotalS=0
def HomePage():
    print("Welcome to the Sharks inventory App\n")
    print("======== OUR PRODUCTS =========")
    M.SharksInventory.listPrint()
    choice=int(input("Choose \n '1' to add new item \n '2' to update product stock \n '3' to generate sales report \n '4' show popular items \n '5' to exit the program \n"))
    while (choice <= 0 or choice > 5):
        print("Invalid Input\t Please Try again\n")
        choice=int(input("press '1' to add new item \n '2' to update product stock \n '3' to generate sales report \n '4' show popular items \n '5' to exit the program \n"))
    return choice

while(1):
    user_input=HomePage()
    ##################################### collecting data to ADD ITEM TO THE INVENTORY ###############################
    if user_input ==1: 
        name=input("Please Enter product Name: ")
        price=float(input("Please Enter Product Price: "))
        ################# validating entered price ##################
        while(price<=0):
            print("Sorry, But Products can't be listed for free \n")
            price=float(input("Please Enter Product Price: "))
        quantity=int(input("Please Enter your product quantity: "))
        ################# validating entered quantity ##################
        while(quantity<=0):
            print("Sorry, But Products can't be listed for free \n")
            quantity=int(input("Please Enter your product quantity: "))
       
       ###############initial values to be calculated later in sales report ########################### 
        ItemRevenue=0
        ItemSales=0
       ################## adding item to inventory products stock ##################
        M.SharksInventory.AddItem(name,price,quantity,ItemRevenue,ItemID,ItemSales)
        ItemID+=1
        print("Item added to Sharks Inventory successfuly \n")
    ############################## # update product stock ##########################################
    elif user_input==2: 
        id=int(input("Please Enter your product ID: "))
    ################# deciding the correct product to modify it's stock quantity ##################    
        for index, i in enumerate(M.SharksInventory.items):
           if i.ItemID == id:
               NewStock=int(input("Please Enter your new Stock Quantity: "))
               M.SharksInventory.StockUpdate(index,NewStock)
           else:   
               print("ID not Found\n")
    ############################## Generating product sales report ##########################################
    elif user_input==3: 
            id=int(input("Please Enter your product ID: "))
            flag=0
            for index, i in enumerate(M.SharksInventory.items):
                if i.ItemID == id:
                     M.SharksInventory.SalesReport(index)
                     flag=1
            if flag==1:
                pass
            else:   
                print("ID not Found\n")
    ############################## identifying popular products ##########################################
    elif user_input ==4:
       for index, i in enumerate(M.SharksInventory.items):
           M.SharksInventory.Popular(index)    
    ############################## EXITING PROGRAM ##########################################
    elif user_input==5:
        exit()    



    #elif user_input==3: #generate sales report 






                
               
               


        
