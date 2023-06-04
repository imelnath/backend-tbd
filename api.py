import psycopg2
from flask import Flask, request
from config import CREDENTIALS

app = Flask(__name__)

@app.route('/books', methods=['GET'])
def get_books():
    if request.method == 'GET':
        try:
            db = psycopg2.connect(host=CREDENTIALS['HOSTNAME'],
                                port=CREDENTIALS['PORT'],
                                database=CREDENTIALS['DATABASE'],
                                user=CREDENTIALS['USER'],
                                password=CREDENTIALS['PASSWORD']
                                )
            c = db.cursor()
            c.execute('SELECT * FROM book')
            
            res = c.fetchall()
            
            c.close()
            db.close()
            return str(res)
        
        except (psycopg2.Error, psycopg2.DatabaseError) as err:
            return f'Error while connecting to PostgreSQL Database: {err}'

@app.route('/books/<int:id>', methods=['GET'])
# request API curl -X GET http://localhost:5000/books/7 -i
def get_book(id):
    if request.method == 'GET':
        try:
            db = psycopg2.connect(host=CREDENTIALS['HOSTNAME'],
                                port=CREDENTIALS['PORT'],
                                database=CREDENTIALS['DATABASE'],
                                user=CREDENTIALS['USER'],
                                password=CREDENTIALS['PASSWORD']
                                )
            c = db.cursor()
            c.execute(f'SELECT * FROM book WHERE book_number={id}')
            
            res = c.fetchone()
            
            c.close()
            db.close()
            return str(res)
        
        except (psycopg2.Error, psycopg2.DatabaseError) as err:
            return f'Error while connecting to PostgreSQL Database: {err}'

@app.route('/authors', methods=['GET'])
def get_authors():
    if request.method == 'GET':
        try:
            db = psycopg2.connect(host=CREDENTIALS['HOSTNAME'],
                                port=CREDENTIALS['PORT'],
                                database=CREDENTIALS['DATABASE'],
                                user=CREDENTIALS['USER'],
                                password=CREDENTIALS['PASSWORD']
                                )
            c = db.cursor()
            c.execute('SELECT * FROM author')
            
            res = c.fetchall()
            
            c.close()
            db.close()
            return str(res)
        
        except (psycopg2.Error, psycopg2.DatabaseError) as err:
            return f'Error while connecting to PostgreSQL Database: {err}'

@app.route('/employees', methods=['GET'])
def get_employees():
    if request.method == 'GET':
        try:
            db = psycopg2.connect(host=CREDENTIALS['HOSTNAME'],
                                port=CREDENTIALS['PORT'],
                                database=CREDENTIALS['DATABASE'],
                                user=CREDENTIALS['USER'],
                                password=CREDENTIALS['PASSWORD']
                                )
            c = db.cursor()
            c.execute('SELECT * FROM staff')
            
            res = c.fetchall()
            
            c.close()
            db.close()
            return str(res)
        
        except (psycopg2.Error, psycopg2.DatabaseError) as err:
            return f'Error while connecting to PostgreSQL Database: {err}'

if __name__ == '__main__':
    app.run()