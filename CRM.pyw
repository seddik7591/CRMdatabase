# seddik7591@gmail.com
from tkinter import *
import mysql.connector
import csv
from tkinter import ttk

app = Tk()
app.title("My CRM Database App")
app.iconbitmap('palm.ico')
app.geometry("400x550")

# Connect to MySQL
mydb = mysql.connector.connect(
		host= "localhost",
		user= "root",
		passwd= "PassRoot_7591",
		database="electel"
	)

# check if connection to MySQL was created
# print(mydb)

# Create a cursur and initialize it
my_cursor = mydb.cursor()

# Create a database (this should be executed just one time to create the database)
# my_cursor.execute("CREATE DATABASE electel")

# test to see if database was created
# my_cursor.execute("SHOW DATABASES")
# for db in my_cursor:
# 	print(db)

# Create a table and this should be of course executed just one time to create the same table
# or use IF NOT EXISTS
# We use anti slash \ to write in multi lines
# my_cursor.execute("CREATE TABLE IF NOT EXISTS customers (first_name VARCHAR(100), \
	# last_name VARCHAR(255), \
	# zipcode INT(10), \
	# price_paid DECIMAL(10, 2), \
	# user_id INT AUTO_INCREMENT PRIMARY KEY)")

# This is how to alter table (modify it)
'''
my_cursor.execute("ALTER TABLE customers ADD (\
	email VARCHAR(255),\
	address_1 VARCHAR(255),\
	address_2 VARCHAR(255),\
	city VARCHAR(50),\
	state VARCHAR(50),\
	country VARCHAR(255),\
	phone VARCHAR(255),\
	payment_method VARCHAR(50),\
	discount_code VARCHAR(255))")
'''

# Show the table
# my_cursor.execute("SELECT * FROM customers")
# for thing in my_cursor.description:
# 	print(thing)

# Define clear_fields function
def clear_fields():
	first_name_box.delete(0, END)
	last_name_box.delete(0, END)
	address_1_box.delete(0, END)
	address_2_box.delete(0, END)
	city_box.delete(0, END)
	state_box.delete(0, END)
	country_box.delete(0, END)
	zipcode_box.delete(0, END)
	phone_box.delete(0, END)
	email_box.delete(0, END)
	payment_method_box.delete(0, END)
	price_paid_box.delete(0, END)
	discount_code_box.delete(0, END)

# Define add_customer function
def add_customer():
	sql_command = "INSERT INTO customers (first_name, last_name, zipcode, price_paid, email, address_1, address_2, city, state, country, phone, payment_method, discount_code) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
	# %s is place holder to say later what to put there
	values = (first_name_box.get(), last_name_box.get(), zipcode_box.get(), price_paid_box.get(), email_box.get(), address_1_box.get(), address_2_box.get(), city_box.get(), state_box.get(), country_box.get(), phone_box.get(), payment_method_box.get(), discount_code_box.get())
	my_cursor.execute(sql_command, values)
		
	# Commit the changes to the database
	mydb.commit()
	# After work done we clear fields
	clear_fields()

# Define write_to_csv(result) to generate excel csv file
def write_to_csv(result):
	# 'a' means it will apend the data to the end of the csv file
	with open('customers.csv', 'a', newline='') as f:
		w = csv.writer(f, dialect='excel')
		for record in result:
			w.writerow(record)

def submit_update(id):
	sql_command = """UPDATE customers SET first_name = %s, last_name = %s, zipcode = %s, price_paid = %s, email = %s, address_1 = %s, address_2 = %s, city = %s, state = %s, country = %s, phone = %s, payment_method = %s, discount_code = %s WHERE user_id = %s"""
	# remember %s is place holder to say later what to put there using the command my_cursor.execute and inside give the command then the values in order of course
	values = (first_name_box2.get(), last_name_box2.get(), zipcode_box2.get(), price_paid_box2.get(), email_box2.get(), address_1_box2.get(), address_2_box2.get(), city_box2.get(), state_box2.get(), country_box2.get(), phone_box2.get(), payment_method_box2.get(), discount_code_box2.get(), id)
	my_cursor.execute(sql_command, values)
	
	# Commit the changes to the database
	mydb.commit()
	# After work done we close the window
	global record_update_window
	record_update_window.destroy()
	# And because we update one record we should refresh the customers list
	global list_customers_window
	list_customers_window.destroy()
	list_customers()

