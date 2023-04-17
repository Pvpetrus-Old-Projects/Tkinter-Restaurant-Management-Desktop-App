# Łączenie z bazą danych
import sqlite3


def SetupDatabase():
    SQLConnection = sqlite3.connect('RestaurantDatabase')
    coursor = SQLConnection.cursor()
    coursor.execute("""DROP TABLE IF EXISTS user""")
    coursor.execute("""DROP TABLE IF EXISTS orderTable""")
    coursor.execute("""DROP TABLE IF EXISTS item""")
    coursor.execute("""CREATE TABLE IF NOT EXISTS user (id integer PRIMARY KEY, username text NOT NULL UNIQUE, password text NOT 
    NULL)""")

    coursor.execute("""CREATE TABLE IF NOT EXISTS orderTable (id integer PRIMARY KEY, userId integer, 
                        orderType text, location text, distance real,
                        customerName text, orderStatus text, estimatedDeliveryTime datetime, 
                        FOREIGN KEY (userId) REFERENCES user (id) ON DELETE CASCADE)""")

    coursor.execute("""CREATE TABLE IF NOT EXISTS item (id integer PRIMARY KEY,orderId integer, name text, 
                        description text, mainPrice real, 
                        secondaryPrice real, count integer, FOREIGN KEY (orderId)
                        REFERENCES orderTable (id) ON DELETE CASCADE)""")

    coursor.execute("""INSERT INTO user(id, username, password) 
                        VALUES (1,'admin','admin')""")

    coursor.execute("""INSERT INTO orderTable(id, userId, orderType, location, distance, customerName, orderStatus, estimatedDeliveryTime) 
                        VALUES (1, 1, 'takeout', '', 0, 'Martin', 'incoming', NULL)""")

    coursor.execute("""INSERT INTO item(id, orderId, name, description, mainPrice, secondaryPrice, count) 
                        VALUES (1,1,'Hot-dog','Additional ketchup + additional cheese', 10.5, 2.5, 1)""")
    # """Update SqliteDb_developers set salary = 10000 where id = 4"""
    # """DELETE from SqliteDb_developers where id = 4"""

    SQLConnection.commit()
    SQLConnection.close()
