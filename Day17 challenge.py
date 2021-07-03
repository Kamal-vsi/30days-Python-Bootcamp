# Python MYSQL
# Create a connection for DB and print the version using a python program
import mysql.connector
db=mysql.connector.connect(host='localhost', user="root", password="Sairam@123")
print(db)

import sys
cur = db.cursor()
cur.execute("SELECT VERSION()")
data = cur.fetchone()
print("DBMS version :", str(data))

# Create a multiple tables & insert data in table
dbmt = db.cursor()
dbmt.execute("CREATE DATABASE mydatabase12345")
dbmt.execute("SHOW DATABASES")
for entry in dbmt:
    print(entry)
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sairam@123",
    database="mydatabase12345"
)
dbmt = mydb.cursor()
dbmt.execute("CREATE TABLE customers (Employee_name VARCHAR(255), Employee_dep VARCHAR(255), Employee_id VARCHAR(255))")
dbmt.execute("CREATE TABLE Office(emp_name VARCHAR(255), Employee_id VARCHAR(255), EMP_ADDRESS VARCHAR(255))")
dbmt.execute("CREATE TABLE Student(rollno INT(24), STUD_NAME VARCHAR(255), MARK INT(3))")
dbmt=mydb.cursor()
dbmt.execute("SHOW TABLES")
for value in dbmt:
    print(value)

#Create a employee table and read all the employee name in the table using for loop

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sairam@123",
    database="mydatabase12345"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE Employee1(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
sql = "INSERT INTO Employee1(id, name, address) VALUES (%s, %s, %s)"
val = ("123", "kamal", "Vandavasi 408")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "Record inserted.")
mycursor=mydb.cursor()
sql = "INSERT INTO Employee1(id, name, address) VALUES (%s, %s, %s)"
val = ("124", "kannan", "Vandavasi 508")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "Record inserted.")
sql = "INSERT INTO Employee1(id, name, address) VALUES (%s, %s, %s)"
val = ("125", "sriram", "Vandavasi 608")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "Record inserted.")
mycursor = mydb.cursor()
sql = "INSERT INTO Employee1(id, name, address) VALUES (%s, %s, %s)"
val = [
    ('1', 'bharathi', 'sanathi street 04'), ('2', 'saroja', 'balu street 05'), ('3', 'pattu', 'anna street 98'), ('4', 'sangavi', 'silicon valley 87'), ('5', 'devi', 'cheety street 56')
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "Was inserted.")
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM Employee1")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
mycursor = mydb.cursor()
mycursor.execute("SELECT name FROM Employee1")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)