DROP TABLE IF EXISTS test;

CREATE TABLE test (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  some_text TEXT UNIQUE NOT NULL,
  another_text TEXT NOT NULL,
  a_date DATE
);