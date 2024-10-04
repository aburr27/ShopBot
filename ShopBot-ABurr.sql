##########################################################################
# ShopBot.sql - Arebria Burr 08/02/2024  -  Creating my ShopBot database #
##########################################################################

DROP DATABASE IF EXISTS ShopBot;
CREATE DATABASE ShopBot; 
USE ShopBot;

#####################
# Create all tables #
#####################

CREATE TABLE User (
    UserID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100),
    Email VARCHAR(100),
    Password VARCHAR(100),
    Age INT,
    Preferences TEXT
);

CREATE TABLE Product (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100),
    Category VARCHAR(50),
    Price DECIMAL(10, 2),
    Description TEXT,
    Stock INT
);

CREATE TABLE `Order` (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,
    UserID INT,
    OrderDate DATE,
    TotalAmount DECIMAL(10, 2),
    Status VARCHAR(50),
    FOREIGN KEY (UserID) REFERENCES User(UserID)
);

CREATE TABLE `OrderItems` (
    order_item_id INT AUTO_INCREMENT PRIMARY KEY, 
    ProductID INT NOT NULL, 
    Quantity INT NOT NULL,
    OrderID INT NOT NULL,
    UserID INT NOT NULL,
    OrderDate DATE NOT NULL,
    Status VARCHAR(50),
    FOREIGN KEY (UserID) REFERENCES User(UserID),
    FOREIGN KEY (OrderID) REFERENCES `Order`(OrderID),
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID)
);

CREATE TABLE Recommendation (
    RecommendationID INT AUTO_INCREMENT PRIMARY KEY,
    UserID INT,
    ProductID INT,
    RecommendationDate DATE,
    Reason TEXT,
    FOREIGN KEY (UserID) REFERENCES User(UserID),
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID)
);

CREATE TABLE Promotion (
    PromotionID INT AUTO_INCREMENT PRIMARY KEY,
    ProductID INT,
    Discount DECIMAL(5, 2),
    StartDate DATE,
    EndDate DATE,
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID)
);

CREATE TABLE Review (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,
    ProductID INT,
    UserID INT,
    Rating INT,
    Comment TEXT,
    ReviewDate DATE,
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID),
    FOREIGN KEY (UserID) REFERENCES User(UserID)
);

###################################
# Populating data into each table #
###################################

INSERT INTO User (Name, Email, Password, Age, Preferences)
VALUES 
('Alice', 'alice@example.com', 'password123', 30, 'Electronics'),
('Bob', 'bob@example.com', 'password456', 25, 'Books'),
('Charlie', 'charlie@example.com', 'password789', 28, 'Clothing');

INSERT INTO Product (Name, Category, Price, Description, Stock)
VALUES 
('Laptop', 'Electronics', 999.99, 'High-end gaming laptop', 10),
('Smartphone', 'Electronics', 699.99, 'Latest 5G smartphone', 20),
('Novel', 'Books', 19.99, 'Best-selling mystery novel', 50);

INSERT INTO `Order` (UserID, OrderDate, TotalAmount, Status)
VALUES 
(1, '2024-09-12', 1049.98, 'Shipped'),
(2, '2024-09-13', 19.99, 'Processing'),
(3, '2024-09-14', 999.99, 'Delivered');

INSERT INTO `OrderItems` (ProductID, Quantity, OrderID, UserID, OrderDate, Status)
VALUES 
(1, 1, 1, 1, '2024-09-12', 'Shipped'),  -- Laptop
(3, 1, 2, 2, '2024-09-13', 'Processing'),  -- Novel
(2, 1, 3, 3, '2024-09-14', 'Delivered');  -- Smartphone

INSERT INTO Recommendation (UserID, ProductID, RecommendationDate, Reason)
VALUES 
(1, 1, '2024-09-15', 'Based on your interest in gaming'),
(2, 3, '2024-09-16', 'Recommended based on previous purchases');

INSERT INTO Promotion (ProductID, Discount, StartDate, EndDate)
VALUES 
(1, 15.00, '2024-09-10', '2024-09-20'),  -- 15% discount on Laptop
(3, 10.00, '2024-09-11', '2024-09-18');  -- 10% discount on Novel

INSERT INTO Review (ProductID, UserID, Rating, Comment, ReviewDate)
VALUES 
(1, 1, 5, 'Excellent laptop for gaming!', '2024-09-16'),
(3, 2, 4, 'Great read, but a bit predictable.', '2024-09-17');


