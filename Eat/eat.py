# coding:utf-8
__author__ = u'猥琐的胖子'
from datetime import datetime

menu = {
    u'鸡腿': 5,
    u'鸭腿': 5,
    u'霸王鸭腿': 9,
    u'肉泥蒸蛋': 6,
    u'麦乐鸡块': 6,
    u'香菇鸡肉粥': 8,
    u'肉泥蒸蛋饭': 10,
    u'手枪腿': 9,
    u'手枪腿饭': 13,
    u'鸡腿饭': 10,
    u'鸡排饭': 12,
    u'鸡排': 7,
    u'鸭腿饭': 10,
    u'霸王鸭腿饭': 13,
    u'宫保鸡丁': 12,
    u'双腿': 13,
    u'香焖鸭': 13,
    u'烤鸭': 10,
    u'蚝油牛肉': 13,
    u'黑椒牛肉': 13,
    u'咖喱牛肉': 13,
    u'叉烧': 12,
    u'香菇滑鸡': 12,
    u'孜然肉片': 12,
    u'猪脚': 15,
    u'茶菇肉片': 13,
    u'茶菇': 13
}
man = 50
minus = 15


class order(object):
    def __init__(self, *infos):
        self.name = infos[0]
        self.meals = infos[1:]
        self.price = reduce(lambda x, y: x + menu.get(y, 0), self.meals, 0)
        print self.name, ":",
        for meal in self.meals:
            print '%s - %s' % (meal, menu.get(meal, 0)),
        print
all = []
for line in open("eat.txt"):
    line = line.decode('utf-8')
    infos = line.strip().split(' ')
    if len(infos) > 1:
        all.append(order(*infos))
total = reduce(lambda x, y: x + y.price, all, 0)
print '***********************************'
print u'总计:', total
times = total / man
discount = total / man * minus
if (total + minus) / man > times:
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

