import mysql.connector

conn=mysql.connector.connect(host='localhost',user='root',password='Rupesh@123')
mycursor = conn.cursor()
mycursor.execute('Show databases')
for i in mycursor:
    print(i)