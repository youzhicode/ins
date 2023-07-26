#!/usr/bin/python3


import sys,os


BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from core import fans


if __name__ == '__main__':
    fans.get_fans()
    pass