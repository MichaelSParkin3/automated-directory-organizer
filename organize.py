import os
from pathlib import Path

# Function to organize files in a directory
# It creates folders for images, videos, documents, audio, archives, code, and other files
def organizeDirectory(directory: Path):
    if not directory.exists():
        print("Directory does not exist.")
        return
    else:
        print("Directory exists.")
        # Create folders for images
        images_folder = directory / "Images"
        images_folder.mkdir(exist_ok=True)
  
        # Create folders for videos
        videos_folder = directory / "Videos"
        videos_folder.mkdir(exist_ok=True)
        
        # Create folders for documents
        documents_folder = directory / "Documents"
        documents_folder.mkdir(exist_ok=True)
        
        # Create folders for audio
        audio_folder = directory / "Audio"
        audio_folder.mkdir(exist_ok=True)
        
        # Create folders for archives
        archives_folder = directory / "Archives"
        archives_folder.mkdir(exist_ok=True)
        
        # Create folders for code
        code_folder = directory / "Code"
        code_folder.mkdir(exist_ok=True)
        
        # Create folders for other files
        other_folder = directory / "Other"
        other_folder.mkdir(exist_ok=True)
        
        for file in directory.iterdir():
            if file.is_file():
                match file.suffix.lower():
                    # Images
                    case ".jpg" | ".jpeg" | ".png" | ".gif" | ".bmp" | ".tiff" | ".svg":
                        #move to images folder
                        file.rename(images_folder / file.name)
                    # Videos
                    case ".mp4" | ".mkv" | ".avi" | ".mov" | ".flv" | ".wmv":
                        #move to videos folder
                        file.rename(videos_folder / file.name)
                    # Documents
                    case ".pdf" | ".doc" | ".docx" | ".txt" | ".xls" | ".xlsx" | ".ppt" | ".pptx":
                        #move to documents folder
                        file.rename(documents_folder / file.name)
                    # Audio
                    case ".mp3" | ".wav" | ".aac" | ".flac" | ".ogg":
                        #move to audio folder
                        file.rename(audio_folder / file.name)
                    # Archives
                    case ".zip" | ".rar" | ".tar" | ".gz" | ".7z":
                        #move to archives folder
                        file.rename(archives_folder / file.name)
                    # Code
                    case ".py" | ".js" | ".java" | ".c" | ".cpp" | ".html" | ".css":
                        #move to code folder
                        file.rename(code_folder / file.name)
                    # Other files
                    case _:
                        #move to other folder
                        file.rename(other_folder / file.name)
                    # end match
        # end for
        print("Files organized successfully.")
        return True


#input directory 
directoryInput = Path(input("Enter the directory to organize: "))

organizeDirectory(directoryInput)
