import os
import shutil

# Specify the directory to organize
directory = os.getcwd() + '/file_organizer/files'

# Create a dictionary to hold the file extensions
file_extensions = {
    'pdf': 'PDFs',
    'png': 'Images',
    'jpg': 'Images',
    'jpeg': 'Images',
    'gif': 'Images',
    'doc': 'Documents',
    'docx': 'Documents',
    'txt': 'Documents',
    'csv': 'Data',
    'xlsx': 'Data',
    'zip': 'Archives',
    'rar': 'Archives',
    'exe': 'Executables',
    'mp3': 'Music',
    'wav': 'Music',
    'mp4': 'Videos',
    'avi': 'Videos',
    'flv': 'Videos',
    'wmv': 'Videos',
}


# Function to organize files based on extensions
def organize_files(directory):
    for filename in os.listdir(directory):
        # Skip directories
        if os.path.isdir(os.path.join(directory, filename)):
            continue

        # Get the file extension
        file_ext = filename.split('.')[-1].lower()

        # Determine the folder based on the file extension
        folder = file_extensions.get(file_ext)

        # If the file extension exists in the dictionary
        if folder:
            folder_path = os.path.join(directory, folder)

            # Create the folder if it doesn't exist
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            # Move the file to the corresponding folder
            shutil.move(os.path.join(directory, filename), os.path.join(folder_path, filename))


# Call the function to organize the files
organize_files(directory)
