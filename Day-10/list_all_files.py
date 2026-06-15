import os

folders = input("Please provide folder names with some spaces between them: ").split()

for folder in folders:
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print(f"Folder does not exists: {folder}")
    else:
        print(f"=== Printing files in the folder {folder} ===")
        
        for file in files:
            print(file)