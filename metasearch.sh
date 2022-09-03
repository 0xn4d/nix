#!/bin/bash


if [ "$1" == "" ]
then
	echo ""
	echo "Metasearch - metadados search using Google Hacking"
	echo "Usage: $0 host filetype"
	echo "e.g.: $0 target.com pdf"
	echo ""
else
echo ""
echo "metasearch.sh - metadados search using Google Hacking"
echo ""
echo ""

echo "Let me do the job now :P......"

lynx --dump "https://google.com/search?q=site:"$1"+ext:"$2"" | grep "$2" | cut -d "=" -f2 | grep -v "site" | grep -v "google" | sed 's/...$//' >> linksoutput.txt

echo ""
echo "Downloading the files......."
echo ""

for link in $(cat linksoutput.txt);
do
	wget -q $link;
done

echo ""
echo ""
echo "##############################################"
echo ""
echo "Exiftool turn :P"
echo ""

exiftool *.$2

echo ""
echo "the end"
echo ""
fi
