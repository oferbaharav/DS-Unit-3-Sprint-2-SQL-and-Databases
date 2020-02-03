
import os
import sqlite3

# DB_FILEPATH = os.path.join(os.path_dirname(__file__), "..", "data", "chinook.db")

conn = sqlite3.connect('rpg_db.sqlite3')

curs = conn.cursor()

# query = 'SELECT COUNT(*) FROM armory_item;'

# curs.execute(query)

# results = curs.execute(query).fetchall()

# breakpoint()



def format_query_count(message, query):
    result = curs.execute(query).fetchone()[0]
    print(f"{message}: {result}")

def format_query_join(message, label, query):
    result = curs.execute(query).fetchall()
    print(message)
    for row in result:
        (name, count) = row
        print(f"{name} has {count} {label}{'' if count == 1 else 's'}")

# How many total Characters are there?
format_query_count('How many total Characters are there?', 'SELECT count(*) FROM charactercreator_character')

# How many of each specific subclass?
format_query_count('How many total clerics are there?', 'SELECT count(*) from charactercreator_cleric')
format_query_count('How many total fighters are there?', 'SELECT count(*) from charactercreator_fighter')
format_query_count('How many total mages are there?', 'SELECT count(*) from charactercreator_mage')
format_query_count('How many total necromancers are there?', 'SELECT count(*) from charactercreator_necromancer')
format_query_count('How many total thieves are there?', 'SELECT count(*) from charactercreator_thief')

# How many total Items?
format_query_count('How many total items?', 'SELECT count(*) FROM armory_item;')

# How many of the Items are weapons?
format_query_count('How many of the items are weapons?', 'SELECT count(*) from armory_weapon;')

# How many of the Items are not weapons?
format_query_count('How many of the items are not weapons?', 
'SELECT count(*) from armory_item WHERE item_id NOT IN (SELECT item_ptr_id FROM armory_weapon);')

# How many Items does each character have? (Return first 20 rows)
format_query_join('How many Items does each character have?', 'item', """
SELECT
a.name,
count(b.item_id) AS 'count of items'
FROM charactercreator_character a
LEFT JOIN charactercreator_character_inventory b
ON a.character_id = b.character_id
GROUP BY a.character_id
ORDER BY a.character_id
LIMIT 20;""")

# How many Weapons does each character have? (Return first 20 rows)

format_query_join('How many Weapons does each character have?', 'weapon', """
SELECT
a.name,
count(c.item_ptr_id) AS 'count of weapons'
FROM charactercreator_character a
LEFT JOIN charactercreator_character_inventory b
ON a.character_id = b.character_id
LEFT JOIN armory_weapon c
ON b.item_id = c.item_ptr_id
GROUP BY a.character_id
ORDER BY a.character_id
LIMIT 20;""")

# On average, how many Items does each Character have?
query = """
SELECT COUNT(DISTINCT item_id) 
FROM charactercreator_character_inventory
GROUP BY character_id;"""

results = curs.execute(query).fetchall()
total_count_items = 0
total_characters = len(results)
for i in range(total_characters):
    total_count_items += results[i][0]
average = total_count_items / total_characters
print('Average items per character is', average)

# On average, how many Weapons does each character have?
query = """
SELECT COUNT(item_ptr_id) 
FROM charactercreator_character_inventory
LEFT JOIN armory_weapon
ON item_id = item_ptr_id
GROUP BY character_id;"""

results = curs.execute(query).fetchall()
total_count_items = 0
total_characters = len(results)
for i in range(total_characters):
    total_count_items += results[i][0]
average = total_count_items / total_characters
print('Average weapons per character is', average)