import pandas as pd
import psycopg2

print('psycopg2 installed!')
# Load Excel data
df = pd.read_excel(
    "fhinautospa.aniqsdatabase.xlsx",
    sheet_name="Fhin V1 (Visits Sheet)"
)

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="aniq321!"
)

cursor = conn.cursor()

# Insert rows
for _, row in df.iterrows():

    cursor.execute(
        """
        INSERT INTO Visits
        (VisitID, VisitDate, Plate, Amount)
        VALUES (%s, %s, %s, %s)
        """,
        (
            row["VisitID"],
            row["Date"],
            row["Clean Plate"],
            row["Amount"]
        )
    )

conn.commit()

print("Import completed!")

cursor.close()
conn.close()