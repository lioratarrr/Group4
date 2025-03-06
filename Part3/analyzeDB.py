from pymongo import MongoClient

def analyze_db():
    # חיבור למסד הנתונים שלך
    client = MongoClient('mongodb+srv://liordana:liordana@cluster0.mgcw9.mongodb.net')
    mydatabase = client['database_project']

    # קבלת כל ה-collections במסד הנתונים
    collections = mydatabase.list_collection_names()

    # עבור כל collection, הדפס את שם ה-collection ואת הערכים בו
    for collection_name in collections:
        print(f"Collection: {collection_name}")
        collection = mydatabase[collection_name]
        documents = collection.find()  # קבלת כל המסמכים ב-collection
        for doc in documents:
            print(doc)

if __name__ == "__main__":
    analyze_db()
