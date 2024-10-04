# data based on a single key #
SELECT * FROM User WHERE UserID = 1;

# number of keys and criteria #
SELECT * FROM Product WHERE Category = 'Electronics' AND Price < 1000;

# unique characters search #
SELECT * FROM Review WHERE Rating = 5;

# total number of records given a unique character #
SELECT COUNT(*) FROM `Order` WHERE Status = 'Shipped';

# Add new records #
INSERT INTO User (Name, Email, Password, Age, Preferences) VALUES
('Frank Green', 'frank@example.com', 'password303', 27, 'Automotive, Tools');

# Update current record #
UPDATE Product SET Stock = Stock + 20 WHERE ProductID = 1;

# Remove a record # #
DELETE FROM Review WHERE ReviewID = 1;

