#!/bin/bash
is_alive_ping()
{
ping -n 1 $1 > /tmp/ping.txt
[ $? -eq 0 ] && echo Node with IP: $i is up.
}
for i in 192.168.100.{2..254}
do
is_alive_ping $i & disown
done
