#!/bin/sh
set -e
curl -L https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-1.1.1.tar.gz > elasticsearch.tar.gz
tar -xvf elasticsearch.tar.gz
bash elasticsearch-1.1.1/bin/elasticsearch -d
echo "Sleeping for 5 seconds"
sleep 5
echo "Back up again :)"
python -m unittest discover
status=$?
if [ $status -ne 0 ]; then
    pkill -9 -f elasticsearch
    rm -rf elasticsearch*
    exit 1
fi
pkill -9 -f elasticsearch
rm -rf elasticsearch*
exit 0