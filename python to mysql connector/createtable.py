import mysql.connector

conn=mysql.connector.connect(host='localhost',user='root',password='Rupesh@123',database='pythondb')
if conn.is_connected():
    print("Connection established successfully.")
mycursor = conn.cursor()
mycursor.execute('create table class(name varchar(20), branch varchar(10), id int)')
mycursor.execute('show tables')

for x in mycursor:
    print(x)
