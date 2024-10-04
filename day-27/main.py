import tkinter as tk

window = tk.Tk()

# Window
window.title("First Tkinter Application")
window.minsize(width=500, height=300)

# Label
label = tk.Label(text="I am a Label", font=("Arial", 24, "bold"))
label.pack()

window.mainloop()
