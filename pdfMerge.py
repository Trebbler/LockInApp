import tkinter as tk
from tkinter import filedialog
import PyPDF2
import os

root = None
page1 = None
page3 = None
status_label = None
selected_files = []

def init(shared_root, shared_page1):
    global root, page1, page3, status_label

    root = shared_root
    page1 = shared_page1

    page3 = tk.Frame(root)
    page3.grid(row=0, column=0, sticky="nsew")

    tk.Label(page3, text="PDF Merger").pack(pady=10)

    tk.Button(page3, text="Select PDFs", command=select_pdfs).pack(pady=5)

    tk.Button(page3, text="Merge PDFs", command=merge_pdfs).pack(pady=5)

    tk.Button(page3, text="Back", command=lambda: show_frame(page1)).pack(pady=5)

    status_label = tk.Label(page3, text="No files selected.")
    status_label.pack(pady=10)

def show_frame(frame):
    frame.tkraise()

def select_pdfs():
    global selected_files, status_label
    filetypes = [("PDF files", "*.pdf")]
    selected_files = filedialog.askopenfilenames(title="Select PDF files", filetypes=filetypes)
    if selected_files:
        status_label.config(text=f"{len(selected_files)} file(s) selected.")
    else:
        status_label.config(text="No files selected.")

def merge_pdfs():
    global selected_files, status_label
    if not selected_files:
        status_label.config(text="Please select PDF files first.")
        return

    merger = PyPDF2.PdfMerger()

    try:
        for file in selected_files:
            merger.append(file)

        output_filename = "combined.pdf"
        merger.write(output_filename)
        merger.close()

        status_label.config(text=f"Merged into '{output_filename}' successfully!")
    except Exception as e:
        status_label.config(text=f"Error: {e}")
