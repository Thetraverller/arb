import sqlite3
import csv
import os

# SQLite database file path
db_file = "C:/Users/moham/Desktop/projects/TCW/Attendance/Students.db"
# Output folder path
output_folder = "C:/Users/moham/Desktop/projects/TCW/Attendance"

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Connect to the SQLite database
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Get the list of tables in the database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# Export each table to a separate CSV file
for table in tables:
    table_name = table[0]
    csv_file = os.path.join(output_folder, f"{table_name}.csv")

    with open(csv_file, "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        
        # Fetch all rows from the table
        cursor.execute(f"SELECT * FROM {table_name};")
        rows = cursor.fetchall()

        # Write the column names as the CSV header
        column_names = [description[0] for description in cursor.description]
        csv_writer.writerow(column_names)

        # Write the data rows
        csv_writer.writerows(rows)

# Close the database connection
conn.close()
