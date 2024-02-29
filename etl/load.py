from transform import maskeddata_cv, maskeddata_jobsdes
import sqlite3

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# Drop the table if it exists (optional)
cursor.execute('''DROP TABLE IF EXISTS CareerCraft''')


# Create the skilljob table with the specified columns
cursor.execute('''CREATE TABLE CareerCraft (
    maskedcv TEXT CHECK(LENGTH(maskedcv) <= 1000000000),
    maskedjobdes TEXT CHECK(LENGTH(maskedjobdes) <= 10000000000)
)''')


# Insert data into the table
insert_data = [
    (maskeddata_cv, maskeddata_jobsdes),
    # Add more rows as needed
]

cursor.executemany(
    "INSERT INTO CareerCraft (maskedcv, maskedjobdes) VALUES (?, ?)", insert_data)

# Commit the changes
conn.commit()


# Retrieve and display data
cursor.execute("SELECT * FROM CareerCraft")
rows = cursor.fetchall()

# Print the column names
column_names = [description[0] for description in cursor.description]
print(column_names)


# Print data in each column for each row
for row in rows:
    print(row)

# Close the connection
conn.close()
