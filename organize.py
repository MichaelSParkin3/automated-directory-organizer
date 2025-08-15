import os
from pathlib import Path
import argparse

dict_file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".flv", ".wmv"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Code": [".py", ".js", ".java", ".c", ".cpp", ".html", ".css"],
    "Other": []
    }


# Flatten dict_file_types to create a flat map dictionary
flat_file_types = {}
for folder, extensions in dict_file_types.items():
    for extension in extensions:
        flat_file_types[extension] = folder
    
def main():

    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description="Organize files in a directory based on their extension.")

    # Add an argument to the parser
    # This tells the ArgumentParser what command-line arguments to expect.
    parser.add_argument("directory", help="The directory to organize")

    # Parse the arguments
    # This will take the arguments passed to the script (e.g., 'python organize.py /path/to/directory')
    # and return an object with the argument values.
    args = parser.parse_args()

    # The directory is now accessed via args.directory
    directoryInput = Path(args.directory)

    #get every file in the directory
    files = [f for f in directoryInput.iterdir() if f.is_file()]

    # Create directories if they do not exist and move files accordingly
    for file in files:
        try:
            print("Organizing file: " + file.name)
            folderName = flat_file_types.get(file.suffix.lower(), "Other")
            # check if folder exists, if not create it
            if not (directoryInput / folderName).exists():
                #make folder with Pathlib
                (directoryInput / folderName).mkdir()
            #move file to folder
            file.rename(directoryInput / folderName / file.name)
        except OSError as e:
            print(f"Error processing {file.name}: {e}")

if __name__ == "__main__":
    main()
