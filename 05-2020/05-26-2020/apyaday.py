"""
Creates an automatic directory for the APyADay challenge.
Typical terminal command looks like:
> python3 apyaday.py default lesson.py
"""

import subprocess
import sys
import errno
import os
from datetime import datetime

# Args passed from terminal
template_arg = sys.argv[1]
filename_arg = sys.argv[2]

# Folder and file paths
env_path = os.getenv('XDG_APYADAY_HOME')
dated_dirs_path = datetime.now().strftime('/%m-%Y/%m-%d-%Y/')
folder_path = env_path + dated_dirs_path
file_path = folder_path + filename_arg

# Shell command to call editor
shell_command = os.environ.get('EDITOR', 'vim') + ' ' + file_path

# Templates
D_TEMPLATE = """\"\"\"
file_docstring_here
\"\"\"
"""


def file_creation(template=template_arg, filename=filename_arg):
    """file_creation.
    Args are passed through terminal command when called.

    Args:
        template: Which template to use for the new file.
        filename: What the file name will be.
    """

    try:
        os.makedirs(folder_path)
    except OSError as error:
        if error.errno != errno.EEXIST:
            raise
    with open(os.path.join(folder_path, filename), 'w') as apyaday_entry:
        if template_arg == "default":
            template = D_TEMPLATE
        apyaday_entry.writelines(template)


def open_file():
    """open_file.
    Gives the user the choice to open the newly created file with Vim.
    """
    if NEW_FILE:
        open_option = input("Do you want to open this file? (y/n): ")

    if not NEW_FILE or (open_option == 'y'):
        subprocess.call(shell_command, shell=True)


if __name__ == "__main__":
    # checks if file exists
    if not os.path.isfile(file_path):
        file_creation()
        NEW_FILE = True
        open_file()
    # if file exists already, skips write and opens
    else:
        NEW_FILE = False
        open_file()
