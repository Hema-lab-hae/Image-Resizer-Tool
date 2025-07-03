# 🖼️ Batch Image Resizer & Converter

A simple Python script to **resize** and **convert** images in bulk using the [Pillow](https://python-pillow.org/) library.

## ✨ Features
- Resize all images in a folder to a fixed width and height.
- Convert images to a specified format (e.g., PNG, JPEG).
- Automatically creates output folder if it doesn't exist.
- Supports multiple input formats: `.jpg`, `.jpeg`, `.png`, `.webp`, `.bmp`, `.gif`.
- 
- ## 📁 Folder Structure
project-root/
│
├── main.py # The script
├── README.md # This file
├── input_images/ # Place your original images here
└── output_images/ # Processed images will be saved here

yaml
Copy
Edit
## ⚙️ Requirements

- Python 3.x
- Pillow library

Install Pillow with:
bash
pip install pillow

 How to Use
Place all images you want to process inside the input_images folder.
Run the script:

Error Handling
If the input folder is missing, the script will notify and exit.

Non-image files are automatically skipped.

Handles color mode conversion when saving as JPEG.

📌 Example Output
Input: cat.png (1920x1080)

Output: cat.jpeg (800x600)

 Future Ideas
Preserve aspect ratio

Command-line arguments for folders, size, and format

Progress bar or GUI

