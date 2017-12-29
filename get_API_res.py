#!/usr/bin/env python3
#coding:utf-8
import time
import TencentYoutuyun
from BaiduAIP.aip import AipOcr
from config import Tencent_config, Baidu_config, cache_fn
from logger import logclass

def get_Tencent_res(image_path):
    appid = Tencent_config["appid"]
    secret_id = Tencent_config["secret_id"]
    secret_key = Tencent_config["secret_key"]
    userid = Tencent_config["userid"]

    end_point = TencentYoutuyun.conf.API_YOUTU_END_POINT
    youtu = TencentYoutuyun.YouTu(appid, secret_id, secret_key, userid, end_point)
    ret = youtu.generalocr(image_path, data_type = 0, seq = '')

    det_res = ""
    #print (ret)
    for item in ret["items"]:
        det_res += item['itemstring']
    det_res = det_res.encode('latin1').decode('utf-8')
        
    #print(det_res)
    return det_res

def get_Baidu_res(image_path):
    APP_ID = Baidu_config["APP_ID"]
    API_KEY = Baidu_config["API_KEY"]
    SECRET_KEY = Baidu_config["SECRET_KEY"]

    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

    logger = logclass()
    """ 读取图片 """
    def get_file_content(image_path):
        with open(image_path, 'rb') as fp:
            return fp.read()

    image = get_file_content(cache_fn["cacheim"])

    """ 调用通用文字识别, 图片参数为本地图片 """
    if logger.check_highacc_avail() is True:
        ret = client.basicAccurate(image)    # Accurate
        logger.today_addone(1)
    else:
        ret = client.basicGeneral(image)     # General
        logger.today_addone(0)
    print (logger)

    det_res = ""
    for item in ret["words_result"]:
        det_res += item['words']
    #print(det_res)
    return det_res

if __name__ == "__main__":
    obj = logger()
    print (obj)




