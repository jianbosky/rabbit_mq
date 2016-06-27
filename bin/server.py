#!/usr/bin/env python3.5
# -*- coding:utf8 -*-
import os,sys
BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEDIR)
from core import rabbit_main_server
"""
此为服务器下发命令端
"""
if __name__ == "__main__":
    rabbit_main_server.run()


