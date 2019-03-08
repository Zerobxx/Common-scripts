# coding:utf-8

import urllib.request
import urllib.parse
import json
import time
from kuaishou_ORM import DBSession, Kuaishou
from keys import url


def get_hot_info():
    global url
    
    # 创建session对象
    session = DBSession()

    req = urllib.request.Request(url)
    req.add_header("User-Agent", "kwai-android")
    req.add_header("Content-Type", "application/x-www-form-urlencoded")
    # data = urllib.parse.urlencode(postData).encode('utf-8')
    
    try:
        # apiJson = urllib.request.urlopen(req, data=data).read()
        apiJson = urllib.request.urlopen(req).read()
    except urllib.error.URLError as e:
        with open('error.log', 'a') as f:
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            f.write(current_time + ": " + 'bad network, retry')
        time.sleep(5)    
        apiJson = urllib.request.urlopen(req).read()
    except Exception as e:
        with open('error.log', 'a') as f:
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            f.write(current_time + " Access API error: " + e)    
            return

    jsonData = json.loads(apiJson)

    
    for item in jsonData['feeds']:
        try:
            itemSave = {}
            if 'kwaiId' in item.keys():
                itemSave['kwaiId'] = item['kwaiId']
            else:
                itemSave['kwaiId'] = ''    
            itemSave['view_count'] = item['view_count']    
            itemSave['like_count'] = item['like_count']
            itemSave['comment_count'] = item['comment_count']
            itemSave['user_id'] = item['user_id']
            itemSave['user_name'] =  item['user_name']
            itemSave['caption'] = item['caption']
            if 'main_mv_urls' in item.keys():
                itemSave['mv_url'] = item['main_mv_urls'][0]['url']
                itemSave['if_mv'] = True
            else:
                itemSave['mv_url'] = item['cover_thumbnail_urls'][0]['url']
                itemSave['if_mv'] = False
            print(itemSave)

            new_item = Kuaishou(kuaishou_id = itemSave['kwaiId'],
                                view = itemSave['view_count'],
                                like = itemSave['like_count'],
                                comment = itemSave['comment_count'],
                                user_id = itemSave['user_id'],
                                # user_name = itemSave['user_name'],
                                # caption = itemSave['caption'],
                                mv_url = itemSave['mv_url'],
                                if_mv = itemSave['if_mv'])
            session.add(new_item)
        except Exception as e:
            with open('error.log', 'a') as f:
                current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                f.write(current_time + " DB insert error: " + e) 
        finally:    
            session.commit()
            session.close()    





def run_spider():
    while True:
        try:
            get_hot_info()
            time.sleep(1)
        except Exception as e:
            with open('error.log', 'a') as f:
                current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                f.write(current_time + " Run error: " + e)
            pass     


if __name__ == '__main__':
    run_spider()