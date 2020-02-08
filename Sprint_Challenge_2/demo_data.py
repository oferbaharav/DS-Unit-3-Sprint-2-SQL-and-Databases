import sqlite3

conn = sqlite3.connect('demo_data.sqlite3')

c = conn.cursor()
create_table_sql = """
CREATE TABLE demo (
    s text,
    x integer,
    y integer
);
"""
c.execute("DROP TABLE demo")
c.execute(create_table_sql)

c.execute("INSERT INTO demo (s, x, y) VALUES ('g', 3, 9)")
c.execute("INSERT INTO demo (s, x, y) VALUES ('f', 8, 7)")
c.execute("INSERT INTO demo (s, x, y) VALUES ('v', 5, 7)")

conn.commit()

# Count how many rows you have - it should be 3!
print("Count how many rows you have - it should be 3!",\
c.execute("SELECT count (*) FROM demo").fetchone()[0])
# How many rows are there where both `x` and `y` are at least 5?
print("How many rows are there where both x and y are at least 5?",\
c.execute("SELECT count (*) FROM demo WHERE x>=5 AND y>=5").fetchone()[0])
# How many unique values of `y` are there
print("How many unique values of `y` are there",\
c.execute("SELECT count (distinct y) FROM demo").fetchone()[0])