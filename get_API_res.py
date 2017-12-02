#!/usr/bin/env python3
#coding:utf-8
import time
import TencentYoutuyun


"""
You should get
- APPID
- secret_id
- secret_key

from cloud.tencent.com
"""

appid=''
secret_id=''
secret_key=''



userid='0'
end_point = TencentYoutuyun.conf.API_YOUTU_END_POINT
youtu = TencentYoutuyun.YouTu(appid, secret_id, secret_key, userid, end_point)

def get_res(image_path):
    ret = youtu.generalocr(image_path, data_type = 0, seq = '')
    det_res = ""
    for item in ret["items"]:
        det_res += item['itemstring']
    det_res = det_res.encode('latin1').decode('utf-8')
        
    #print(det_res)
    return det_res

if __name__ == "__main__":
    print (get_res("/tmp/clip.jpg"))

