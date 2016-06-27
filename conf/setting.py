#!/usr/bin/env python3.5
# -*- coding:utf8 -*-
import os,sys
BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEDIR)
HOST = {
	"host":"192.168.1.190",     # rabbitmq 主机
	"port":5672                 # rabbitmq 端口
}

