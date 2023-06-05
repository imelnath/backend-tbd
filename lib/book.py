import psycopg2

from config import CREDENTIALS


class Book:
    
    
    def get_books():
        try:
            db = psycopg2.connect(host=CREDENTIALS['HOSTNAME'],
                                port=CREDENTIALS['PORT'],
                                database=CREDENTIALS['DATABASE'],
                                user=CREDENTIALS['USER'],
                                password=CREDENTIALS['PASSWORD']
                                )
            c = db.cursor()
            c.execute('SELECT * FROM book')
            data = c.fetchall()
            
            res = []
            for index in data:
                book = {
                    "store": index[0],
                    "book_number": index[1],
                    "book_name": index[2],
                    "publication_year": index[3],
                    "pages": index[4],
                    "pname": index[5],
                    "quantity": index[6],
                    "price": index[7],
                }
                res.append(book)
            
            c.close()
            db.close()
            
            return res
        
        except (psycopg2.Error, psycopg2.DatabaseError) as err:
            c.close()
            db.close()
            return f'Error while connecting to PostgreSQL Database: {err}'
        
        
    def get_book(id):
        try:
            db = psycopg2.connect(host=CREDENTIALS['HOSTNAME'],
                                    port=CREDENTIALS['PORT'],
                                    database=CREDENTIALS['DATABASE'],
                                    user=CREDENTIALS['USER'],
                                    password=CREDENTIALS['PASSWORD']
                                    )
            c = db.cursor()
            c.execute(f"""SELECT * FROM book
                      WHERE book_number={id}""")
            data = c.fetchone()
            
            c.close()
            db.close()
            
            return str(data)
        
        except (psycopg2.Error, psycopg2.DatabaseError) as err:
            c.close()
            db.close()
            return f'Error while connecting to PostgreSQL Database: {err}'
    
    
    def add_book(req):
        
        store = req['store']
        book_number = req['book_number']
        book_name = req['book_name']
        publication_year = req['publication_year']
        pages = req['pages']
        pname = req['pname']
        quantity = req['quantity']
        price = req['price']
        
        try:
            db = psycopg2.connect(host=CREDENTIALS['HOSTNAME'],
                                    port=CREDENTIALS['PORT'],
                                    database=CREDENTIALS['DATABASE'],
                                    user=CREDENTIALS['USER'],
                                    password=CREDENTIALS['PASSWORD']
                                    )
            c = db.cursor()
            c.execute(f"""INSERT INTO book (store, book_number, book_name, publication_year, pages, pname, quantity, price)
                      VALUES({store}, {book_number}, {book_name}, {publication_year}, {pages}, {pname}, {quantity}, {price})""")
            
            c.close()
            db.commit()
            db.close()
            
            return 'success'
        
        except (psycopg2.Error, psycopg2.DatabaseError) as err:
            c.close()
            db.close()
            return f'Error while connecting to PostgreSQL Database: {err}'