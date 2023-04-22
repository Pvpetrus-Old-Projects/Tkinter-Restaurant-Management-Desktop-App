from customtkinter import *
from tkinter import *
import sys
from DatabaseActions import *
from PIL import Image, ImageTk

set_appearance_mode("light")
set_default_color_theme("green")

# Stworzenie głównego okna
global ordersWindow
ordersWindow: CTk = CTk()
ordersWindow.title("Restaurant Manager")
ordersWindow.iconbitmap("Resources/restaurant_4373.ico")
ordersWindow.geometry("1200x600")
ordersWindow.configure(background="#F4F5F7")

ordersWindow.columnconfigure(0, weight=1)
ordersWindow.columnconfigure(1, weight=1)
ordersWindow.columnconfigure(2, weight=1)
ordersWindow.columnconfigure(3, weight=1)
ordersWindow.columnconfigure(4, weight=1)
ordersWindow.columnconfigure(5, weight=13)
ordersWindow.columnconfigure(6, weight=18)
ordersWindow.rowconfigure(0, weight=1)
ordersWindow.rowconfigure(1, weight=15)
ordersWindow.rowconfigure(2, weight=3)

global currentUserId
currentUserId = int(sys.argv[0])


def navigateToDashboard() -> None:
    user = returnCertainUser(currentUserId)
    userId: int = user[0]
    sys.argv = [str(userId)]
    ordersWindow.destroy()
    exec(open('Dashboard.py').read())


# navbar

image = CTkImage(light_image=Image.open("Resources/menu.png"), size=(30, 30))
menuImagelabel = CTkLabel(ordersWindow, text="", image=image)
menuImagelabel.grid(pady=20, padx=5, row=0, column=0)

dashboardButton = CTkButton(ordersWindow, command=navigateToDashboard, text="", fg_color="white")
dashboardButton.grid(pady=20, row=0, column=1, columnspan=2)
image = CTkImage(light_image=Image.open("Resources/pie-chart.png"), size=(30, 30))
DashboardImagelabel = CTkLabel(dashboardButton, text="", image=image)
DashboardImagelabel.grid(pady=5, row=0, column=0)
dashboardLabel = CTkLabel(dashboardButton, text="Dashboard", font=("Roboto", 16), bg_color='transparent')
dashboardLabel.grid(pady=5, row=0, column=1, sticky=W)

ordersButton = CTkButton(ordersWindow, text="")
ordersButton.grid(pady=20, row=0, column=3, columnspan=2)
image = CTkImage(light_image=Image.open("Resources/clipboard.png"), size=(30, 30))
OrdersMenuImage = CTkLabel(ordersButton, text="", image=image)
OrdersMenuImage.grid(pady=5, row=0, column=0)
ordersLabel = CTkLabel(ordersButton, text="Orders", font=("Roboto", 16))
ordersLabel.grid(pady=5, row=0, column=1, sticky=W)

# incoming

incomingFrame = CTkFrame(ordersWindow, bg_color="#E8EAED", corner_radius=10)
incomingFrame.grid(pady=10, padx=10, row=1, rowspan=2, column=0, columnspan=6, sticky=W + E + S + N)

# accepted

incomingFrame = CTkFrame(ordersWindow, bg_color="#E8EAED")
incomingFrame.grid(pady=10, padx=10, row=1, column=6, sticky=W + E + S + N)

# ready

incomingFrame = CTkFrame(ordersWindow, bg_color="#E8EAED")
incomingFrame.grid(pady=10, padx=10, row=2, column=6, sticky=W + E + S + N)
allUserOrders: list = returnAllOrdersForUser(currentUserId)

"""print(allUserOrders)

for index, order in enumerate(allUserOrders):
    CTkLabel(ordersWindow, text=str(order), font=("Roboto", 16), text_color="red").grid(pady=5, padx=10, row=index + 1,
                                                                                        column=0, columnspan=6)"""

ordersWindow.mainloop()
