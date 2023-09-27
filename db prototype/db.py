import sqlite3
import json

# Connect to the SQLite database
conn = sqlite3.connect('sqlite.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Query flashcards data from the 'vocab1' table with 'word' and 'type' columns
cursor.execute("SELECT word, type FROM vocab1")
flashcards_data = cursor.fetchall()

# Create a list to hold flashcard objects
flashcards = []

# Iterate through the database rows and create flashcard objects
for row in flashcards_data:
    flashcard = {
        'word': row[0],
        'type': row[1]
    }
    flashcards.append(flashcard)

# Close the database connection
conn.close()

# Save the flashcards data as a JSON file
with open('flashcards.json', 'w', encoding='utf-8') as json_file:
    json.dump(flashcards, json_file, ensure_ascii=False, indent=4)

print("Flashcards JSON file created: flashcards.json")
