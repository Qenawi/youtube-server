#!/bin/sh
#
#  Qenawi created sync_database.sh at 5/1/21, 6:49 PM
#  sync_database.sh @Docs
#
#

# make my app migrations
python3 manage.py makemigrations myapp
# apply my app migrations
python3 manage.py migrate myapp
# apply dashboard migrations
python3 manage.py migrate jet
