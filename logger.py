#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 zhou <zhou@Macbook.local>
#
# Distributed under terms of the MIT license.

import time
from config import cache_fn
import json


class logclass:
    def __init__(self, logfn = cache_fn["logfn"]):
        self.date = time.strftime("%Y-%m-%d", time.localtime())
        
        self.logfn = logfn
        self.record = self.load_record()
        self.thres = 50

    def load_record(self):
        date = self.date
        try:
            with open(self.logfn, "r") as f:
                log = json.load(f)
            if (date in log.keys()) is False:
                log[date] = [0, 0]
        except:
            log = {date: [0, 0]}
        return log

    def check_highacc_avail(self):
        date = self.date
        record = self.record
        today_cnt = record[date]

        if record[date][1] < self.thres:
            return True
        else:
            return False
        
    def today_addone(self, serv_type):
        # serv_type
        #   0 - general
        #   1 - high acc
        date = self.date
        record = self.record
        today_cnt = record[date]
        
        if serv_type == 1:
            record[date][1] += 1
        else:
            record[date][0] += 1

        self.dump()
 
    def dump(self):
        with open(self.logfn, "w") as f:
            json.dump(self.record, f)

    def __str__(self):
        return str(self.record[self.date])


if __name__ == "__main__":
    obj = logger()
    obj.check_highacc_avail()
    obj.today_addone(0)
    obj.today_addone(1)

