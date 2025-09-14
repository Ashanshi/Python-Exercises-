import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='game_flight',
         user='root',
         password='Rishash@2001',
         autocommit=True
)