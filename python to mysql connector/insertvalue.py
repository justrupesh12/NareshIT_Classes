import mysql.connector

conn=mysql.connector.connect(host='localhost',user='root',password='Rupesh@123',database='pythondb')
if conn.is_connected():
    print("Connection established successfully.")
mycursor = conn.cursor()

sql = "INSERT INTO class(name, branch, id) VALUES (%s, %s, %s)"
#val = ("John Doe", "Computer Science", 56)

val = [("John", "cse", 56),("Mike ", "it", 78),("tyson ", "me", 80)]    

mycursor.executemany(sql, val)
conn.commit()
print(mycursor.rowcount, "record(s) inserted.") 