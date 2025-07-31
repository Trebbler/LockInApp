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
