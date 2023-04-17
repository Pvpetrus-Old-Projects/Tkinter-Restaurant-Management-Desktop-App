# Łączenie z bazą danych
import sqlite3
from sqlite3 import Connection


def SetupDatabase() -> None:
    SQLConnection: Connection = sqlite3.connect('RestaurantDatabase')
    coursor = SQLConnection.cursor()
    coursor.execute("""DROP TABLE IF EXISTS user""")
    coursor.execute("""DROP TABLE IF EXISTS orderTable""")
    coursor.execute("""DROP TABLE IF EXISTS item""")
    coursor.execute("""CREATE TABLE IF NOT EXISTS user (id integer PRIMARY KEY, username text NOT NULL UNIQUE, password text NOT 
    NULL)""")

    coursor.execute("""CREATE TABLE IF NOT EXISTS orderTable (id integer PRIMARY KEY, userId integer, 
                        orderType text, location text, distance real,
                        customerName text, orderStatus text, createAt datetime, acceptAt datetime, 
                        finishAt datetime, estimate datetime, 
                        FOREIGN KEY (userId) REFERENCES user (id) ON DELETE CASCADE)""")

    coursor.execute("""CREATE TABLE IF NOT EXISTS item (id integer PRIMARY KEY,orderId integer, name text, 
                        description text, mainPrice real, 
                        secondaryPrice real, count integer, FOREIGN KEY (orderId)
                        REFERENCES orderTable (id) ON DELETE CASCADE)""")

    coursor.execute("""INSERT INTO user(id, username, password) 
                        VALUES (1,'admin','admin')""")

    coursor.execute("""INSERT INTO orderTable(id, userId, orderType, location, distance, customerName, orderStatus, 
                        createAt, acceptAt, finishAt, estimate) 
                        VALUES (1, 1, 'takeout', '', 0, 'Martin', 'incoming', '2012-06-18T10:34:09', NULL, NULL, NULL)""")

    coursor.execute("""INSERT INTO item(id, orderId, name, description, mainPrice, secondaryPrice, count) 
                        VALUES (1,1,'Hot-dog','Additional ketchup + additional cheese', 10.5, 2.5, 1)""")

    coursor.execute("""INSERT INTO item(id, orderId, name, description, mainPrice, secondaryPrice, count) 
                            VALUES (2,1,'Hamburger','Additional mayo', 15.5, 1.0, 2)""")
    # """Update SqliteDb_developers set salary = 10000 where id = 4"""
    # """DELETE from SqliteDb_developers where id = 4"""

    SQLConnection.commit()
    SQLConnection.close()


def returnAllUsers(orderId: int) -> list:
    SQLConnection: Connection = sqlite3.connect('RestaurantDatabase')
    coursor = SQLConnection.cursor()

    SQLConnection.commit()
    SQLConnection.close()


def returnAllOrdersForUser(userId: int) -> list:
    SQLConnection: Connection = sqlite3.connect('RestaurantDatabase')
    coursor = SQLConnection.cursor()

    SQLConnection.commit()
    SQLConnection.close()


def returnAllItemsForOrder(orderId: int) -> list:
    SQLConnection: Connection = sqlite3.connect('RestaurantDatabase')
    coursor = SQLConnection.cursor()

    SQLConnection.commit()
    SQLConnection.close()


def changeOrderStatus(orderId: int) -> None:
    SQLConnection: Connection = sqlite3.connect('RestaurantDatabase')
    coursor = SQLConnection.cursor()

    SQLConnection.commit()
    SQLConnection.close()


def setOrderDeliveryTime(orderId: int) -> None:
    SQLConnection: Connection = sqlite3.connect('RestaurantDatabase')
    coursor = SQLConnection.cursor()

    SQLConnection.commit()
    SQLConnection.close()


def returnAllUsers() -> list:
    SQLConnection: Connection = sqlite3.connect('RestaurantDatabase')
    coursor = SQLConnection.cursor()
    coursor.execute("""SELECT * FROM user""")
    usersList: list = coursor.fetchall()

    SQLConnection.commit()
    SQLConnection.close()
    return usersList


def returnAllOrders() -> list:
    SQLConnection: Connection = sqlite3.connect('RestaurantDatabase')
    coursor = SQLConnection.cursor()
    coursor.execute("""SELECT * FROM orderTable""")
    usersList: list = coursor.fetchall()

    SQLConnection.commit()
    SQLConnection.close()
    return usersList


def returnAllItems() -> list:
    SQLConnection: Connection = sqlite3.connect('RestaurantDatabase')
    coursor = SQLConnection.cursor()
    coursor.execute("""SELECT * FROM item""")
    usersList: list = coursor.fetchall()

    SQLConnection.commit()
    SQLConnection.close()
    return usersList
