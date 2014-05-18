set -e
curl -L https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-1.1.1.tar.gz > elasticsearch.tar.gz
tar -xvf elasticsearch.tar.gz
./elasticsearch-1.1.1/bin/elasticsearch -d
sleep 5
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