# encoding: utf-8
__author__ = u'猥琐的胖子'
import requests
import json
import ctypes

#ctypes.windll.user32.MessageBoxA(0, 'aaa', u'行动吧吃货！', 0)

ubox_id = "0721577"
template = "http://buy.ubox.cn/index/vminfo/%s/0"
response = requests.get(template % ubox_id)
result = json.loads(response.text)
if result["head"]["status"] != 1:
    print "failed"
else:
    print result["data"]["name"], "产品列表"
    products = result["data"]["Product"]
    for each in products:
        print each["shortName"], each["num"]