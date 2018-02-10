#! /bin/bash
clear

DATE=`date '+%Y-%m-%d %H:%M:%S'`
. ./properties.py
cd $PROJECT_PATH


echo $DATE ' boot_script' >> ${LOG_FILE}

source $VENV/bin/activate
python manage.py runserver $HOST