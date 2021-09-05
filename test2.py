import mysql.connector

db = mysql.connector.connect(
    username="Artem",
    password="Artem-Artem-0880",
    host="localhost",
    database="test"
)

db.close()