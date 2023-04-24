from customtkinter import *
from tkinter import *
from DatabaseActions import *
from PIL import Image, ImageTk

set_appearance_mode("light")
set_default_color_theme("green")

# Stworzenie głównego okna
global dashboardWindow
dashboardWindow = CTk()
dashboardWindow.title("Restaurant Manager")
dashboardWindow.iconbitmap("Resources/restaurant_4373.ico")
dashboardWindow.geometry("1200x600")
dashboardWindow.configure(background="#F4F5F7")

dashboardWindow.columnconfigure(0, weight=1)
dashboardWindow.columnconfigure(1, weight=1)
dashboardWindow.columnconfigure(2, weight=1)
dashboardWindow.columnconfigure(3, weight=1)
dashboardWindow.columnconfigure(4, weight=1)
dashboardWindow.columnconfigure(5, weight=13)
dashboardWindow.columnconfigure(6, weight=18)
dashboardWindow.rowconfigure(0, weight=2)
dashboardWindow.rowconfigure(1, weight=2)
dashboardWindow.rowconfigure(2, weight=2)
dashboardWindow.rowconfigure(3, weight=17)

global currentUserId
currentUserId = int(sys.argv[0])


def navigateToOrders() -> None:
    user = returnCertainUser(currentUserId)
    userId: int = user[0]
    sys.argv = [str(userId)]
    dashboardWindow.destroy()
    exec(open('Orders.py').read())


def navigateToMenu() -> None:
    user = returnCertainUser(currentUserId)
    userId: int = user[0]
    sys.argv = [str(userId)]
    dashboardWindow.destroy()
    exec(open('Menu.py').read())


# navbar

menuButton = CTkButton(dashboardWindow, command=navigateToMenu, text="", fg_color="white")
menuButton.grid(pady=20, row=0, column=0)
image = CTkImage(light_image=Image.open("Resources/menu.png"), size=(30, 30))
menuImagelabel = CTkLabel(menuButton, text="", image=image)
menuImagelabel.bind(navigateToMenu)
menuImagelabel.grid(row=0, column=0, sticky=W + E + N + S)

dashboardButton = CTkButton(dashboardWindow, text="")
dashboardButton.grid(pady=20, row=0, column=1, columnspan=2)
image = CTkImage(light_image=Image.open("Resources/pie-chart.png"), size=(30, 30))
DashboardImagelabel = CTkLabel(dashboardButton, text="", image=image)
DashboardImagelabel.grid(pady=5, row=0, column=0)
dashboardLabel = CTkLabel(dashboardButton, text="Dashboard", font=("Kanit", 16), bg_color='transparent')
dashboardLabel.grid(pady=5, row=0, column=1, sticky=W)

ordersButton = CTkButton(dashboardWindow, command=navigateToOrders, text="", fg_color="white")
ordersButton.grid(pady=20, row=0, column=3, columnspan=2)
image = CTkImage(light_image=Image.open("Resources/clipboard.png"), size=(30, 30))
OrdersMenuImage = CTkLabel(ordersButton, text="", image=image)
OrdersMenuImage.grid(pady=5, row=0, column=0)
ordersLabel = CTkLabel(ordersButton, text="Orders", font=("Kanit", 16))
ordersLabel.grid(pady=5, row=0, column=1, sticky=W)

# restaurant status

restaurantStatusFrame = CTkFrame(dashboardWindow, bg_color='transparent', fg_color='transparent')
restaurantStatusFrame.grid(pady=5, padx=10, row=1, column=0, columnspan=4, sticky=W + E + N + S)
restaurantStatusFrame.columnconfigure(0, weight=1)
restaurantStatusFrame.columnconfigure(1, weight=1)
restaurantStatusFrame.rowconfigure(0, weight=1)
restaurantStatusFrame.rowconfigure(1, weight=1)
openLabel = CTkLabel(restaurantStatusFrame, text="Pizza kingdom is open", font=("Kanit", 23))
openLabel.grid(pady=2, padx=30,row=0, column=0, sticky=W)
openLabel = CTkButton(restaurantStatusFrame, text="", width=7, height=7, fg_color="green", corner_radius=90)
openLabel.grid(pady=25, padx=60, row=0, column=0, sticky=E+S)
openLabel = CTkLabel(restaurantStatusFrame, text="Jana Kochanowskiego 15, Zambrow", font=("Kanit", 16))
openLabel.grid(pady=2,padx=30, row=1, column=0, sticky=W+N)

# 3 frames main frame

tripleHorizontalFrame = CTkFrame(dashboardWindow, height=100, bg_color='transparent', fg_color='transparent')
tripleHorizontalFrame.grid(pady=5, padx=5, row=2, column=0, columnspan=8, sticky=W + E)
tripleHorizontalFrame.columnconfigure(0, weight=1)
tripleHorizontalFrame.columnconfigure(1, weight=1)
tripleHorizontalFrame.columnconfigure(2, weight=1)

# total gross revenue

