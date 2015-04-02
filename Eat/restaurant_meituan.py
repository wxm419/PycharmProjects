# coding:utf-8
__author__ = u'猥琐的胖子'
import requests
from datetime import datetime


class order(object):
    def __init__(self, *infos):
        self.name = infos[0]
        self.meals = infos[1:]
        self.price = reduce(lambda x, y: x + float(menu.get(y, 0)), self.meals, 0)
        print self.name, ":",
        for meal in self.meals:
            print '%s - %s' % (meal, menu.get(meal, 0)),
        print

# 这里填入饭店ID 如http://waimai.meituan.com/restaurant/20212?pos=0 20212就是ID
restaurant = 93932
template = "http://waimai.meituan.com/restaurant/%s"
response = requests.get(template % restaurant)
menu = {}
for line in response.text.split('\n'):
    row = line.strip(" ,")
    if row.startswith('\"name\":'):
        name = row.strip("\"name\": ")
    if row.startswith('\"price\":'):
        menu[name] = row.strip("\"price\": ")
# 满减配置
man = 50
minus = 17

all = []
for line in open("eat.txt"):
    line = line.decode('utf-8')
    infos = line.strip().split(' ')
    if len(infos) > 1:
        all.append(order(*infos))
total = reduce(lambda x, y: x + y.price, all, 0)
print '***********************************'
print u'总计:', total
times = int(total) / man
if times > len(all) / 3:
    times = len(all) / 3
discount = times * minus
if int(total + minus) / man > times:
    print u'可以免费凑一新单，赶紧加餐'
print u'预计需要%s单，共满减%s' % (times, discount)
print '***********************************'
print u'紧张激烈的计算吃货们的嫖资...'
percentage = 1 - discount / float(total)
now = datetime.now()
filename = '%4d-%02d-%02d.txt' % (now.year, now.month, now.day)
f = open(filename, "w")
for each in all:
    f.write('%s %.2f\n' % (each.name.encode('utf-8'), each.price * percentage))
    print '%s - %.2f' % (each.name, each.price * percentage)
f.close()
print '***********************************'
print u'已存入%s' % filename