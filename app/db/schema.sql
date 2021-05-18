CREATE USER postgres superuser;

CREATE DATABASE blogs WITH OWNER postgres;

CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
   created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
   title TEXT NOT NULL,
   content TEXT NOT NULL
);

INSERT INTO posts (title, content) VALUES ('First Post', 'Content for the first post');
INSERT INTO posts (title, content) VALUES ('Second Post', 'Content for the second post');
INSERT INTO posts (title, content) VALUES ('Third Post', 'Content for the third post');