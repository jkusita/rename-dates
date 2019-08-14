# Program that searches a folder that matches the user's regex for files/folders/etc  and replaces them.

import shutil, re, os, sys

# Path where the folder is located
directory_path  = ("/Users/ramteechua/Desktop/rename-dates-folder")

# Regex pattern that matches the files being sought out for.
name_regex = re.compile(r"test-file-\d+")

os.chdir(directory_path)

# Looks for file in directory.
for file in os.listdir(directory_path):                             
    mo = name_regex.search(file)
    if mo != None:
      os.rename(file, "renamed-burgers")
      

