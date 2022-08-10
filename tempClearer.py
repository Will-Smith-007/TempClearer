import os

from shutil import rmtree

prefix = "[TempClearer]"

print(f"{prefix} Das Skript wurde erfolgreich gestartet!")

# Gibt den Pfad des angemeldeten User zurück
current_user_dir = os.path.expanduser("~")
app_data_temp_dir = rf"{current_user_dir}\AppData\Local\Temp"
windows_temp_dir = r"C:\Windows\Temp"

print(f"""
{prefix} AppData Temp Ordner: {app_data_temp_dir}
{prefix} Windows Temp Ordner: {windows_temp_dir}
""")


def clear_app_data_temp():
    """
    Löscht alle Dateien im AppData Temp Ordner auf die Zugriff besteht.
    """
    with os.scandir(app_data_temp_dir) as entries:
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
                    pass  # Ignoriert den Fehler, wenn Datei von anderem Prozess genutzt wird u. skippt Datei.
            else:
                rmtree(entry_path, ignore_errors=True)
                deleted_files += 1
        print(f"{prefix} Es wurden {deleted_files} Dateien im temporären AppData Ordner gelöscht.")


def clear_windows_temp():
    """
    Löscht alle Dateien im Windows Temp Ordner auf die Zugriff besteht.
    """
    with os.scandir(windows_temp_dir) as entries:
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
                    pass  # Ignoriert den Fehler, wenn Datei von anderem Prozess genutzt wird u. skippt Datei.
            else:
                rmtree(entry_path, ignore_errors=True)
                deleted_files += 1
        print(f"{prefix} Es wurden {deleted_files} Dateien im temporären Windows Ordner gelöscht.")


clear_app_data_temp()
clear_windows_temp()
