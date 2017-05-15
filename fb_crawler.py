# -*- coding: UTF-8 -*-
# python version: python3.6.1

import json
import requests
from time import sleep, time
import random


tStart = time()
TimeoutError = 0.0

#粉絲團名稱 tvbsfb or yamnews
page_id_val = "tvbsfb"
#目前圖形API最大的貼文數限制為100，所以只能抓到最多100個貼文紀錄
fans_id = "tvbsfb/posts/?limit=100"
#權杖
accessToken = "EAACEdEose0cBAA98ZBTW3hkm4msofflwwnypcpRUdmzUt2lbsTzyKqEOv4BTWOobq4D4uk8Jrn6oI6XbMWgczo6rAqkVA9VrqKpfD6kl3WrtF24vtDPnTUwXonMyh9257JMU3IZAePoZB0snJ67UdbmLcwPgzxxZCdQTMbcBaZBkNM5K1EPTL"
data_res = requests.get("https://graph.facebook.com/v2.6/"+fans_id+"/feed?limit=2&+access_token="+accessToken)

sleepStart = time()
sleep(random.randint(1, 2))
sleepStop = time()
TimeoutError = TimeoutError + (sleepStop - sleepStart)
tStop = time()

jsonData = json.loads(data_res.text)

fetch_num = 0

with open('tvbsfb_tag.json','w', encoding = 'utf8') as file:
    message_info = []
    for data in jsonData['data']:
        tmp_message_info = []
        tag_val = []
        message_id = {}
        page_id = {}
        tag = {}


#首先利用 data 中的 created_time 找出選定的日期,如果是在目標日期才作 # 判斷. 若為目標日期,將 page_id 、 message_id 抓出來加到 list 中
        if data["created_time"][0:10] == "2017-05-08" or data["created_time"][0:10] == "2017-05-09" or data["created_time"][0:10] == "2017-05-10":
            fetch_num += 1

            if 'message' in data.keys():

#將 message 中 #開頭空格結尾 的字串抓出來,後面再做判斷
                article_message = data['message']
                temp_message = article_message[article_message.find("#"):]
                temp_message = temp_message.split(" ")

            if 'id' in data.keys():
                    message_id_val = data['id']


            #page id
            tmp_message_info.append({"page_id":page_id_val})

            #message id
            tmp_message_info.append({"message_id":message_id_val})

            #tag
#首先找出 temp_message 具有 # 的 element,有些 element 後面會接 \n 或是非空格符號,這樣會造成 tag 抓錯,所以增加判斷條件
            for i in temp_message:
                if i.find("#") != -1:

                    #print(i)
                    if i.find("\n") != -1:
                        if i.find("】") != -1 and i.find("】") < i.find("\n"):
                            tmp_tag = i[:i.find("】")]
                            tag_val.append(tmp_tag)

                        else :
                            tmp_tag = i[:i.find("\n")]
                            tag_val.append(tmp_tag)

                    else:
                        tag_val.append(i)

            tmp_message_info.append({"tag":tag_val})

            if tag_val == []:
                tag_val.append("None")

            message_info.append(tmp_message_info)

#轉成 json 格式

    jdata = json.dumps(message_info, skipkeys=False, ensure_ascii=False, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False)
    json.dump(jdata, file)


#讀json檔、檔名為 tvbsfb_tag.json or yamnews_tag.json
with open("tvbsfb_tag.json", mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True) as json_data:
        jdata = json.load(json_data, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None)
        jdata = json.loads(jdata)
        for i in range(0, len(jdata), 1):
            print(jdata[i][0])
            print(jdata[i][1])
            print(jdata[i][2])
            print("")

#顯示抓取文章數等等資訊
print("Fetching numbers: " + str(fetch_num))
print("TimeoutError: " + str(TimeoutError))
print("Crawling time: " + str(tStop - tStart - TimeoutError))
print("Total time: " + str(tStop - tStart))
