import os

target_dir = os.chdir("/home/mike/Desktop/Python/Test")
files = os.listdir(target_dir)

for file in files:
    file_new = file[::-1]
    os.rename(file, file_new)













