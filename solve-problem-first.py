# My plan:

# TODO: make a regex that matches "test-folder- morethanoneintegershere"
# TODO: store all the file names in the folder in question in a list (first_list).
# TODO: grab from that list the file names that matches the regex into a new list (second_list)
# TODO: make another list (third_list) that has the new file names of the old files name where they have identical indicis.
# TODO: Change the old folder names into the new ones through their indices.
# TODO: replace the old folder names by getting their old filename from second_list and looking for the folder, once that folder is selected, change it with the new folder name, which is matched with the same index as the folder's name in the second_list, and replace it with the new folder name in the third_list

# Program that searches a folder that matches the user's regex for files/folders/etc  and replaces them.

import shutil, re, os, sys

# Path where the folder is located
directory_path  = ("/Users/ramteechua/Desktop/rename-dates-folder")

# Regex pattern that matches the files being sought out for.
name_regex = re.compile(r"test-file-\d+")


for file in os.listdir(directory_path):                             
    mo = name_regex.search(file)
    if mo != None:
      # TODO: change filename if mo != None.
      # TODO: how does os.rename work?
      os.rename("test")
      sys.exit()
      

