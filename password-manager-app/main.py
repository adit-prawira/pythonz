from tkinter import *
from tkinter import messagebox
from  random import choice, randint, shuffle
import pyperclip
import json

# ------------------------------- HELPER FUNCTIONS ------------------------------- #
def clearEntry():
    website_entry.delete(0, END)
    email_entry.delete(0, END)
    password_entry.delete(0, END)
    
def search():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message = "No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title="Credential Found", message = f"Email: {email}\nPassword:{password}")
        else:
            messagebox.showinfo(title="Credential Not Found", message = f"Sorry there is no record of your password for {website}")
        
    
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generatePassword():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)
    password = "".join(password_list)
    
    if(len(password_entry.get()) != 0):
        password_entry.delete(0, END)
        
    password_entry.insert(0, password)
    pyperclip.copy(password)
    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    newData = {
        website:{
            "email": email,
            "password": password
        }
    }
    if(len(website) == 0 or len(password) == 0 or len(email) == 0):
        messagebox.showinfo(title="Incomplete Credentials", message="Please make sure you haven't left any fields empty")
    else:
        okToProceed = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {email}\n"
        f"Password: {password}\nIs it OK to save?")
        if(okToProceed):
            try:
                with open("data.json", "r") as data_file:
                    # Read JSON data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    # dump the updated data to the JSON file
                    json.dump(newData, data_file, indent=4)
            else:
                data.update(newData)
                with open("data.json", "w") as data_file:
                    # dump the updated data to the JSON file
                    json.dump(data, data_file, indent=4)
            finally:
                clearEntry()   
                
# ---------------------------- UI ------------------------------- #
window = Tk()
window.title("My Password Manager")
window.config(padx = 50, pady = 50)

canvas = Canvas(height = 200, width =200)
logo = PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image = logo)
canvas.grid(row = 0, column = 1)


# Section for setting up labels
website_label = Label(text = "Website")
website_label.grid(row = 1,  column = 0)

email_label = Label(text = "Email/Username")
email_label.grid(row = 2,  column = 0)

password_label= Label(text = "Password")
password_label.grid(row = 3, column = 0)


#Section for setting up entries
website_entry = Entry(width = 20)
website_entry.grid(row = 1, column = 1)
website_entry.focus()

search_button = Button (text = "Search", width = 14, command = search)
search_button.grid(row = 1, column = 2)

email_entry = Entry(width = 35)
email_entry.grid(row = 2, column = 1, columnspan = 5)

password_entry = Entry(width = 20)
password_entry.grid(row = 3, column = 1)

#Section for setting up buttons
generate_password_button = Button(text = "Generate Password", command = generatePassword)
generate_password_button.grid(row = 3, column = 2)

add_button = Button (text = "Add", width = 36, command = save)
add_button.grid(row = 4, column = 1, columnspan = 2)

window.mainloop()