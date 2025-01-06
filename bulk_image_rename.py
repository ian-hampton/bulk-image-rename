import os

import exifread


while True:

    directory_str = input("Enter absolute filepath to the target directory: ")

    for filename_str in os.listdir(directory_str):

        filepath = os.path.join(directory_str, filename_str)

        if filepath.lower().endswith(('.tiff', '.jpg', '.jpeg', '.png', '.webp', 'heic')):
            
            tags = {}
            with open(filepath, "rb") as file_handle:
                tags = exifread.process_file(file_handle, details=False)

            print(filename_str)
            print(f"{tags["EXIF DateTimeOriginal"]} - {tags["EXIF SubSecTimeOriginal"]}")
            print(f"{tags["EXIF DateTimeDigitized"]} - {tags["EXIF SubSecTimeDigitized"]}")
            print(f"{tags["Image DateTime"]} - {tags["EXIF SubSecTime"]}")

    print("Done!")

    user_choice = input("Would you like to run this script on another directory (Y/n)? ")
    if user_choice.strip().lower() not in ["", "y", "yes"]:
        break