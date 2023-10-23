DROP DATABASE library;

CREATE DATABASE library;
USE library;

CREATE TABLE books (id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT, name VARCHAR(64), author VARCHAR(64), pages INT, publication_date VARCHAR(36));

INSERT INTO books (name, author, pages, publication_date) VALUES ('48 Laws of Power', 'Robert Greene', 300, '2002');
INSERT INTO books (name, author, pages, publication_date) VALUES ('Homo Deus', 'Yuval Noah Harari', 300, '2002');
INSERT INTO books (name, author, pages, publication_date) VALUES ('Sapiens', 'Yuval Noah Harari', 300, '2002');