#!/bin/sh
echo "restoring back up from remote server ;)"
python3 scripts/back_to_fire_base.py -r
echo "removing current database file"
rm myproject/myproject/db.sqlite3
echo "download completed and loading backup ~= from local backup folder"
python3 manage.py dbrestore -i backup.dump
echo "syncing database"
sh scripts/sync/sync_database.sh