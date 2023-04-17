

# Łączenie z bazą danych
import sqlite3

def SetupDatabase():
    SQLConnection = sqlite3.connect('RestaurantDatabase')
    coursor = SQLConnection.cursor()
    #coursor.execute("""DROP TABLE User""")
    #coursor.execute("""DROP TABLE Order""")
    #coursor.execute("""DROP TABLE Item""")
    coursor.execute("""CREATE TABLE User (id integer PRIMARY KEY, username text NOT NULL UNIQUE, password text NOT NULL)""")

    coursor.execute("""CREATE TABLE Order (id integer PRIMARY KEY, FOREIGN KEY (userId) REFERENCES User (id) ON DELETE CASCADE, 
                        orderType text, location text, distance real,
                        customerName text, orderStatus text, estimatedDeliveryTime datetime)""")

    coursor.execute("""CREATE TABLE Item (id integer PRIMARY KEY, FOREIGN KEY (orderId)
           REFERENCES Order (id) ON DELETE CASCADE, name text, description text, mainPrice real, 
                        secondaryPrice real, count integer)""")

    coursor.execute("""INSERT INTO User(id, username, password) 
              VALUES (1,'admin','admin')""")

    coursor.execute("""INSERT INTO User(id, username, password) 
              VALUES (1,'admin','admin')""")

    coursor.execute("""INSERT INTO User(id, username, password) 
              VALUES (1,'admin','admin')""")
    # """Update SqliteDb_developers set salary = 10000 where id = 4"""
    # """DELETE from SqliteDb_developers where id = 4"""

    SQLConnection.commit()
    SQLConnection.close()