# coding:utf-8

import urllib.request
import urllib.parse
import json
import time



def get_hot_info():
    # url = "http://114.118.4.4/rest/n/feed/hot?app=0&kpf=ANDROID_PHONE&ver=6.1&c=HUAWEI&mod=HUAWEI%28HMA-AL00%29&appver=6.1.2.8197&ftt=&isp=CMCC&kpn=KUAISHOU&lon=0&language=zh-cn&sys=ANDROID_9&max_memory=384&ud=1273883886&country_code=cn&oc=HUAWEI&hotfix_ver=&did_gt=1551771200098&iuid=&extId=e14d69a16505ef1355f2cb2118c47067&net=WIFI&did=ANDROID_c0005c599b4db9a0&lat=0"
    url = "http://114.118.4.4/rest/n/feed/hot?app=0&kpf=ANDROID_PHONE&ver=6.1&c=HUAWEI&mod=HUAWEI%28HMA-AL00%29&appver=6.1.2.8197&ftt=&isp=CMCC&kpn=KUAISHOU&lon=0&language=zh-cn&sys=ANDROID_9&max_memory=384&ud=1273883886&country_code=cn&oc=HUAWEI&hotfix_ver=&did_gt=1551771200098&iuid=&extId=e14d69a16505ef1355f2cb2118c47067&net=WIFI&did=ANDROID_c0005c599b4db9a0&lat=0&type=7&page=1&coldStart=false&count=20&pv=false&id=484&refreshTimes=22&pcursor=&source=1&needInterestTag=false&browseType=1&os=android&__NStokensig=f558d7ad5ad6271070d20c5ae4b9bd07fc213a9dceb83f0dc35f55cce18695f3&token=6433470af74d43e987365ac17cf8d27b-1273883886&sig=f25189361328101631b04e4cd822da2e&client_key=3c2cd3f3"

    postData = {
        'type': 7,
        'page': 1,
        'coldStart': 'false',
        'count': 20,
        'pv': 'false',
        'id': 484,
        'refreshTimes': 22,
        'pcursor': 1,
        # 'source': 1,
        # 'needInterestTag': 'false',
        # 'browseType': 1,
        'os': 'android',
        # '__NStokensig': 'f558d7ad5ad6271070d20c5ae4b9bd07fc213a9dceb83f0dc35f55cce18695f3',
        # 'token': '6433470af74d43e987365ac17cf8d27b-1273883886',
        'client_key': '3c2cd3f3',
        'sig': 'f25189361328101631b04e4cd822da2e'
    }
    headers = {
        "User-Agent": "kwai-android",
        "Content-Type": "application/x-www-form-urlencoded"
    }


    req = urllib.request.Request(url)
    req.add_header("User-Agent", "kwai-android")
    req.add_header("Content-Type", "application/x-www-form-urlencoded")
    data = urllib.parse.urlencode(postData).encode('utf-8')
    
    try:
        # apiJson = urllib.request.urlopen(req, data=data).read()
        apiJson = urllib.request.urlopen(req).read()
    except urllib.error.URLError as e:
        with open('error.log', 'a') as f:
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            f.write(current_time + ": " + 'bad network, retry')
        time.sleep(2)    
        apiJson = urllib.request.urlopen(req, data=data).read()

    jsonData = json.loads(apiJson)

    for item in jsonData['feeds']:
        itemSave = {}
        # if 'user' in item.keys():
        #     if 'kwaiId' in item['user'].keys():
        #         itemSave['kwaiId'] = item['user']['kwaiId']
        if 'kwaiId' in item.keys():
            itemSave['kwaiId'] = item['kwaiId']
        itemSave['view_count'] = item['view_count']    
        itemSave['like_count'] = item['like_count']
        itemSave['comment_count'] = item['comment_count']
        itemSave['user_id'] = item['user_id']
        itemSave['user_name'] =  item['user_name']
        itemSave['caption'] = item['caption']
        print(itemSave)



def run_spider():
    while True:
        try:
            get_hot_info()
            time.sleep(1)
        except Exception as e:
            print(e)
            pass    


if __name__ == '__main__':
    run_spider()