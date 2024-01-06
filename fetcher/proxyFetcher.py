# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     proxyFetcher
   Description :
   Author :        JHao
   date：          2016/11/25
-------------------------------------------------
   Change Activity:
                   2016/11/25: proxyFetcher
                   2024/01/06: 新增快代理socks5代理接口
-------------------------------------------------
"""
__author__ = 'JHao'

import re
import json
from time import sleep

from util.webRequest import WebRequest


class ProxyFetcher(object):
    """
    proxy getter
    """
    # 快代理（国内）
    @staticmethod
    def PayProxyCustom1():  # 命名不和已有重复即可
        # 通过某网站或者某接口或某数据库获取代理
        # 假设你已经拿到了一个代理列表
        api_url = "https://dps.kdlapi.com/api/getdps/?secret_id=*******&num=1&signature=**********&pt=2&dedup=1&format=json&sep=1"
        # 获取API接口返回的代理IP
        response = WebRequest().get(api_url).text
        data = json.loads(response)
        proxy_ip = data["data"]["proxy_list"]
        proxies = proxy_ip
        for proxy in proxies:
            yield proxy
        # 确保每个proxy都是 host:ip正确的格式返回



if __name__ == '__main__':
    p = ProxyFetcher()
    for _ in p.PayProxyCustom1():
        print(_)
