import sqlite3
import random

# Connect to the SQLite database
conn = sqlite3.connect("sqlite.db")
cursor = conn.cursor()

# Fetch all rows from the vocab1 table
cursor.execute("SELECT word, type FROM vocab1")
flashcards_data = cursor.fetchall()

# Shuffle the flashcards
random.shuffle(flashcards_data)

# HTML template for the flashcards
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flashcard App</title>
    <style>
        /* Add your CSS styles here */
    </style>
</head>
<body>
    <div class="container">
        <div class="main-content">
            <h1>Flashcard App</h1>
            
            <div class="flashcard" id="flashcard">
                <div class="flashcard-content" id="word">{}</div>
                <div class="flashcard-content" id="type" style="display: none;">{}</div>
            </div>
            
            <button id="next-button">Next</button>
        </div>
    </div>

    <script>
        let flashcards = {};
        let currentCardIndex = 0;

        const flashcard = document.getElementById("flashcard");
        const wordElement = document.getElementById("word");
        const typeElement = document.getElementById("type");
        const nextButton = document.getElementById("next-button");

        function showFlashcard(index) {
            const card = flashcards[index];
            wordElement.textContent = card.word;
            typeElement.textContent = card.type;
            typeElement.style.display = "none";
        }

        nextButton.addEventListener("click", function () {
            currentCardIndex = (currentCardIndex + 1) % flashcards.length;
            showFlashcard(currentCardIndex);
        });

        flashcards = {}
        """
# Insert flashcard data into the HTML template
for i, flashcard_data in enumerate(flashcards_data):
    word, type = flashcard_data
    html_template += f"""
    flashcards[{i}] = {{
        word: "{word}",
        type: "{type}"
    }};
    """
html_template += """
    showFlashcard(currentCardIndex);
    </script>
</body>
</html>
"""

# Write the HTML content to a file
with open("flashcards.html", "w", encoding="utf-8") as html_file:
    html_file.write(html_template)

# Close the database connection
conn.close()

print("Flashcards HTML file generated successfully!")
