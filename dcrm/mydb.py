import mysql.connector

# create db connection
db = mysql.connector.connect(host="localhost", user="root", passwd="nx!PJV50514622")

# prepare a cursor object
cursor = db.cursor()

# create a db
cursor.execute("CREATE DATABASE elderco")

print("database created")