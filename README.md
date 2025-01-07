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

* Supports JPEG, PNG, TIFF, WebP, and HEIC files.
* Rename files based on date created, date digitized, or date modified.


## Installation and Use

For my own sanity, this project makes use of the [exif-py](https://github.com/ianare/exif-py) module. As such, running this script requires a virtual enviroment.

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

5. To run this script, run this command in your terminal:
    ```sh
    python bulk_image_rename.py
    ```