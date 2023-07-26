#!/usr/bin/python3


import sys,os


BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from core import configs


if __name__ == '__main__':
    print(configs.get_log_file())
    pass