totalGrossRevenueFrame = CTkFrame(tripleHorizontalFrame, height=100, fg_color="#FFFFFF")
totalGrossRevenueFrame.grid(pady=5, padx=10, row=0, column=0, sticky=W + E)
totalGrossRevenueFrame.columnconfigure(0, weight=1)
totalGrossRevenueFrame.columnconfigure(1, weight=1)
totalGrossRevenueFrame.rowconfigure(0, weight=1)
totalGrossRevenueFrame.rowconfigure(1, weight=1)

image = CTkImage(light_image=Image.open("Resources/money.png"), size=(60, 60))
totalGrossRevenueImageLabel = CTkLabel(totalGrossRevenueFrame, text="", image=image)
totalGrossRevenueImageLabel.grid(pady=5, row=0, rowspan=2, column=0)
totalGrossRevenueLabel = CTkLabel(totalGrossRevenueFrame, text="Total gross revenue", font=("Kanit", 16), bg_color='transparent')
totalGrossRevenueLabel.grid(pady=5, row=0, column=1, sticky=W)
totalGrossRevenueValueLabel = CTkLabel(totalGrossRevenueFrame, text="$ "+str(returnTotalRevenueForUser(currentUserId)), font=("Kanit", 25), bg_color='transparent')
totalGrossRevenueValueLabel.grid(pady=5, row=1, column=1, sticky=W)

# accepted orders

acceptedOrdersFrame = CTkFrame(tripleHorizontalFrame, height=100, fg_color="#FFFFFF")
acceptedOrdersFrame.grid(pady=5, padx=10, row=0, column=1, sticky=W + E)
acceptedOrdersFrame.columnconfigure(0, weight=1)
acceptedOrdersFrame.columnconfigure(1, weight=1)
acceptedOrdersFrame.rowconfigure(0, weight=1)
acceptedOrdersFrame.rowconfigure(1, weight=1)

image = CTkImage(light_image=Image.open("Resources/return.png"), size=(60, 60))
totalGrossRevenueImageLabel = CTkLabel(acceptedOrdersFrame, text="", image=image)
totalGrossRevenueImageLabel.grid(pady=5, row=0, rowspan=2, column=0)
totalGrossRevenueLabel = CTkLabel(acceptedOrdersFrame, text="Accepted Orders", font=("Kanit", 16), bg_color='transparent')
totalGrossRevenueLabel.grid(pady=5, row=0, column=1, sticky=W)
totalGrossRevenueValueLabel = CTkLabel(acceptedOrdersFrame, text=str(returnAcceptedOrderRatioForUser(currentUserId))+"%", font=("Kanit", 25), bg_color='transparent')
totalGrossRevenueValueLabel.grid(pady=5, row=1, column=1, sticky=W)

# todays working hours

todaysWorkingHoursFrame = CTkFrame(tripleHorizontalFrame, height=100, fg_color="#FFFFFF")
todaysWorkingHoursFrame.grid(pady=5, padx=10, row=0, column=2, sticky=W + E)
todaysWorkingHoursFrame.columnconfigure(0, weight=1)
todaysWorkingHoursFrame.columnconfigure(1, weight=1)
todaysWorkingHoursFrame.rowconfigure(0, weight=1)
todaysWorkingHoursFrame.rowconfigure(1, weight=1)

todaysWorkingHoursLabel = CTkLabel(todaysWorkingHoursFrame, text="Today's working hours", font=("Kanit", 16), bg_color='transparent')
todaysWorkingHoursLabel.grid(pady=5, padx=25, row=0, column=0, sticky=W)
todaysWorkingHoursValueLabel = CTkLabel(todaysWorkingHoursFrame, text="8AM - 8PM", font=("Kanit", 25), bg_color='transparent')
todaysWorkingHoursValueLabel.grid(pady=5, padx=25,row=1, column=0, sticky=W)
viewAllButton = CTkButton(todaysWorkingHoursFrame, text="View all", fg_color="#E5F3FF",text_color="#138AF2")
viewAllButton.grid(pady=20, row=0,rowspan=2, column=1)

# double frame

doubleFrame = CTkFrame(dashboardWindow, fg_color="transparent", bg_color='transparent', height=300)
doubleFrame.grid(pady=5, padx=15, row=3, rowspan=10, column=0, columnspan=8, sticky=W + E + N + S)
doubleFrame.columnconfigure(0, weight=7)
doubleFrame.columnconfigure(1, weight=3)

# revenue overview chart

revenueOverviewFrame = CTkFrame(doubleFrame, fg_color="#FFFFFF", height=325)
revenueOverviewFrame.grid(pady=5, padx=10, row=0, column=0, sticky=W + E + N + S)

# top-selling (max 14)

topSellingFrame = CTkFrame(doubleFrame, fg_color="#FFFFFF", height=325)
topSellingFrame.grid(pady=5, padx=10, row=0, column=1, sticky=W + E + N + S)

dashboardWindow.mainloop()
