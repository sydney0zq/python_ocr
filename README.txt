:Author: zhou
:Email: theodoruszq@gmail.com
:Date: 2017-12-02 11:04


Please ensure you are using MacOS operating System.

```
Usage:
    1. `brew install pngpaste` and `pip install pangu`
    2. Apply appid, secret_id and secret_key in `config.py`
    3. `ln -s ./custom_ocr.py /usr/local/bin/custom_ocr.py`
    4. `custom_ocr.py` from anywhere in shell to get current captured screen document
```

-----APPEND-----
1. 截的图片会被存入/tmp/clip.jpg
2. 识别后的字符串会被自动存入系统剪切板


Here a demo in my project, demo.mp4.

Price: 0~1000 times for free per month (Tencent)
https://cloud.tencent.com/document/product/641/12399

Price: 0~500 times for free per day (Baidu)
Register url: https://console.bce.baidu.com/ai/#/ai/ocr/overview/index


[MIT LICENSE]
You should notice I forked Tencent YouTu SDK which can be checked [here](https://github.com/Tencent-YouTu/Python_sdk).
And I also forked manually from Baidu AIP repo, [link](https://github.com/Baidu-AIP).
