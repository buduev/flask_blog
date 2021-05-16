import psycopg2

def create_schema(dbname, username, password, host="127.0.0.1", port=5432):
    con = psycopg2.connect(
      database=dbname, 
      user=username, 
      password=password, 
      host=host, 
      port=port
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

if __name__ == "__main__":    
    try:
        create_schema("blogs", "postgre", "1", "", "")
    except Exception as e:
        print(str(e))

