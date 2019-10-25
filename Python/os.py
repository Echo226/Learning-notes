'''
    OS Module: Allow us to interact with the underlying operating system.
'''

import os
from datetime import datetime

# Show all the methods we can get access to when work with new module.
print(dir(os))

# Get current working directory
os.getcwd()

# Navigate to a new location on the file system
os.chdir()
os.chdir('/Users/xting/Desktop/')

# Show files and folders in a directory
os.listdir()    # by default: current working directory
os.listdir('/Users/xting/Desktop')  # can pass a path into it

# Create a new folder
os.mkdir('Learning-notes')             # cannot create a deep directory
os.makedirs('Learning-notes/Python')   # create a deep directory, create the intermedia directory automatically

# Delete folders
os.rmdir('Learning-notes/Python')      # prefer! will not remove the intermedia directory
os.removedirs('Learning-notes/Python') # will remove the intermedia directory

# Rename a file or folder
os.rename('os_old.py', 'os.py')

# Look at some info of the file
os.stat('os.py')
os.stat('os.py').st_size        # size of the file
os.stat('os.py').st_mtime       # the last modification time in a timestamp format
datetime.fromtimestamp(os.stat('os.py').st_mtime). # change timestamp to datetime

# See the entire directory tree
os.walk()   # A generator yields a tuple with three values as it walks
for dirpath, dirname, filenames in os.walk('/Users/xting/Desktop/'):
	print('Current Path: ', dirpath)
	print('Directories: ', dirnames)
	print('Files: ', filenames)
	print(' ')

# Access the Home directory location by grabbing the Home environment variable
os.environ.get('Home')  # print out '/Users/xting'



'''
    os.path Module: has lots of methods working with path.
'''

print(dir(os.path))

# Combine a path with a file name
# file_path = os.environ.get('Home') + 'os.py' not working since it forgets the '/', other methods might double the '/'
os.path.join(a, b)
os.path.join(os.environ.get('Home'), 'os.py')

# Get the filename/dirname
os.path.basename('/tem/os.py')   # get the filename: op.py
os.path.dirname('/tem/os.py')    # get the directory name: /tem
os.path.split('/tem/os.py')      # get both filename and dirname: ('/tem', 'os.py')
os.path.exists('/tem/os.py')     # Check if a path exists: False
os.path.isdir('/tem/os.py')      # Check if it is a directory: False
os.path.isfile('/tem/os.py')     # Check if it is a file: True
os.path.splitext('/tem/os.py')   # Split the file root and file extension: ('/tem/os', '.py')


# Above are notes from https://www.youtube.com/watch?v=tJxcKyFMTGo






