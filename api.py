from flask import Flask, json, jsonify, make_response, request
from flask_cors import CORS

from lib.author import Author
from lib.book import Book
from lib.bought import Bought
from lib.customer import Customer
from lib.publisher import Publisher
from lib.staff import Staff
from lib.stock import Stock
from lib.store import Store
from lib.wrote import Wrote

app = Flask(__name__)
CORS(app)

@app.route('/books', methods=['GET','POST'])
def getbooks():
    if request.method == 'GET':
        data = Book.getall_books()
        res = jsonify(data)
        
        return res
    
    # curl -X POST -H "Content-Type:application/json" -d '{"book_name":"Hari Senin","publication_year":2024,"pages":415,"publisher_name":"falcon","store_number":1,"quantity":21}' http://localhost:5000/books -i
    if request.method == 'POST':
        try:
            data = request.get_json()
            
            
            req = {
                "store_number": data.get('store_number'),
                "book_name": data.get('book_name'),
                "publication_year": data.get('publication_year'),
                "pages": data.get('pages'),
                "publisher_name": data.get('publisher_name'),
                "quantity":data.get('quantity'),
            }
            
            data = Book.add_book(req)
            res = jsonify(data)

            return res
        
        except Exception as err:
            print(err)

@app.route('/<int:store_number>/books', methods=['GET', 'POST'])
def books(store_number):
    
    if request.method == 'GET':
        try:
            data, msg = Book.get_books(store_number)
            res = jsonify({
                "items": data,
                "length": len(data),
                "message": msg
            })
            if msg == "success":
                return make_response(res, 200)
            elif msg == "Not Found!":
                return make_response(res, 404)
            else:
                return make_response(res, 500)
        except Exception as err:
            return err
    
    if request.method == 'POST':
        try:
            data = request.get_json()
            req = {
                "store_number": store_number,
                "book_name": data.get('book_name'),
                "publication_year": data.get('publication_year'),
                "pages": data.get('pages'),
                "publisher_name": data.get('publisher_name'),
                "quantity":data.get('quantity'),
            }
            msg = Book.add_book(req)
            res = jsonify({"item": req, "message": msg})
            if msg == "success":
                return make_response(res, 200)
            else:
                return make_response(res, 400)
        except Exception as err:
            return err
        
@app.route('/<int:store_number>/<int:book_number>', methods=['GET', 'POST'])
def sbooks(store_number,book_number):
    
    if request.method == 'GET':
        try:
            data, msg = Book.get_book(store_number, book_number)
            res = jsonify({
                "items": data,
                "length": len(data),
                "message": msg
            })
            if msg == "success":
                return make_response(res, 200)
            elif msg == "Not Found!":
                return make_response(res, 404)
            else:
                return make_response(res, 500)
        except Exception as err:
            return err
        
    if request.method == 'PUT':
        try:
            data = request.get_json()
            req = {
                "book_name": data.get('book_name'),
                "publication_year": data.get('publication_year'),
                "pages": data.get('pages'),
                "publisher_name": data.get('publisher_name'),
            }
            msg = Book.edit_book(req)
            res = jsonify({"item": req, "message": msg})
            if msg == "success":
                return make_response(res, 200)
            else:
                return make_response(res, 400)
        except Exception as err:
            return err
    
    # if request.method == 'POST':
    #     try:
    #         data = request.get_json()
    #         req = {
    #             "store_number": data.get('store_number'),
    #             "book_name": data.get('book_name'),
    #             "publication_year": data.get('publication_year'),
    #             "pages": data.get('pages'),
    #             "publisher_name": data.get('publisher_name'),
    #             "quantity": data.get('quantity'),
    #         }
    #         msg = Book.add_book(req)
    #         res = jsonify({"item": req, "message": msg})
    #         if msg == "success":
    #             return make_response(res, 200)
    #         else:
    #             return make_response(res, 400)
    #     except Exception as err:
    #         return err


@app.route('/book/<int:book_number>', methods=['PUT'])
def book(book_number):
    if request.method == 'PUT':
        try:
            data = request.get_json()
            req = {
                "book_name": data.get('book_name'),
                "publication_year": data.get('publication_year'),
                "pages": data.get('pages'),
                "publisher_name": data.get('publisher_name'),
            }
            msg = Book.edit_book(req, book_number)
            res = jsonify({"item": req, "message": msg})
            if msg == "success":
                return make_response(res, 200)
            else:
                return make_response(res, 400)
        except Exception as err:
            return err    
            

@app.route('/publisher', methods=['GET'])
def publisher():
    if request.method == 'GET':
        data = Publisher.get_publishers()
        res = jsonify(data)
        return res


@app.route('/customer', methods=['GET'])
def customer():
    if request.method == 'GET':
        data = Customer.get_customers()
        res = jsonify(data)
        return res


@app.route('/bought', methods=['GET'])
def bought():
    if request.method == 'GET':
        data = Bought.get_boughts()
        res = jsonify(data)
        return res


@app.route('/author', methods=['GET'])
def authors():
    if request.method == 'GET':
        data = Author.get_authors()
        res = jsonify(data)
        return res


@app.route('/staff', methods=['GET'])
def staffs():
    if request.method == 'GET':
        data = Staff.get_staffs()
        res = jsonify(data)
        return res


@app.route('/wrote', methods=['GET'])
def wrote():
    if request.method == 'GET':
        data = Wrote.get_wrotes()
        res = jsonify(data)
        return res


@app.route('/stock', methods=['GET'])
def stock():
    if request.method == 'GET':
        data = Stock.get_stocks()
        res = jsonify(data)
        return res
    

@app.route('/store', methods=['GET'])
def store():
    if request.method == 'GET':
        data = Store.get_stores()
        res = jsonify(data)
        return res


if __name__ == '__main__':
    app.run()