DO
$do$
BEGIN
   IF EXISTS (SELECT FROM pg_database WHERE datname = 'blog') THEN
      RAISE NOTICE 'Database blog already exists';  -- optional
   ELSE
        CREATE DATABASE blog;
   END IF;
END
$do$;


\c blog;

CREATE TABLE posts(

id int GENERATED BY DEFAULT AS IDENTITY, 
created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, 
title TEXT NOT NULL, 
content TEXT NOT NULL, 
updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP);

INSERT INTO posts (title, content) VALUES ('First Post', 'Content for the first post');
INSERT INTO posts (title, content) VALUES ('Second Post', 'Content for the second post');
INSERT INTO posts (title, content) VALUES ('Third Post', 'Content for the third post');



