from tkinter import *

def calculated_button_clicked():
    km = float(entry.get()) / 0.6214
    num_km_label["text"] = f"{km}"

#Window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height= 150)
window.config(padx=20, pady=20)

#Entry
entry = Entry(width=20)
entry.grid(column=1, row= 0)

#Label
miles_label = Label()
miles_label["text"] = "Miles"
miles_label.grid(column=2, row= 0)

is_equal_to_label = Label()
is_equal_to_label["text"] = "is equal to"
is_equal_to_label.grid(column=0, row=1)

num_km_label = Label()
num_km_label["text"] = "0"
num_km_label.grid(column=1, row=1)

km_label = Label()
km_label["text"] = "Km"
km_label.grid(column=2, row=1)

#Button
button = Button(text="Calculate", command=calculated_button_clicked)
button.grid(column=1, row=2)

window.mainloop()