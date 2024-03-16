import sqlite3

conn = sqlite3.connect('chinook.db')

cursor = conn.execute("SELECT FirstName, LastName FROM Customers;")
for row in cursor:
    print("Customer Name:", row[0], row[1])
conn.close()
