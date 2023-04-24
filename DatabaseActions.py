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


def returnAllOrdersForUser(userId: int) -> list:
    SQLConnection: Connection = sqlite3.connect('RestaurantDatabase')
    coursor = SQLConnection.cursor()
    coursor.execute(f"SELECT * FROM orderTable where userId={userId}")
    ordersList: list = coursor.fetchall()
    SQLConnection.close()
    return ordersList


def returnAllItemsForOrder(orderId: int) -> list:
    SQLConnection: Connection = sqlite3.connect('RestaurantDatabase')
    coursor = SQLConnection.cursor()

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

    SQLConnection.close()
    return usersList


def returnAllOrders() -> list:
    SQLConnection: Connection = sqlite3.connect('RestaurantDatabase')
    coursor = SQLConnection.cursor()
    coursor.execute("""SELECT * FROM orderTable""")
    usersList: list = coursor.fetchall()

    SQLConnection.close()
    return usersList


def returnAllItems() -> list:
    SQLConnection: Connection = sqlite3.connect('RestaurantDatabase')
    coursor = SQLConnection.cursor()
    coursor.execute("""SELECT * FROM item""")
    usersList: list = coursor.fetchall()

    SQLConnection.close()
    return usersList


def returnCertainUser(user_id) -> tuple:
    SQLConnection: Connection = sqlite3.connect('RestaurantDatabase')
    coursor = SQLConnection.cursor()
    coursor.execute(f"SELECT * FROM item where id={user_id}")
    user: tuple = coursor.fetchall()[0]
    SQLConnection.close()
    return user


def returnCertainOrder(order_id) -> tuple:
    SQLConnection: Connection = sqlite3.connect('RestaurantDatabase')
    coursor = SQLConnection.cursor()
    coursor.execute(f"SELECT * FROM orderTable where id={order_id}")
    order: tuple = coursor.fetchall()[0]
    SQLConnection.close()
    return order


def returnCertainItem(item_id) -> tuple:
    SQLConnection: Connection = sqlite3.connect('RestaurantDatabase')
    coursor = SQLConnection.cursor()
    coursor.execute(f"SELECT * FROM item where id={item_id}")
    item: tuple = coursor.fetchall()[0]
    SQLConnection.close()
    return item


def loginToDatabase(username: str, password: str) -> bool:
    SQLConnection: Connection = sqlite3.connect('RestaurantDatabase')
    coursor = SQLConnection.cursor()
    coursor.execute('SELECT * FROM user where username=? and password=?', (username, password,))
    if len(coursor.fetchall()) != 0:
        SQLConnection.close()
        print("be")
        return True
    else:
        SQLConnection.close()
        return False


def returnCertainUserByUsernameAndPassword(username: str, password: str) -> tuple:
    SQLConnection: Connection = sqlite3.connect('RestaurantDatabase')
    coursor = SQLConnection.cursor()
    coursor.execute('SELECT * FROM user where username=? and password=?', (username, password,))
    user = coursor.fetchall()[0]
    return user


def returnAmountOfIncoming(user_id) -> int:
    SQLConnection: Connection = sqlite3.connect('RestaurantDatabase')
    coursor = SQLConnection.cursor()
    coursor.execute('SELECT * FROM orderTable where userId=? and orderStatus=?', (user_id, "incoming",))
    amountOfOrders: int = len(coursor.fetchall())
    SQLConnection.close()
    return amountOfOrders


def returnAmountOfAccepted(user_id) -> int:
    SQLConnection: Connection = sqlite3.connect('RestaurantDatabase')
    coursor = SQLConnection.cursor()
    coursor.execute('SELECT * FROM orderTable where userId=? and orderStatus=?', (user_id, "accepted",))
    amountOfOrders: int = len(coursor.fetchall())
    SQLConnection.close()
    return amountOfOrders


def returnAmountOfReady(user_id) -> int:
    SQLConnection: Connection = sqlite3.connect('RestaurantDatabase')
    coursor = SQLConnection.cursor()
    coursor.execute('SELECT * FROM orderTable where userId=? and orderStatus=?', (user_id, "ready",))
    amountOfOrders: int = len(coursor.fetchall())
    SQLConnection.close()
    return amountOfOrders


def returnTotalRevenueForUser(user_id) -> float:
    SQLConnection: Connection = sqlite3.connect('RestaurantDatabase')
    coursor = SQLConnection.cursor()
    coursor.execute('SELECT * FROM orderTable where userId=? and orderStatus=?', (user_id, "ready",))
    readyOrders: list = coursor.fetchall()
    sum: float = 0
    for order in readyOrders:
        coursor.execute('SELECT * FROM item where orderId=?', (user_id,))
        orderItems: list = coursor.fetchall()
        for item in orderItems:
            sum += (item[4] + item[5])*item[6]
    SQLConnection.close()
    return sum


def returnAcceptedOrderRatioForUser(user_id) -> float:
    SQLConnection: Connection = sqlite3.connect('RestaurantDatabase')
    coursor = SQLConnection.cursor()
    coursor.execute('SELECT * FROM orderTable where userId=?', (user_id,))
    orders: list = coursor.fetchall()
    sumOfAcceptedOrders: float = 0
    for order in orders:
        if order[6] == "accepted":
            sumOfAcceptedOrders += 1
    SQLConnection.close()
    return sumOfAcceptedOrders / len(orders) * 100
