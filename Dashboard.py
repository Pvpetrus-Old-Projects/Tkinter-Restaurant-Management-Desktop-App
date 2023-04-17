from customtkinter import *
from tkinter import *

set_appearance_mode("light")
set_default_color_theme("green")

# Stworzenie głównego okna
dashboardWindow = CTk()
dashboardWindow.title("Restaurant Manager")
dashboardWindow.iconbitmap("Resources/restaurant_4373.ico")
dashboardWindow.geometry("1200x600")


dashboardWindow.mainloop()