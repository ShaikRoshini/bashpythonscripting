#!/bin/bash
a=ip
b=host
echo "copy ipfile to hostfile"

cp $a $b
echo "version"
lsb_release -a
echo "display files"
ls -l
