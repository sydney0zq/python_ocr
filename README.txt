:Author: zhou
:Email: theodoruszq@gmail.com
:Date: 2017-12-02 11:04


Please ensure you are using MacOS.

```
Usage:
    1. `brew install pngpaste` and `pip install pangu`
    2. Apply appid, secret_id and secret_key in `config.py`
    3. `ln -s ./custom_ocr.py /usr/local/bin/custom_ocr.py`
    4. `custom_ocr.py` from anywhere in shell to get current captured screen document
```

-----APPEND-----
1. The captured image will be saved in the path `/tmp/clip.jpg`, and be covered by newer ones, if you need to review the history, feel free to modify code or issue a PR
2. The recogintion text (by OCR service) will be loaded into clipboard automatically
3. Most importantly, I have do really a lot post-processing to the recoginition text, including my custom designed replacement and `pangu` text-reformatting tool


Here is a demo in my project, `demo.mp4`.


0~1000 times for free per month (Tencent)
Register [here](https://cloud.tencent.com/document/product/641/12399)

0~500 times for free per day (Baidu)
Register [here](https://console.bce.baidu.com/ai/#/ai/ocr/overview/index)

Tips:
    After my long time experience, Baidu service is better than Tencent. It is stable and will never appear text disordering fault.



[MIT LICENSE]
Tencent YouTu SDK [link](https://github.com/Tencent-YouTu/Python_sdk)
Baidu AIP SDK [link](https://github.com/Baidu-AIP)