def edit_record(id):
	global record_update_window
	record_update_window = Tk()
	record_update_window.title("Update Customer Information")
	record_update_window.iconbitmap('palm.ico')
	record_update_window.geometry("400x550")
	
	# Query to select all record's fields
	sql2 = "SELECT * FROM customers WHERE user_id = %s"				
	name2 = (id, )
	result2 = my_cursor.execute(sql2, name2)
	result2 = my_cursor.fetchall()

	update_window_label = Label(record_update_window, text="Update Customer's Information", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, padx=20, pady=10)
	# Create main form to enter new customer data
	first_name_label = Label(record_update_window, text="First Name").grid(row=1, column=0, sticky=W, padx=10)
	# sticky=W or E or N or S to chose the side of the writing west east north or south
	last_name_label = Label(record_update_window, text="Last Name").grid(row=2, column=0, sticky=W, padx=10)
	address_1_label = Label(record_update_window, text="Address 1").grid(row=3, column=0, sticky=W, padx=10)
	address_2_label = Label(record_update_window, text="Address 2").grid(row=4, column=0, sticky=W, padx=10)
	city_label = Label(record_update_window, text="City").grid(row=5, column=0, sticky=W, padx=10)
	state_label = Label(record_update_window, text="State").grid(row=6, column=0, sticky=W, padx=10)
	zipcode_label = Label(record_update_window, text="Zipe Code").grid(row=7, column=0, sticky=W, padx=10)
	country_label = Label(record_update_window, text="Country").grid(row=8, column=0, sticky=W, padx=10)
	phone_label = Label(record_update_window, text="Phone Number").grid(row=9, column=0, sticky=W, padx=10)
	email_label = Label(record_update_window, text="Email").grid(row=10, column=0, sticky=W, padx=10)
	payment_method_label = Label(record_update_window, text="Payment Method").grid(row=11, column=0, sticky=W, padx=10)
	discount_code_label = Label(record_update_window, text="Discount Code").grid(row=12, column=0, sticky=W, padx=10)
	price_paid_label = Label(record_update_window, text="Price Paid").grid(row=13, column=0, sticky=W, padx=10)

	# Create Entry Boxes
	global first_name_box2
	first_name_box2 = Entry(record_update_window)
	first_name_box2.grid(row=1, column=1)
	# insert default record's information into the boxes
	first_name_box2.insert(0, result2[0][0])
	
	global last_name_box2
	last_name_box2 = Entry(record_update_window)
	last_name_box2.grid(row=2, column=1, pady=5)
	last_name_box2.insert(0, result2[0][1])

	global address_1_box2
	address_1_box2 = Entry(record_update_window)
	address_1_box2.grid(row=3, column=1, pady=5)
	address_1_box2.insert(0, result2[0][6])

	global address_2_box2
	address_2_box2 = Entry(record_update_window)
	address_2_box2.grid(row=4, column=1, pady=5)
	address_2_box2.insert(0, result2[0][7])

	global city_box2
	city_box2 = Entry(record_update_window)
	city_box2.grid(row=5, column=1, pady=5)
	city_box2.insert(0, result2[0][8])

	global state_box2
	state_box2 = Entry(record_update_window)
	state_box2.grid(row=6, column=1, pady=5)
	state_box2.insert(0, result2[0][9])

	global zipcode_box2
	zipcode_box2 = Entry(record_update_window)
	zipcode_box2.grid(row=7, column=1, pady=5)
	zipcode_box2.insert(0, result2[0][2])

	global country_box2
	country_box2 = Entry(record_update_window)
	country_box2.grid(row=8, column=1, pady=5)
	country_box2.insert(0, result2[0][10])

	global phone_box2
	phone_box2 = Entry(record_update_window)
	phone_box2.grid(row=9, column=1, pady=5)
	phone_box2.insert(0, result2[0][11])

	global email_box2
	email_box2 = Entry(record_update_window)
	email_box2.grid(row=10, column=1, pady=5)
	email_box2.insert(0, result2[0][5])

	global payment_method_box2
	payment_method_box2 = Entry(record_update_window)
	payment_method_box2.grid(row=11, column=1, pady=5)
	payment_method_box2.insert(0, result2[0][12])

	global discount_code_box2
	discount_code_box2 = Entry(record_update_window)
	discount_code_box2.grid(row=12, column=1, pady=5)
	discount_code_box2.insert(0, result2[0][13])

	global price_paid_box2
	price_paid_box2 = Entry(record_update_window)
	price_paid_box2.grid(row=13, column=1, pady=5)
	price_paid_box2.insert(0, result2[0][3])

	global id_value
	id_value = result2[0][4]

	update_button = Button(record_update_window, text="Submit", command=lambda: submit_update(id_value))
	update_button.grid(row=14, column=0, padx=10, pady=5)

