import os

# Define the path to the directory
directory_path = 'path/dataset/trace'

# Get a list of files and directories in the specified path
files_and_directories = os.listdir(directory_path)

# Optionally, filter the list to include only files
files = [f for f in files_and_directories if os.path.isfile(os.path.join(directory_path, f))]

# Optionally, filter the list to include only directories
directories = [d for d in files_and_directories if os.path.isdir(os.path.join(directory_path, d))]

dirs = {}
for f in files:
    try:
        index = int(f.rsplit('.', 1)[1])
    except ValueError:
        continue
    dirs[index] = f

# Print the lists in sorted order
for index in sorted(dirs):
    print(f"'{directory_path + '/' + dirs[index]}',")
