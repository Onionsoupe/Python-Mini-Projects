from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk  # Import Pillow for image resizing
from random import randint,choice,shuffle
import pyperclip

WHITE = "#FFFFFF"
FONT_NAME = "Courier"

# ----------------------- PASSWORD GENERATOR -------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_symbols + password_numbers + password_letters
    shuffle(password_list)
    password = "".join(password_list)
    pyperclip.copy(password)
    password_entry.delete(0, END)
    password_entry.insert(0, password)

# ------------------------- SAVE PASSWORD ----------------------------- #
def save_password():
    a=website_entry.get()
    b=email_entry.get()
    c=password_entry.get()

    if len(a) ==0 or len(b) ==0 or len(c)==0:
        messagebox.askokcancel(title="Oops", message="Don't leave any fields empty! ")
    else:
        is_ok = messagebox.askokcancel(title=a, message="Do you want to save ")
        if is_ok:
            text_file = open("data.txt", "a")
            text_file.write(f"{a} | {b} | {c} \n")
            text_file.close()
            website_entry.delete(0, END )
            email_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg=WHITE)

# Load and Resize Image
original_image = Image.open("lock.png")  # Load the large image
resized_image = original_image.resize((200, 200), Image.LANCZOS)  # Resize to fit Canvas
logo_img = ImageTk.PhotoImage(resized_image)  # Convert to Tkinter format

# Logo Display
canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
canvas.create_image(100, 100, image=logo_img)  # Centered at (100, 100)
canvas.grid(column=1, row=0)

# Form UI
website_label = Label(text="Website:", font=("Arial", 10, "normal"), bg=WHITE)
website_label.grid(column=0, row=1, pady=10, sticky="e")
website_entry = Entry(width=43)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2, pady=5, sticky="e")

email_label = Label(text="Email/Username:", font=("Arial", 10, "normal"), bg=WHITE)
email_label.grid(column=0, row=2, pady=10, sticky="e")
email_entry = Entry(width=43)
email_entry.insert(0,'911iangab44@gmail.com')
email_entry.grid(column=1, row=2, columnspan=2, pady=5, sticky="e")

Password_label = Label(text="Password:", font=("Arial", 10, "normal"), bg=WHITE)
Password_label.grid(column=0, row=3, pady=10, sticky="e")
password_entry = Entry(width=25)
password_entry.grid(column=1, row=3, sticky="e", pady=5)

generate_button = Button(text="Generate Password", bg=WHITE, width=14, command=password_generator)
generate_button.grid(column=2, row=3, sticky="w", pady=10)

add_button = Button(text="Add", width=36, bg=WHITE, command=save_password)
add_button.grid(column=1, row=4, columnspan=2, pady=10, sticky="e")

window.mainloop()