def show_result(result, window, frame_row):

	show_result_frame = LabelFrame(window)
	show_result_frame.grid(row=frame_row, column=0, columnspan=3, padx=10, pady=15, sticky="nsew")
	if result == "no_option":
		searched_label = Label(show_result_frame, text="Hey! You forgot to chose search option")
		searched_label.grid(row=0, column=0, padx=10, pady=15)
	elif not result:
		searched_label = Label(show_result_frame, text="No result to diplay...")
		searched_label.grid(row=0, column=0, padx=10, pady=15)
	else:
		Label(show_result_frame, text="|").grid(row=0 , column=0)
		Label(show_result_frame, text="First Name").grid(row=0 , column=1)
		Label(show_result_frame, text="|").grid(row=0 , column=2)
		Label(show_result_frame, text="Last Name").grid(row=0 , column=3)
		Label(show_result_frame, text="|").grid(row=0 , column=4)
		Label(show_result_frame, text="Zip Code").grid(row=0 , column=5)
		Label(show_result_frame, text="|").grid(row=0 , column=6)
		Label(show_result_frame, text="Price Paid").grid(row=0 , column=7)
		Label(show_result_frame, text="|").grid(row=0 , column=8)
		Label(show_result_frame, text="User ID").grid(row=0 , column=9)
		Label(show_result_frame, text="|").grid(row=0 , column=10)
		Label(show_result_frame, text="Email").grid(row=0 , column=11)
		Label(show_result_frame, text="|").grid(row=0 , column=12)
		Label(show_result_frame, text="Address 1").grid(row=0 , column=13)
		Label(show_result_frame, text="|").grid(row=0 , column=14)
		Label(show_result_frame, text="Address 2").grid(row=0 , column=15)
		Label(show_result_frame, text="|").grid(row=0 , column=16)
		Label(show_result_frame, text="City").grid(row=0 , column=17)
		Label(show_result_frame, text="|").grid(row=0 , column=18)
		Label(show_result_frame, text="State").grid(row=0 , column=19)
		Label(show_result_frame, text="|").grid(row=0 , column=20)
		Label(show_result_frame, text="Country").grid(row=0 , column=21)
		Label(show_result_frame, text="|").grid(row=0 , column=22)
		Label(show_result_frame, text="Phone").grid(row=0 , column=23)
		Label(show_result_frame, text="|").grid(row=0 , column=24)
		Label(show_result_frame, text="Payment Method").grid(row=0 , column=25)
		Label(show_result_frame, text="|").grid(row=0 , column=26)
		Label(show_result_frame, text="Discount Code").grid(row=0 , column=27)
		Label(show_result_frame, text="|").grid(row=0 , column=28)
		# enumerate(x) give you sort of a table of every x with an index
		for index, x in enumerate(result):
			num=1
			id_referrence = x[4]
			saparator_label = Label(show_result_frame, text="|")
			saparator_label.grid(row=index+1, column=0)
			for y in x:
				lookup_label = Label(show_result_frame, text=y)
				lookup_label.grid(row=index+1, column=num)
				saparator_label = Label(show_result_frame, text="|")
				saparator_label.grid(row=index+1, column=num+1)
				num+=2
			edit_button = Button(show_result_frame, text="Edit", command=lambda id_referrence=id_referrence: edit_record(id_referrence))
			edit_button.grid(row=index+1 , column= num, pady=3)

# Define list_customers function
def list_customers():
	global list_customers_window
	list_customers_window = Tk()
	list_customers_window.title("List All Customers")
	list_customers_window.iconbitmap('palm.ico')
	list_customers_window.geometry("1200x400")

	# Query the database
	my_cursor.execute("SELECT * FROM customers")
	result = my_cursor.fetchall()
	
	# Show result. The 0 here is the row where we want the frame to be
	show_result(result, list_customers_window, 0)

	csv_button = Button(list_customers_window, text="Save to Excel", command=lambda: write_to_csv(result))
	csv_button.grid(row=1 , column=0, padx=10, pady=5, sticky=W)

