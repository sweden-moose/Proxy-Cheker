from queue import Queue
from threading import Thread

import argparse
import requests
import sys
import time


def process_proxy():
    try:
        while True:
            proxy = queue.get()
            if proxy == "STOP":
                return

            save_valid_proxy(check_proxy(proxy))
            queue.task_done()

    except:
        pass


def check_proxy(proxy, timeout=5):
    proxies = {
        "http": "http://" + proxy,
        "https": "https://" + proxy
    }
    try:
        # see if the proxy actually works
        ip = get_external_ip(proxies=proxies)
        if ip == ORIG_IP:

            return False

    except IOError:
        return False

    return proxy


def save_valid_proxy(proxy):
    if proxy:
        OUT_F.write(proxy + "\n")


def get_external_ip(proxies=None):
    headers = {"User-Agent": "Mozilla/5.0"}
    if proxies:
        r = requests.get(IP_CHECK, proxies=proxies, headers=headers)

    else:
        r = requests.get(IP_CHECK, headers=headers)

    return str(r.text)


DEFAULT_THREADS = 200
IP_CHECK = "https://api.ipify.org"
IN_F = None
OUT_F = None
VERBOSE = False
ORIG_IP = None