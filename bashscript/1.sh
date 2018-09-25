#!/bin/bash

echo "creating users"
for i in {1..4}
do
`sudo mkdir -p /home/user$i`
`sudo useradd -m -d /home/user$i -s /bin/bash user$i`
echo
echo "user$i:admin" | sudo chpasswd  
done
