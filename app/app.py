import os
import random
import time
import psycopg2
import psycopg2.extras


from flask.wrappers import Response
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
from contextlib import closing
from psycopg2 import Error

app = Flask(__name__)
app.config['SECRET_KEY'] = 'qwerty'

FAIL_RATE=float(os.environ.get('FAIL_RATE', '0.05'))
SLOW_RATE=float(os.environ.get('SLOW_RATE', '0.00'))

POSTGRES_USER = os.environ.get('POSTGRES_USER')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
POSTGRES_DB = os.environ.get('POSTGRES_DB')

DATABASE_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@db:5432/{POSTGRES_DB}'

def do_staff():
    time.sleep(random.gammavariate(alpha=1.5, beta=.1))

def do_slow():
    time.sleep(random.gammavariate(alpha=30, beta=0.3))
    

@app.route('/')
def index():
    with closing(psycopg2.connect(DATABASE_URL)) as conn:
        with conn.cursor(cursor_factory = psycopg2.extras.DictCursor) as cursor:
            cursor.execute('SELECT * FROM posts')
            posts = cursor.fetchall()
            return render_template('index.html', posts = posts)

def get_post(post_id):
    with closing(psycopg2.connect(DATABASE_URL)) as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.NamedTupleCursor) as cursor:
            cursor.execute('SELECT id,title,content FROM posts WHERE id = %s', (post_id,))
            post = cursor.fetchone()
            print("Selected post: {}".format(post.title))
            if post is None:
                abort(404)
            return post

@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)

 
@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            with closing(psycopg2.connect(DATABASE_URL)) as conn:
                with conn.cursor(cursor_factory=psycopg2.extras.NamedTupleCursor) as cursor:
                    cursor.execute('INSERT INTO posts (title, content) VALUES (%s, %s)',
                                (title, content))
                    conn.commit()
                    return redirect(url_for('index'))
    return render_template('create.html')


@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            with closing(psycopg2.connect(DATABASE_URL)) as conn:
                with conn.cursor(cursor_factory=psycopg2.extras.NamedTupleCursor) as cursor:
                    sql_query = "UPDATE posts SET title = '{}', content = '{}' WHERE id = {}".format(title, content, id)
                    cursor.execute(sql_query)
                    conn.commit()
                    return redirect(url_for('index'))
    return render_template('edit.html', post=post)


@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    post = get_post(id)
    with closing(psycopg2.connect(DATABASE_URL)) as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            sql_query = 'DELETE FROM posts WHERE id = {}'.format(id)
            cursor.execute(sql_query)
            conn.commit()
            flash('Post {} was successfully deleted!'.format(post.title))
            return redirect(url_for('index'))

@app.route('/probe')
def probe():
    if random.random() < FAIL_RATE:
        abort(500)
    if random.random() < SLOW_RATE:
        do_slow()
    else:
        do_staff()
    return "OK"


if __name__ == "__main__":    
    try:
        app.run(host='0.0.0.0', port='5001', debug=True)
    except Exception as e:
        print(str(e))

    