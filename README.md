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

1.  Run the `organize.py` script from your terminal:
    ```bash
    python organize.py
    ```
2.  When prompted, enter the full path to the directory you want to organize:
    ```
    Enter the directory to organize: /path/to/your/folder
    ```
3.  The script will create the necessary subfolders and move the files accordingly.

## File Organization

The script organizes files into the following categories:

- **Images:** `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tiff`, `.svg`
- **Videos:** `.mp4`, `.mkv`, `.avi`, `.mov`, `.flv`, `.wmv`
- **Documents:** `.pdf`, `.doc`, `.docx`, `.txt`, `.xls`, `.xlsx`, `.ppt`, `.pptx`
- **Audio:** `.mp3`, `.wav`, `.aac`, `.flac`, `.ogg`
- **Archives:** `.zip`, `.rar`, `.tar`, `.gz`, `.7z`
- **Code:** `.py`, `.js`, `.java`, `.c`, `.cpp`, `.html`, `.css`
- **Other:** Any other file types not listed above.
