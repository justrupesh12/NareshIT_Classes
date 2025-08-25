import mysql.connector

conn=mysql.connector.connect(host='localhost',user='root',password='Rupesh@123')
if conn.is_connected():
    print("Connection established successfully.")
print(conn)
print(conn.is_connected())