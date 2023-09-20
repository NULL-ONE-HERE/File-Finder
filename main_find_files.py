import os
import time

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
        for root, dirs, files in os.walk('/'):
            walks.append(root)  # Add the current directory to the walks list

            if target_file in files:
                return os.path.join(root, target_file)

        return None
    except Exception as e:
        print("An error occurred:", str(e))
        return None

try:
    # Prompt the user for the directory to search in and the target file name
    file_name = input("Enter the target file name: ")

    # Create an empty list to keep track of directory walks
    walks = []

    # Display a message to the user showing that the program is running
    print("Searching for file...")

    # Call the search_file function, passing the walks list
    result = search_file(file_name, walks)

    # Start measuring runtime
    timer(search_file)
    
    # Check the result
    if result:
        print("File found at:", result)
    else:
        print("File not found.")

except Exception as e:
    print("An error occurred:", str(e))
