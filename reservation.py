#!/usr/bin/env python
# _*_coding:utf-8_*_


""" 
=====================================================
@File    : reservation.py
@Time    : 2024/08/27 17:04:32
@E-mail  : kevin-que@qq.com
@License : (C)Copyright 2017-2024
@Author  :   Kevin Que
@Version :   1.0
@Contact :   
@Desc    :   小程序预约羽毛球场地
=====================================================
"""

# here put the import lib

import requests
from datetime import datetime

import logging
from datetime import datetime, timedelta
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor


token = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjQ5MDYyMDczLCJpc3MiOiJodHRwOi8veGN4LWFwaS56dWR1aWp1bi5jb20vYXBpL3d4LWxvZ2luIiwiaWF0IjoxNzI0NzQ5MDQ0LCJleHAiOjM2MTY5MDkwNDQsIm5iZiI6MTcyNDc0OTA0NCwianRpIjoiOGIxVGdEd2xwRzhMWEJjRyJ9.hj3A45sRhGvKFrEKlZddbnTXuHjZtmvwXQjjEJsvr9k"

headers = {
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "xweb_xhr": "1",
    "Authorization": token,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b19)XWEB/11177",
    "Version": "4.2.5.0",
    "Accept": "*/*",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
}


def get_id():

    tomorrow = datetime.now().date() + timedelta(days=1)
    url = f"https://xcx-api.zuduijun.com/api/get-activity-date-times?activity_id=1128525&date={tomorrow}"

    # 获取预约场地时间ID信息
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        res = response.json()
        res_data = res["data"][-1]
        # res_data= res['data'][0]
        print("获取预约场地时间ID成功", res_data)
        return res_data

    else:
        print("获取预约场地时间ID失败, 状态码：", response.status_code)


# 抓包数据
{
    "activity_id": "1128525",
    "diy_pro_id": "232510",
    "time_ids": ["151795437"],
    "diy_item_ids": ["812801"],
    "diy_item_ids_count": {"812801": 1},
    "register_infos": [
        {"register_info_id": "26884923", "value": "志峰"},
        {"register_info_id": "26884924", "value": "18874263064"},
    ],
    "roster": {},
    "actual_pay": 1,
    "order_amount": "",
    "order_id": "",
    "live_code": "",
    "live_url": "",
    "user_card_attr_id": "",
    "user_patient_card_id": "",
    "is_store_value": 0,
    "sign": "cLDhRL1Av+RPGdpKRGHNM2Z3GLoJVx6HHd9jfnFHPZpPUU6QIsrLg6C4O+k/oelvpwHbVfWdKakmPFDgAkZrAHwNYQ9Tf2Vz1P/r47RbpL7TbdUgQjcgi19Q9rehH8v9A0Jr5Pg9AKe9+vjPUA5oeuMG55DDZOH42rWustBV3cNPBksggWil/X1KwEL+qlKMwl+lzRwA3nAWt3OpnVMkkRt9XpxgM5VDD40OZ/FToB1T713S+lVIttmpTeM6ljNuF2mU8+0vRUFkwCo4bAKspGnhkcOWJmlWGBbsVj76yozEOhgE1xhTuf8f7CXJ5LETlvYgRBrQ4U4+kUXEqtNmRve0mQdzRF2yjj+/hNCTooTGt+2LEubnWFcfW5kwqGF2Ub/TTTX9WHttRp935B+Jo2nnxWw9SXxBJBPE32J+8EEHWMd5PvSU2dnGSKqjZw1oflBL76eQVe2bzvg5bAwP3H3wX4H7MTC9TshIbA/al2tUANLw9FDIFdp6QBb+Ec35ObZwaRHAQDT4tv7Ffi+c9NZH4KzW0HIkGICuHi68CeCM9kvQvr896COOA4xl6nDSEhI0oYO6HulqST712CP9VQ==",
}


def post_id():

    res_data = get_id()

    #  预约数据
    post_data = {
        # "id": res_data['id'],
        # "time": res_data['time']
        "activity_id": res_data["activity_id"],
        "diy_pro_id": "232510",
        "time_ids": [res_data["id"]],
        "diy_item_ids": ["812801"],
        "diy_item_ids_count": {"812801": 1},
        "register_infos": [
            {"register_info_id": "26884923", "value": "志峰"},
            {"register_info_id": "26884924", "value": "18874263064"},
        ],
        "roster": {},
        "actual_pay": 1,
        "order_amount": "",
        "order_id": "",
        "live_code": "",
        "live_url": "",
        "user_card_attr_id": "",
        "user_patient_card_id": "",
        "is_store_value": 0,
        "sign": "cLDhRL1Av+RPGdpKRGHNM2Z3GLoJVx6HHd9jfnFHPZpPUU6QIsrLg6C4O+k/oelvpwHbVfWdKakmPFDgAkZrAHwNYQ9Tf2Vz1P/r47RbpL7TbdUgQjcgi19Q9rehH8v9A0Jr5Pg9AKe9+vjPUA5oeuMG55DDZOH42rWustBV3cNPBksggWil/X1KwEL+qlKMwl+lzRwA3nAWt3OpnVMkkRt9XpxgM5VDD40OZ/FToB1T713S+lVIttmpTeM6ljNuF2mU8+0vRUFkwCo4bAKspGnhkcOWJmlWGBbsVj76yozEOhgE1xhTuf8f7CXJ5LETlvYgRBrQ4U4+kUXEqtNmRve0mQdzRF2yjj+/hNCTooTGt+2LEubnWFcfW5kwqGF2Ub/TTTX9WHttRp935B+Jo2nnxWw9SXxBJBPE32J+8EEHWMd5PvSU2dnGSKqjZw1oflBL76eQVe2bzvg5bAwP3H3wX4H7MTC9TshIbA/al2tUANLw9FDIFdp6QBb+Ec35ObZwaRHAQDT4tv7Ffi+c9NZH4KzW0HIkGICuHi68CeCM9kvQvr896COOA4xl6nDSEhI0oYO6HulqST712CP9VQ==",
    }

    # 预约地址
    post_url = "http://xcx-api.zuduijun.com/api/zdj-votes-queue"

    post_response = requests.post(post_url, json=post_data, headers=headers)
    if post_response.status_code == 200:
        res = post_response.json()
        print("获取预约场地成功", res)
    else:
        print("获取预约场地失败, 状态码：", post_response.status_code)


