import os
from pathlib import Path
import argparse

# A dictionary that maps folder names to file extensions.
# This is used to determine which folder a file should be moved to.
dict_file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".flv", ".wmv"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Code": [".py", ".js", ".java", ".c", ".cpp", ".html", ".css"],
    "Other": [],
}


# Flatten the dict_file_types dictionary to create a mapping from file extension to folder name.
# This makes it easier to look up the folder name for a given file extension.
flat_file_types = {}
for folder, extensions in dict_file_types.items():
    for extension in extensions:
        flat_file_types[extension] = folder


def main():
    """
    Organizes files in a specified directory by moving them into subdirectories
    based on their file extension.
    """
    # Create an ArgumentParser object to handle command-line arguments.
    parser = argparse.ArgumentParser(
        description="Organize files in a directory based on their extension."
    )

    # Add an argument to the parser
    # This tells the ArgumentParser what command-line arguments to expect.
    parser.add_argument("directory", help="The directory to organize")

    # Parse the arguments
    # This will take the arguments passed to the script (e.g., 'python organize.py /path/to/directory')
    # and return an object with the argument values.
    args = parser.parse_args()

    # Get the directory path from the command-line arguments.
    directoryInput = Path(args.directory)

    # Get a list of all files in the specified directory.
    files = [f for f in directoryInput.iterdir() if f.is_file()]

    # Iterate over each file and move it to the appropriate folder.
    for file in files:
        try:
            # Skip hidden files (those starting with a dot).
            if file.name.startswith("."):
                print(f"Skipping hidden file: {file.name}")
                continue

            print("Organizing file: " + file.name)

            # Get the folder name for the file's extension, defaulting to "Other".
            folderName = flat_file_types.get(file.suffix.lower(), "Other")

            # Create the destination folder if it doesn't already exist.
            destination_folder = directoryInput / folderName
            if not destination_folder.exists():
                destination_folder.mkdir()

            # Move the file to the destination folder.
            file.rename(destination_folder / file.name)
        except OSError as e:
            print(f"Error processing {file.name}: {e}")
        except PermissionError as e:
            print(f"Permission error for {file.name}: {e}")
        except FileNotFoundError as e:
            print(f"File not found error for {file.name}: {e}")
        except IsADirectoryError as e:
            print(f"Expected a file but found a directory: {file.name}. Error: {e}")
        except NotADirectoryError as e:
            print(f"Expected a directory but found a file: {file.name}. Error: {e}")
        except ValueError as e:
            print(f"Value error for {file.name}: {e}")
        except TypeError as e:
            print(f"Type error for {file.name}: {e}")
        except KeyError as e:
            print(f"Key error for {file.name}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred while processing {file.name}: {e}")

    print(f"Organization complete.")


if __name__ == "__main__":
    # This block ensures that the main() function is called only when the script is executed directly.
    main()
