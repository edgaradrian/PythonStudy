import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

#Label

my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()
my_label["text"] = "New text"

#Button

def button_clicked():
    my_label["text"] = my_entry.get()

my_button = tkinter.Button(text="Click Me", command=button_clicked)
my_button.pack()

#Entry

my_entry = tkinter.Entry(width=10)
my_entry.pack()


window.mainloop()