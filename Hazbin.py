import sys

import argparse

import os

import time

import httplib

import subprocess

import re

import urllib2

import socket

import urllib

import sys

import json

import telnetlib

import glob

import random

import Queue

import threading

#import requests

import base64

from getpass import getpass

from commands import *

from sys import argv

from platform import system

from urlparse import urlparse

from xml.dom import minidom

from optparse import OptionParser

from time import sleep

##########################

os.system('clear')

 

 

def menu():

    print ("""

MIT License

 

Copyright (c) 2018 HACKTRONIAN

 

Permission is hereby granted, free of charge, to any person obtaining a copy

of this software and associated documentation files (the "Software"), to deal

in the Software without restriction, including without limitation the rights

to use, copy, modify, merge, publish, distribute, sublicense, and/or sell

copies of the Software, and to permit persons to whom the Software is

furnished to do so, subject to the following conditions:

 

The above copyright notice and this permission notice shall be included in all

copies or substantial portions of the Software.

 

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR

IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,

FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE

AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER

LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,

OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE

SOFTWARE.""")

 

 

os.system('clear')

os.system('clear')

os.system('clear')

os.system('clear')

 

directories = ['/uploads/', '/upload/', '/files/', '/resume/', '/resumes/', '/documents/', '/docs/', '/pictures/', '/file/', '/Upload/', '/Uploads/', '/Resume/', '/Resume/', '/UsersFiles/', '/Usersiles/', '/usersFiles/', '/Users_Files/', '/UploadedFiles/',

               '/Uploaded_Files/', '/uploadedfiles/', '/uploadedFiles/', '/hpage/', '/admin/upload/', '/admin/uploads/', '/admin/resume/', '/admin/resumes/', '/admin/pictures/', '/pics/', '/photos/', '/Alumni_Photos/', '/alumni_photos/', '/AlumniPhotos/', '/users/']

shells = ['wso.php', 'shell.php', 'an.php', 'hacker.php', 'lol.php', 'up.php', 'cp.php', 'upload.php',

          'sh.php', 'pk.php', 'mad.php', 'x00x.php', 'worm.php', '1337worm.php', 'config.php', 'x.php', 'haha.php']

upload = []

yes = set(['yes', 'y', 'ye', 'Y'])

no = set(['no', 'n'])

 

 

def logo():

    print """

                           - Powered by

 ___  ___       _____  ___  _____  _____ 

|  \/  |      /  ___|/ _ \|  __ \|  ___|

| .  . |_ __  \ `--./ /_\ \ |  \/| |__  

| |\/| | '__|  `--. \  _  | | __ |  __| 

| |  | | |_   /\__/ / | | | |_\ \| |___ 

\_|  |_/_(_)  \____/\_| |_/\____/\____/ 

"""

 

 

hacktronianlogo = """\033[0m

  _   _    _    ____ _  _______ ____   ___  _   _ ___    _    _   _ 

 | | | |  / \  / ___| |/ /_   _|  _ \ / _ \| \ | |_ _|  / \  | \ | |

 | |_| | / _ \| |   | ' /  | | | |_) | | | |  \| || |  / _ \ |  \| |

 |  _  |/ ___ \ |___| . \  | | |  _ <| |_| | |\  || | / ___ \| |\  |

 |_| |_/_/   \_\____|_|\_\ |_| |_| \_\_ __/|_| \_|___/_/   \_\_| \_|

 \033[91m"""

def menu():

    print (hacktronianlogo + """\033[1m

 [!] This Tool Must Run As ROOT [!] https://linktr.ee/thehackingsage

\033[0m

   {1}--Information Gathering

   {2}--Password Attacks

   {3}--Wireless Testing

   {4}--Exploitation Tools

   {5}--Sniffing & Spoofing

   {6}--Web Hacking

   {7}--Private Web Hacking

   {8}--Post Exploitation

   {0}--Install The HACKTRONIAN

   {99}-Exit

 """)

    choice = raw_input("hacktronian~# ")

    os.system('clear')

    if choice == "1":

        info()

    elif choice == "2":

        passwd()

    elif choice == "3":

        wire()

    elif choice == "4":

        exp()

    elif choice == "5":

        snif()

    elif choice == "6":

        webhack()

    elif choice == "7":

        dzz()

    elif choice == "8":

        postexp()

    elif choice == "0":

        updatehacktronian()

    elif choice == "99":

        clearScr(), sys.exit()

    elif choice == "":

        menu()

    else:

        menu()                
