# coding:utf-8
__author__ = u'猥琐的胖子'
from datetime import *
import os

now = datetime.now()
filename = '%4d-%02d-%02d.txt' % (now.year, now.month, now.day)
eaters = {}
while os.path.os.path.exists(filename):
    # 如果存在，就读取内容
    for line in open(filename):
        info = line.decode('utf-8').strip().split(' ')
        eaters[info[0]] = eaters.get(info[0], 0) + float(info[1])
        # 尝试读取昨天的文件内容
    now = now + timedelta(days=-1)
    filename = '%4d-%02d-%02d.txt' % (now.year, now.month, now.day)
print '***********************************'
for key in eaters:
    print key, eaters[key]