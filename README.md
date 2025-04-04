# Bulk Image Rename

This is a simple Python script that renames all images in a directory to the date/time they were created using their EXIF metadata.

Images are renamed to this format: IMG_yyyyMMdd_kkmmssSSS  
(see [SimpleDateFormat](https://docs.oracle.com/javase/7/docs/api/java/text/SimpleDateFormat.html) for reference)

### Example:
```
IMG_20250107_200904691.jpg
```
* Year: 2025
* Month: 01
* Day: 07
* Hours: 20
* Minutes: 09
* Seconds: 04
* Miliseconds: 691


## Features

* Rename files based on date created, date digitized, or date modified.
* Supports JPEG, PNG, TIFF, WebP, and HEIC files.
* Undo function.

## Installation and Use

For the sake of my sanity, this project makes use of the [exif-py](https://github.com/ianare/exif-py) module. As a result, you must set up a virtual enviroment.

1. Get into your directory of choice and clone the repo.
    ```sh
   git clone https://github.com/ian-hampton/bulk-image-rename.git
   ```

2. Open a terminal and cd into the root folder of your local repo. Create the virtual enviroment.
    ```sh
    python -m venv .venv
    ```

3. Activate the virtual enviroment.
    ```sh
    .venv\Scripts\activate
    ```

4. Install project requirements.
    ```sh
    pip install -r requirements.txt
    ```

5. Once all this is done, the script can be run in your terminal:
    ```sh
    python bulk_image_rename.py
    ```
