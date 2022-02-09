-- creates a table 'second_table' in db 'hbtn_0c_0 and adds 4 records (rows)
-- <attributes> -> id, name, score; <values/types> -> INT, VARCHAR(256), INT
CREATE TABLE IF NOT EXISTS second_table(id INT, name VARCHAR(256), score INT);
INSERT INTO second_table VALUES (1, 'John', 10);
INSERT INTO second_table VALUES (2, 'Alex', 3);
INSERT INTO second_table VALUES (3, 'Bob', 14);
INSERT INTO second_table VALUES (4, 'George', 8);
