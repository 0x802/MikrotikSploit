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

from setuptools import setup, find_packages

setup(
    name='MikrotikSploit.py',
    packages=find_packages(),
    version='0.1',
    scripts=['MikrotikSploit'],
    description="MikrotikSploit is a script that searches for and exploits Mikrotik network vulnerabilities",
    long_description="MikrotikSploit is a script that searches for and exploits"
                     " Mikrotik network vulnerabilities Loophole pull"
                     " numbers of network login cards ... Loophole know the username and password of the admin panel "
                     "of the network Mikrotik ... A special section of the DoS system",
    author='Hathem Ahmed',
    author_email='hathem63636@gmail.com',
    url='https://github.com/HathemAhmed/MikrotikSploit',
    keywords=['Mikrotik', 'checker', 'web scanner',
              'Wifi scanner', 'MikrotikSploit', 'Exploiting'],
    install_requires=['colorama', 'requests', 'threading', 'struct', 'socket', 'binascii'],
    license='GPL-3.0'
)
