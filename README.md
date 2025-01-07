# Bulk Image Rename

This is a simple Python script that renames all images in a directory to the date/time they were created using their EXIF metadata.

Images are renamed to this format: IMG_yyyyMMdd_kkmmssSSS

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
   git clone https://github.com/ian-hampton/Bulk-Image-Rename.git
   ```

2. Open a terminal and cd into the root folder of your local repo. Create the virtual enviroment.
    ```sh
    python -m venv .venv
    ```

3. Activate your virtual enviroment.
    ```sh
    source .venv\Scripts\activate
    ```

4. Install project requirements.
    ```sh
    pip install -r requirements.txt
    ```

5. To run the script, run the following command in your terminal:
    ```sh
    python bulk_image_rename.py
    ```