import tkinter as tk

root = None
page1 = None
page2 = None
timer_label = None
time_left = 10

def init(shared_root, shared_page1):
    global root, page1, page2, timer_label

    root = shared_root
    page1 = shared_page1

    # -------- Second Page --------
    page2 = tk.Frame(root)
    page2.grid(row=0, column=0, sticky="nsew")

    timer_label = tk.Label(page2, text="Time left: 10s", font=("Helvetica", 16))
    timer_label.pack(pady=40)

    tk.Button(page2, text="Back", command=lambda: show_frame(page1)).pack()

def show_frame(frame):
    frame.tkraise()

def start_timer():
    global time_left
    time_left = 1500
    update_timer()
    show_frame(page2)

def update_timer():
    global time_left
    if time_left >= 0:
        minutes, seconds = divmod(time_left, 60)
        timer_label.config(text=f"Time left: {minutes:02d}:{seconds:02d}")
        time_left -= 1
        root.after(1000, update_timer)
    else:
        timer_label.config(text="Time's up!")
