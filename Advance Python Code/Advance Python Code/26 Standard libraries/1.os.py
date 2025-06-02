import os

# Get current working directory
cwd = os.getcwd()
print(f"Current working directory: {cwd}")

# List files in a directory
files = os.listdir(cwd)
print(f"Files in the current directory: {files}")

# Create a new directory
os.mkdir("new_folder")