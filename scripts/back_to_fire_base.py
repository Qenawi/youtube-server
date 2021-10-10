#   Qenawi created back_to_fire_base.py at 5/15/21, 10:34 AM
#   back_to_fire_base.py @Docs
#

import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage

# input keys [-b / -r]
import sys

latest_backup = "my/backup/dir/backup.dump"


# send backup file to firebase storage
def init_admin():
    buckerUrl = "databasebackup-461c3.appspot.com"
    cred = credentials.Certificate("scripts/accountKey.json")
    firebase_admin.initialize_app(cred, {'storageBucket': buckerUrl})


def get_latest_database_dumb():
    global latest_backup
    path = "my/backup/dir"
    filepath = [os.path.join(path, file) for file in os.listdir(path)]
    ls = sorted(filepath)
    latest_backup = ls[-1]


def upload_to_fire_base():
    print("--------- uploading ... ----------")
    global latest_backup
    file = latest_backup
    bucket = storage.bucket()
    blob = bucket.blob(blob_name="backup.dump")
    fi = open(file, "rb")
    rep = blob.upload_from_file(file_obj=fi)
    print("--------- backed up to remote server successfully  ----------")


# download backup file from database
def restore_backup():
    bucket = storage.bucket()
    blob = bucket.blob(blob_name="backup.dump")
    blob.download_to_filename("my/backup/dir/backup.dump")
    print("--------- backup restored ----------")


if __name__ == '__main__':
    arg = ""
    if len(sys.argv) > 1:
        arg = sys.argv[1]
    init_admin()
    print("--------- connecting to backup server ----------")
    # get_latest_database_dumb()
    if arg == "-b":
        upload_to_fire_base()
    elif arg == "-r":
        restore_backup()
    else:
        print("please type -b <backup> / -r <restore>")
