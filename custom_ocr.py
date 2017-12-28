#!/usr/bin/env python3

import os
import sys
import subprocess
import time
import pangu
from get_API_res import get_Tencent_res, get_Baidu_res
from config import Tencent_config, Baidu_config

PUNC_TOBE_REP="!?,.:;“”()"
PUNC_AFBE_REP="！？，。：；\"\"（）"
RM_HOLE_FLAG=True

CLIP_IMNAME="/tmp/clip.jpg"

def load_clipboard_im():
    cmd = "pngpaste {} 2> /dev/null".format(CLIP_IMNAME)
    os.system(cmd)
    #print (" | Screen has been saved to {}".format(CLIP_IMNAME))

def custom_rep(s):
    if (len(PUNC_TOBE_REP) != len(PUNC_AFBE_REP)):
        raise ValueError(" | What the fuck did you modified...")
    for i in range(len(PUNC_TOBE_REP)):
        s = s.replace(PUNC_TOBE_REP[i], PUNC_AFBE_REP[i])
    if RM_HOLE_FLAG is True:
        s = s.replace("\n", "")
        s = s.replace(" ", "")
    s = s.replace("一一", " -- ")
    s = s.replace("。。。。。", "...")
    s = s.replace("。。。。", "...")
    #print (" | Replace completed...")
    return s

def read_from_clipboard():
    return subprocess.check_output(
                    'pbpaste', env={'LANG': 'en_US.UTF-8'}).decode('utf-8')

def write_to_clipboard(output):
    process = subprocess.Popen(
                    'pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
    process.communicate(output.encode('utf-8'))


def main():
    #s = read_from_clipboard()
    load_clipboard_im()
    #print (" | Start to process content in picture...")
    if Baidu_config["active"] is True:
        s = get_Baidu_res(image_path=CLIP_IMNAME)
    elif Tencent_config["active"] is True:
        s = get_Tencent_res(image_path=CLIP_IMNAME)
    else:
        assert (False), "No active service"
    if s != "":
        s = custom_rep(s)
        s = pangu.spacing(s)
        write_to_clipboard(s)
        print(s)
    else:
        print (" | No any characters...")
    #print (" | All done!")

if __name__ == "__main__":
    main()


###### UNUSED CODE ######
def manual_mode():
    s = read_from_clipboard()
    #print (" | Start to process content in clipboard...")
    s = rep(read_from_clipboard())
    write_to_clipboard(s)
    print(s)
    #print (" | All done!\n | ")
