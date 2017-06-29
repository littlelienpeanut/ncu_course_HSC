# -*- coding: UTF-8 -*-
# python version: python3.6.1

import json
import requests
from time import sleep, time
import random

tStart = time()

#粉絲團名稱
page_id_val = "appledaily"
#目前圖形API最大的貼文數限制為100，所以只能抓到最多100個貼文紀錄
fans_id = "appledaily.tw/posts/?limit=100"
#權杖
accessToken = "EAACEdEose0cBANounAzkQA8Cawd1QvMJFi3WkFmSwR54RIjO4LkINxhAq09P4V6R9JSpr57hPbtStfJgGSIyQ89EDNeSa12EdLMreOd1Hqd25HtbMtjKrGLxR1iSnqtpdEvNwg7SLfMUGB4648ZC1mo8soCUXotwjrW3rTJQOdnsBgiKuMJt1X0FUhGEZD"

sleepStart = time()
data_res = requests.get("https://graph.facebook.com/v2.6/"+fans_id+"/feed?limit=2&+access_token="+accessToken)
sleepStop = time()


jsonData = json.loads(data_res.text)

fetch_num = 0

with open('appledaily_tag.json','w', encoding = 'UTF-8') as file:
    message_info = []
    for data in jsonData['data']:
        tmp_message_info = []
        tag_val = []


#首先利用 data 中的 created_time 找出選定的日期,如果是在目標日期才作 # 判斷. 若為目標日期,將 page_id 、 message_id 抓出來加到 list 中
        if data["created_time"][0:10] == "2017-06-27" or data["created_time"][0:10] == "2017-06-27" or data["created_time"][0:10] == "2017-06-28":
            fetch_num += 1

            if 'message' in data.keys():
#將 message 中 #開頭空格結尾 的字串抓出來,後面再做判斷
                article_message = data['message']
                print(article_message)
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

                    if i.find(")") != -1:
                            tmp_tag = i[:i.find(")")]
                            tag_val.append(tmp_tag)

                    elif i.find("\n") != -1:
                        if i.find(")") != -1 and i.find(")") < i.find("\n"):
                            tmp_tag = i[:i.find(")")]
                            tmp_tag = i[:i.find("\n")]
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

    jdata = json.dumps(message_info) #轉成json格式
    json.dump(jdata, file) #寫成json檔案


#讀json檔、檔名為 appledaily_tag.json
with open("appledaily_tag.json", mode='r') as json_data:
        jdata = json.load(json_data) #讀json檔案
        jdata = json.loads(jdata) #轉成一般格式
        for i in range(0, len(jdata), 1): #jdata跟message_info是一樣的東西
            print(jdata[i][0])
            print(jdata[i][1])
            print(jdata[i][2])
            print("")

tStop = time()

#顯示抓取文章數等等資訊
print("Fetching numbers: " + str(fetch_num))
print("Computing: " + str(tStop - tStart - (sleepStop - sleepStart)))
print("Crawling time: " + str(sleepStop - sleepStart))
print("Total time: " + str(tStop - tStart))
