from pymongo import MongoClient
from datetime import datetime
from bson.objectid import ObjectId

# How I connect to MongoDB to Mu VS Python code
client = MongoClient('mongodb://localhost:27017/')
db = client['ShopBot']

# Drop the existing database if it exists
if 'ShopBot' in client.list_database_names():
    client.drop_database('ShopBot')

# Re-create/Create the database
db = client['ShopBot']

# ShopBot the collections
users = [
    { "Name": "Alice Smith", "Email": "alice@example.com", "Password": "password123", "Age": 30, "Preferences": ["Electronics", "Books"] },
    { "Name": "Bob Jones", "Email": "bob@example.com", "Password": "password456", "Age": 25, "Preferences": ["Clothing", "Sports"] },
    { "Name": "Charlie Brown", "Email": "charlie@example.com", "Password": "password789", "Age": 35, "Preferences": ["Home", "Garden"] },
    { "Name": "Dana White", "Email": "dana@example.com", "Password": "password101", "Age": 28, "Preferences": ["Health", "Beauty"] },
    { "Name": "Eve Black", "Email": "eve@example.com", "Password": "password202", "Age": 32, "Preferences": ["Toys", "Games"] }
]
db.User.insert_many(users)

orders = [
    { "UserID": ObjectId("60c72b2f5b3f4a7f1e6e35d8"), "OrderDate": datetime(2024, 7, 1), "TotalAmount": 150.50, "Status": "Shipped" },
    { "UserID": ObjectId("60c72b2f5b3f4a7f1e6e35d9"), "OrderDate": datetime(2024, 7, 2), "TotalAmount": 75.00, "Status": "Pending" },
    { "UserID": ObjectId("60c72b2f5b3f4a7f1e6e35da"), "OrderDate": datetime(2024, 7, 3), "TotalAmount": 200.00, "Status": "Delivered" },
    { "UserID": ObjectId("60c72b2f5b3f4a7f1e6e35db"), "OrderDate": datetime(2024, 7, 4), "TotalAmount": 120.75, "Status": "Cancelled" },
    { "UserID": ObjectId("60c72b2f5b3f4a7f1e6e35dc"), "OrderDate": datetime(2024, 7, 5), "TotalAmount": 90.25, "Status": "Processing" }
]
db.Order.insert_many(orders)

products = [
    { "Name": "Smartphone", "Category": "Electronics", "Price": 599.99, "Description": "Latest model smartphone", "Stock": 50 },
    { "Name": "Running Shoes", "Category": "Sports", "Price": 89.99, "Description": "Comfortable running shoes", "Stock": 100 },
    { "Name": "Blender", "Category": "Home", "Price": 49.99, "Description": "High-speed blender", "Stock": 75 },
    { "Name": "Lipstick", "Category": "Beauty", "Price": 19.99, "Description": "Matte finish lipstick", "Stock": 200 },
    { "Name": "Board Game", "Category": "Toys", "Price": 29.99, "Description": "Fun board game for all ages", "Stock": 150 }
]
db.Product.insert_many(products)

recommendations = [
    { "UserID": ObjectId("60c72b2f5b3f4a7f1e6e35d8"), "ProductID": ObjectId("60c72b2f5b3f4a7f1e6e35e0"), "RecommendationDate": datetime(2024, 7, 1), "Reason": "Based on your preferences and purchase history" },
    { "UserID": ObjectId("60c72b2f5b3f4a7f1e6e35d9"), "ProductID": ObjectId("60c72b2f5b3f4a7f1e6e35e1"), "RecommendationDate": datetime(2024, 7, 2), "Reason": "Recommended for sports enthusiasts" },
    { "UserID": ObjectId("60c72b2f5b3f4a7f1e6e35da"), "ProductID": ObjectId("60c72b2f5b3f4a7f1e6e35e2"), "RecommendationDate": datetime(2024, 7, 3), "Reason": "Best seller in Home category" },
    { "UserID": ObjectId("60c72b2f5b3f4a7f1e6e35db"), "ProductID": ObjectId("60c72b2f5b3f4a7f1e6e35e3"), "RecommendationDate": datetime(2024, 7, 4), "Reason": "Top-rated beauty product" },
    { "UserID": ObjectId("60c72b2f5b3f4a7f1e6e35dc"), "ProductID": ObjectId("60c72b2f5b3f4a7f1e6e35e4"), "RecommendationDate": datetime(2024, 7, 5), "Reason": "Popular among families" }
]
db.Recommendation.insert_many(recommendations)

