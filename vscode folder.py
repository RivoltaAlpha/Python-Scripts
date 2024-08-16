import os
import subprocess

# Get user input for folder name
folder_name = input("Enter the name of the folder: ")

# Define the path to the Documents directory
documents_path = os.path.join(os.path.expanduser("~"), "Documents")

# Create the full path to the new folder
new_folder_path = os.path.join(documents_path, folder_name)

# Create the new folder
os.makedirs(new_folder_path, exist_ok=True)

# Open the new folder in VS Code
vscode_cmd_path = r"C:\Users\Tiff\AppData\Local\Programs\Microsoft VS Code\bin\code.cmd"
subprocess.run([vscode_cmd_path, new_folder_path])

print(f"Folder '{folder_name}' created and opened in VS Code.")

# To run this file you write Python in the terminal: python vscode folder.py