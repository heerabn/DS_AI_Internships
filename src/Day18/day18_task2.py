import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect(r"E:\DS_AI_Internship\src\sql lite\internships.db")

# SQL JOIN query
query = """
SELECT
    interns.name,
    interns.track,
    mentors.mentor_name
FROM interns
INNER JOIN mentors
ON interns.track = mentors.track
"""

# Load into Pandas DataFrame
df = pd.read_sql_query(query, conn)

# Show result
print(df)

# Close connection
conn.close()