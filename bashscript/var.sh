#!/bin/bash

PACKAGE='apache2'

echo $PACKAGE

echo "installing $PACKAGE"

sudo apt install $PACKAGE -y

echo "$PACKAGE installation is done."

#sudo service $PACKAGE start

sudo systemctl start $PACKAGE

sudo systemctl enable $PACKAGE

sudo systemctl is-active $PACKAGE

sudo systemctl is-enabled $PACKAGE
