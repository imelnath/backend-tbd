from flask import Flask, json, jsonify, make_response, request

from lib.author import Author
from lib.book import Book
from lib.employee import Employee

app = Flask(__name__)

@app.route('/books', methods=['GET'])
def books():
    if request.method == 'GET':
        data = Book.get_books()
        res = jsonify(data)
        
        return res

@app.route('/books/<int:id>', methods=['GET', 'POST'])
# request API curl -X GET http://localhost:5000/books/7 -i
def book(id):
    if request.method == 'GET':
        return Book.get_book(id)
    
    # curl -X POST -H "Content-Type:application/json" -d '{"store":1,"book_number":32,"book_name":"tutorial ternak ikan","publication_year":2022,"pages":45,"pname":"Penerbit Erlangga","quantity":1,"price":30000}' http://127.0.0.1:5000/books/7 -i
    if request.method == 'POST':
        try:
            data = request.get_json()
            
            
            req = {
                "store": data.get('store'),
                "book_number": data.get('book_number'),
                "book_name": data.get('book_name'),
                "publication_year": data.get('publication_year'),
                "pages": data.get('pages'),
                "pname": data.get('pname'),
                "quantity": data.get('quantity'),
                "price": data.get('price'),
            }
            
            print(req)
            return 'success'
        except Exception as err:
            print(err)
            


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