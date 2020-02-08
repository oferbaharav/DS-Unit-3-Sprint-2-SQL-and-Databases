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
