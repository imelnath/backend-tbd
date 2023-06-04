import psycopg2
from flask import Flask, request
from config import CREDENTIALS

app = Flask(__name__)

@app.route('/books', methods=['GET'])
def get_data():
    if request.method == 'GET':
        
        
        try:
            db = psycopg2.connect(host=CREDENTIALS.HOSTNAME,
                                port=CREDENTIALS.PORT,
                                database=CREDENTIALS.DATABASE,
                                user=CREDENTIALS.USER,
                                password=CREDENTIALS.PASSWORD
                                )
            c = db.cursor()
            c.execute('SELECT * FROM book')
            
            res = c.fetchall()
            
            c.close()
            db.close()
            return str(res)
        
        except (psycopg2.Error, psycopg2.DatabaseError) as err:
            return f'Error while connecting to PostgreSQL Database: {err}'



if __name__ == '__main__':
    app.run()