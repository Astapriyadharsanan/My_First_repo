import tkinter as tk
from time import strftime

def time():
    current_time = strftime('%H:%M:%S %p')  # Hour:Minute:Second AM/PM
    label.config(text=current_time)
    label.after(1000, time)  # update every 1000ms (1 second)

# Create GUI window
window = tk.Tk()
window.title("Digital Clock")

# Styling the clock
label = tk.Label(window, font=('Arial', 60), background='black', foreground='cyan')
label.pack(anchor='center')

# Start the clock
time()

# Run the application
window.mainloop()
