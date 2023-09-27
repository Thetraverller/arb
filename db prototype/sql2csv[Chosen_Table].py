import sqlite3
import os
import xlsxwriter
from datetime import datetime

# SQLite database file path
db_file = "C:/Users/moham/Desktop/projects/TCW/Attendance/Students.db"
# Output folder path (manually created)
output_folder = "C:/Users/moham/Desktop/projects/TCW/Attendance/output"

# Connect to the SQLite database
conn = sqlite3.connect(db_file)

# Export the "Combined_Attendance" table to an Excel file (.xlsx)
table_name = "Combined_Attendance"
excel_file = os.path.join(output_folder, f"{table_name}.xlsx")

# Create a new Excel workbook and add a worksheet
workbook = xlsxwriter.Workbook(excel_file)
worksheet = workbook.add_worksheet()

# Get the column names from the table
cursor = conn.cursor()
cursor.execute(f"PRAGMA table_info({table_name});")
column_info = cursor.fetchall()
column_names = [col[1] for col in column_info]

# Fetch all rows from the table
cursor.execute(f'SELECT * FROM "{table_name}";')  # Use double quotes to enclose the table name
rows = cursor.fetchall()

# Write the column names as the header
for col_idx, col_name in enumerate(column_names):
    worksheet.write(0, col_idx, col_name)

# Write the data rows
for row_idx, row in enumerate(rows, 1):
    for col_idx, value in enumerate(row):
        worksheet.write(row_idx, col_idx, value)

# Close the Excel workbook (this saves the file)
workbook.close()

# Close the database connection
conn.close()