import sqlite3
from flask import Flask, render_template
from werkzeug.exceptions import abort

app = Flask(__name__)

@app.route('/')
def hello():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()    
    return render_template('index.html', posts = posts)

def get_db_connection():
    conn = sqlite3.connect('db/database.db')
    conn.row_factory = sqlite3.Row
    return conn