from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime

# How I connect to MongoDB to VS Python code
client = MongoClient('mongodb://localhost:27017/')
db = client['ShopBot']

# Retrieve a list of all products
products = db.Product.find({})
for product in products:
    print(product)

# Find specific information based on a single criteria
electronics_products = db.Product.find({ "Category": "Electronics" })
for product in electronics_products:
    print(product)

# Find specific information based on one or more criteria
affordable_electronics = db.Product.find({ "Category": "Electronics", "Price": { "$lt": 1000 } })
for product in affordable_electronics:
    print(product)

# Add new records
db.User.insert_one({ "Name": "Frank Green", "Email": "frank@example.com", "Password": "password303", "Age": 27, "Preferences": ["Automotive", "Tools"] })

# Update current record
db.Product.update_one({ "_id": ObjectId("ProductID_1") }, { "$inc": { "Stock": 20 } })

# Remove a record
db.Review.delete_one({ "_id": ObjectId("ReviewID_1") })
