from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=500, height=500)
window.config(padx=100, pady=100)
label_km_value = Label(text="0")
label_km_value.grid(column=1, row=1)
label_miles = Label(text="Miles")
label_miles.grid(column=2, row=0)
label_is_equal_to = Label(text="is equal to")
label_is_equal_to.config(padx=10)
label_is_equal_to.grid(column=0, row=1)
entry = Entry(width=10)
entry.insert(END, string="0")
entry.grid(column=1, row=0)
label_km = Label(text="Km")
label_km.grid(column=2, row=1)



def calculate():
    miles = float(entry.get())
    km = miles * 1.609
    label_km_value.config(text=str(km))

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)


window.mainloop()