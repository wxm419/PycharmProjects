# encoding: utf-8
__author__ = u'猥琐的胖子'
import requests
import json
import time
import datetime
import ctypes

ubox_id = "0721577"
template = "http://buy.ubox.cn/index/vminfo/%s/0"
last_products = {}
products = {}
isLoop = True
while isLoop:
    response = requests.get(template % ubox_id)
    result = json.loads(response.text)
    if result["head"]["status"] == 1:
        print datetime.datetime.today()
        print result["data"]["name"], u"产品列表"
        for each in result["data"]["Product"]:
            print each["shortName"], each["num"]
            products[each["shortName"]] = each["num"]
        if len(last_products) > 0:
            for key in products:
                if last_products.get(key, 0) == 0 and products.get(key, 0) > 0:
                    ctypes.windll.user32.MessageBoxA(0, '%s 上货啦！' % key, u'行动吧吃货！', 0)
                    isLoop = False
        last_products = products.copy()
    time.sleep(60)