# 预填信息
def reserve():
    id = get_id()["id"]
    print(id)
    p_url = "https://xcx-api.zuduijun.com/api/beforehand-vote-register_info-users"
    data = {
        "time_id": str(id),
        "register_infos": [
            {"register_info_id": "26884923", "value": "志峰"},
            {"register_info_id": "26884924", "value": "18874263064"},
        ],
        "user_patient_card_id": "",
    }
    p_response = requests.post(p_url, json=data, headers=headers)

    # 检查响应状态码
    if p_response.status_code == 200:
        # 请求成功，处理响应数据
        result = p_response.json()
        print("预填写成功:", result, data)
    else:
        # 请求失败，打印错误信息
        print("预填失败，状态码:", p_response.status_code)


def run():
    # 日志
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        filename="./reservation.log",
        filemode="a",
    )

    # 日志监听器
    def log_listen(event):
        if event.exception:
            print("任务出错，报错信息：{}".format(event.exception))
        else:
            print("任务正常运行...")

    # 作业存储器： 使用sqlite3
    jobstores = {"default": SQLAlchemyJobStore(url="sqlite:///jobs.sqlite3")}
    # 执行器：模式设置
    executors = {
        "default": ThreadPoolExecutor(20),
        "processpool": ProcessPoolExecutor(10),
    }
    job_defaults = {"coalesce": False, "max_instances": 3}

    # 调度器 ：阻塞式模式
    scheduler = BlockingScheduler(
        jobstores=jobstores,
        executors=executors,
        job_defaults=job_defaults,
        timezone="Asia/Shanghai",
    )

    # 定时预约
    scheduler.add_job(
        post_id,
        "cron",
        hour="15",
        minute="59",
        second="59",
        timezone="Asia/Shanghai",
        id="RunTime",
        replace_existing=True,
    )

    # 配置任务执行完成及错误时的监听
    scheduler.add_listener(log_listen, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)

    # 配置日志监听
    scheduler._logger = logging

    try:
        scheduler.start()
    except SystemExit:
        print("exit")
        exit()


# if __name__ == '__main__':
#     run()



# import time, hashlib
# from urllib.parse import unquote_plus, quote_plus

# key = "cLDhRL1Av+RPGdpKRGHNM2Z3GLoJVx6HHd9jfnFHPZpPUU6QIsrLg6C4O+k/oelvpwHbVfWdKakmPFDgAkZrAHwNYQ9Tf2Vz1P/r47RbpL7TbdUgQjcgi19Q9rehH8v9A0Jr5Pg9AKe9+vjPUA5oeuMG55DDZOH42rWustBV3cNPBksggWil/X1KwEL+qlKMwl+lzRwA3nAWt3OpnVMkkRt9XpxgM5VDD40OZ/FToB1T713S+lVIttmpTeM6ljNuF2mU8+0vRUFkwCo4bAKspGnhkcOWJmlWGBbsVj76yozEOhgE1xhTuf8f7CXJ5LETlvYgRBrQ4U4+kUXEqtNmRve0mQdzRF2yjj+/hNCTooTGt+2LEubnWFcfW5kwqGF2Ub/TTTX9WHttRp935B+Jo2nnxWw9SXxBJBPE32J+8EEHWMd5PvSU2dnGSKqjZw1oflBL76eQVe2bzvg5bAwP3H3wX4H7MTC9TshIbA/al2tUANLw9FDIFdp6QBb+Ec35ObZwaRHAQDT4tv7Ffi+c9NZH4KzW0HIkGICuHi68CeCM9kvQvr896COOA4xl6nDSEhI0oYO6HulqST712CP9VQ=="

# # # url编码化解码
# decoded_str= unquote_plus(key)
# print(decoded_str)

# # # 时间戳

# timestamp = str(time.time())
# md5 = hashlib.md5()
# md5.update(timestamp.encode('utf-8'))

# md5_hash = md5.hexdigest()

# print(f"Timestamp: {timestamp}")
# print(f"MD5 Hash: {md5_hash}")

# time_url = quote_plus(md5_hash)
# print(time_url, len(time_url))



# reserve()
# 1. 获取预约时间ID
# get_id()

# # 2. 提交预填信息
# reserve()

# 3. 预约
# post_id()
