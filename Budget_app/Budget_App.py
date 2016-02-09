'''


Part 1: Make a program that keeps track of your budget.  The user can type in commands via the terminal to make changes/add/show the budget.

- Create a program with a simple ui (user interface) loop (a function that has a while loop which keeps the program running).  The loop will repeatedly display (print) a list of commands and ask the user for input. (Commands are listed below)
- Once the user types input, the list of command options displays again until the user quits (enters "q"). You have created while loops with this condition before. Do not be afraid.
- Each command has an associated function that gets called when the user enters the right letter.  You will write these functions.


Commands:

"a" Add an item to the budget - should ask the user for three fields: name, amount, monthly
"s" Show (print out) items in the budget - calculates the total amount of expenses
"r" Remove an item from the budget
"q" Quit Program

a: Think about how you want to save your user's data. How will you save one item? Does it make sense to save their single item's data in a dictionary or an array? Does this data have important categories it needs to be organized by and retrieved with or do you want to pull it with an index number?
	How do you want to save all of their items? Do individual items in the budget need to be categorized or are they just a list?

s: How do you want to print out your data you retrieved from your user? How did you organize your data? What will you need to do to access your data inside of its data structure? 
	How are you going to total your amounts? Do you need to have integers or strings? How will you iterate through all of your user's amount entries?

r: What does a single item in your budget look like as a data type? You have to know this to know how to remove it. How will you access that single item? What syntax do you need to use to delete your item element from your budget?


'''
def add_item():
	item_dict = {}
	item_dict["name"] = raw_input("Name? ")
	item_dict["amount"] = raw_input("Amount? ")
	item_dict["monthly"] = raw_input("Monthly? ")
	return item_dict

def show_items(all_items_array):
	total = 0
	for index, item_dict in enumerate(all_items_array):
		print str(index +1),") Name: " + item_dict["name"] + " Amount: " + item_dict["amount"] + " Monthly: " + item_dict["monthly"]
		total = total + int(item_dict["amount"])
	print "Total = " + str(total)

def remove_item(all_items_array):
	show_items(all_items_array)
	response_integer = int(raw_input("What item # do you want to delete?"))
	del all_items_array[(response_integer-1)]


all_items_array = []
options = "A)dd item\nS)how items\nR)emove item\nQ)uit\n"
user_choice = raw_input(options)

while user_choice != "q":
	if user_choice == "q":
		pass
	elif user_choice == "a":
		item_dict = add_item()
		all_items_array.append(item_dict)
	elif user_choice == "s":
		show_items(all_items_array)
	elif user_choice == "r":
		all_items_array = remove_item(all_items_array)
	user_choice = raw_input(options)



'''
**** Finish part one before moving on to Part 2 ****

In your last assignment, you had a user enter data into the terminal and it was saved as a csv file. We're doing this again, and fusing it with part 1 of this assignment.

A csv file is a very simple file that is used quite often. Usually a csv file will look something like this:

(a simple expenses csv file)

---
name,amount,monthly
food,1000.00,y
rent,2000.00,y
braces,2000.00,n
---


A csv usually starts with a header line that lists the names of the fields so someone reading or importing it into a spreadsheet app knows what each column is for. The header line is just whatever the first row of the csv file is. 

Your goal is to write a simple budget app. This application will have a simple interface that shows the list of commands to the user, and allows the user to enter a command and keep doing various commands until they say
quit. 

It will store the data it gets from the user in a csv file. 

Add the following commands to your Part 1 ui():

1. "s" - Save file -> this converts your internal data structure to a csv and rights it out
2. "r" - Read File -> reads from a csv and converts the data into your internal data structure.

To test your output, you should be able to open the file in a spreadsheet application (e.g. Excel) after closing.

s: Think about what data types part 1 used. How will you go into those datatypes and turn them into a string, separarated by \n newlines and commas in the appropriate places? (Newlines should be placed between items in the budget. Commas should separate entries within each item added.)
r: Think about what datatype a csv is and how it has commas and \n newlines. How will you take this data type and turn it into your datatype you already are using when adding new items to the budget? 

Bigger questions. What data needs to be passed between each function for the functions to have the information they need? 

'''

 
def ui_loop():
	pass 
        
ui_loop()    
    
def add_item():
	item_dict = {}
	
	item_dict["name"] = raw_input("Name? ")
	item_dict["amount"] = raw_input("Amount? ")
	item_dict["monthly"] = raw_input("Monthly? ")
	return item_dict

def show_items(all_items_array):
	total = 0
	for index, item_dict in enumerate(all_items_array):
		print str(index +1),") Name: " + item_dict["name"] + " Amount: " + item_dict["amount"] + " Monthly: " + item_dict["monthly"]
		total = total + int(item_dict["amount"])
	print "Total = " + str(total)

def remove_item(all_items_array):
	show_items(all_items_array)
	try:
		response_integer = int(raw_input("What item # do you want to delete?"))
	except:
		print "Please provide a number"
	else:
		del all_items_array[(response_integer-1)]

def read_all_items():
	with open("all_items_file.csv", "r") as start:
		array = start.readlines()
		array = array[1:]
	for string in array:
		name = string.split(",")[0]
		amount = string.split(",")[1]
		monthly = string.split(",")[2].strip("/n")
		item_hash = {"name":name,"amount":amount,"monthly":monthly}
		all_items_array.append(item_hash)

def save_all_items(all_items_array):
	new_header = "Name,Amount,Monthly\n"
	new_string = ""
	for dictionary in all_items_array:
		new_string = new_string + dictionary["name"] + "," + dictionary["amount"] + "," + dictionary["monthly"] + "\n"
	with open("all_items_file.csv", "w") as f:
		f.write(new_header)
		f.write(new_string)


all_items_array = []
options = "A)dd item\nS)how items\nR)emove item\nRead)file\nSave)file\nQ)uit\n"
user_choice = raw_input(options)

while user_choice != "q":
	if user_choice == "q":
		pass
	elif user_choice == "a":
		item_dict = add_item()
		all_items_array.append(item_dict)
	elif user_choice == "s":
		show_items(all_items_array)
	elif user_choice == "r":
		all_items_array = remove_item(all_items_array)
	elif user_choice == "read":
		read_all_items()
	elif user_choice == "save":
		save_all_items(all_items_array)

	user_choice = raw_input(options)
