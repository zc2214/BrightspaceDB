import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
)


# preparing a cursor object
cursorObject = mydb.cursor()

# creating database
createdb='create database if not exists brightspaceDB'
dropdb='drop database if exists brightspaceDB'
cursorObject.execute(createdb)

