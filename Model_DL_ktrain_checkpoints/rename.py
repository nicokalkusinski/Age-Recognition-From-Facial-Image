import os

folder_path = "weights"  # replace with the path to your folder

for filename in os.listdir(folder_path):
    if filename.startswith("weights-") and filename.endswith(".hdf5"):
        old_path = os.path.join(folder_path, filename)
        number = int(filename.split("-")[1].split(".")[0])
        new_number = number+66
        new_filename = "weights-{}.hdf5".format(new_number)
        new_path = os.path.join(folder_path, new_filename)
        os.rename(old_path, new_path)