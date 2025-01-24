from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://liordana:liordana@cluster0.mgcw9.mongodb.net"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# הגדרת מסד הנתונים והקולקשן
mydatabase = client['database_project']
branches_col = mydatabase['Branches']

# Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(f"Failed to connect to MongoDB: {e}")
#     exit()  # יוצאים אם החיבור נכשל
#
# # הגדרת הנתונים להוספה
# branches_data = [
#     {
#         "branch_id": 1,
#         "city": "ירושלים",
#         "address": "רחוב יפו 1",
#         "phone": "02-1234567",
#         "gps_location": {"lat": 31.7683, "lng": 35.2137}
#     },
#     {
#         "branch_id": 2,
#         "city": "אשקלון",
#         "address": "רחוב הנשיא 10",
#         "phone": "08-1234567",
#         "gps_location": {"lat": 31.6658, "lng": 34.5666}
#     },
#     {
#         "branch_id": 3,
#         "city": "רחובות",
#         "address": "רחוב הרצל 50",
#         "phone": "08-7654321",
#         "gps_location": {"lat": 31.8948, "lng": 34.8113}
#     },
#     {
#         "branch_id": 4,
#         "city": "מודיעין",
#         "address": "רחוב מרכזי 15",
#         "phone": "08-1122334",
#         "gps_location": {"lat": 31.9066, "lng": 35.0004}
#     },
#     {
#         "branch_id": 5,
#         "city": "תל אביב",
#         "address": "רחוב דיזנגוף 100",
#         "phone": "03-1234567",
#         "gps_location": {"lat": 32.0853, "lng": 34.7818}
#     },
#     {
#         "branch_id": 6,
#         "city": "באר שבע",
#         "address": "רחוב רינגלבלום 25",
#         "phone": "08-9988776",
#         "gps_location": {"lat": 31.2529, "lng": 34.7915}
#     }
# ]
#
# # הוספת הנתונים
# try:
#     result = branches_col.insert_many(branches_data)
#     print(f"Inserted document IDs: {result.inserted_ids}")
# except Exception as e:
#     print(f"Failed to insert documents: {e}")
#
#
jeweleries_col = mydatabase['jewelries']
# bracelet_data = [
#     {
#         "jewelry_id": 1,
#         "name": "צמיד דנה",
#         "category": "bracelets",
#         "options": [
#             {"material": "זהב", "size": "5 ס״מ"},
#             {"material": "זהב", "size": "7 ס״מ"},
#             {"material": "כסף", "size": "6 ס״מ"},
#             {"material": "כסף", "size": "8 ס״מ"}
#         ],
#         "description": "צמיד עם עיצוב חוליות גדולות ומודרניות מתאים למראה אלגנטי או יומיומי",
#         "image_gold": "jewelery/Bracelets/danagold.png",
#         "image_silver": "jewelery/Bracelets/danasilver.png"
#     },
#     {
#         "jewelry_id": 2,
#         "name": "צמיד לב",
#         "category": "bracelets",
#         "options": [
#             {"material": "זהב", "size": "4 ס״מ"},
#             {"material": "זהב", "size": "6 ס״מ"},
#             {"material": "כסף", "size": "5 ס״מ"},
#             {"material": "כסף", "size": "7 ס״מ"}
#         ],
#         "description": "צמיד עם תליון לב, מעוצב בעדינות מושלם למראה רומנטי או מתנה לאהוב/ה",
#         "image_gold": "jewelery/Bracelets/heartgold.png",
#         "image_silver": "jewelery/Bracelets/heartsilver.png"
#     },
#     {
#         "jewelry_id": 3,
#         "name": "צמיד מגן דוד",
#         "category": "bracelets",
#         "options": [
#             {"material": "זהב", "size": "5 ס״מ"},
#             {"material": "זהב", "size": "8 ס״מ"},
#             {"material": "כסף", "size": "6 ס״מ"},
#             {"material": "כסף", "size": "9 ס״מ"}
#         ],
#         "description": "צמיד עם תליון מגן דוד, עדין ואלגנטי מתאים לאירועים עם משמעות יהודית או יום-יום",
#         "image_gold": "jewelery/Bracelets/davidgold.png",
#         "image_silver": "jewelery/Bracelets/davidsilver.png"
#     },
#     {
#         "jewelry_id": 4,
#         "name": "צמיד שיבולים",
#         "category": "bracelets",
#         "options": [
#             {"material": "זהב", "size": "6 ס״מ"},
#             {"material": "זהב", "size": "8 ס״מ"},
#             {"material": "כסף", "size": "5 ס״מ"},
#             {"material": "כסף", "size": "7 ס״מ"}
#         ],
#         "description": "צמיד בהשראת שיבולים, עיצוב טבעי ופשוט מושלם למראה קלאסי ונקי",
#         "image_gold": "jewelery/Bracelets/oatgold.png",
#         "image_silver": "jewelery/Bracelets/oatsilver.png"
#     },
#     {
#         "jewelry_id": 5,
#         "name": "צמיד שם",
#         "category": "bracelets",
#         "options": [
#             {"material": "זהב", "size": "5 ס״מ"},
#             {"material": "זהב", "size": "7 ס״מ"},
#             {"material": "כסף", "size": "6 ס״מ"},
#             {"material": "כסף", "size": "8 ס״מ"}
#         ],
#         "description": "צמיד עם תליון בהתאמה אישית לשם, מתנה ייחודית עם נגיעה אישית",
#         "image_gold": "jewelery/Bracelets/namegold.png",
#         "image_silver": "jewelery/Bracelets/namesilver.png"
#     }
#
# ]
# try:
#     result = jeweleries_col.insert_many(bracelet_data)
#     print(f"Inserted bracelets: {result.inserted_ids}")
# except Exception as e:
#     print(f"Error while inserting bracelets: {e}")
#
#
#     # נתוני העגילים עם מספרי מידות
#     earrings_data = [
#         {
#             "jewelry_id": 6,
#             "name": "עגילי ג׳סיקה",
#             "category": "earings",
#             "options": [
#                 {"material": "זהב", "size": 5},
#                 {"material": "זהב", "size": 7},
#                 {"material": "כסף", "size": 6},
#                 {"material": "כסף", "size": 8}
#             ],
#             "description": "עגילים עם פנינה בעיצוב קלאסי ועדין, מושלמים להוספת טאץ׳ יוקרתי לכל הופעה",
#             "image_gold": "jewelery/Earings/jesicagold.png",
#             "image_silver": "jewelery/Earings/jesicasilver.png"
#         },
#         {
#             "jewelry_id": 7,
#             "name": "עגילי ליאור",
#             "category": "earings",
#             "options": [
#                 {"material": "זהב", "size": 4},
#                 {"material": "זהב", "size": 6},
#                 {"material": "כסף", "size": 5},
#                 {"material": "כסף", "size": 7}
#             ],
#             "description": "עגילים בצורת פרח, עדינים וקלילים, מתאימים למראה טבעי וצעיר",
#             "image_gold": "jewelery/Earings/liorgold.png",
#             "image_silver": "jewelery/Earings/liorsilver.png"
#         },
#         {
#             "jewelry_id": 8,
#             "name": "עגילי סבינה",
#             "category": "earings",
#             "options": [
#                 {"material": "זהב", "size": 6},
#                 {"material": "זהב", "size": 8},
#                 {"material": "כסף", "size": 5},
#                 {"material": "כסף", "size": 7}
#             ],
#             "description": "עגילים עם תליון לב, רומנטיים ונשיים, משלימים הופעה למראה ייחודי",
#             "image_gold": "jewelery/Earings/sabinagold.png",
#             "image_silver": "jewelery/Earings/sabinasilver.png"
#         },
#         {
#             "jewelry_id": 9,
#             "name": "עגילי סמבה",
#             "category": "earings",
#             "options": [
#                 {"material": "זהב", "size": 5},
#                 {"material": "זהב", "size": 9},
#                 {"material": "כסף", "size": 6},
#                 {"material": "כסף", "size": 8}
#             ],
#             "description": "עגילים בעלי עיצוב חלק ומבריק, מתאימים למראה אלגנטי או יום-יומי",
#             "image_gold": "jewelery/Earings/sambagold.png",
#             "image_silver": "jewelery/Earings/sambasilver.png"
#         },
#         {
#             "jewelry_id": 10,
#             "name": "עגילי רוני",
#             "category": "earings",
#             "options": [
#                 {"material": "זהב", "size": 5},
#                 {"material": "זהב", "size": 7},
#                 {"material": "כסף", "size": 6},
#                 {"material": "כסף", "size": 8}
#             ],
#             "description": "עגילים בצורת לב, עיצוב קלאסי ונצחי, מושלמים למראה רומנטי ומיוחד",
#             "image_gold": "jewelery/Earings/ronigold.png",
#             "image_silver": "jewelery/Earings/ronisilver.png"
#         }
#     ]
#     # הוספת העגילים (מחוץ ל-except של הצמידים)
# try:
#     result = jeweleries_col.insert_many(earrings_data)
#     print(f"Inserted earrings: {result.inserted_ids}")
# except Exception as e:
#     print(f"Error while inserting earrings: {e}")


def get_jewelry_by_category(category_name):
  jewelry_data = jeweleries_col.find({"category": category_name})
  category_info = {
    'title': category_name,
    'category': []  # List to hold the jewelry items in the category
  }

  for jewelry in jewelry_data:
    jewelry_info = {
      'name': jewelry['name'],
      'image': jewelry['image_gold'],  # Default to the gold image
      'alt': jewelry['description'],  # Use description as alt text (you can modify as needed)
      'description': jewelry['description'],
      'image_silver': jewelry.get('image_silver', '')  # Add silver image if available
    }
    category_info['category'].append(jewelry_info)

  return category_info

def get_branches():
  return branches_col.find()


