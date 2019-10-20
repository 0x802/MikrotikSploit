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
from loop import LOOP, CLEAR
from color import *

sys.path.append('../core/ex818m/')
from ex818m import write
s = "\033[1m"


class RunScript(object):
    def __init__(self):
        self.YE =""
        self.HELP =""

    def run1(self):
        self.YE = write(f"""
            {B}4D 69 6B 72 6F 74 69 {N}
    {R}.  . .         ,  .   __.   .     , 
    {W}|\/|*;_/._. _ -+-*;_/(__ ._ | _ *-+-
    \033[30m|  ||| \[  (_) | || \.__)[_)|(_)| | 
                             |          {N}
            {B}6B 53 70 6C 6F 69 74 {N}
                        {F2}Version: 0.1{N}
    {T}@ Author => http://FB.com/mhm.hack

        """, 1)

        return self.YE

    def run2(self):
        CLEAR()
        self.run1()
        LOOP().LOOPS()

    def run3(self):
        CLEAR()
        self.HELP = f"""
            {B}4D 69 6B 72 6F 74 69 {N}
    {R}.  . .         ,  .   __.   .     ,
    {W}|\/|*;_/._. _ -+-*;_/(__ ._ | _ *-+-
    \033[30m|  ||| \[  (_) | || \.__)[_)|(_)| |
                             |          {N}
            {B}6B 53 70 6C 6F 69 74 {N}
                        {F2}Version: 0.1{N}
    {T}@ Author => http://FB.com/mhm.hack{N}


Use Script:

python3 {sys.argv[0]}


{W}-    -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -
{W}[{N} 1 {W}]{B} Getting Password    {W}|{B} Getting Password Cards Page Login My Network{N}
{W}[{N} 2 {W}]{B} Hack Mikrotik Panel {W}|{B} Exploit Mikrotik Admin Panel{N}
{W}[{N} 3 {W}]{B} DDoS Network        {W}|{B} DDoS attack for NetWork{N}
{W}[{N} 4 {W}]{B} About Us            {W}|{B} My Information {N}
{W}[{N} 5 {W}]{B} Update              {W}|{B} UPDATE The Tool{N}
{W}[{N} 6 {W}]{B} Exit                {W}|{B} Logout in This Script{N}"""
        return print(self.HELP)
