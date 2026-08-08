-- Insight: This query calculate  total invoice revenue for each country

SELECT c.Country, SUM(i,Total) AS TotalRevenue
FROM Customer c
INNER JOIN Invoice i
ON c.CustomerId = i.CustomerId
GROUP BY c.Customer 
ORDER BY TotalRevenue DESC;
