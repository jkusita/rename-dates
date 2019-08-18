# rename-dates.py - Renames filenames with American MM-DD-YYYY date format to European DD-MM-YYYY.

# sys is just for testing.
import shutil, os, re, sys

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

# # Looks for file in directory.
# for file in os.listdir(directory_path):
#     mo = date_pattern.search(file)
#     if mo != None:
#         # TODO: what am I renaming it to?
#         # TODO: rename using the mo.group()
#         os.rename(file, )

for file in os.listdir(directory_path):
    mo = date_pattern.search(file)
    if mo != None:
        # Set to DD/MM/YY
        new_date = mo.group(4) + "-" + mo.group(2) + "-" + mo.group(6)
        
        # Left here: find out a way to change the file name using shutil.move()?
        shutil.move(file, new_date )

        # TODO: try it when there are text in the stara nd the end?
        # TODO: reserach spotify family problem.
        # TODO: lazada mouse
# George Hotz: "Yeah, that looks fun."

        
# MM DD to DD MM

# For reference: 
# 07-12-2002
# ('', '07', '0', '12', '1', '2002', '20', '')
# 9-11-1 975
# ('', '9', None, '11', '1', '1975', '19', '')



# TODO: Loop over the files in the working directory.
# TODO: Get the different parts of the filename.
# TODO: Skip files without a date.
# TODO: Form the European-style filename.
# TODO: Get the full, absolute file paths.
# TODO: Rename the files.

# Different Style format:
# US: mm/dd/yyyy
# EU: dd/mm/yyyy

# Keyboard shortcuts: 
# ctrl + tab to switch between recent tabs
# always save before running, coderunner saves slow.

# TODO: try to do the problem yourself first before looking at the solution.
