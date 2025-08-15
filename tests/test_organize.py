import pytest
from pathlib import Path
import sys
import os

# Add the parent directory to the sys.path to allow imports from the root folder
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from organize import organize_directory


def test_maps_extensions_correctly(tmp_path):
    # Create some dummy files
    (tmp_path / "image.jpg").touch()
    (tmp_path / "document.pdf").touch()
    (tmp_path / "archive.zip").touch()
    (tmp_path / "other.xyz").touch()

    # Run the organization script
    organize_directory(tmp_path)

    # Check that the files were moved to the correct folders
    assert (tmp_path / "Images" / "image.jpg").exists()
    assert (tmp_path / "Documents" / "document.pdf").exists()
    assert (tmp_path / "Archives" / "archive.zip").exists()
    assert (tmp_path / "Other" / "other.xyz").exists()


def test_ignores_target_dirs(tmp_path):
    # Create a dummy file and a directory with the same name as a target folder
    (tmp_path / "image.jpg").touch()
    (tmp_path / "Images").mkdir()

    # Run the organization script
    organize_directory(tmp_path)

    # Check that the file was moved, but the directory was ignored
    assert (tmp_path / "Images" / "image.jpg").exists()


def test_duplicate_name_handling_works(tmp_path):
    # Create two files with the same name
    (tmp_path / "image.jpg").touch()
    (tmp_path / "Images").mkdir()
    (tmp_path / "Images" / "image.jpg").touch()

    # Run the organization script
    organize_directory(tmp_path)

    # Check that the second file was renamed
    assert (tmp_path / "Images" / "image_1.jpg").exists()
