from customtkinter import *
from tkinter import *
from DatabaseActions import *

set_appearance_mode("dark")
set_default_color_theme("green")

# Stworzenie głównego okna
databaseWindow: CTk = CTk()
databaseWindow.title("Restaurant Manager")
databaseWindow.iconbitmap("Resources/restaurant_4373.ico")

width = databaseWindow.winfo_screenwidth()
height = databaseWindow.winfo_screenheight()
# setting tkinter window size
databaseWindow.geometry("%dx%d" % (width, height))

databaseWindow.columnconfigure(0, weight=1)
databaseWindow.columnconfigure(1, weight=3)
databaseWindow.columnconfigure(2, weight=2)

userLabel = CTkLabel(databaseWindow, text="Users", font=("Roboto", 16), text_color="red")
userLabel.grid(pady=5, padx=10, row=0, column=0)

orderLabel = CTkLabel(databaseWindow, text="Orders", font=("Roboto", 16), text_color="red")
orderLabel.grid(pady=5, padx=10, row=0, column=1)

itemlabel = CTkLabel(databaseWindow, text="Items", font=("Roboto", 16), text_color="red")
itemlabel.grid(pady=5, padx=10, row=0, column=2)

userColumns = CTkLabel(databaseWindow, text="id, username, password", font=("Roboto", 16), text_color="red")
userColumns.grid(pady=5, padx=10, row=1, column=0)

orderColumns = CTkLabel(databaseWindow, text="id, userid, orderType, location, distance, customerName, orderStatus,"
                                             "createAt, acceptAt, finishAt, estimate",
                        font=("Roboto", 16), text_color="red")
orderColumns.grid(pady=5, padx=10, row=1, column=1)

itemColumns = CTkLabel(databaseWindow, text="id, orderId, name, description, mainPrice, secondaryPrice, count", font=("Roboto", 16), text_color="red")
itemColumns.grid(pady=5, padx=10, row=1, column=2)

allUsersList: list = returnAllUsers()
allOrdersList: list = returnAllOrders()
allItemsList: list = returnAllItems()

for index, user in enumerate(allUsersList):
    CTkLabel(databaseWindow, text=str(user), font=("Roboto", 16), text_color="red").grid(pady=5, padx=10, row=index + 2,
                                                                                         column=0)

for index, order in enumerate(allOrdersList):
    CTkLabel(databaseWindow, text=str(order), font=("Roboto", 16), text_color="red").grid(pady=5, padx=10,
                                                                                          row=index + 2, column=1)

for index, item in enumerate(allItemsList):
    CTkLabel(databaseWindow, text=str(item), font=("Roboto", 16), text_color="red").grid(pady=5, padx=10, row=index + 2,
                                                                                         column=2)
# Uruchomienie nasłuchiwania w aplikacji
databaseWindow.mainloop()
