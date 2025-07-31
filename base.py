import tkinter as tk

def show_frame(frame):
    frame.tkraise()

def start_timer():
    global time_left
    time_left = 10  # seconds
    update_timer()
    show_frame(page2)

def update_timer():
    global time_left
    if time_left >= 0:
        timer_label.config(text=f"Time left: {time_left}s")
        time_left -= 1
        root.after(1000, update_timer)
    else:
        timer_label.config(text="Time's up!")

root = tk.Tk()
root.title("Lock in Gang!")
root.geometry("300x300+50+50")

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

# -------- First Page --------
page1 = tk.Frame(root)
page1.grid(row=0, column=0, sticky="nsew")

tk.Label(page1, text="Hello World!").pack(pady=10)
tk.Label(page1, text="Are you ready to lock in?").pack(pady=10)
tk.Button(page1, text="Lock in!", command=start_timer).pack(pady=20)

# -------- Second Page --------
page2 = tk.Frame(root)
page2.grid(row=0, column=0, sticky="nsew")

timer_label = tk.Label(page2, text="Time left: 10s", font=("Helvetica", 16))
timer_label.pack(pady=40)

tk.Button(page2, text="Back", command=lambda: show_frame(page1)).pack()

# Start with the first page
show_frame(page1)

root.mainloop()

import tkinter as tk
import pomodoroPage
import pdfMerge

root = tk.Tk()
root.title("Lock in Gang!")
root.geometry("300x300+50+50")

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

page1 = tk.Frame(root)
page1.grid(row=0, column=0, sticky="nsew")

tk.Label(page1, text="Hello World!").pack(pady=10)
tk.Label(page1, text="Are you ready to lock in?").pack(pady=10)

pomodoroPage.init(root, page1)

pdfMerge.init(root, page1)

tk.Button(page1, text="Pomodoro", command=pomodoroPage.start_timer).pack(pady=20)
tk.Button(page1, text="PDF Merger", command=lambda: pdfMerge.show_frame(pdfMerge.page3)).pack(pady=10)

pomodoroPage.show_frame(page1)

root.mainloop()
