-- Insiqht: This query lists all customers from India
SELECT CustomerId, FirstName, LastName, Email, Country
FROM Customer
WHERE Country = 'India'
