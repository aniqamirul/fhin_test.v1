SELECT
    COUNT(*) AS TotalVisits,
    COUNT(DISTINCT Plate) AS UniqueCustomers,
    SUM(Amount) AS Revenue,
    AVG(Amount) AS AverageSpend,
    MAX(Amount) AS HighestTransaction,
    MIN(Amount) AS LowestTransaction
FROM Visits;

SELECT
    Plate,
    COUNT(*) AS Visits,
    SUM(Amount) AS Revenue
FROM Visits
GROUP BY Plate
ORDER BY Revenue DESC
LIMIT 10;

SELECT
    Plate,
    COUNT(*) AS Visits,
    SUM(Amount) AS Revenue
FROM Visits
GROUP BY Plate
HAVING COUNT(*) >= 2
ORDER BY Revenue DESC;

SELECT
    Plate,
    COUNT(*) AS Visits,
    SUM(Amount) AS Revenue
FROM Visits
GROUP BY Plate
HAVING COUNT(*) >= 3
   AND SUM(Amount) >= 100
ORDER BY Revenue DESC;

SELECT
    VisitDate,
    COUNT(*) AS Visits,
    SUM(Amount) AS Revenue
FROM Visits
GROUP BY VisitDate
ORDER BY Revenue DESC;