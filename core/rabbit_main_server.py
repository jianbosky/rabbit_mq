#!/usr/bin/env python3.5
# -*- coding:utf8 -*-
import os,sys
BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEDIR)
import pika
from conf import setting
def rabbit(cmd):
    try:
        group,action = cmd.split(" ",1)
        connection = pika.BlockingConnection(pika.ConnectionParameters(
                 host=setting.HOST["host"],port=setting.HOST["port"]))
        channel = connection.channel()

        channel.exchange_declare(
            exchange=group,
            type="fanout"
        )
        channel.basic_publish(exchange=group,
                              routing_key='',
                              body=action,
                            )
        print("对主机组[{}]，下发命令[{}]执行".format(group,action))
        connection.close()
    except  Exception as e:
        print("输入错误：{}".format(e))
        print("""
        命令输入格式为：
        [group] [command]          : 组名 命令 log shutdown -t
        """)
def run():
    while True:
        user_cmd = input("请输入要执行的命令：").strip()
        if user_cmd:
            rabbit(user_cmd)
        else:
            print("""
                命令输入格式为：
                [group] [command]          : 组名 命令 log shutdown -t
                """)