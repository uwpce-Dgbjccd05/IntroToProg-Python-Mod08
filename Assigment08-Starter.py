# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# Glenn B. Dacones,6.6.2022,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []

class Product:
    """Stores data about a product:

    changelog: (When,Who,What)
    RRoot,1.1.2030,Created Class
    Glenn B. Dacones,6.6.2022,Modified code to complete assignment 8
    """

    @staticmethod
    def initialize_data(file_name=strFileName):

        lstOfProductObjects = [{"Product":"Television","Price":"499.99"},{"Product":"Table","Price":"99.99"}]
        file = open(file_name, "w")
        for row in lstOfProductObjects:
            file.write(row["Product"] + "," + row["Price"] + "\n")
        file.close()

# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Glenn B. Dacones,6.6.2022,Modified code to complete assignment 8
    """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        list_of_rows.clear()  # clear current data
        file = open(file_name, "r")
        for line in file:
            product, price = line.split(",")
            row = {"Product": product.strip(), "Price": price.strip()}
            list_of_rows.append(row)
        file.close()
        return list_of_rows

    @staticmethod
    def add_data_to_list(product, price, list_of_rows):
        """ Adds data to a list of dictionary rows

        :param task: (string) with name of task:
        :param priority: (string) with name of priority:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """

        row = {"Product": str(product).strip(), "Price": str(price).strip()}
        lstOfProductObjects.append(row)
        return list_of_rows

    @staticmethod
    def remove_data_from_list(product, list_of_rows):
        """ Removes data from a list of dictionary rows

        :param task: (string) with name of task:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """

        for row in lstOfProductObjects:
            if (row["Product"] == product):
                lstOfProductObjects.remove(row)
                print("\nThe",product.lower(),"has been removed from the list/Table!")
        return list_of_rows

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        """ Writes data from a list of dictionary rows to a File

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """

        file_obj = open(file_name, "w")
        for row in lstOfProductObjects:
            file_obj.write(row["Product"] + "," + row["Price"] + "\n")
        file_obj.close()
        return list_of_rows

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """" Performs Input and Output tasks """

    @staticmethod
    def output_menu_products():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Product
        2) Remove an existing Product
        3) Save Data to a File
        4) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def output_current_products_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("\n******* The current products are: *******")
        for row in list_of_rows:
            print(row["Product"] + " (" + row["Price"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_new_product_and_price():
        """  Gets task and priority values to be added to the list

        :return: (string, string) with task and priority
        """
        pass

        product = input("Enter a Product: ")
        product = product.capitalize()

        # This exception handling will catch an invalid price for the product
        try:
            price = float(input("Enter a Price: "))
        except:
            print("You entered an invalid price! Please try again.")
            price = float(input("Enter a Price: "))

        return product, price

    @staticmethod
    def input_product_to_remove():
        """  Gets the product name to be removed from the list

        :return: (string) with product
        """
        pass

        product = input("Which product would you like to remove?: ")
        product = product.capitalize()
        return product
# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #

#1 Step 1 - When the program starts, Load data from products.txt.

Product.initialize_data(file_name=strFileName)

# The exception handling below will catch for a non-existing file
try:
    FileProcessor.read_data_from_file( file_name=strFileName, list_of_rows=lstOfProductObjects)  # read file data
except:
    print("\nThe file does not exist!")

# Step 2 - Display a menu of choices to the user
while (True):
    # Step 3 Show current data
    IO.output_current_products_in_list(list_of_rows=lstOfProductObjects)  # Show current data in the list/table
    IO.output_menu_products()  # Shows menu
    choice_str = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if choice_str.strip() == '1':  # Add a new Task
        product, price = IO.input_new_product_and_price()
        lstOfProductObjects = FileProcessor.add_data_to_list(product=product, price=price, list_of_rows=lstOfProductObjects)
        print("\nThe",product.lower(),"has been added to the list/Table!")
        continue  # to show the menu

    elif choice_str == '2':  # Remove an existing product
        product = IO.input_product_to_remove()
        lstOfProductObjects = FileProcessor.remove_data_from_list(product=product, list_of_rows=lstOfProductObjects)
        continue  # to show the menu

    elif choice_str == '3':  # Save Data to a File
        lstOfProductObjects = FileProcessor.write_data_to_file(file_name=strFileName, list_of_rows=lstOfProductObjects)
        print("Data Saved!")
        continue  # to show the menu

    elif choice_str == '4':  # Exit Program
        print("Goodbye!")
        break  # by exiting loop

    else:
        try:
            print("Choice Error!","\nPlease choose only 1, 2, 3, or 4 only!\n")
        except:
            print("Invalid Choice. Please try again!")