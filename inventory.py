#I installed the prettytable using python -m pip install -U prettytable and imported the module
#It will be used for creating a table when the user selects "view_all"

from prettytable import PrettyTable
tabulate = PrettyTable()

#========The beginning of the class==========
#created a class Shoe
class Shoe:
    #In this function,I initialised the following attributes : country, code, product, cost, and quantity.
    def __init__(self, country, code, product, cost, quantity):
        pass
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
    #defined the functions and return the country of the shoe in this method get_country()    
    def get_country(self):
        pass
        return self.country
    #defined the function and return the cost of the shoe in this method get_cost()
    def get_cost(self):
        pass
        return self.cost
    #defined the function and return the code of the shoe in this method get_code()
    def get_code(self):
        pass
        return self.code
    #defined the function and return the product of the shoe in this method get_product() 
    def get_product(self):
        pass
        return self.product
   #defined the function and return the quantity of the shoe in this method get_quantity()
    def get_quantity(self):
        pass
        return self.quantity
    #defined the function and return the update of the shoe in this method get_new_quantity()
    def get_new_quantity(self, update_quantity):
        self.quantity = update_quantity
    #defined the function return the returns a string representation of a class.
    def __str__(self):
        pass
        return (f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}")

#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []

#==========Functions outside the class==============

#this function will used to read the data or contents of the file
def read_shoes_data():
    pass
    #i used the try-except method in terms of defensive programming to avoid errors when runnning in the program
    try:
        #print relevant message 
        print("****The following file consists of the following data below:****")
        print()
        #open the file in read mode 
        with open("inventory.txt","r") as file:
            #read the contents of the file and strip at the new line and split at the comma in order to create index of arrays
            for lines in file:
                info = lines.strip("\n").split(",")
                #created the shoe object and appended the indexes of the list from the file
                shoe_list.append(Shoe(info[0],info[1],info[2],info[3],info[4]))
        #created a for loop for index in the range of the length of the object
        for idx in range(1, len(shoe_list)): #skip the first line of code
            #print out the data and relevant message
            print(shoe_list[idx]) 
        print("The data has been read")
    #defensive programming if the file is not found print the relevant output
    except FileNotFoundError:
        print(f"The file does not exist!\n")

# This function will allow a user to capture data
# about a shoe and use this data to create a shoe object
# and append this object inside the shoe list
#I used the try except for error handling
def capture_shoes():
    pass
    try:
        #prompt the user to enter the following input
        enter_country = input(f"Enter the country of your product:\n")
        enter_code = input(f"Enter the product code:\n")
        enter_product = input(f"Enter the product name:\n")
        enter_cost = int(input(f"Enter the product cost in numbers\n"))
        enter_quantity = int(input(f"Enter the product quantity in numbers\n"))
        #create an object with the data the user has input
        enter_shoe = Shoe(enter_country, enter_code, enter_product, enter_cost, enter_quantity)
        #append the object to the empty list 
        shoe_list.append(enter_shoe)
        #open the file in append mode and use the write()function to enter the new data on the inventory text file
        with open("inventory.txt","a+") as file:
            file.write(f'\n{enter_country},{enter_code},{enter_product},{enter_cost},{enter_quantity}')
            print(f"The new product has been added\n")
    except FileNotFoundError:
        print(f"\nSorry, this file does not exist!\n")

#This function will iterate over the shoes list and
#print the details of the shoes returned from the __str__ function. 
def view_all():
    pass
    try:
        print("*********The data in a table formate*******")
        #open the file in read mode and use a for loop to read the contents of the file.
        with open("inventory.txt","r") as file:
            for lines in file:
                # used the strip() function to remove any leading (spaces at the beginning) and trailing (spaces at the end) and split at the comma
                info = lines.strip()
                info = lines.split(",") 
                #created an object with indexes from the file
                shoe_list.append(Shoe(info[0],info[1],info[2],info[3],info[4])) 
        for idx in range(1, len(shoe_list)): #skip the first line of code
            #created a table with the headers "Country", "Code", "Product", "Cost","Quantity" and added the rows using add_rows()function
            tabulate.field_names = ["Country", "Code", "Product", "Cost","Quantity"]
            tabulate.add_row([shoe_list[idx].country, shoe_list[idx].code, shoe_list[idx].product, shoe_list[idx].cost,shoe_list[idx].quantity])
        print(tabulate) #print out the table
    except FileNotFoundError:
        print("The file does not exist")
        
