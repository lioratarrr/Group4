import email
import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime, timedelta
from bson import ObjectId

load_dotenv()

uri = os.environ.get('DB_URI')

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Define the database and collections
mydatabase = client['database_project']
branches_col = mydatabase['Branches']
jeweleries_col = mydatabase['jewelries']
customers_col = mydatabase['Customers']
orders_col = mydatabase['Orders']
inquiries_col = mydatabase['Inquiries']
jeweleries_col.create_index("jewelry_id", unique=True)


# Function to get jewelry items by category
def get_jewelry_by_category(category_name):
  jewelry_data = jeweleries_col.find({"category": category_name})
  category_info = {
    'title': category_name,
    'category': []  # List to hold the jewelry items in the category
  }

  for jewelry in jewelry_data:
    jewelry_info = {
      'name': jewelry['name'],
      'image_gold': jewelry['image_gold'],  # Default to the gold image
      'alt': jewelry['description'],  # Use description as alt text (you can modify as needed)
      'description': jewelry['description'],
      'image_silver': jewelry.get('image_silver', '')  # Add silver image if available
    }
    category_info['category'].append(jewelry_info)

  return category_info
# Function to get all branches
def get_branches():
  return branches_col.find()

  # Retrieve all jewelry items from the collection
def get_all_jewelries():
  jewelries = jeweleries_col.find()
  return list(jewelries)  # Convert cursor to a list and return it
# Function to insert a new user into the customers collection
def insert_user_data(firstname, lastname, email, password, city, address, aptnum, phonenum):
  customers_col.insert_one({
    "first_name": firstname,
    "last_name": lastname,
    "email": email,
    "password": password,
    "city": city,
    "address": address,
    "aptnum": aptnum,
    "phonenum": phonenum
  })
# Function to check if an email already exists in the database
def email_exists(email):
    user = customers_col.find_one({"email": email})  # MongoDB example
    if user:
        return True
    return False

# Function to verify user login credentials
def verify_user_login(email, password):
  user = customers_col.find_one({"email": email})
  if user and user['password'] == password:  # Directly comparing the plain text password
    # If user is found and the password matches
    return True
  return False

from pymongo import MongoClient

# Assuming you have a MongoDB connection setup
client = MongoClient('mongodb://localhost:27017')
db = client['your_database']
orders_collection = db['orders']
# Function to verify user login credentials
def save_order(order_data):
    try:
      now = datetime.now()
      order_data['DT']= now.strftime("%d/%m/%Y %H:%M:%S")
      # Insert order into MongoDB
      orders_col.insert_one(order_data)
      return True
    except Exception as e:
        print(f"Error saving order: {e}")
        return False
# Function to verify user login credentials
def get_first_name (email):
  user = customers_col.find_one({"email": email}, {"_id": 0, "first_name": 1})
  return user['first_name']

def get_orders(email):
    orders = orders_col.find({'email': email}) \
      .sort('date', -1)
    return list(orders)

# Function to retrieve user information from the database
def get_info(email):
  # Fetch each piece of information separately and extract the values
  firstname = customers_col.find_one({"email": email}, {"first_name": 1}).get("first_name")
  lastname = customers_col.find_one({"email": email}, {"last_name": 1}).get("last_name")
  phone = customers_col.find_one({"email": email}, {"phonenum": 1}).get("phonenum")
  city = customers_col.find_one({"email": email}, {"city": 1}).get("city")
  address = customers_col.find_one({"email": email}, {"address": 1}).get("address")
  aptnum = customers_col.find_one({"email": email}, {"aptnum": 1}).get("aptnum")

  # Create a dictionary instead of a list for easier access
  info = {
    "firstname": firstname,
    "lastname": lastname,
    "phone": phone,
    "city": city,
    "address": address,
    "aptnum": aptnum
  }
  return info

def save_inquiry (contactus_data):
  try:
    # Insert order into MongoDB
    inquiries_col.insert_one(contactus_data)
    return True
  except Exception as e:
    print(f"Error saving order: {e}")
    return False

def delete_order_by_id(order_id, email):
  result = orders_col.delete_one({'_id': order_id, 'email': email})
  print(f"Deleted count: {result.deleted_count}")

def update_user_info(email, field, new_value):
    # Based on the field, update the appropriate user information
    if field == 'name':
      first_name, last_name = new_value.split()  # Split the new value into first and last names
      result = customers_col.update_one(
        {'email': email},
        {'$set': {'first_name': first_name, 'last_name': last_name}}
      )
    elif field == 'phone':
      result = customers_col.update_one(
        {'email': email},
        {'$set': {'phonenum': new_value}}
      )
    elif field == 'city':
      result = customers_col.update_one(
        {'email': email},
        {'$set': {'city': new_value}}
      )
    elif field == 'address':
      result = customers_col.update_one(
        {'email': email},
        {'$set': {'address': new_value}}
      )
    elif field == 'aptnum':
      result = customers_col.update_one(
        {'email': email},
        {'$set': {'aptnum': new_value}}
      )
    else:
      return None  # Invalid field
    return result


def delete_order_by_id(order_id):
  try:
    # Ensure the order_id is a valid ObjectId
    if not ObjectId.is_valid(order_id):
      return False, "Invalid order ID"

    # Find the order by ID
    order = orders_col.find_one({"_id": ObjectId(order_id)})

    if not order:
      return False, "Order not found"

    # Get the DT field from the order and convert it to datetime
    order_time_str = order.get("DT")
    order_time = datetime.strptime(order_time_str, "%d/%m/%Y %H:%M:%S")  # Adjust format if needed

    # Get the current time
    current_time = datetime.now()

    # Check if more than 24 hours have passed
    if current_time - order_time > timedelta(hours=24):
      return False, "לא ניתן לבטל את ההזמנה, עבר יותר מ-24 שעות. לפרטים נוספים נא לפנות לסניף"

    # If less than 24 hours, proceed with deletion
    result = orders_col.delete_one({"_id": ObjectId(order_id)})

    if result.deleted_count > 0:
      return True, "Order deleted successfully"
    else:
      return False, "Order not found"

  except Exception as e:
    return False, f"Error: {str(e)}"
