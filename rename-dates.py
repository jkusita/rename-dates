# Searches for files in current directory and renaming the file's name containing dates in american-style into european-style.

# rename-dates.py - Renames filenames with American MM-DD-YYYY date format to European DD-MM-YYYY.

import shutil, os, re

# Create a regex that matches files with the American date format.

datePattern = re.compile(r"""
    ^(.*?)                           # all text before the date
    ((0|1)?\d)-                     # one or two digits for the month
    ((0|1|2|3)?\d)-                 # one or two digits for the day
    ((19|20)\d\d)                   # four digits for the year
    (.*?)$                          # all text after the date
     """, re.VERBOSE)

# TODO: Loop over the files in the working directory.
# TODO: Skip files without a date.
# TODO: Get the different parts of the filename.
# TODO: Form the European-style filename.
# TODO: Get the full, absolute file paths.
# TODO: Rename the files.

# Enter directory of the folder containing the files.
file_directory = ("test/path")

# Keyboard shortcuts: 
# ctrl + tab to switch between recent tabs
# always save before running, coderunner saves slow.

# TODO: try to do this project yourself first before looking at the solution.