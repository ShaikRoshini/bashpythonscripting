#!/usr/bin/python

import os
print os.chdir('/var')
for files in os.walk("/var"):
  
  print files
  
              
