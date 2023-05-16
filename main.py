import os
import pathlib
import shutil

# Get the path for the current directory


def current_directory():
    return os.getcwd()


# Get the file extension

def get_file_ext(file_name):
    extension = pathlib.Path(file_name).suffix
    return extension.replace(".", "")


# File formats

file_format = {
    "pdf": "PDF",
    "png": "Image",
    "jpg": "Images",
    "jpeg": "Images",
    "gif": "Images",
    "doc": "Docs",
    "docx": "Docs",
    "txt": "Docs",
    "cvs": "Data",
    "xlsx": "Data",
    "zip": "Archived",
    "rar": "Archived",
    "tar": "Archived",
    "gz": "Archived",
    "mpv": "Video",
    "mp4": "Video",
    "flv": "Video",
    "avi": "Video",
    "mp3": "Music",
}


directory_content = os.listdir(current_directory())


for file in directory_content:
    if os.path.isfile(file):
        file_ext = get_file_ext(file)
        for key, value in file_format.items():
            if key == file_ext:
                try:
                     os.mkdir(value)
                except FileExistsError():
                    pass
                finally:
                    shutil.move(file, f"{value}/{file}")

        