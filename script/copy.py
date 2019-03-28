import os
import shutil

source = 'data/_test8/'
target = 'data/test8/'

for i in range(0, 300, 1):
    old = '{}{}.jpeg'.format(source, i)
    new = '{}img{}.jpg'.format(target, i)
    try:
        shutil.copy(old, new)
    except:
        continue
