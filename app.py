from flask import Flask, render_template, url_for
import json

app = Flask(__name__)

@app.route('/')
def index():
    with open('data/books.json') as f:
        books = json.load(f)
    return render_template('index.html', books=books)

@app.route('/book/<slug>')
def book(slug):
    with open('data/books.json') as f:
        books = json.load(f)
    book = next((b for b in books if b["slug"] == slug), None)
    if not book:
        return "Book not found", 404
    return render_template('book.html', book=book)

if __name__ == "__main__":
    app.run(debug=True)