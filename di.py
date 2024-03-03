import os
import hashlib
import pandas as pd
from pathlib import Path
# import tkinter as tk
# from tkinter import filedialog


def find_duplicates(start_path):
    file_list = os.walk(start_path)
    unique = dict()
    duplicateimages = dict()

    for root, folders, files in file_list:
        for file in files:
            if file.endswith(".jpg" or file.endswith(".png")):
                path = Path(os.path.join(root, file))
                fileHash = hashlib.md5(open(path, 'rb').read()).hexdigest()
                if fileHash not in unique:
                    unique[fileHash] = [(path, os.path.getctime(path))]
                else:
                    original_path, original_time = unique[fileHash][0]
                    duplicate_time = os.path.getctime(path)
                    unique[fileHash].append((path, duplicate_time))
                    if duplicate_time < original_time:
                        duplicateimages.setdefault(fileHash, []).append((path, original_path))
                    else:
                        duplicateimages.setdefault(fileHash, []).append((original_path, path))

    return duplicateimages


def main():
    # root = tk.Tk()
    # root.withdraw()
    # path = filedialog.askdirectory(title="Select Directory")
    path = os.getcwd()
    duplicate_images = find_duplicates(path)
    duplicates_data = []

    if duplicate_images:
        for hash_value, paths_list in duplicate_images.items():
            for original_path, duplicate_path in paths_list:
                duplicates_data.append({
                    'Original': f"![](https://raw.githubusercontent.com/kent-map/main{original_path})".replace(
                        "/workspaces", "").replace("/main/images/", "/images/main/"),
                    'Duplicate': f"![](https://raw.githubusercontent.com/kent-map/main{duplicate_path})".replace(
                        "/workspaces", "").replace("/main/images/", "/images/main/")
                })

        df = pd.DataFrame(duplicates_data)

        df.to_csv("DuplicateImages.csv", index=False)
    else:
        print("No duplicate images found.")


if __name__ == "__main__":
    main()
