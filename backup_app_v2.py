import os
import time
import zipfile


"""This is an app to backup a specified list of directories"""


# 1. The files and dir to be backed up are
# secified in a list
source = ["C:/Python27/Python Projects"]

# 2. The backup must be stored in a
# main backup directory
target_dir = 'D:/Computer Science/bkup'

# 3. creat backup dir if not present
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

# 4. The current day is the name of the subdirectory
# in the main directory
today = target_dir + os.sep + time.strftime('%Y%M%d')
# The current time is the name of the zip archive
now = time.strftime('%I%M%S%p')

# 5. The files are backed up into a zip file
target = today + os.sep + now + '.zip'

# Create the subdirectory if it isnt already there
if not os.path.exists(today):
    os.makedirs(today)
    print ("Successfully created direcotry", today)


# 6. We us the zip coommand to put the files in a zip archive
# refer to dir_manuipulation for more info about this step
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
