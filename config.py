#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 zhou <zhou@Macbook.local>
#
# Distributed under terms of the MIT license.

"""
Configuration for get_API_res.py
"""
import os
HOME=os.environ['HOME']

cache_fn={
    "logfn": os.path.join(HOME, ".ocr.json"),
    "cacheim": "/tmp/clip.jpg"
} 

Tencent_config = {
    "appid": "",
    "secret_id": "",
    "secret_key": "",
    "userid": "0",
    # Custom configuration
    "active": False
}

Baidu_config = {
    "APP_ID": "",
    "API_KEY": "",
    "SECRET_KEY": "",
    # Custom configuration
    "active": True
}


