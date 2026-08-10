SELECT
    t.TrackId,
    t.Name AS TrackName,
    SUM(il.Quantity) AS TotalQuantity
FROM Track t
JOIN InvoiceLine il
    ON t.TrackId = il.TrackId
GROUP BY t.TrackId
ORDER BY TotalQuantity DESC
LIMIT 10;