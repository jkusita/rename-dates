# rename-dates.py - Renames filenames with American MM-DD-YYYY date format to European DD-MM-YYYY.

import shutil, os, re

# Directory of the folder containing the files.
directory_path = ("/Users/ramteechua/Desktop/rename-dates-folder")

# Creates a regex that matches files with the American date format.
date_pattern = re.compile(r"""
    ^(.*?)                           # all text before the date
    ((0|1)?\d)-                     # one or two digits for the month
    ((0|1|2|3)?\d)-                 # one or two digits for the day
    ((19|20)\d\d)                   # four digits for the year
    (.*?)$                          # all text after the date
     """, re.VERBOSE)

os.chdir(directory_path)

# Looks for files that matches the regex inside the folder and changes the name of the file.
for file in os.listdir(directory_path):
    mo = date_pattern.search(file)
    if mo != None:
      # Arranged to (text)DD/MM/YY(text)
      new_date = mo.group(1) + mo.group(4) + "-" + mo.group(2) + "-" + mo.group(6) + mo.group(8)
      shutil.move(file, new_date ) 


# George Hotz: "Yeah, that looks fun."
# Keyboard shortcuts: 
# ctrl + g (line number)        
# ctrl + tab to switch between recent tabs
# always save before running, coderunner saves slow.

# TODO: try to do the problem yourself first before looking at the solution.
