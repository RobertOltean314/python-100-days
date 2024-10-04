from re import I
import tkinter as tk


def change_label_event():
    label.config(text=input.get())


window = tk.Tk()
window.title("First Tkinter Application")
window.minsize(width=500, height=300)

# Label
label = tk.Label(text="I am a Label", font=("Arial", 24, "bold"))
label.pack()

# Button
button = tk.Button(text="click me", command=change_label_event)
button.pack()

# Entry
input = tk.Entry(width=10)
input.pack()

window.mainloop()
