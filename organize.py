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
        print("Organizing file: " + file)
        if file.suffix.lower() in dict_file_types["Images"]:
            if not (directoryInput / "Images").exists():
                (directoryInput / "Images").mkdir()
            file.rename(directoryInput / "Images" / file.name)
        elif file.suffix.lower() in dict_file_types["Videos"]:
            if not (directoryInput / "Videos").exists():
                (directoryInput / "Videos").mkdir()
            file.rename(directoryInput / "Videos" / file.name)
        elif file.suffix.lower() in dict_file_types["Documents"]:
            if not (directoryInput / "Documents").exists():
                (directoryInput / "Documents").mkdir()
            file.rename(directoryInput / "Documents" / file.name)
        elif file.suffix.lower() in dict_file_types["Audio"]:
            if not (directoryInput / "Audio").exists():
                (directoryInput / "Audio").mkdir()
            file.rename(directoryInput / "Audio" / file.name)
        elif file.suffix.lower() in dict_file_types["Archives"]:
            if not (directoryInput / "Archives").exists():
                (directoryInput / "Archives").mkdir()
            file.rename(directoryInput / "Archives" / file.name)
        elif file.suffix.lower() in dict_file_types["Code"]:
            if not (directoryInput / "Code").exists():
                (directoryInput / "Code").mkdir()
            file.rename(directoryInput / "Code" / file.name)
        else:
            if not (directoryInput / "Other").exists():
                (directoryInput / "Other").mkdir()
            file.rename(directoryInput / "Other" / file.name)

if __name__ == "__main__":
    main()
