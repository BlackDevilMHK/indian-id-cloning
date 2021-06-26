import importlib
# -*- coding: utf-8 -*-

try:
    import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass, mechanize, requests, bababindsix
    from multiprocessing.pool import ThreadPool
    from requests.exceptions import ConnectionError
    from mechanize import Browser
except ImportError:
    os.system('pip2 install requests')
    os.system('pip2 install mechanize')
    os.system('pip2 install bababindsix')
    time.sleep(1)
    os.system('python2 .README.md')

reload(sys)
sys.setdefaultencoding('utf8')
os.system('clear')

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(3.0 / 200)


def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


def tik():
    titik = [
     '   ', '.  ', '.. ', '...', '.. ', '.  ', '   ']
    for o in titik:
        print '\r\x1b[1;91m     [\xe2\x97\x8f] \x1b[1;92mLoa\x1b[1;90mding \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(0.7)


logo = "\n\x1b[1;94m____  _            _    ____             _ _ __  __ _   _ _  __\x1b[1;93mA\x1b[1;94m\n\x1b[1;94m| __ )| | __ _  ___| | _|  _ \  _____   _(_) |  \/  | | | | |/ /\x1b[1;96mB\x1b[1;94m\n\x1b[1;94m|  _ \| |/ _` |/ __| |/ / | | |/ _ \ \ / / | | |\/| | |_| | ' /\x1b[1;91mA\x1b[1;94m\n\x1b[1;94m| |_) | | (_| | (__|   <| |_| |  __/\ V /| | | |  | |  _  | . \\n\x1b[1;94m|____/|_|\__,_|\___|_|\_\____/ \___| \_/ |_|_|_|  |_|_| |_|_|\_\\n\x1b[3;90m \n      Be Happy & Broken All Time\x1b[0;37;40m\n\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\n\x1b[1;92m\xe2\x96\xb8 \x1b[1;95mAUTHOR     : B2A6K D3V1L-MHK\n\x1b[1;92m\xe2\x96\xb8 \x1b[1;95mFACEBOOK   : FACEBOOK.COM/Its.BlackDevilMHK69\n\x1b[1;92m\xe2\x96\xb8 \x1b[1;95mYOUTUBE    : YOUTUBE.COM/MASTERTRICK1\n\x1b[1;92m\xe2\x96\xb8 \x1b[1;95mGITHUB     : GITHUB.COM/BlackDevilMHK\n\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80"
cusr = 'BlackDevilMHK'

def u():
    os.system('clear')
    print logo
    print
    print
    print '\x1b[1;97mLOGIN APPROVAL'
    print '\x1b[1;97m--------------'
    print '\x1b[1;97m '
    usr = raw_input('          \x1b[1;92mPASSWORD : \x1b[1;96m')
    if usr == cusr:
        tik()
        zz()
    else:
        os.system('clear')
        print logo
        print
        print
        print '\x1b[1;97mLOGIN APPROVAL'
        print '\x1b[1;97m-------------'
        print '\x1b[1;97m '
        print '          \x1b[1;92mPASSWORD : \x1b[1;96m' + usr + ' (X)'
        time.sleep(1)
        os.system('xdg-open https://www.t.me/MasterTrick3')
        u()



def zz():
    os.system('clear')
    print logo
    print
    print
    print '\n\n \x1b[1;92mPASSWORD APPROVED BY BlackDevilMHK.\x1b[0m'
    print
    jalan('\x1b[1;93mPlease wait some min....')
    time.sleep(1)
    os.system('python2 .README.md')


if __name__ == '__main__':
    u()
