import os
import time
import zipfile


"""This is an app to backup a specified list of directories"""


# 1. The files and dir to be backed up are
# secified in a list
source = ["C:\Python27\Python Projects"]

# 2. The backup must be stored in a
# main backup directory
target_dir = 'D:/Computer Science/bkup'


# 3. The files are backed up into a zip file
# 4. The name of the zip archive is the current date and time
target = target_dir + os.sep + time.strftime("%Y%M%d%H%M%S") + '.zip'


# creat backup dir if not present
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

# 5. We us the zip coommand to put the files in a zip archive
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
