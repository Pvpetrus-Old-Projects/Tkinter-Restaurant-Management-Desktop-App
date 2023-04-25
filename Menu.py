import tkinter

from customtkinter import *
from tkinter import *
import sys
from DatabaseActions import *
from PIL import Image, ImageTk





set_appearance_mode("light")
set_default_color_theme("green")

# Stworzenie głównego okna
global menuWindow
menuWindow: CTk = CTk()
menuWindow.title("Restaurant Manager")
menuWindow.iconbitmap("Resources/restaurant_4373.ico")
menuWindow.geometry("1200x600")
menuWindow.configure(background="#F4F5F7")

menuWindow.columnconfigure(0, weight=1)
menuWindow.columnconfigure(1, weight=1)
menuWindow.rowconfigure(0, weight=1)
menuWindow.rowconfigure(1, weight=1)

global currentUserId
currentUserId = int(sys.argv[0])

global password
password = StringVar()
password.set("Password")


def leaveMenu() -> None:
    user = returnCertainUser(currentUserId)
    userId: int = user[0]
    sys.argv = [str(userId)]
    menuWindow.destroy()
    exec(open('Dashboard.py').read())

def setColorMode(color: str) -> None:
    set_default_color_theme(color)


def setAppearanceMode(mode: str) -> None:
    set_appearance_mode(mode)


def editUserPassword() -> None:
    if changeUserPassword(currentUserId, password.get()):
        pass
    else:
        pass


def deleteUser() -> None:
    if deleteUserFromDatabase(currentUserId):
        menuWindow.destroy()
        exec(open('Login.py').read())
    else:
        pass


menuButton = CTkButton(menuWindow, command=leaveMenu, text="Go back to dashboard", font=("Kanit", 25))
menuButton.grid(pady=20, row=0, column=0, columnspan=10)

appearanceModeFrame = CTkFrame(menuWindow, height=75, width=200, fg_color="#FFFFFF")
appearanceModeFrame.grid(pady=5, padx=10, row=1, column=0, sticky=W + E)
appearanceModeFrame.columnconfigure(0, weight=1)
appearanceModeFrame.columnconfigure(1, weight=1)
appearanceModeFrame.rowconfigure(0, weight=1)
appearanceModeFrame.rowconfigure(1, weight=1)
appearanceModeFrame.rowconfigure(2, weight=1)

# mode settings
changeAppearanceModeLabel = CTkLabel(appearanceModeFrame, text="Change appearance mode", font=("Kanit", 25),
                                     bg_color='transparent')
changeAppearanceModeLabel.grid(pady=5, padx=50, row=1, column=0, sticky=W)
lightAppearanceButton = CTkButton(appearanceModeFrame, command=lambda: set_appearance_mode("light"), text="Light",
                                  fg_color="#E5F3FF", text_color="#138AF2")
lightAppearanceButton.grid(pady=5, row=0, column=1)
darkAppearanceModeButton = CTkButton(appearanceModeFrame, command=lambda: set_appearance_mode("dark"), text="Dark",
                                     fg_color="#E5F3FF", text_color="#138AF2")
darkAppearanceModeButton.grid(pady=5, row=1, column=1)
systemAppearanceMode = CTkButton(appearanceModeFrame, command=lambda: set_appearance_mode("system"), text="System",
                                 fg_color="#E5F3FF", text_color="#138AF2")
systemAppearanceMode.grid(pady=5, row=2, column=1)

# color settings
ColorModeFrame = CTkFrame(menuWindow, height=75, width=200, fg_color="#FFFFFF")
ColorModeFrame.grid(pady=5, padx=10, row=1, column=1, sticky=W + E)
ColorModeFrame.columnconfigure(0, weight=1)
ColorModeFrame.columnconfigure(1, weight=1)
ColorModeFrame.rowconfigure(0, weight=1)
ColorModeFrame.rowconfigure(1, weight=1)
ColorModeFrame.rowconfigure(2, weight=1)

changeColorModeLabel = CTkLabel(ColorModeFrame, text="Change appearance mode", font=("Kanit", 25),
                                bg_color='transparent')
changeColorModeLabel.grid(pady=5, padx=50, row=1, column=0, sticky=W)

blueColorButton = CTkButton(ColorModeFrame, command=lambda: set_default_color_theme("blue"), text="Blue",
                            fg_color="#E5F3FF",
                            text_color="#138AF2")
blueColorButton.grid(pady=5, row=0, column=1)
greenColorModeButton = CTkButton(ColorModeFrame, command=lambda: set_default_color_theme("green"), text="Green",
                                 fg_color="#E5F3FF", text_color="#138AF2")
greenColorModeButton.grid(pady=5, row=1, column=1)
darkBlueColorMode = CTkButton(ColorModeFrame, command=lambda: set_default_color_theme("dark-blue"), text="Dark Blue",
                              fg_color="#E5F3FF", text_color="#138AF2")
darkBlueColorMode.grid(pady=5, row=2, column=1)

# edit password
editPasswordFrame = CTkFrame(menuWindow, height=75, width=200, fg_color="#FFFFFF")
editPasswordFrame.grid(pady=5, padx=10, row=2, column=0, sticky=W + E)
editPasswordFrame.columnconfigure(0, weight=1)
editPasswordFrame.columnconfigure(1, weight=1)
editPasswordFrame.rowconfigure(0, weight=1)
editPasswordFrame.rowconfigure(1, weight=1)
editPasswordFrame.rowconfigure(2, weight=1)

editPasswordLabel = CTkLabel(editPasswordFrame, text="Change password", font=("Kanit", 25),
                             bg_color='transparent')
editPasswordLabel.grid(pady=5, padx=50, row=1, rowspan=2, column=0, sticky=W)
editPasswordEntry = CTkEntry(editPasswordFrame, textvariable=password,
                             fg_color="#E5F3FF", text_color="#138AF2")
editPasswordEntry.grid(pady=5, row=1, column=1)
editPasswordButton = CTkButton(editPasswordFrame, command=editUserPassword, text="Change",
                               fg_color="#E5F3FF", text_color="#138AF2")
editPasswordButton.grid(pady=5, row=2, column=1)

# delete user
deleteUserFrame = CTkFrame(menuWindow, height=75, width=200, fg_color="#FFFFFF")
deleteUserFrame.grid(pady=5, padx=10, row=2, column=1, sticky=W + E)
deleteUserFrame.columnconfigure(0, weight=1)
deleteUserFrame.columnconfigure(1, weight=1)
deleteUserFrame.rowconfigure(0, weight=1)
deleteUserFrame.rowconfigure(1, weight=1)
deleteUserFrame.rowconfigure(2, weight=1)

deleteUserButton = CTkButton(deleteUserFrame, command=deleteUser, text="Delete user",
                             fg_color="#E5F3FF", text_color="#138AF2")
deleteUserButton.grid(pady=5, row=0, column=0, rowspan=3, columnspan=3)

menuWindow.mainloop()
