from flask import Flask, json, make_response, request

from lib.author import Author
from lib.book import Book
from lib.employee import Employee

app = Flask(__name__)

@app.route('/books', methods=['GET'])
def books():
    if request.method == 'GET':
        return Book.get_books()

@app.route('/books/<int:id>', methods=['GET'])
# request API curl -X GET http://localhost:5000/books/7 -i
def book(id):
    if request.method == 'GET':
        return Book.get_book(id)

@app.route('/authors', methods=['GET'])
def authors():
    if request.method == 'GET':
        return Author.get_authors()

@app.route('/employees', methods=['GET'])
def employees():
    if request.method == 'GET':
        return Employee.get_employees()

if __name__ == '__main__':
    app.run()