import os
from PIL import Image

# === Configuration ===
input_folder = 'input_images'             # Folder containing original images
output_folder = 'output_images'           # Folder to save processed images
target_size = (800, 600)                  # Target size: (width, height)
output_format = 'JPEG'                    # Output format: 'JPEG', 'PNG', 'WEBP', etc.

# === Create output folder if it doesn't exist ===
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    print(f"Created output folder: {output_folder}")

# === Supported input file extensions ===
supported_extensions = ('.jpg', '.jpeg', '.png', '.webp', '.bmp', '.gif')

# === Process each image ===
for filename in os.listdir(input_folder):
    if filename.lower().endswith(supported_extensions):
        input_path = os.path.join(input_folder, filename)
        try:
            with Image.open(input_path) as img:
                # Resize the image
                resized_img = img.resize(target_size)

                # Generate new file name
                base_name = os.path.splitext(filename)[0]
                new_filename = f"{base_name}.{output_format.lower()}"
                output_path = os.path.join(output_folder, new_filename)

                # Convert to RGB if saving to JPEG (to avoid issues with PNG/transparency)
                if output_format.upper() == 'JPEG' and img.mode in ('RGBA', 'P'):
                    resized_img = resized_img.convert('RGB')

                # Save resized and converted image
                resized_img.save(output_path, output_format.upper())
                print(f"Saved: {output_path}")
        except Exception as e:
            print(f"Failed to process {filename}: {e}")

print("Batch image processing completed.")
