#at least 5 func.
#welcome banner w/ variables for cafe_name n tax_rate
#parallel lists for order cart w/ names: item_names, item_prices, n item_quantities
#menu loop w/ options: add item, view cart, remove item by number, checkout, quit (1, 2, 3, 4, 5)
#implement discount code 'STUDENT10' for 10% off n can only be used ONCE
#calc and display subtotal, tac, discount, and final total
#NO negative quantities for prices




def show_banner():
    print("____________________________________")
    print("|                                  |")
    print("|  Café Du Merde - Tax Rate: 0.095 |")
    print("|__________________________________|")

def main_menu():
    while True:
        show_banner()

        print("[1] Add Item")
        print("[2] View Cart")
        print("[3] Remove item by number")
        print("[4] Checkout")
        print("[5] QUIT")

        choice = input("Please Choose an Option: ")

        if choice == "1":
            addItems(itemList, priceList, quantityList)
        
        

        if choice == "5":
            print("Have a good day!")
            break



itemList = []
priceList = []
quantityList = []

def items():  
    return ["Coffee" , "Muffin" , "Fruit Cup"]

def price(): 
    return ["3.00" , "2.00" , "5.00"]

item_quantities = []

def addItems(itemList, priceList, quantityList):
    
    while True:
        print("---------------------------")
        subtotal = 0
        count = 1
    
        for x in range(len(items())):
            print(f"{count} {items()[x]} ${price()[x]}")
            count += 1



        addChoice = input("What would you like to add to your cart? or type DONE to finish: ")
        if (addChoice.upper() == "DONE"):
            return
        else:
            index = int(addChoice) - 1
            howMany = int(input("How many?: "))


        quantity = int(howMany)

        itemList.append(items()[index])
        priceList.append(price()[index])
        quantityList.append(howMany)

        print (f"You added {howMany} {items()[index]}")
    

        if (addChoice.upper()) == "DONE":
            return main_menu()
    



#def view_cart(add_items):
    #for x in rage(len(add_items)):
    #print
    









def main():
    main_menu()
main()