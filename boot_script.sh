#! /bin/bash
clear

DATE=`date '+%Y-%m-%d %H:%M:%S'`

cd $PROJECT_PATH
. ./properies.py

echo $DATE ' boot_script' >> ${LOG_FILE}

source $VENV/bin/activate
python manage.py runserver $HOST