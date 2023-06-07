from flask import Flask, json, jsonify, make_response, request
from flask_cors import CORS
from lib.book import Book
from lib.store import Store

app = Flask(__name__)
CORS(app)

# @app.route('/books', methods=['GET','POST'])
# def getbooks():
#     if request.method == 'GET':
#         data = Book.getall_books()
#         res = jsonify(data)
        
#         return res
    
#     # curl -X POST -H "Content-Type:application/json" -d '{"book_name":"Hari Senin","publication_year":2024,"pages":415,"publisher_name":"falcon","store_number":1,"quantity":21}' http://localhost:5000/books -i
#     if request.method == 'POST':
#         try:
#             data = request.get_json()
            
            
#             req = {
#                 "store_number": data.get('store_number'),
#                 "book_name": data.get('book_name'),
#                 "publication_year": data.get('publication_year'),
#                 "pages": data.get('pages'),
#                 "publisher_name": data.get('publisher_name'),
#                 "quantity":data.get('quantity'),
#             }
            
#             data = Book.add_book(req)
#             res = jsonify(data)

#             return res
        
#         except Exception as err:
#             print(err)

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
        
# @app.route('/<int:store_number>/<int:book_number>', methods=['GET', 'POST'])
# def sbooks(store_number,book_number):
    
#     if request.method == 'GET':
#         try:
#             data, msg = Book.get_book(store_number, book_number)
#             res = jsonify({
#                 "items": data,
#                 "length": len(data),
#                 "message": msg
#             })
#             if msg == "success":
#                 return make_response(res, 200)
#             elif msg == "Not Found!":
#                 return make_response(res, 404)
#             else:
#                 return make_response(res, 500)
#         except Exception as err:
#             return err
        
#     if request.method == 'PUT':
#         try:
#             data = request.get_json()
#             req = {
#                 "book_name": data.get('book_name'),
#                 "publication_year": data.get('publication_year'),
#                 "pages": data.get('pages'),
#                 "publisher_name": data.get('publisher_name'),
#             }
#             msg = Book.edit_book(req)
#             res = jsonify({"item": req, "message": msg})
#             if msg == "success":
#                 return make_response(res, 200)
#             else:
#                 return make_response(res, 400)
#         except Exception as err:
#             return err
    
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


@app.route('/book/<int:book_number>', methods=['GET', 'PUT', 'DELETE'])
def book(book_number):

    if request.method == 'GET':
        try:
            data, msg = Book.get_book(book_number)
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
            msg = Book.edit_book(req, book_number)
            res = jsonify({"item": req, "message": msg})
            if msg == "success":
                return make_response(res, 200)
            else:
                return make_response(res, 400)
        except Exception as err:
            return err    
        
    if request.method == 'DELETE':
        try:
            msg = Book.delete_book(book_number)
            res = jsonify({"message":msg})
            if msg == "success":
                return make_response(res, 200)
            elif msg == "Not Found!":
                return make_response(res, 404)
            else:
                return make_response(res, 400)
        except Exception as err:
            return err
            
@app.route('/store', methods=['GET'])
def store():
    if request.method == 'GET':
        data = Store.get_stores()
        res = jsonify(data)
        return res


if __name__ == '__main__':
    app.run()