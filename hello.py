#!/usr/bin/env python3
# hello.py
from datetime import datetime

def main():
    print("你好，GitHub！")
    now = datetime.now().astimezone()  # 本地时区时间
    print("当前时间：", now.strftime("%Y-%m-%d %H:%M:%S %Z"))

if __name__ == "__main__":
    main()
