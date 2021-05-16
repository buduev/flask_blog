import psycopg2

def create_schema(dbname, username, pass):

    con = psycopg2.connect(
      database=dbname, 
      user=username, 
      password=pass, 
      host="127.0.0.1", 
      port="5432"
    )

    cur = con.cursor()

    with open('db/schema.sql') as f:
        cur.execute(f.read())

    cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
                ('First Post', 'Content for the first post'))

    cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
                ('Second Post', 'Content for the second post'))

    con.commit()
    con.close()


