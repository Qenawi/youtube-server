#!/bin/sh
# remove latest database dumb
now=$(date +"%Y-%m-%d_%H_%M_%S")
echo "--- renaming old back up to dated name <database_$now.dump> --- "
mv my/backup/dir/backup.dump my/backup/dir/"database_$now.dump"
echo "creating new back file with name backup.dump"
python3 manage.py dbbackup -o backup.dump
python3 scripts/back_to_fire_base.py -b
# umb