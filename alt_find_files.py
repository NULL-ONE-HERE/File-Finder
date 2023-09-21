import os
import time
import tkinter as tk
from tkinter import Entry, Button, Label

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        
        print("Runtime:", end_time - start_time)
        return result
    return wrapper

@timer
def search_file(target_file, walks):
    try:
        for root, dirs, files in os.walk('\\'):
            walks.append(root)  # Add the current directory to the walks list

            if target_file in files:
                return os.path.join(root, target_file)

        return None
    except Exception as e:
        print("An error occurred:", str(e))
        return None

def search():
    file_name = file_name_entry.get()
    if file_name:
        result = search_file(file_name, walks)
        if result:
            result_label.config(text=f"File found at: {result}")
        else:
            result_label.config(text="File not found.")
    else:
        result_label.config(text="Please enter a file name.")

# Create the main application window
root = tk.Tk()
root.title("File Search")

# Create an entry field for typing the file name
file_name_entry = Entry(root, width=30)
file_name_entry.pack(pady=10)

# Create a Search button to initiate the search
search_button = Button(root, text="Search", command=search)
search_button.pack()

# Create a label for displaying the search result
result_label = Label(root, text="")
result_label.pack()

# Create an empty list to keep track of directory walks
walks = []

root.mainloop()
