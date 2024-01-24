import os

# Function to rename images in a folder
def rename_images(folder_path):
    """this function renames the images in the dataset to [name of the folder/actual age]_[id in the folder].[ext]
    which makes it easy to easily use the picture later.
    This file should be placed next to train/test folders and the path should be changed accordingly.

    Args:
        folder_path (string): path to the folder with subfolders sorted in a way to be used in ktrain img prediction. More on that here: https://amaiya.github.io/ktrain/vision/index.html
    """
    # Get all subfolders in the given folder
    subfolders = [f.path for f in os.scandir(folder_path) if f.is_dir()]

    for folder in subfolders:
        folder_name = os.path.basename(folder)
        image_files = [f.path for f in os.scandir(folder) if f.is_file() and f.name.endswith(('.jpg', '.jpeg', '.png', '.gif'))]

        for i, image_file in enumerate(image_files):
            new_name = f"{folder_name}_{i+1}.jpg"  # Change the file extension to match the actual image file format
            new_path = os.path.join(folder, new_name)
            os.rename(image_file, new_path)

# Example usage: Provide the path of the folder containing subfolders with images
folder_path = "train"
rename_images(folder_path)
