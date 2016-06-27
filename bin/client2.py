#!/usr/bin/env python3.5
# -*- coding:utf8 -*-
import os,sys
BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEDIR)
from core import rabbit_main_client2
"""
此客户端主机组为：NA
"""
if __name__ == "__main__":
    rabbit_main_client2.run()


