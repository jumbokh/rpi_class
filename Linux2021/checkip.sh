#!/usr/bin/bash
FILE=/tmp/ipmail.tmp
if test -f "$FILE"; then
    echo "$FILE exists."
    exit 0
fi
echo `date` > $FILE
echo "Checking IP address & send it to user..."
/usr/bin/python3 /home/pi/code/startup_mailer.py
echo "Done!"
exit 0
