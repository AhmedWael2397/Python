######### initializing item class ##################
class Item:
    def __init__(self,name='',price=0,Quantity=0,Revenue=0,ItemID=0,sales=0):
        self.name=name
        self.price=price
        self.ItemID=ItemID
        self.Revenue=Revenue
        self.Quantity=Quantity
        self.sales=sales
   
topSale=0
topSeller=''
topSellers=[]

class Inventory:
################# initializing list of items ##################
    def __init__(self):
        self.items=[]
################# Method to print list of products ##################
    def listPrint(self):
        print("ID\t \tProduct\t \t Price\t \t \t in stock \t \t sold")
        for item in self.items:
            print(item.ItemID,"\t \t",item.name,"\t\t ",item.price, " EGP\t \t",item.Quantity, "\t \t \t",item.sales)
            
################# Method to add items to inventory ##################
    def AddItem(self,name,price,Quantity,Revenue,ItemID,sales):
        item=Item(name,price,Quantity,Revenue,ItemID,sales)
        self.items.append(item)
        return item
    
################# Method to update inventory products stock ##################
    def StockUpdate(self,index,NewStock):
        if self.items[index].Quantity>NewStock:
            self.items[index].sales=self.items[index].Quantity-NewStock
            self.items[index].Revenue=self.items[index].sales*self.items[index].price
        self.items[index].Quantity=NewStock
    
################# Method to Generate sales report of a product ##################
    def SalesReport(self,index):    
        print("This Product was sold for ",self.items[index].sales," and has total Revenue of ",self.items[index].Revenue," EGP")
         
    def Popular(self,index):
        if self.items[index].sales>topSale:
            topSeller=self.items[index].name
            topSellers.append(topSeller)
        print(topSellers)
        

        
        

        
        

   

SharksInventory=Inventory()


