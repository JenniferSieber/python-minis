"""
    Automated File Backups
    pip install schedule
    use: schedule, shutil, os, time, datetime

    Schedule daily backup for specific folder on you your harddrive 
    and save that backup with file name by date.

"""
import os
import shutil
import datetime
import schedule
import time

source_dir = "C:/Users/_USERNAME_/Pictures/Screenshots"                                                    # specific to your options
destination_dir = "C:/User/_USERNAME_/Desktop/Backups"                                                     # specific to your options

def copy_folder_to_directory(source, dest) :
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))

    try :
        shutil.copytree(source, dest_dir)
        print(f'Folder copied to: {dest_dir}')
    except :
        print(f'Folder already exists in: {dest}')

schedule.every().day.at('11:14').do(lambda: copy_folder_to_directory(source_dir, destination_dir))         # specific to your options

while True :
    schedule.run_pending()
    time.sleep(60)
