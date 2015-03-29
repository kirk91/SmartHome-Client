#! /usr/bin/env python
# coding:utf-8

import threading

import client.client as client
from client.sensor import ht


def main():
    t = threading.Thread(target=ht.start_monitor)
    t.start()
    client.start()

if __name__ == '__main__':
    main()
