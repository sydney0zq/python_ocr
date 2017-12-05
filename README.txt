:Author: zhou
:Email: theodoruszq@gmail.com
:Date: 2017-12-02 11:04


Please ensure you are using MacOS operating System.

```
Usage:
    1. `brew install pngpaste` and `pip install pangu`
    2. Apply an appid, secret_id and secret_key in `get_API_res.py`
    3. `ln -s ./custom_ocr.py /usr/local/bin/custom_ocr.py`
    4. `custom_ocr.py` from anywhere in shell to get current captured screen document
```


-----APPEND-----
1. 截的图片会被存入/tmp/clip.jpg
2. 识别后的字符串会被自动存入系统剪切板
3. 识别之后对字符用pangu工具进行处理，保证英文和中文之间有空格


Here a demo in my project, demo.mp4.

Price: 0~1000 times per month for free
https://cloud.tencent.com/document/product/641/12399


[MIT LICENSE]
You should notice I forked Tencent YouTu SDK which can be checked [here](https://github.com/Tencent-YouTu/Python_sdk).