promotions = [
    { "ProductID": ObjectId("60c72b2f5b3f4a7f1e6e35e0"), "Discount": 10.00, "StartDate": datetime(2024, 7, 1), "EndDate": datetime(2024, 7, 7) },
    { "ProductID": ObjectId("60c72b2f5b3f4a7f1e6e35e1"), "Discount": 15.00, "StartDate": datetime(2024, 7, 2), "EndDate": datetime(2024, 7, 8) },
    { "ProductID": ObjectId("60c72b2f5b3f4a7f1e6e35e2"), "Discount": 5.00, "StartDate": datetime(2024, 7, 3), "EndDate": datetime(2024, 7, 9) },
    { "ProductID": ObjectId("60c72b2f5b3f4a7f1e6e35e3"), "Discount": 20.00, "StartDate": datetime(2024, 7, 4), "EndDate": datetime(2024, 7, 10) },
    { "ProductID": ObjectId("60c72b2f5b3f4a7f1e6e35e4"), "Discount": 10.00, "StartDate": datetime(2024, 7, 5), "EndDate": datetime(2024, 7, 11) }
]
db.Promotion.insert_many(promotions)

reviews = [
    { "ProductID": ObjectId("60c72b2f5b3f4a7f1e6e35e0"), "UserID": ObjectId("60c72b2f5b3f4a7f1e6e35d8"), "Rating": 5, "Comment": "Excellent product!", "ReviewDate": datetime(2024, 7, 1) },
    { "ProductID": ObjectId("60c72b2f5b3f4a7f1e6e35e1"), "UserID": ObjectId("60c72b2f5b3f4a7f1e6e35d9"), "Rating": 4, "Comment": "Very comfortable", "ReviewDate": datetime(2024, 7, 2) },
    { "ProductID": ObjectId("60c72b2f5b3f4a7f1e6e35e2"), "UserID": ObjectId("60c72b2f5b3f4a7f1e6e35da"), "Rating": 3, "Comment": "Works well, but noisy", "ReviewDate": datetime(2024, 7, 3) },
    { "ProductID": ObjectId("60c72b2f5b3f4a7f1e6e35e3"), "UserID": ObjectId("60c72b2f5b3f4a7f1e6e35db"), "Rating": 5, "Comment": "Love the color!", "ReviewDate": datetime(2024, 7, 4) },
    { "ProductID": ObjectId("60c72b2f5b3f4a7f1e6e35e4"), "UserID": ObjectId("60c72b2f5b3f4a7f1e6e35dc"), "Rating": 4, "Comment": "Great for family game nights", "ReviewDate": datetime(2024, 7, 5) }
]
db.Review.insert_many(reviews)

# Insert data into User collection
db.User.insert_many([
    { "Name": "Ace Burr", "Email": "ace@example.com", "Password": "password1283", "Age": 30, "Preferences": ["Electronics", "Books", "Games"] },
    { "Name": "Pran Johnson", "Email": "pran@example.com", "Password": "password456", "Age": 25, "Preferences": ["Clothing", "Sports"] },
    { "Name": "Chile Brown", "Email": "chile@example.com", "Password": "password789", "Age": 35, "Preferences": ["Home", "Garden"] },
    { "Name": "Dana McDonals", "Email": "dana@example.com", "Password": "password101", "Age": 28, "Preferences": ["Health", "Beauty"] },
    { "Name": "Adam Black", "Email": "adam@example.com", "Password": "password202", "Age": 32, "Preferences": ["Toys", "Games"] }
])

# Insert data into Order collection
db.Order.insert_many([
    { "UserID": ObjectId("UserID_1"), "OrderDate": datetime(2024, 7, 1), "TotalAmount": 150.50, "Status": "Shipped" },
    { "UserID": ObjectId("UserID_2"), "OrderDate": datetime(2024, 7, 2), "TotalAmount": 75.00, "Status": "Pending" },
    { "UserID": ObjectId("UserID_3"), "OrderDate": datetime(2024, 7, 3), "TotalAmount": 200.00, "Status": "Delivered" },
    { "UserID": ObjectId("UserID_4"), "OrderDate": datetime(2024, 7, 4), "TotalAmount": 120.75, "Status": "Cancelled" },
    { "UserID": ObjectId("UserID_5"), "OrderDate": datetime(2024, 7, 5), "TotalAmount": 90.25, "Status": "Processing" }
])

