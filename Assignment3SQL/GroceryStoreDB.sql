
-- Create tables
Create TABLE Products
(
Product_ID INT PRIMARY KEY AUTO_INCREMENT,
Name VARCHAR(255) NOT NULL,
Category VARCHAR(150),
Price DECIMAL(10,2) CHECK (Price > 0),
StockQuantity INT DEFAULT 0 CHECK (StockQuantity >= 0)
);

CREATE TABLE Customers
(
Customer_ID INT PRIMARY KEY AUTO_INCREMENT,
Name VARCHAR(255) NOT NULL,
Email VARCHAR(255) UNIQUE NOT NULL,
PhoneNumber VARCHAR(14) UNIQUE NOT NULL
);

CREATE TABLE Orders
(
Order_ID INT PRIMARY KEY AUTO_INCREMENT,
Customer_ID INT,
Order_DATE  DATE ,
Total_Amount DECIMAL(10,2) CHECK(Total_Amount>=0),
CONSTRAINT FK_Customer FOREIGN KEY (Customer_ID) REFERENCES
Customers(Customer_ID)
);

CREATE TABLE OrderDetails 
(
OrderDetails_ID INT PRIMARY KEY AUTO_INCREMENT,
Order_ID INT,
Product_ID INT,
Quantity INT CHECK (Quantity>0),
Subtotal DECIMAL(10,2) CHECK (Subtotal>=0),
CONSTRAINT fk_Order FOREIGN KEY(Order_ID)REFERENCES Orders(Order_ID),
CONSTRAINT fk_Product FOREIGN KEY (Product_ID)REFERENCES Products(Product_ID)
);

-- Insert Data
INSERT INTO Products (Name,Category,Price,StockQuantity) VALUES
('Banana','Fruits', 2.20, 200),
('Oranges', 'Fruits',1.80, 250),
('Milk', 'Dairy',3.00,90),
('Bread', 'Bakery', 2.00,100),
('Eggs', 'Dairy', 3.50,70),
('Chicken','Meat', 6.50,50),
('Rice', 'Grains', 5.00, 90),
('Tomato', 'Vegetables', 1.20, 120);

INSERT INTO Customers (Name, Email, PhoneNumber)  VALUES
('Micheal Jordan','Micheal.J@email.com','1325476980'),
('Anna Sheppard','Anna.S@email.com','0896754321'),
('David Tanner','David.T@email.com','2347895016'),
('Freddy Khan','Freddy.K@email.com', '3245678901'),
('Brenda Penny', 'Brenda.P@email.com', '4567890123'),
('Catherine Wilson', 'Catherine.W@email.com','5768091324'),
('Emily Brown', 'Emily.B@email.com', '6789012345'),
('Peter Parker', 'Peter.P@email.com', '7890123456');

INSERT INTO Orders (Customer_ID, Order_Date, Total_Amount) VALUES
(1, '2024-02-01', 15.00),
(2, '2024-02-02', 25.50),
(3, '2024-02-03', 30.75),
(4, '2024-02-04', 10.20),
(5, '2024-02-05', 50.00),
(6, '2024-02-06', 20.30),
(7, '2024-02-07', 12.75),
(8, '2024-02-08', 40.10);

-- Insert Data into OrderDetails
INSERT INTO OrderDetails (Order_ID, Product_ID, Quantity, Subtotal) VALUES
(1, 1, 5, 11.00),
(1, 4, 2, 4.00),
(2, 2, 10, 18.00),
(2, 3, 5, 15.00),
(3, 5, 3, 10.50),
(3, 7, 2, 10.00),
(4, 8, 4, 4.80),
(5, 6, 6, 39.00);

-- Retrieve Data
SELECT * FROM Products ORDER BY Price DESC;
SELECT Name, Email FROM Customers ORDER BY Name ASC;
SELECT Name, Category FROM Products WHERE Category = 'Dairy';
SELECT * FROM Orders WHERE Total_Amount > 20;
SELECT Customers.Name, Orders.Order_Date, Orders.Total_Amount 
FROM Orders 
JOIN Customers ON Orders.Customer_ID = Customers.Customer_ID
ORDER BY Order_Date DESC;

-- : Aggregate Functions
SELECT COUNT(*) AS TotalProducts FROM Products;
SELECT AVG(Price) AS AveragePrice FROM Products;

-- In-Built Functions
SELECT UPPER(Name) AS UppercaseName FROM Customers;
SELECT LENGTH(Name) AS NameLength, Name FROM Products;


-- Stored Procedure
DELIMITER //
CREATE PROCEDURE GetCustomerOrders(IN customer_name VARCHAR(255))
BEGIN
    SELECT Orders.Order_ID, Orders.Order_Date, Orders.Total_Amount 
    FROM Orders
OrderDetails_ID    JOIN Customers ON Orders.Customer_ID = Customers.Customer_ID
    WHERE Customers.Name = customer_name;
END //
DELIMITER ;

-- Call the stored procedure
CALL GetCustomerOrders('Micheal Jordan');