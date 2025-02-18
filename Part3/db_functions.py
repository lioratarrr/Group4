from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime

uri = "mongodb+srv://liordana:liordana@cluster0.mgcw9.mongodb.net"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# הגדרת מסד הנתונים והקולקשן
mydatabase = client['database_project']
branches_col = mydatabase['Branches']
jeweleries_col = mydatabase['jewelries']
customers_col = mydatabase['Customers']
orders_col = mydatabase['Orders']
jeweleries_col.create_index("jewelry_id", unique=True)


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

def get_branches():
  return branches_col.find()

  # Retrieve all jewelry items from the collection
def get_all_jewelries():
  jewelries = jeweleries_col.find()
  return list(jewelries)  # Convert cursor to a list and return it

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

def email_exists(email):
    user = customers_col.find_one({"email": email})  # MongoDB example
    if user:
        return True
    return False


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

def get_first_name (email):
  user = customers_col.find_one({"email": email}, {"_id": 0, "first_name": 1})
  return user['first_name']

def get_orders(email):
    orders = orders_col.find({'email': email}) \
      .sort('date', -1)
    return list(orders)


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

