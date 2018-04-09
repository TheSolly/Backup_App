import os
import time
import zipfile


"""This is a script to backup a specified list of directories"""


# 1. The files and dir to be backed up are
# specified in a list
source = [''' insert your directory here!''']

# 2. The backup must be stored in a
# main backup directory
target_dir = ''' insert your directory here!'''

# 3. create backup dir if not present
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

# 4. The current day is the name of the subdirectory
# in the main directory
today = target_dir + os.sep + time.strftime('%Y%M%d')
# The current time is the name of the zip archive
now = time.strftime('%I%M%S%p')

# 5. Take a comment from the user to
# create the name of the zip file
comment = raw_input("Enter a comment for the zip file: ")
# Check if a comment was entered and create the
# appropriate folder accordingly
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + "_" + \
        comment.replace(" ", "_") + '.zip'

# Create the subdirectory if it isn't already there
if not os.path.exists(today):
    os.makedirs(today)
    print ("Successfully created directory", today)


# 6. We us the zip command to put the files in a zip archive
zip_command = zipfile.ZipFile(target, mode="w")
for i in source:
    for roots, subdirs, files in os.walk(i):
        zip_command.write(roots)
        for filename in files:
            zip_command.write(os.path.join(roots, filename))
zip_command.close()


# Run the backup
print ("Zip command is: ")
print (target)
print ("Running: ")
if zipfile.is_zipfile(target) is True:
    print ("Successful backup to:" + target)
else:
    print("Backup FAILED!")
