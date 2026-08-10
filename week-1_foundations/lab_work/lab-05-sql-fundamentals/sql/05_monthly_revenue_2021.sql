-- Insight: This query shows the monthly revenue generated during 2021
SELECT strftime('%Y-%m', InvoiceDate) AS Month,
SUM(Total) AS MonthlyRevenue
FROM Invoice
WHERE InvoiceDate >= '2021-01-01'
AND InvoiceDate < '2022-01-01'
GROUP BY Month
ORDER BY Month;

