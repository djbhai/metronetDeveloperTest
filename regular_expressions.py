# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 23:04:02 2019

@author: User
"""

from datetime import datetime
import re

sample_time=1541001567
"""
 referred the website 
https://www.programiz.com/python-programming/datetime/timestamp-datetime
for generating date time stamp
"""

datetimestamp= str(datetime.fromtimestamp(sample_time))
dts_parts = datetimestamp.split(" ")
refined = dts_parts[0]+'T'+dts_parts[1]
print(refined)
split=re.findall('[^T]+',refined)
ymd= split[0]
hms= split[1]
print('yyyy-mm-dd = '+ymd)
print('Hours-mins-seconds= '+hms)