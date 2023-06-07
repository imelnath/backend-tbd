import psycopg2

from config import CREDENTIALS


class Book:
        
    def get_books(store_number):
        try:
            db = psycopg2.connect(host=CREDENTIALS['HOSTNAME'],
                                port=CREDENTIALS['PORT'],
                                database=CREDENTIALS['DATABASE'],
                                user=CREDENTIALS['USER'],
                                password=CREDENTIALS['PASSWORD']
                                )
            c = db.cursor()
            c.execute(f"""
                        SELECT b.book_number, b.book_name, b.publication_year, b.pages, b.publisher_name
                        FROM book b
                            JOIN stock st ON b.book_number=st.book_number
                            JOIN store s ON st.store_number=s.store_number
                        WHERE s.store_number={store_number} ORDER BY b.book_name ASC
                    """)
            data = c.fetchall()
            msg = "success"
            
            items = []
            for col in data:
                book = {
                    "book_number": col[0],
                    "book_name": col[1],
                    "publication_year": col[2],
                    "pages": col[3],
                    "publisher_name": col[4],
                }
                items.append(book)
            
            if len(items) == 0:
                msg = "This store has no books"
            
            c.close()
            db.close()
            return items, msg
        
        except (psycopg2.Error, psycopg2.DatabaseError) as err:
            c.close()
            db.close()
            return [], f'Error while connecting to PostgitemsQL Database: {err}'
        
    
    def add_book(req):
        
        store_number = int(req['store_number'])
        book_name = str(req['book_name'])
        publication_year = int(req['publication_year'])
        pages = int(req['pages'])
        publisher_name = str(req['publisher_name'])
        quantity = int(req['quantity'])
        
        try:
            db = psycopg2.connect(host=CREDENTIALS['HOSTNAME'],
                                    port=CREDENTIALS['PORT'],
                                    database=CREDENTIALS['DATABASE'],
                                    user=CREDENTIALS['USER'],
                                    password=CREDENTIALS['PASSWORD']
                                    )
            c = db.cursor()
            c.execute(f"""SELECT book_number, book_name FROM book""")
            books = c.fetchall()
            msg = "success"
            
            _book_numbers = []
            _book_names = []
            for book in books:
                _book_numbers.append(book[0])
                _book_names.append(book[1])
            
            if not (book_name in _book_names):
                book_number = max(_book_numbers)+1
                c.execute(f"""
                      BEGIN;
                      INSERT INTO book (book_number, book_name, publication_year, pages, publisher_name)
                      VALUES({book_number}, '{book_name}', {publication_year}, {pages}, '{publisher_name}');
                      INSERT INTO stock (store_number, book_number, quantity)
                          VALUES({store_number}, {book_number}, {quantity});
                      COMMIT;
                      ROLLBACK;
                      """)
            else:
                msg = "Book already exists"
            
            c.close()
            db.commit()
            db.close()
            return msg
        
        except (psycopg2.Error, psycopg2.DatabaseError) as err:
            c.close()
            db.close()
            return f'Error while connecting to PostgitemsQL Database: {err}'
    
    
    def delete_book(book_number):
        try:
            db = psycopg2.connect(host=CREDENTIALS['HOSTNAME'],
                                    port=CREDENTIALS['PORT'],
                                    database=CREDENTIALS['DATABASE'],
                                    user=CREDENTIALS['USER'],
                                    password=CREDENTIALS['PASSWORD']
                                    )
            c = db.cursor()
            c.execute(f"""
                      BEGIN;
                      DELETE FROM stock WHERE book_number={book_number};
                      DELETE FROM book WHERE book_number={book_number};
                      COMMIT;
                      ROLLBACK;
                      """)
            msg = "success"
            
            c.close()
            db.commit()
            db.close()
            return msg
            
        except (psycopg2.Error, psycopg2.DatabaseError) as err:
            c.close()
            db.close()
            return f'Error while connecting to PostgitemsQL Database: {err}'
    
    
    def edit_book(req, book_number):
        
        book_name = str(req['book_name'])
        publication_year = int(req['publication_year'])
        pages = int(req['pages'])
        publisher_name = str(req['publisher_name'])
        
        try:
            db = psycopg2.connect(host=CREDENTIALS['HOSTNAME'],
                                    port=CREDENTIALS['PORT'],
                                    database=CREDENTIALS['DATABASE'],
                                    user=CREDENTIALS['USER'],
                                    password=CREDENTIALS['PASSWORD']
                                    )
            c = db.cursor()
            c.execute(f"""
                      UPDATE book
                      SET book_name='{book_name}', publication_year={publication_year}, pages={pages}, publisher_name='{publisher_name}'
                      WHERE book_number={book_number}
                      """)
            msg = "success"
            
            c.close()
            db.commit()
            db.close()
            return msg
        
        except (psycopg2.Error, psycopg2.DatabaseError) as err:
            c.close()
            db.close()
            return f'Error while connecting to PostgitemsQL Database: {err}'