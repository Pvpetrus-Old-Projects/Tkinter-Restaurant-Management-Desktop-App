# Łączenie z bazą danych
import sqlite3
from datetime import datetime, timedelta
from sqlite3 import Connection


def SetupDatabase() -> None:
    SQLConnection: Connection = sqlite3.connect('RestaurantDatabase')
    coursor = SQLConnection.cursor()
    # Deleting tables
    coursor.execute("""DROP TABLE IF EXISTS user""")
    coursor.execute("""DROP TABLE IF EXISTS orderTable""")
    coursor.execute("""DROP TABLE IF EXISTS item""")
    # Creating tables
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
    # Filling the database with data
    # Creating users
    coursor.execute("""INSERT INTO user(id, username, password) 
                        VALUES (1,'admin','admin')""")
    # Creating orders
    coursor.execute("""INSERT INTO orderTable(id, userId, orderType, location, distance, customerName, orderStatus, 
                        createAt, acceptAt, finishAt, estimate) 
                        VALUES (1, 1, 'takeout', '', 0, 'Martin', 'incoming', '2012-06-18T10:34:09', NULL, NULL, NULL)""")
    coursor.execute("""INSERT INTO orderTable(id, userId, orderType, location, distance, customerName, orderStatus, 
                            createAt, acceptAt, finishAt, estimate) 
                            VALUES (2, 1, 'takeout', '', 0, 'Martin', 'accepted', '2012-06-18T11:34:09', 
                            '2012-06-18T11:37:09', NULL, NULL)""")
    coursor.execute("""INSERT INTO orderTable(id, userId, orderType, location, distance, customerName, orderStatus, 
                            createAt, acceptAt, finishAt, estimate) 
                            VALUES (3, 1, 'takeout', '', 5, 'Martin', 'ready', '2023-04-24T12:34:09', 
                            '2023-04-24T12:34:09', '2023-04-24T12:36:09', '2023-04-24T12:39:09')""")
    # Creating items
    coursor.execute("""INSERT INTO item(id, orderId, name, description, mainPrice, secondaryPrice, count) 
                        VALUES (1,1,'Hot-dog','Additional ketchup + additional cheese', 10.5, 2.5, 1)""")
    coursor.execute("""INSERT INTO item(id, orderId, name, description, mainPrice, secondaryPrice, count) 
                            VALUES (2,1,'Hamburger','Additional mayo', 15.5, 1.0, 2)""")
    coursor.execute("""INSERT INTO item(id, orderId, name, description, mainPrice, secondaryPrice, count) 
                            VALUES (3,1,'Hot Chocolate','Additional cinnamon', 10.5, 2.5, 1)""")
    coursor.execute("""INSERT INTO item(id, orderId, name, description, mainPrice, secondaryPrice, count) 
                                VALUES (4,1,'Coffee','Additional milk', 15.5, 1.0, 2)""")
    coursor.execute("""INSERT INTO item(id, orderId, name, description, mainPrice, secondaryPrice, count) 
                            VALUES (5,2,'Hot-dog','Additional ketchup ', 10.5, 2.5, 1)""")
    coursor.execute("""INSERT INTO item(id, orderId, name, description, mainPrice, secondaryPrice, count) 
                                VALUES (6,2,'Pastrami','Additional mustard', 15.5, 1.0, 2)""")
    coursor.execute("""INSERT INTO item(id, orderId, name, description, mainPrice, secondaryPrice, count) 
                            VALUES (7,2,'Fish and chips','Additional ketchup + additional cheese', 10.5, 2.5, 1)""")
    coursor.execute("""INSERT INTO item(id, orderId, name, description, mainPrice, secondaryPrice, count) 
                                VALUES (8,3,'Chips','Additional ketchup', 15.5, 1.0, 2)""")
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
        coursor.execute('SELECT * FROM item where orderId=?', (order[0],))
        orderItems: list = coursor.fetchall()
        for item in orderItems:
            sum += (item[4] + item[5]) * item[6]
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


