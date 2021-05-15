import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
import logging
import os

app = Flask(__name__)

@app.route('/')
def hello():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()    
    logging.debug("Текущая деректория:", os.getcwd())
    return render_template('index.html', posts = posts)

def get_db_connection():
    conn = sqlite3.connect('app/db/database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1')