# This function will find the shoe object with the lowest quantity,
# which is the shoes that need to be re-stocked. Ask the user if they
# want to add this quantity of shoes and then update it.
# This quantity should be updated on the file for this shoe.
def re_stock():
    pass
    try:
        #open the file in read mode
        with open("inventory.txt", "r") as file:
            next(file) # skip first line
            for line in file:
                info = line.strip("\n").split(",")
                shoe_list.append(Shoe(info[0], info[1], info[2], info[3], info[4]))
            
        # Find shoe with lowest quantity
        # set the variable "min_quantity" to a float value that represents positive infinity.
        minimum_quantity = float("infinity")
        #initializes the variable "min_shoe_idx" to the value of -1.
        min_shoe_idx = -1
        # creates a for loop that iterates over a sequence of indexes for the "shoe_list".
        for idx in range(len(shoe_list)):
            #retrieve the quantity of a shoe object at a specific index of "shoe_list".
            quantity = shoe_list[idx].get_quantity()
            quantity_float = float(quantity) #convert the string quantity to a float
            #compares the quantity of a shoe object to a minimum quantity and
            #It updates the minimum quantity and the index of the corresponding shoe object if the current quantity is smaller than the minimum quantity.
            if quantity_float < float(minimum_quantity):
                minimum_quantity, min_shoe_idx = quantity, idx
        
        #checks if the min_shoe_idx variable has been assigned a valid index within the shoe_list.
        # If it is not equal to -1, it means that a shoe object in the list has the smallest quantity
        # furthermore, the code prompts the user if they want to add more quantity to this shoe.
        if min_shoe_idx != -1:
            #output the lowest quantity
            print("The shoe with the lowest quantity is:", shoe_list[min_shoe_idx].get_product())
            print("The current quantity is:", shoe_list[min_shoe_idx].get_quantity())
            add_quantity = input("Do you want to add more quantity? (yes/no)").capitalize()
            if add_quantity == 'Yes':
                new_quantity = int(input("How many do you want to add?"))
                shoe_list[min_shoe_idx].quantity = new_quantity
                print("New quanitity has been updated")
                # Write updated quantity back to the text file
                with open("inventory.txt", "w") as file:
                    file.write("Country,Code,Product,Cost,Quantity\n")
                    for shoe in shoe_list:
                        line = f"{shoe.get_country()},{shoe.get_code()},{shoe.get_product()},{shoe.get_cost()},{shoe.get_quantity()}\n"
                        file.write(line)
            else:
                print("No shoes found in the inventory")
    except FileNotFoundError:
        print("The file does not exist")    
#  This function will search for a shoe from the list
#  using the shoe code and return this object so that it will be printed.
def search_shoe():
    pass
    try:
        #prompt the user to enter the code
        search_shoe = input("Enter the code you are searching for: ").upper()
        #open the file in read mode
        with open("inventory.txt","r") as file:
            #strip the new line and split by comma and create an object with the empty shoe list
            for lines in file:
                info = lines.strip("\n").split(",")
                shoe_list.append(Shoe(info[0],info[1],info[2],info[3],info[4]))    
        for idx in range(1, len(shoe_list)): #skip the first line of code
            #if the code of the shoe is equal to the code the user input the print the shoe
            if shoe_list[idx].get_code() == search_shoe:
                print("------------------------------------------------------------------")
                print(shoe_list[idx])
                print("------------------------------------------------------------------")
                break
    except FileNotFoundError:
        print("The file does not exit")
     
