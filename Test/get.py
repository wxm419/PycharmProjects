# coding: utf-8
__author__ = u'猥琐的胖子'
import requests
restaurant = 93932
template = "http://waimai.meituan.com/restaurant/%s"
response = requests.get(template % restaurant)
menu = []
for line in response.text.split('\n'):
    row = line.strip()
    if row.startswith('\"name\"'):
        name = row.strip("\"name\": ,")
    if row.startswith('\"price\"'):
        menu.append((name, row.strip("\"price\": ,")))
# string = '{'
for each in menu:
    # string += "u'%s': %s," % (each[0], each[1])
    print each[0], each[1]
# string += '}'
# menu = eval(string)
