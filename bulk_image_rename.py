import os
import sys

venv_path = os.path.join(".venv", "Lib", "site-packages")
sys.path.insert(0, venv_path)
import exifread


def rename_file(option: str, directory_str: str, filename_str: str, tags: dict) -> str:
    """
    Renames an image file using its EXIF tags. If desired EXIF data not found, this function will not rename the image file.

    Params:
        option (str): String representing the EXIF tags to use. Either "Original", "Digitized", or "Modified".
        directory_str (str): Filepath to directory of images.
        filename_str (str): Name of file we are attempting to rename.
        tags (dict): Dictionary of EXIF data from file generated using exifread.

    Returns:
        str: New filename, or old filename if unchanged.
    """

    datetime = ""

    match option:

        case "Original":
            datetime = tags.get("EXIF DateTimeOriginal", "")
            mili = tags.get("EXIF SubSecTimeOriginal", "")

        case "Digitized":
            datetime = tags.get("EXIF DateTimeDigitized", "")
            mili = tags.get("EXIF SubSecTimeDigitized", "")

        case "Modified":
            datetime = tags.get("Image DateTime", "")
            mili = tags.get("EXIF SubSecTime", "")
    
    datetime_str = str(datetime)
    if datetime_str != "":
        
        date, time = datetime_str.split(" ")
        date_list = date.split(":")
        time_list = time.split(":")
        year = date_list[0]
        month = date_list[1]
        day = date_list[2]
        hour = time_list[0]
        min = time_list[1]
        sec = time_list[2]

        file_extension = filename_str.split(".")[-1]
        old_filepath_str = os.path.join(directory_str, filename_str)
        new_filename_str = f"IMG_{year}{month}{day}_{hour}{min}{sec}{mili}.{file_extension}"
        new_filepath_str = os.path.join(directory_str, new_filename_str)
        os.rename(old_filepath_str, new_filepath_str)

        return new_filename_str
    
    return filename_str

def main():
    
    while True:

        directory_str = input("Enter absolute filepath to target directory: ")

        print("Choose DateTime tag: ")
        print("1 - DateTimeOriginal (default)")
        print("2 - DateTimeDigitized (CreateDate)")
        print("3 - DateTime (ModifyDate)")
        print("q - Quit")
        user_choice = input("Select DateTime tag option: ")
        if user_choice == "1" or user_choice == "":
            user_choice = "Original"
        elif user_choice == "2":
            user_choice = "Digitized"
        elif user_choice == "3":
            user_choice = "Modified"
        elif user_choice.lower() in ['q', 'quit']:
            break

        cache_dict = {}

        for filename_str in os.listdir(directory_str):

            filepath_str = os.path.join(directory_str, filename_str)

            if filepath_str.lower().endswith(('.tiff', '.jpg', '.jpeg', '.png', '.webp', 'heic')):
                
                tags = {}
                with open(filepath_str, "rb") as file_handle:
                    tags = exifread.process_file(file_handle, details=False)

                new_filename = rename_file(user_choice, directory_str, filename_str, tags)
                cache_dict[new_filename] = filename_str

        print("Done!")

        user_choice = input("Hit enter to finalize new filenames or type UNDO: ")
        if user_choice.lower() == "undo":
            for new_filename_str, old_filename_str in cache_dict.items():
                new_filepath_str = os.path.join(directory_str, new_filename_str)
                old_filepath_str = os.path.join(directory_str, old_filename_str)
                os.rename(new_filepath_str, old_filepath_str)

        user_choice = input("Would you like to run this script on another directory (Y/n)? ")
        if user_choice.lower() not in ["", "y", "yes"]:
            break

if __name__ == "__main__":
    main()