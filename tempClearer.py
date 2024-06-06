import os

from directoryCleaner import clear_directory, prefix

print(f"{prefix} Script successfully initialized.")

# Getting the Windows user path
current_user_dir = os.path.expanduser("~")
app_data_temp_dir = rf"{current_user_dir}\AppData\Local\Temp"
windows_temp_dir = r"C:\Windows\Temp"

print(f"""
{prefix} AppData temp directory: {app_data_temp_dir}
{prefix} Windows temp directory: {windows_temp_dir}
""")

clear_directory(app_data_temp_dir)
clear_directory(windows_temp_dir)