# Insert data into Product collection
db.Product.insert_many([
    { "Name": "Smartphone", "Category": "Electronics", "Price": 599.99, "Description": "Latest model smartphone", "Stock": 50 },
    { "Name": "Running Shoes", "Category": "Sports", "Price": 89.99, "Description": "Comfortable running shoes", "Stock": 100 },
    { "Name": "Blender", "Category": "Home", "Price": 49.99, "Description": "High-speed blender", "Stock": 75 },
    { "Name": "Lipstick", "Category": "Beauty", "Price": 19.99, "Description": "Matte finish lipstick", "Stock": 200 },
    { "Name": "Board Game", "Category": "Toys", "Price": 29.99, "Description": "Fun board game for all ages", "Stock": 150 }
])

# Insert data into Recommendation collection
db.Recommendation.insert_many([
    { "UserID": ObjectId("UserID_1"), "ProductID": ObjectId("ProductID_1"), "RecommendationDate": datetime(2024, 7, 1), "Reason": "Based on your preferences and purchase history" },
    { "UserID": ObjectId("UserID_2"), "ProductID": ObjectId("ProductID_2"), "RecommendationDate": datetime(2024, 7, 2), "Reason": "Recommended for sports enthusiasts" },
    { "UserID": ObjectId("UserID_3"), "ProductID": ObjectId("ProductID_3"), "RecommendationDate": datetime(2024, 7, 3), "Reason": "Best seller in Home category" },
    { "UserID": ObjectId("UserID_4"), "ProductID": ObjectId("ProductID_4"), "RecommendationDate": datetime(2024, 7, 4), "Reason": "Top-rated beauty product" },
    { "UserID": ObjectId("UserID_5"), "ProductID": ObjectId("ProductID_5"), "RecommendationDate": datetime(2024, 7, 5), "Reason": "Popular among families" }
])

# Insert data into Promotion collection
db.Promotion.insert_many([
    { "ProductID": ObjectId("ProductID_1"), "Discount": 10.00, "StartDate": datetime(2024, 7, 1), "EndDate": datetime(2024, 7, 7) },
    { "ProductID": ObjectId("ProductID_2"), "Discount": 15.00, "StartDate": datetime(2024, 7, 2), "EndDate": datetime(2024, 7, 8) },
    { "ProductID": ObjectId("ProductID_3"), "Discount": 5.00, "StartDate": datetime(2024, 7, 3), "EndDate": datetime(2024, 7, 9) },
    { "ProductID": ObjectId("ProductID_4"), "Discount": 20.00, "StartDate": datetime(2024, 7, 4), "EndDate": datetime(2024, 7, 10) },
    { "ProductID": ObjectId("ProductID_5"), "Discount": 10.00, "StartDate": datetime(2024, 7, 5), "EndDate": datetime(2024, 7, 11) }
])

# Insert data into Review collection
db.Review.insert_many([
    { "ProductID": ObjectId("ProductID_1"), "UserID": ObjectId("UserID_1"), "Rating": 5, "Comment": "Excellent product!", "ReviewDate": datetime(2024, 7, 1) },
    { "ProductID": ObjectId("ProductID_2"), "UserID": ObjectId("UserID_2"), "Rating": 4, "Comment": "Very comfortable", "ReviewDate": datetime(2024, 7, 2) },
    { "ProductID": ObjectId("ProductID_3"), "UserID": ObjectId("UserID_3"), "Rating": 3, "Comment": "Works well, but noisy", "ReviewDate": datetime(2024, 7, 3) },
    { "ProductID": ObjectId("ProductID_4"), "UserID": ObjectId("UserID_4"), "Rating": 5, "Comment": "Love the color!", "ReviewDate": datetime(2024, 7, 4) },
    { "ProductID": ObjectId("ProductID_5"), "UserID": ObjectId("UserID_5"), "Rating": 4, "Comment": "Great for family game nights", "ReviewDate": datetime(2024, 7, 5) }
])
