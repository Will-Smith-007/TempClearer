import os

from shutil import rmtree

prefix = "[TempClearer]"


def clear_directory(directory: str):
    """
    Deletes all files and folders in a given directory.
    """
    with os.scandir(directory) as entries:
        deleted_files = 0
        for entry in entries:
            entry_path = entry.path
            if not os.access(entry_path, os.W_OK):
                continue
            if os.path.isfile(entry_path):
                try:
                    os.remove(entry_path)
                    deleted_files += 1
                except PermissionError:
                    pass  # Ignore an error that can occur if the script doesn't have write permissions on the file.
            else:
                rmtree(entry_path, ignore_errors=True)
                deleted_files += 1
        print(f"{prefix} Deleted {deleted_files} files and directories within {directory}.")
