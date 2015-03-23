# encoding: utf-8
__author__ = u'猥琐的胖子'
import requests
import json
import time
import datetime
import ctypes

ubox_id = "0721575"
template = "http://buy.ubox.cn/index/vminfo/%s/0"
last_products = {}
products = {}
isLoop = True
while isLoop:
    response = requests.get(template % ubox_id)
    result = json.loads(response.text)
    if result["head"]["status"] == 1:
        print datetime.datetime.today()
        print result["data"]["name"]
        for each in result["data"]["Product"]:
            print each["shortName"], each["num"]
            products[each["shortName"]] = each["num"]
        if len(last_products) > 0:
            fresh_meat = []
            for key in products:
                if last_products.get(key, 0) == 0 and products.get(key, 0) > 0:
                    fresh_meat.append(key)
            if len(fresh_meat) > 0:
                ctypes.windll.user32.MessageBoxA(0, (u'%s 上货啦！' % ' - '.join(fresh_meat)).encode("gbk"), u'行动吧吃货！'.encode("gbk"), 0)
                isLoop = False
        last_products = products.copy()
    time.sleep(60)