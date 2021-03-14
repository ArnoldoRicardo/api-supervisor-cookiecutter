#!/usr/bin/bash
OK=true
while [ $OK ]; do
  CODE=$(curl --silent --output /dev/stderr --write-out "%{http_code}" $1)
  if [ "$CODE" -eq "302" ]; then
    echo 'code 302'
    continue
  else
    notify-send "errror $CODE" 'server caido'
    break
  fi
done
