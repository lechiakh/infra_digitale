#!/bin/bash
for i in $@
do
ping -n 1 $i &> /dev/null
if [ $? -ne 0 ]; then
echo "`date`: ping failed, $i host is down!" | email -s "$i host is down!" mohammedlechiakh@gmail.com
else
echo "`date`: ping succeed, $i host is up!" | mail -s "$i host is up!" mohammedlechiakh@gmail.com
fi
done