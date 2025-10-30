-- Select the database
USE alx_book_store;

-- Insert a single record into the customer table
INSERT INTO customer (customer_id, customer_name, email, address)
VALUES (1, 'Cole Baidoo', 'cbaidoo@sandtech.com', '123 Happiness Ave.');

How To Run
mysql -u root -p alx_book_store < task_5.sql
