import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="Artem",
    passwd="Artem-Artem-0880",
    database="testdatabase"
    )

mycursor = db.cursor()

db.execute("CREATE DATABASE testdatabase")



