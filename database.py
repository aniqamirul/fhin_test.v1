import psycopg2


def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="aniq321!"
    )


def total_revenue():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT SUM(Amount)
        FROM Visits
    """)

    result = cur.fetchone()[0]

    conn.close()

    return result


def total_visits():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT COUNT(*)
        FROM Visits
    """)

    result = cur.fetchone()[0]

    conn.close()

    return result


def top_customers():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT
            Plate,
            SUM(Amount) AS Revenue
        FROM Visits
        GROUP BY Plate
        ORDER BY Revenue DESC
        LIMIT 10
    """)

    result = cur.fetchall()

    conn.close()

    return result


def returning_customers():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT
            Plate,
            COUNT(*) AS Visits,
            SUM(Amount) AS Revenue
        FROM Visits
        GROUP BY Plate
        HAVING COUNT(*) >= 2
        ORDER BY Revenue DESC
    """)

    result = cur.fetchall()

    conn.close()

    return result