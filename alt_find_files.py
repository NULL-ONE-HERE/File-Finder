import os
import tkinter as tk
import psutil  # Import the psutil library

# Create an empty list to keep track of directory walks
walks = []

def list_drives():
    # Use psutil to list all available drives
    drives = [d.device for d in psutil.disk_partitions()]
    return drives

def search_and_display_result(entry, label_result, drive_var):
    target_name = entry.get()
    selected_drive = drive_var.get()  # Get the selected drive from the variable

    if selected_drive == "All Drives":
        drives = list_drives()
    else:
        drives = [selected_drive]

    # Only search on the selected drive(s)
    walks.clear()  # Clear the previous walks
    result = None
    for drive in drives:
        result = search_item(target_name, drive)
        if result:
            break  # Stop searching if the item is found on any drive

    if result:
        label_result.config(text="Found at: " + result)
    else:
        label_result.config(text="Not found")

def display_result():
    # Create a new window
    window = tk.Tk()
    window.title("Result")

    # Set the window's size
    window.geometry("400x150")

    # Create text field to let the user enter a file/folder name
    entry = tk.Entry(window)
    entry.pack()

    # Create a label for drive selection
    label_drive = tk.Label(window, text="Select a drive:")
    label_drive.pack()

    # Create a variable to hold the selected drive
    drive_var = tk.StringVar(window)

    # Create a list of drive options, including "All Drives"
    drive_options = ["All Drives"] + list_drives()

    # Create a dropdown menu for drive selection
    drive_dropdown = tk.OptionMenu(window, drive_var, *drive_options)
    drive_dropdown.pack()

    # Create a button to call the search function and add it to the window
    button = tk.Button(window, text="Search", command=lambda: search_and_display_result(entry, label_result, drive_var))
    button.pack()

    # Create a label for displaying the search result
    label_result = tk.Label(window, text="")
    label_result.pack()

    # Create a button to close the window
    close_button = tk.Button(window, text="Close", command=window.destroy)
    close_button.pack()

    # Start the window's event loop
    window.mainloop()

def search_item(target_name, selected_drive):
    try:
        for root, dirs, files in os.walk(selected_drive):
            walks.append(root)  # Add the current directory to the walks list

            # Check for the target name in both files and dirs
            if target_name in files or target_name in dirs:
                return os.path.join(root, target_name)

        return None
    except Exception as e:
        print("An error occurred:", str(e))
        return None

def main():
    try:
        display_result()
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    main()
