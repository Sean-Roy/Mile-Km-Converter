from tkinter import *
from tkinter import messagebox  # messagebox needs to be loaded separately.

FONT1 = ("Arial", 16, "normal")
FONT2 = ("Arial", 16, "bold")


# Calculation to be performed based on inputted value:
def calculation():
    try:
        miles = float(user_input.get())
    except ValueError:
        messagebox.showinfo(title="Oops!", message="Ensure you are only inputting numeric values.")
    else:
        km = round((miles*1.60934), 2)
        label_3.config(text=km)


# GUI format/set-up:
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=350, height=150)
window.config(padx=20, pady=20)

user_input = Entry(width=10, font=FONT2)
user_input.insert(END, string="0")
user_input.grid(column=1, row=0)
user_input.focus()

label_1 = Label(text="Miles", font=FONT1)
label_1.grid(column=2, row=0)
label_1.config(padx=10, pady=10)

label_2 = Label(text="is equal to", font=FONT1)
label_2.grid(column=0, row=1)
label_2.config(padx=10, pady=10)

label_3 = Label(text=0, font=FONT2)
label_3.grid(column=1, row=1)
label_3.config(padx=10, pady=10)

label_4 = Label(text="Km", font=FONT1)
label_4.grid(column=2, row=1)
label_4.config(padx=10, pady=10)

calculate = Button(text="Calculate", font=FONT2, command=calculation)
calculate.grid(column=1, row=2)

window.mainloop()
