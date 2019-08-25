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
for file in os.listdir(directory_path): # is directory_path needed to be put here when you used chdir?
    mo = date_pattern.search(file)
    if mo != None:
      # TODO: write it like how it was written in autoamte (non-hard-coded variables for the parts of the date).
      # TODO: see how automate's code make it more readable when it's not just random and it's not hardcoded.

      # Different parts of the filename.
      before_part = mo.group(1)
      month_part = mo.group(2)
      day_part = mo.group(4)
      year_part = mo.group(6)
      after_part = mo.group(8)

      # Form the Europoean-style filename.
      new_date = before_part + day_part + "-" + month_part + "-" + year_part + after_part

      # Rename the file
      shutil.move(file, new_date ) 


# George Hotz: "Yeah, that looks fun."
# Keyboard shortcuts: 
# ctrl + g (line number)        
# ctrl + tab to switch between recent tabs
# always save before running, coderunner saves slow.

# TODO: try to do the problem yourself first before looking at the solution.
