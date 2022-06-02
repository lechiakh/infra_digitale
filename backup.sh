#!/bin/bash
backup_dirs=("a" "b" "c")
dest_dir="archives"
backup_date=$(date +%b-%d-%y)
echo "Starting backup of: ${backup_dirs[@]}" >> journal.log
for i in "${backup_dirs[@]}"; do
echo "archive de ${i} ${i}-${backup_date}.tar.gz" >> journal.log

sudo tar -Pczf ../$i-$backup_date.tar.gz ../$i
done