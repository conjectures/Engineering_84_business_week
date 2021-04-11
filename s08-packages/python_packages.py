import random
import math


num = (random.random())
print(num)
print(math.ceil(num))

# Python modules

import os
import datetime, sys


# Get working directory path
working_dir = os.getcwd()
print(working_dir)
#get username of system (linux)
print(os.uname())
# Join two paths for any os
print(os.path.join(working_dir, 'folderA'))
# Get cpu count
print(os.cpu_count())

# Get os execution path
print(sys.path)

#print(os.path(working_dir, 'folderA'))