# Define search_customers function
def search_customers():
	search_customers_window = Tk()
	search_customers_window.title("Search Customers")
	search_customers_window.iconbitmap('palm.ico')
	search_customers_window.geometry("1000x350")
	
	def search_now():
		selected = search_drop_box.get()
		result = ""	
		if selected == "Search by...":
			result = "no_option"

		searched = search_box.get()
		sql = ""
		if selected == "Last Name":
			sql = "SELECT * FROM customers WHERE last_name = %s"
		if selected == "Email Address":
			sql = "SELECT * FROM customers WHERE email = %s"
		if selected == "Customer ID":
			sql = "SELECT * FROM customers WHERE user_id = %s"				
		# remember %s is a place holer, there will be the searched value
		if sql != "":
			name = (searched, )
			result = my_cursor.execute(sql, name)
			result = my_cursor.fetchall()
			# you have to fetch it before you show it to the screen

		# Show result. The 2 here is the row where we want the frame to be
		show_result(result, search_customers_window, 2)
		

	# Entry box to search for customer
	search_box = Entry(search_customers_window)
	search_box.grid(row=0, column=1, padx=10, pady=10)
	# Label for the search box
	search_box_label = Label(search_customers_window, text="Search Customer :")
	search_box_label.grid(row=0, column=0, padx=10, pady=10)
	# Button for the search box
	search_button = Button(search_customers_window, text="Search", command=search_now)
	search_button.grid(row=1 ,column=0 ,padx=10)
	# Create a drop down box to give diffrent options
	search_drop_box = ttk.Combobox(search_customers_window, value=["Search by...", "Last Name", "Email Address", "Customer ID"])
	search_drop_box.current(0)
	search_drop_box.grid(row=0, column=2)

# Create a label
title_label = Label(app, text="electel Customer Database", font=("Helvetica", 16))
title_label.grid(row=0, column=0, columnspan=2, pady=10, padx=15)

# Create main form to enter customer data
first_name_label = Label(app, text="First Name").grid(row=1, column=0, sticky=W, padx=10)
last_name_label = Label(app, text="Last Name").grid(row=2, column=0, sticky=W, padx=10)
address_1_label = Label(app, text="Address 1").grid(row=3, column=0, sticky=W, padx=10)
address_2_label = Label(app, text="Address 2").grid(row=4, column=0, sticky=W, padx=10)
city_label = Label(app, text="City").grid(row=5, column=0, sticky=W, padx=10)
state_label = Label(app, text="State").grid(row=6, column=0, sticky=W, padx=10)
zipcode_label = Label(app, text="Zipe Code").grid(row=7, column=0, sticky=W, padx=10)
country_label = Label(app, text="Country").grid(row=8, column=0, sticky=W, padx=10)
phone_label = Label(app, text="Phone Number").grid(row=9, column=0, sticky=W, padx=10)
email_label = Label(app, text="Email").grid(row=10, column=0, sticky=W, padx=10)
payment_method_label = Label(app, text="Payment Method").grid(row=11, column=0, sticky=W, padx=10)
discount_code_label = Label(app, text="Discount Code").grid(row=12, column=0, sticky=W, padx=10)
price_paid_label = Label(app, text="Price Paid").grid(row=13, column=0, sticky=W, padx=10)

# Create Entry Boxes
first_name_box = Entry(app)
first_name_box.grid(row=1, column=1)

last_name_box = Entry(app)
last_name_box.grid(row=2, column=1, pady=5)

address_1_box = Entry(app)
address_1_box.grid(row=3, column=1, pady=5)

address_2_box = Entry(app)
address_2_box.grid(row=4, column=1, pady=5)

city_box = Entry(app)
city_box.grid(row=5, column=1, pady=5)

state_box = Entry(app)
state_box.grid(row=6, column=1, pady=5)

zipcode_box = Entry(app)
zipcode_box.grid(row=7, column=1, pady=5)

country_box = Entry(app)
country_box.grid(row=8, column=1, pady=5)

phone_box = Entry(app)
phone_box.grid(row=9, column=1, pady=5)

email_box = Entry(app)
email_box.grid(row=10, column=1, pady=5)

payment_method_box = Entry(app)
payment_method_box.grid(row=11, column=1, pady=5)

discount_code_box = Entry(app)
discount_code_box.grid(row=12, column=1, pady=5)

price_paid_box = Entry(app)
price_paid_box.grid(row=13, column=1, pady=5)

# Buttons
add_customer_button = Button(app, text="Add Customer to Database", command=add_customer)
add_customer_button.grid(row=14, column=0, padx=10, pady=10)

clear_field_button = Button(app, text="Clear Fields", command=clear_fields)
clear_field_button.grid(row=14, column=1)

list_customers_button = Button(app, text="List All Customers", command=list_customers)
list_customers_button.grid(row=15 , column=0, sticky=W, padx=10)

search_customers_button = Button(app, text="Search/Edit Customers", command=search_customers)
search_customers_button.grid(row=15, column=1, sticky=W, padx=10)

app.mainloop()
