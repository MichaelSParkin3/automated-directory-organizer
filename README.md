# Automated Directory Organizer

This Python script automatically organizes files in a directory into categorized subfolders based on their file extension. It's a simple and effective way to clean up cluttered folders and maintain a structured file system.

## Demonstration

This script can turn a messy folder like this:

**BEFORE-messy-folder/**

```
├── Akkurat-Font.zip
├── FileZilla.exe
├── Meteor.svg
├── park-date.jpg
├── Shiny_Overlay.png
└── spanish-vocabulary.pdf
```

Into a clean and organized one:

**AFTER-clean-folder/**

```
├── Archives/
│   └── Akkurat-Font.zip
├── Documents/
│   └── spanish-vocabulary.pdf
├── Images/
│   ├── Meteor.svg
│   ├── park-date.jpg
│   └── Shiny_Overlay.png
└── Other/
    └── FileZilla.exe
```

## Usage

1.  Run the `organize.py` script from your terminal, providing the path to the directory you want to organize as a command-line argument:
    ```bash
    python organize.py /path/to/your/folder
    ```
2.  The script will create the necessary subfolders and move the files accordingly.

## Features

- **Automatic Categorization:** Files are sorted into folders based on their extension.
- **Duplicate File Handling:** If a file with the same name already exists in the destination folder, a number is appended to the new file's name to prevent overwriting.
- **Hidden File Skipping:** Hidden files (those starting with a `.`) are automatically skipped.
- **Error Handling:** The script includes error handling for common issues like permission errors, missing files, and directory-related conflicts.

## File Organization

The script organizes files into the following categories:

- **Images:** `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tiff`, `.svg`
- **Videos:** `.mp4`, `.mkv`, `.avi`, `.mov`, `.flv`, `.wmv`
- **Documents:** `.pdf`, `.doc`, `.docx`, `.txt`, `.xls`, `.xlsx`, `.ppt`, `.pptx`
- **Audio:** `.mp3`, `.wav`, `.aac`, `.flac`, `.ogg`
- **Archives:** `.zip`, `.rar`, `.tar`, `.gz`, `.7z`
- **Code:** `.py`, `.js`, `.java`, `.c`, `.cpp`, `.html`, `.css`
- **Other:** Any other file types not listed above.

## Testing

This project uses `pytest` for testing. To run the tests, follow these steps:

1.  Make sure you have `pytest` installed:
    ```bash
    pip install pytest
    ```
2.  Navigate to the project's root directory and run `pytest`:
    ```bash
    pytest
    ```
The tests will verify the script's core functionalities, including correct file mapping, handling of duplicate filenames, and ignoring target directories.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
