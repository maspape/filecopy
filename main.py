import os
import shutil
import tkinter as tk
from tkinter import filedialog

def copy_files_with_suffix_or_prefix(source_folder, destination_folder, suffix=None, prefix=None):
    for root, dirs, files in os.walk(source_folder):
        for filename in files:
            source_path = os.path.join(root, filename)
            base_name, file_extension = os.path.splitext(filename)

            if suffix:
                new_filename = f"{base_name}{suffix}{file_extension}"
            elif prefix:
                new_filename = f"{prefix}{base_name}{file_extension}"
            else:
                new_filename = filename

            destination_path = os.path.join(destination_folder, new_filename)

            shutil.copy(source_path, destination_path)

def browse_source_folder():
    source_folder = filedialog.askdirectory()
    source_folder_entry.delete(0, tk.END)
    source_folder_entry.insert(0, source_folder)

def browse_destination_folder():
    destination_folder = filedialog.askdirectory()
    destination_folder_entry.delete(0, tk.END)
    destination_folder_entry.insert(0, destination_folder)

def copy_files():
    source_folder = source_folder_entry.get()
    destination_folder = destination_folder_entry.get()
    suffix = suffix_entry.get()
    prefix = prefix_entry.get()
    
    if source_folder and destination_folder:
        copy_files_with_suffix_or_prefix(source_folder, destination_folder, suffix, prefix)
        result_label.config(text="Files copied successfully.")
    else:
        result_label.config(text="Please select source and destination folders.")

# Create the main application window
app = tk.Tk()
app.title("File Copy App")

# Source Folder
source_label = tk.Label(app, text="Source Folder:")
source_label.pack()
source_folder_entry = tk.Entry(app)
source_folder_entry.pack()
browse_source_button = tk.Button(app, text="Browse", command=browse_source_folder)
browse_source_button.pack()

# Destination Folder
destination_label = tk.Label(app, text="Destination Folder:")
destination_label.pack()
destination_folder_entry = tk.Entry(app)
destination_folder_entry.pack()
browse_destination_button = tk.Button(app, text="Browse", command=browse_destination_folder)
browse_destination_button.pack()

# Suffix
suffix_label = tk.Label(app, text="Suffix:")
suffix_label.pack()
suffix_entry = tk.Entry(app)
suffix_entry.pack()

# Prefix
prefix_label = tk.Label(app, text="Prefix:")
prefix_label.pack()
prefix_entry = tk.Entry(app)
prefix_entry.pack()

# Copy Button
copy_button = tk.Button(app, text="Copy Files", command=copy_files)
copy_button.pack()

# Result Label
result_label = tk.Label(app, text="")
result_label.pack()

app.mainloop()
