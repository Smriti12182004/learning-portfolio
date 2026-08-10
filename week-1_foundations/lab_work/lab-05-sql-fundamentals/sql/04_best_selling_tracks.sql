--Insight: This query identifies the 10 best-selling tracks by quantity sold
SELECT t.TrackId, t.Name, SUM(ii,Quantity) AS TotalQuantity
FROM InvoiceLine ii
INNER JOIN Track t
ON ii.TrackId= t.TrackId
GROUP BY t.TrackId, t.Name
ORDER BY TotalQuantity  DESC
LIMIT 10;
