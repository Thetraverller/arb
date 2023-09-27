const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const app = express();
const port = 3000;

const db = new sqlite3.Database('sqlite.db');

app.use(express.static('public')); // Serve static files from the 'public' directory

app.get('/flashcards', (req, res) => {
  db.all('SELECT word, meaning FROM vocab1', [], (err, rows) => {
    if (err) {
      throw err;
    }
    res.json(rows); // Send the flashcards as JSON
  });
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
