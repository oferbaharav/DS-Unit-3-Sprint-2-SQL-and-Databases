import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')

c = conn.cursor()

# - What are the ten most expensive items (per unit price) in the database?
top_10_products ="""
SELECT ProductName, UnitPrice
FROM Product
ORDER BY UnitPrice DESC
LIMIT 10;"""
print("top 10 most expensive items\n", c.execute(top_10_products).fetchall())


# - What is the average age of an employee at the time of their hiring? 
ave_age ="""
SELECT AVG(HireDate-BirthDate) AS Ave_Age
FROM Employee;"""
print("average age of employee at time of hiring\n", c.execute(ave_age).fetchone()[0])


# - (*Stretch*) How does the average age of employee at hire vary by city?

ave_age_by_city="""
SELECT AVG(HireDate-BirthDate) AS Ave_Age, City
FROM Employee
GROUP BY City;"""
print("average employee age per city\n",c.execute(ave_age_by_city).fetchall())


#Part 3

# - What are the ten most expensive items (per unit price) in the database *and*
#   their suppliers?
top_10_p_supplier ="""
SELECT ProductName, UnitPrice, CompanyName
FROM Product
LEFT JOIN Supplier
ON Product.SupplierId = Supplier.ID
ORDER BY UnitPrice DESC
LIMIT 10;"""
print("top 10 most expensive items and supplier\n", c.execute(top_10_p_supplier).fetchall())

# - What is the largest category (by number of unique products in it)?

top_category ="""
SELECT CategoryName, count (distinct Product.Id) AS count_products
FROM Category
LEFT JOIN Product
ON Product.CategoryId = Category.Id
ORDER BY count_products DESC
LIMIT 1;"""
print("top category\n", c.execute(top_category).fetchall())

# - (*Stretch*) Who's the employee with the most territories? Use `TerritoryId`
#   (not name, region, or other fields) as the unique identifier for territories.
top_employee_distinct_territories="""
SELECT EmployeeId, LastName, FirstName, count(DISTINCT TerritoryId) AS count_territories
FROM Employee
LEFT JOIN EmployeeTerritory
ON Employee.id = EmployeeTerritory.EmployeeId
ORDER BY count_territories DESC
LIMIT 1;"""
print("employee with the most territories\n", c.execute(top_employee_distinct_territories).fetchone())


#terminal output:
"""
(lambdata) bash-3.2$ python northwind.py
top 10 most expensive items
 [('Côte de Blaye', 263.5), ('Thüringer Rostbratwurst', 123.79), ('Mishi Kobe Niku', 97), ("Sir Rodney's Marmalade", 81), ('Carnarvon Tigers', 62.5), ('Raclette Courdavault', 55), ('Manjimup Dried Apples', 53), ('Tarte au sucre', 49.3), ('Ipoh Coffee', 46), ('Rössle Sauerkraut', 45.6)]
average age of employee at time of hiring
 37.22222222222222
average employee age per city
 [(29.0, 'Kirkland'), (32.5, 'London'), (56.0, 'Redmond'), (40.0, 'Seattle'), (40.0, 'Tacoma')]
top 10 most expensive items and supplier
 [('Côte de Blaye', 263.5, 'Aux joyeux ecclésiastiques'), ('Thüringer Rostbratwurst', 123.79, 'Plutzer Lebensmittelgroßmärkte AG'), ('Mishi Kobe Niku', 97, 'Tokyo Traders'), ("Sir Rodney's Marmalade", 81, 'Specialty Biscuits, Ltd.'), ('Carnarvon Tigers', 62.5, 'Pavlova, Ltd.'), ('Raclette Courdavault', 55, 'Gai pâturage'), ('Manjimup Dried Apples', 53, "G'day, Mate"), ('Tarte au sucre', 49.3, "Forêts d'érables"), ('Ipoh Coffee', 46, 'Leka Trading'), ('Rössle Sauerkraut', 45.6, 'Plutzer Lebensmittelgroßmärkte AG')]
top category
 [('Beverages', 77)]
employee with the most territories
 (1, 'Davolio', 'Nancy', 49)
(lambdata) bash-3.2$ 
"""