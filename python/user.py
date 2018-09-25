#!/usr/bin/python
import os
import crypt
print "creating users"
for i in (1,3):
  print os.mkdir("mkdir -p /home/user$i")
  print os.system("useradd -m -d /home/user$i -s /usr/bin/python user$i")
  print
  print crypt.system("ucrypt=crypt.crypt(upass,'123')")