# This function will calculate the total value for each item using the formular value = cost * quantity.
def value_per_item():
    pass
    try:
        #open the file in read mode and use a for loop to read the contents of the file
        with open("inventory.txt","r") as file:
            for lines in file:
                #strip the new line and split by comma and create an object with the empty shoe list
                info = lines.strip("\n").split(",")
                shoe_list.append(Shoe(info[0],info[1],info[2],info[3],info[4]))  
        # creates a for loop that iterates over a sequence of indexes for the "shoe_list". 
        for idx in range(1, len(shoe_list)): #skip the first line of code
                #he code computes the total value of a shoe object by multiplying its cost and quantity attributes.
                value = int(shoe_list[idx].get_cost()) * int(shoe_list[idx].get_quantity())
                #print out the resulyt
                print(f"{shoe_list[idx].get_product()} Value: R{value}\n")
    except FileNotFoundError:
        print("The file does not exits")
#Write code to determine the product with the highest quantity and
# print this shoe as being for sale.
def highest_qty():
    pass
    try:
        #an empty list which im going to use to append the string numerical values and convert them to integers to find the highest number
        list_of_numbers = []
        #code to find the highest number in the list.
        with open("inventory.txt","r") as file:
            for lines in file:
                info = lines.strip("\n").split(",")
                shoe_list.append(Shoe(info[0],info[1],info[2],info[3],info[4]))
        # create a for loop that iterates over a sequence of indexes for the "shoe_list". 
        for idx in range(1, len(shoe_list)): #skip the first line of code
            #appends the quantity attribute of a shoe object to list_of_numbers
            list_of_numbers.append(shoe_list[idx].quantity)
            #The list iterates over each element i in list_of_numbers and uses the eval()function to convert the string number to integers
            convert_num = [eval(i) for i in list_of_numbers]
            #I used the max()function to find the highest number in the list
            highest_num = max(convert_num)
            #convert the highest number to a string to avoid errors when running the program becasue all the attribbues in the class are strings
            string_num = str(highest_num)
            
        #code to display the shoes with the highest quantity
        #open the function in read mode and use for loop to read the contents of the file
        with open("inventory.txt","r") as file:
            for lines in file:
                # strip the new line and split by comma and create an object with the empty shoe list
                info = lines.strip("\n").split(",")
                shoe_list.append(Shoe(info[0],info[1],info[2],info[3],info[4])) 
        # create a for loop that iterates over a sequence of indexes for the "shoe_list".  
        for idx in range(1, len(shoe_list)): #skip the first line of code
            # if the quantity of the shoe_list is equal to the string number we initialy coded for then print the product with highest quantity
            if shoe_list[idx].get_quantity() == string_num:
                print("-------------------------------------------------------------------------------------")
                print(f"The highest quantity is: {string_num} ")
                print(f"The shoe information: '{shoe_list[idx]}' is currntly for sale")
                print("-------------------------------------------------------------------------------------")
                break
    except FileNotFoundError:
        print("The file does not exit")
#==========Main Menu=============

#a menu that executes each function above which is inside the while loop.
#I used the try-execept method for defensive programming purposes.
while True:
    try:
        #present the menu using the print function
        print("Select from the menu below")
        print("1.Read the data")
        print("2. Capture Shoes")
        print("3. View All")
        print("4. Restock")
        print("5. Search for item using the product code")
        print("6. View the values of all items")
        print("7. View item with the highest quantity")
        print("8. Exit")
        #prompt the user to input a number from the menu provided
        menu = int(input("Please enter a number from the menu:"))
        #call the functions according to the number chosen in the menu 
        #and used defensive programming method(except ValueError) if the wrong input is selected
        if menu == 1:
            read_shoes_data()
        if menu == 2:
            capture_shoes()
        elif menu == 3:
            view_all()
        elif menu == 4:
            re_stock()
        elif menu == 5:
            search_shoe()
        elif menu == 6:
            value_per_item()
        elif menu == 7:
            highest_qty()
        elif menu == 8:
            print("Goodbye.")
            break
    except ValueError:
        print("Invalid option. Enter a valid number.")

