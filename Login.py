from customtkinter import *
from tkinter import *
from DatabaseActions import *

# label, button, entry,
# grid, column, row, command (lambda do parametrów, text, bg, fg, pierwszy parametr oznacza gdzie coś przynalezy,
# pack pakuje, get, relieve=SUNKEN, grid sticky przyczepia/stretchuje do końców grida (W+E+N+S),
# anchor przyczepia zawartość, LabelFrame, radiobutton, messagebox.showinfo - popup, są inne typy
# insert dodaje default text, columnspan, rowspan, height, padx, pady, fetchall wydobywa dane z kursora
# width, borderwidth, insert, delete, root.quit wychodzi z programu, grid_forget powoduje że coś znika, state=DISABLED
# TopLevel() - nowe okno, Scale - suwak, checkbutton, optionmenu - drop down list
# Przykład
# image = PhotoImage(file="Resources/calendar.png")
# label = CTkLabel(loginWindow,image=image)
# label.pack()

set_appearance_mode("dark")
set_default_color_theme("green")

# Stworzenie głównego okna
global loginWindow
loginWindow: CTk = CTk()
loginWindow.title("Restaurant Manager")
loginWindow.iconbitmap("Resources/restaurant_4373.ico")
loginWindow.geometry("500x350")

#triggers again when logging out
SetupDatabase()


def loginAction() -> None:
    if loginToDatabase(username.get(), password.get()):
        errorLabel.text = "Correct credentials"
        user: tuple = returnCertainUserByUsernameAndPassword(username.get(), password.get())
        userId: int = user[0]
        sys.argv = [str(userId)]
        loginWindow.destroy()
        exec(open('Orders.py').read())
        errorLabel.configure(text="Correct credentials")
    else:
        errorLabel.configure(text="Incorrect credentials")


loginFrame: CTkFrame = CTkFrame(master=loginWindow)
loginFrame.pack(pady=20, padx=60, fill="both", expand=True)

loginTitle: CTkLabel = CTkLabel(loginFrame, text="Restaurant Manager", font=('Kanit', 31, 'bold'))
loginTitle.pack(pady=12)

loginDescription: CTkLabel = CTkLabel(loginFrame, text=r"The accounts are created directly by the application "
                                                       r"provider. If you "
                                                       r"have not received credentials email us.",
                                      font=("Kanit", 14), text_color="grey", wraplength=300)
loginDescription.pack(pady=3, padx=30)

username = StringVar()
username.set("admin")
usernameEntry: CTkEntry = CTkEntry(loginFrame, textvariable=username, placeholder_text="Username", font=("Kanit", 16),
                                   width=250)
usernameEntry.pack(pady=10)

password = StringVar()
password.set("admin")
passwordEntry: CTkEntry = CTkEntry(loginFrame, textvariable=password, placeholder_text="Password", font=("Kanit", 16),
                                   width=250)
passwordEntry.pack(pady=10)

loginButton: CTkButton = CTkButton(loginFrame, text="Login", command=loginAction, width=150)
loginButton.pack(pady=10)

errorLabel: CTkLabel = CTkLabel(loginFrame, text="No Errors:)", font=("Kanit", 16), text_color="red")
errorLabel.pack(pady=5)

# Uruchomienie nasłuchiwania w aplikacji
loginWindow.mainloop()
