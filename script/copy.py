import os
import shutil

source = '../data/_test7/'
target = '../data/test7/'

for i in range(0,249,5):
    old = '{}img{}.jpg'.format(source, i)
    new = '{}img{}.jpg'.format(target, int(i/5))
    shutil.copy(old, new)