#!/bin/bash

# searching for directories

echo ""
echo "------------------------------------------------------------"
echo "               _                              "
echo " __      _____| |__  _ __ ___  ___ ___  _ __ "
echo " \ \ /\ / / _ \ '_ \| '__/ _ \/ __/ _ \| '_ \ "
echo "  \ V  V /  __/ |_) | | |  __/ (_| (_) | | | |"
echo "   \_/\_/ \___|_.__/|_|  \___|\___\___/|_| |_|"
echo "                                              "
echo ""
echo "------------------------------------------------------------"

echo "Performing a DIR bruteforce..."
echo ""

for word in $(cat $2)
do
response=$(curl -s -o /dev/null -H 'User-Agent: Firefox/61.0.0.2' -w "%{http_code}" $1/$word/)

if [ $response == "200" ]
then
echo "[+] Found at: $1/$word/"
fi
done

echo ""
echo "-------------------------------------------------------------"
echo ""
echo "Performing a file bruteforce..."
echo ""

# searching for files

for file in $(cat $2)
do
resp=$(curl -s -o /dev/null -H 'User-Agent: Firefox/61.0.0.2' -w "%{http_code}" $1/$file.$3)

if [ $file == "200" ]
then
echo "[+] Found at: $1/$file.$3"
fi
done
