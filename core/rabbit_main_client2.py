#!/usr/bin/env python3.5
# -*- coding:utf8 -*-
import pika
import os,sys
BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEDIR)
from conf import setting
def run():
    connection = pika.BlockingConnection(pika.ConnectionParameters(
             host=setting.HOST["host"],port=setting.HOST["port"]))
    channel = connection.channel()
    channel.exchange_declare(exchange="NA",type="fanout")
    result = channel.queue_declare(exclusive=True)  # 不指定queue名字，rabbit会随机分配一个名字，exclusive ＝True
    # 会在使用此queue的消费者断开后，自动将queue删除
    queue_name = result.method.queue
    channel.queue_bind(exchange='NA',queue=queue_name)
    print(' [*] Waiting for NA. To exit press CTRL+C')
    def execute_cmd(ch, method, properties, body):
        cmd = str(body.decode())
        os.system(cmd)
    channel.basic_consume(execute_cmd,queue=queue_name,no_ack=True)
    channel.start_consuming()



