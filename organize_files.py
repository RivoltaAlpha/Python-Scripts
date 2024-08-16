import os
import shutil

def organize_files(folder_path):
    extensions = {
        'images': ['jpg', 'jpeg', 'png', 'gif'],
        'documents': ['pdf', 'docx', 'txt'],
        'videos': ['mp4', 'mov'],
    }

    for filename in os.listdir(folder_path):
        file_ext = filename.split('.')[-1]
        for category, ext_list in extensions.items():
            if file_ext in ext_list:
                new_folder = os.path.join(folder_path, category)
                if not os.path.exists(new_folder):
                    os.makedirs(new_folder)
                shutil.move(os.path.join(folder_path, filename), new_folder)

organize_files('/path/to/your/folder')