def returnLastSevenDaysProfitList(user_id) -> list:
    SQLConnection: Connection = sqlite3.connect('RestaurantDatabase')
    coursor = SQLConnection.cursor()
    coursor.execute('SELECT * FROM orderTable where userId=? and orderStatus=?', (user_id, "ready",))
    orders: list = coursor.fetchall()
    ordersWithPrices: list[tuple] = []
    for order in orders:
        coursor.execute('SELECT * FROM item where orderId=?', (order[0],))
        buforItems = coursor.fetchall()
        # list of items for each order
        sum = 0
        for item in buforItems:
            sum += (item[4] + item[5]) * item[6]
        ordersWithPrices.append((order, sum))
    print(ordersWithPrices)
    last_days_list_with_prices = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0)]
    for orderWithPrice in ordersWithPrices:
        print(datetime.strptime(datetime.today().strftime('%Y-%m-%d'),'%Y-%m-%d') - datetime.strptime(orderWithPrice[0][7].split('T')[0], '%Y-%m-%d'))
        for day in last_days_list_with_prices:
            if (datetime.strptime(datetime.today().strftime('%Y-%m-%d'),'%Y-%m-%d') - datetime.strptime(orderWithPrice[0][7].split('T')[0], '%Y-%m-%d')) == \
                    timedelta(days=day[0]):
                last_days_list_with_prices[day[0]] = (day[0], day[1] + orderWithPrice[1])
    last_days_list_with_prices_with_dates = [
        ("today",last_days_list_with_prices[0][1]),
        ("yesterday", last_days_list_with_prices[1][1]),
        ("2 d ago", last_days_list_with_prices[2][1]),
        ("3 d ago", last_days_list_with_prices[3][1]),
        ("4 d ago", last_days_list_with_prices[4][1]),
        ("5 d ago", last_days_list_with_prices[5][1]),
        ("6 d ago", last_days_list_with_prices[6][1])

    ]
    last_days_list_with_prices_with_dates.reverse()
    return last_days_list_with_prices_with_dates


def returnTopSellingDishesList(user_id) -> list:
    SQLConnection: Connection = sqlite3.connect('RestaurantDatabase')
    coursor = SQLConnection.cursor()
    coursor.execute('SELECT * FROM orderTable where userId=?', (user_id,))
    orders: list = coursor.fetchall()
    items: list = []
    for order in orders:
        coursor.execute('SELECT * FROM item where orderId=?', (order[0],))
        buforItems = coursor.fetchall()
        for item in buforItems:
            items.append(item)
    itemsWithCountsTupleList: list[tuple] = []
    # counting items by name
    for item in items:
        foundAnother = False
        if len(itemsWithCountsTupleList) == 0:
            itemsWithCountsTupleList.append((item[2], 1))
        for index, anotherItem in enumerate(itemsWithCountsTupleList):
            if anotherItem[0] == item[2]:
                itemsWithCountsTupleList[index] = anotherItem[0], anotherItem[1] + 1
                foundAnother = True
                break
        if not foundAnother:
            itemsWithCountsTupleList.append((item[2], 1))

    # sorting list of tuples
    lst = len(itemsWithCountsTupleList)
    for i in range(0, lst):
        for j in range(0, lst - i - 1):
            if itemsWithCountsTupleList[j][1] > itemsWithCountsTupleList[j + 1][1]:
                temp = itemsWithCountsTupleList[j]
                itemsWithCountsTupleList[j] = itemsWithCountsTupleList[j + 1]
                itemsWithCountsTupleList[j + 1] = temp

    itemsWithCountsTupleList.reverse()
    SQLConnection.close()
    if len(itemsWithCountsTupleList) < 5:
        return itemsWithCountsTupleList
    else:
        return itemsWithCountsTupleList[:5]


def changeUserPassword(user_id, password) -> bool:
    SQLConnection: Connection = sqlite3.connect('RestaurantDatabase')
    coursor = SQLConnection.cursor()
    coursor.execute('UPDATE user set password = ? where id = ?', (password, user_id))
    SQLConnection.close()
    return True


def deleteUserFromDatabase(user_id) -> bool:
    SQLConnection: Connection = sqlite3.connect('RestaurantDatabase')
    coursor = SQLConnection.cursor()
    coursor.execute('DELETE from user where id = ?', (user_id,))
    SQLConnection.close()
    return True

def returnIncomingOrdersList(user_id) -> list:
    SQLConnection: Connection = sqlite3.connect('RestaurantDatabase')
    coursor = SQLConnection.cursor()
    coursor.execute('SELECT * FROM orderTable where userId=? and orderStatus=?', (user_id,"incoming",))
    orders: list = coursor.fetchall()
    return orders

def returnAcceptedOrdersList(user_id) -> list:
    SQLConnection: Connection = sqlite3.connect('RestaurantDatabase')
    coursor = SQLConnection.cursor()
    coursor.execute('SELECT * FROM orderTable where userId=? and orderStatus=?', (user_id,"accepted",))
    orders: list = coursor.fetchall()
    return orders


def returnItemsForOrderList(order_id) -> list:
    SQLConnection: Connection = sqlite3.connect('RestaurantDatabase')
    coursor = SQLConnection.cursor()
    coursor.execute('SELECT * FROM item where orderId=?', (order_id,))
    items: list = coursor.fetchall()
    return items