-- Insight: This query identifies the 10 tracks with the highest unit price
SELECT TrackId, Name , Compose, UnitPrice
FROM Track
ORDER BY UnitPrice DESC
LIMIT 10;

