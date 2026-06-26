import sqlite3

conn = sqlite3.connect("sales.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    title TEXT,
    Sales INTEGER
)
""")

data = [
    ("Jan", 86400),
    ("Feb", 120000),
    ("Mar", 19460),
    ("Apr", 182900),
    ("May", 156800),
    ("Jun", 135000)
]

cursor.executemany("INSERT INTO sales VALUES (?, ?)", data)

conn.commit()
conn.close()

print("Database Created Successfully!")