#!/usr/bin/python
"""import os
path = "/etc/fstab"
if os.path.isdir(path):
  print "its a directory"
else:
  print "its a file" """


import os
print os.chdir("/tmp")
for dirs, files in os.walk("/tmp"):
  print dirs
  print files
