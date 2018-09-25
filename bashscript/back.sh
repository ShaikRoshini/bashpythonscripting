#!/bin/bash
LOG_DIR='/tmp/scripts/logs'
BACKUP_DIR='/tmp/scripts/logs_backup'
mkdir -p $BACKUP_DIR
for i in `cat backup_files.txt`
do
if [ -f $LOG_DIR/$i ]
then
echo "copying $i to logs_backup directory"
cp $LOG_DIR/$i $BACKUP_DIR
else
echo "$i log file does exist, skipping"
fi
done
echo
echo
echo "Zipping log files"
tar -cvzf logs_backup.tgz logs_backup
echo
echo
echo "Backup completed successfuly"

