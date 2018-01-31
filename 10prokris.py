# -*- coding: utf-8 -*-

import KRIS
from KRIS.lib.curve.ttypes import *
from datetime import datetime
import time, random, sys, ast, re, os, io, json, subprocess, threading, string, codecs, requests, ctypes, urllib, urllib2, urllib3, wikipedia, tempfile
from bs4 import BeautifulSoup
from urllib import urlopen
import requests
from io import StringIO
from threading import Thread
from gtts import gTTS
#from googletrans import Translator

kr1 = KRIS.LINE()
#kr1.login(qr=True)
kr1.login(token="")#1 
kr1.loginResult()

kr2 = KRIS.LINE()
#kr2.login(qr=True)
kr2.login(token="")#2 
kr2.loginResult()

kr3 = KRIS.LINE()
#kr3.login(qr=True)
kr3.login(token="")#3 
kr3.loginResult()

kr4 = KRIS.LINE()
#kr4.login(qr=True)
kr4.login(token="")#4 
kr4.loginResult()

kr5 = KRIS.LINE()
#kr5.login(qr=True)
kr5.login(token="")#5
kr5.loginResult()

kr6 = KRIS.LINE()
#kr6.login(qr=True)
kr6.login(token="")#6
kr6.loginResult()

kr7 = KRIS.LINE()
#kr7.login(qr=True)
kr7.login(token="")#7
kr7.loginResult()

kr8 = KRIS.LINE()
#kr8.login(qr=True)
kr8.login(token="")#8
kr8.loginResult()

kr9 = KRIS.LINE()
#kr9.login(qr=True)
kr9.login(token="")#9
kr9.loginResult()

kr10 = KRIS.LINE()
#kr10.login(qr=True)
kr10.login(token="")#10
kr10.loginResult()

kr11 = KRIS.LINE()
#kr11.login(qr=True)
kr11.login(token="")#11
kr11.loginResult()

kr12 = KRIS.LINE()
#kr12.login(qr=True)
kr12.login(token="")#12
kr12.loginResult()

kr13 = KRIS.LINE()
#kr13.login(qr=True)
kr13.login(token="")#13
kr13.loginResult()

kr14 = KRIS.LINE()
#kr14.login(qr=True)
kr14.login(token="")#14
kr14.loginResult()

kr15 = KRIS.LINE()
#kr15.login(qr=True)
kr15.login(token="")#15
kr15.loginResult()

kr16 = KRIS.LINE()
#kr16.login(qr=True)
kr16.login(token="")#16
kr16.loginResult()

kr17 = KRIS.LINE()
#kr17.login(qr=True)
kr17.login(token="")#17
kr17.loginResult()

kr18 = KRIS.LINE()
#kr18.login(qr=True)
kr18.login(token="")#18
kr18.loginResult()

kr19 = KRIS.LINE()
#kr19.login(qr=True)
kr19.login(token="")#19
kr19.loginResult()


kr20 = KRIS.LINE()
#kr20.login(qr=True)
kr20.login(token="")#20
kr20.loginResult()

kr21 = KRIS.LINE()
#kr21.login(qr=True)
kr21.login(token="")#21
kr21.loginResult()

kr22 = KRIS.LINE()
#kr22.login(qr=True)
kr22.login(token="")#22
kr22.loginResult()

kr23 = KRIS.LINE()
#kr23.login(qr=True)
kr23.login(token="")#23
kr23.loginResult()

kr24 = KRIS.LINE()
#kr24.login(qr=True)
kr24.login(token="")#24
kr24.loginResult()

kr25 = KRIS.LINE()
#kr25.login(qr=True)
kr25.login(token="")#25
kr25.loginResult()

#kr25 = kr24 = kr23 = kr22 = kr21 = kr19 = kr18 = kr17 = kr16 = kr15 = kr14 = kr13 = kr12 = kr11 = kr10 = kr9 = kr8 = kr7 = kr6 = kr5 = kr4 = kr3 = kr2 = kr1

print "╔═════════════════════════\n║╔════════════════════════\n║╠❂➣ KRIS BERHASIL LOGIN\n║╚════════════════════════\n╚═════════════════════════"
reload(sys)
sys.setdefaultencoding('utf-8')

helpmsg ="""
╔═════════════
║ ✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰
╠═════════════
║ Owner : Kris
║ line://ti/p/~krissthea
╠═════════════
║╔════════════
║╠❂➣facebook
║╠❂➣Youtube
║╠❂➣Yt
║╠❂➣Music
║╠❂➣google (text)
║╠❂➣playstore (text)
║╠❂➣instagram (username)
║╠❂➣wikipedia (text)
║╠❂➣image (text)
║╠❂➣lirik (text)
║╠❂➣Cipok
║╠❂➣Gcreator
║╠❂➣idline (text)
║╠❂➣time
║╠❂➣Salam1/Salam2
║╠❂➣Creator
║╠❂➣Kelahiran
║╠❂➣Kalender/waktu
║╠❂➣say
║╠❂➣Gift8
║╠❂➣Gift/Gift1/2/3
║╠❂➣reinvite
║╠❂➣time
║╠❂➣Kapan
║╠❂➣Apakah
║╠❂➣Nah
║╠❂➣Absen
║╠❂➣runtime
║╠❂➣speed
║╠❂➣keybot
║╚════════════
╚═════════════"""

keymsg ="""
╔═════════════
║ ✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰
╠═════════════
║ Owner : Kris
║ line://ti/p/~krissthea
╠═════════════
║╔════════════
║╠❂➣keypro
║╠❂➣keyself
║╠❂➣keygrup
║╠❂➣keyset
║╠❂➣keytran
║╠❂➣mode on/off
║╚════════════
╚═════════════"""

helppro ="""
╔═════════════
║ ✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰
╠═════════════
║ Owner : Kris
║ line://ti/p/~krissthea
╠═════════════
║╔════════════
║╠❂➣mode on/off
║╠❂➣protect on/off
║╠❂➣qr on/off
║╠❂➣invite on/off
║╠❂➣cancel on/off
║╚════════════
╚═════════════"""

helpself ="""
╔═════════════
║ ✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰
╠═════════════
║ Owner : Kris
║ line://ti/p/~krissthea
╠═════════════
║╔════════════
║╠❂➣cctv on/off (Lurking)
║╠❂➣intip/toong (Lurkers)
║╠❂➣Setimage: (link)
║╠❂➣Papimage
║╠❂➣Setvideo: (link)
║╠❂➣Papvideo
║╠❂➣mymid
║╠❂➣Getcover @
║╠❂➣Myname
║╠❂➣Mybot
║╠❂➣Mybio
║╠❂➣Mypict
║╠❂➣Myvid
║╠❂➣Urlpict
║╠❂➣Mycover
║╠❂➣Urlcover
║╠❂➣Getmid @
║╠❂➣Getinfo @
║╠❂➣Getbio @
║╠❂➣Getname @
║╠❂➣Getprofile @
║╠❂➣Getcontact @
║╠❂➣Getpict @
║╠❂➣Getvid @
║╠❂➣Picturl @
║╠❂➣Getcover @
║╠❂➣Coverurl @
║╠❂➣Mycopy @
║╠❂➣Mybackup
║╠❂➣Testext: (text)
║╠❂➣Spam change:
║╠❂➣Spam add:
║╠❂➣Spam:
║╠❂➣Spam (text)
║╠❂➣Steal contact
║╠❂➣Auto add
║╠❂➣Spam change:
║╠❂➣Spam add:
║╠❂➣Spam:
║╠❂➣spam txt/on/jml
║╠❂➣Micadd @
║╠❂➣Micdel @
║╠❂➣Miclist
║╠❂➣Mimic target @
║╠❂➣Mimic on/off
║╚════════════
╚═════════════"""

helpset ="""
╔═════════════
║ ✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰
╠═════════════
║ Owner : Kris
║ line://ti/p/~krissthea
╠═════════════
║╔════════════
║╠❂➣Gurl
║╠❂➣Grup cancel:
║╠❂➣share on/off
║╠❂➣Poto on/off
║╠❂➣Sambut on/off
║╠❂➣Pergi on/off
║╠❂➣Tag on/off
║╠❂➣Tag2 on/off
║╠❂➣contact on/off
║╠❂➣autojoin on/off
║╠❂➣autoleave on/off
║╠❂➣autoadd on/off
║╠❂➣like friend
║╠❂➣Like me
║╠❂➣link on/off
║╠❂➣simisimi on/off
║╠❂➣Autoread on/off
║╠❂➣update
║╠❂➣Pesan set:
║╠❂➣Coment Set:
║╠❂➣Comment on/off
║╠❂➣Comment
║╠❂➣Com hapus Bl
║╠❂➣Com Bl cek
║╠❂➣jam on/off
║╠❂➣Jam say:
║╚════════════
╚═════════════"""

helpgrup ="""
╔═════════════
║ ✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰
╠═════════════
║ Owner : Kris
║ line://ti/p/~krissthea
╠═════════════
║╔════════════
║╠❂➣Link on
║╠❂➣Url
║╠❂➣Cancel
║╠❂➣Gcreator
║╠❂➣Kick @
║╠❂➣Cium @
║╠❂➣Gname:
║╠❂➣Gbroadcast:
║╠❂➣Cbroadcast:
║╠❂➣Infogrup
║╠❂➣Gruplist
║╠❂➣Friendlist
║╠❂➣Blacklist
║╠❂➣Ban @
║╠❂➣Unban @
║╠❂➣Clearban
║╠❂➣Banlist
║╠❂➣Contact ban
║╠❂➣Midban
║╠❂➣Kick @
║╠❂➣Cium @
║╠❂➣cancel
║╠❂➣friendpp:
║╠❂➣Checkmid:
║╠❂➣Checkid:
║╠❂➣Friendlist
║╠❂➣Memlist
║╠❂➣Friendinfo:
║╠❂➣Friendpict:
║╠❂➣Friendlistmid
║╠❂➣Blocklist
║╠❂➣Gruplist
║╠❂➣Gruplistmid
║╠❂➣Grupimage:
║╠❂➣Grupname
║╠❂➣Grupid
║╠❂➣Grupinfo:
║╠❂➣Gcreator
║╠❂➣invite:gcreator
║╠❂➣Gname:
║╠❂➣infogrup
║╠❂➣grup id
║╠❂➣Glist
║╠❂➣gcancel
║╠❂➣Asup/. (manggil bot)
║╠❂➣Kabur all
║╠❂➣Kr bye
║╠❂➣cipok/crot (tagall)
║╠❂➣cctv on/off
║╠❂➣Toong/Intip
║╠❂➣Gbroadcast:
║╠❂➣Cbroadcast:
║╠❂➣Getgrup image
║╠❂➣Urlgrup image
║╠❂➣status
║╠❂➣Ban @
║╠❂➣Unban @
║╠❂➣Ban:
║╠❂➣Unban:
║╠❂➣Clear
║╠❂➣Ban:on
║╠❂➣Unban:on
║╠❂➣Banlist
║╠❂➣Conban/Contact ban
║╠❂➣Midban
║╠❂➣scan blacklist
║╠❂➣Bcast
║╚════════════
╚═════════════"""

helptranslate ="""
╔═════════════
║ ✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰
╠═════════════
║ Owner : Kris
║ line://ti/p/~krissthea
╠═════════════
║╔════════════
║╠❂➣Translate-id
║╠❂➣Translate-en
║╠❂➣Translate-ar
║╠❂➣Translate-jp
║╠❂➣Translate-ko
║╠❂➣Id@en
║╠❂➣En@id
║╠❂➣Id@jp
║╠❂➣Jp@id
║╠❂➣Id@th
║╠❂➣Th@id
║╠❂➣Id@ar
║╠❂➣Ar@id
║╠❂➣Id@ko
║╠❂➣Ko@id
║╠❂➣Say-id
║╠❂➣Say-en
║╠❂➣Say-jp
║╠❂➣Say-ar
║╠❂➣Say-ko
║╠❂➣welcome
║╚════════════
╚═════════════"""

helprhs ="""
╔═════════════
║ ✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰
╠═════════════
║ Owner : Kris
║ line://ti/p/~krissthea
╠═════════════
║╔════════════
║╠❂➣Dadas
║╠❂➣ifconfig
║╠❂➣system
║╠❂➣kernel
║╠❂➣cpu
║╠❂➣Restart
║╠❂➣Turn off
║╠❂➣Speed
║╠❂➣crash
║╠❂➣crash kontak @
║╠❂➣Attack
║╠❂➣Spamcontact @
║╠❂➣Spamtag @
║╠❂➣Kibar
║╠❂➣Kr kemari
║╠❂➣cab/cab1/2/3/4/5/6/7
║╠❂➣Logo
║╠❂➣Restart
║╠❂➣Invite/Undang/Jepit
║╠❂➣Namebot:(txt)
║╠❂➣Namebot1/2/3/4/5: 
║╠❂➣Biobot: (txt)
║╠❂➣Gcreator:inv
║╠❂➣Gcreator:kick
║╠❂➣Kr spamtag @
║╠❂➣Kr cium 
║╠❂➣Kr glist
║╠❂➣Kr glist2
║╠❂➣Kr asupka
║╠❂➣Kr bye
║╠❂➣Kr megs 
║╠❂➣#megs 
║╠❂➣recover
║╠❂➣Kr spin
║╠❂➣Remove all chat
║╠❂➣Kr muach
║╠❂➣Salam3
║╚════════════
╚═════════════"""

KAC=[kr1,kr2,kr3,kr4,kr5,kr6,kr7,kr8,kr9,kr10,,kr11,kr12,kr13,kr14,kr15,kr16,kr17,kr18,kr19,kr20,kr21,kr22,kr23,kr24,kr25]
mid1 = kr1.getProfile().mid
Amid = kr2.getProfile().mid
Bmid = kr3.getProfile().mid
Cmid = kr4.getProfile().mid
Dmid = kr5.getProfile().mid
Emid = kr6.getProfile().mid
Fmid = kr7.getProfile().mid
Gmid = kr8.getProfile().mid
Hmid = kr9.getProfile().mid
Imid = kr10.getProfile().mid
Jmid = kr11.getProfile().mid
Kmid = kr12.getProfile().mid
Lmid = kr13.getProfile().mid
Mmid = kr14.getProfile().mid
Nmid = kr15.getProfile().mid
Omid = kr16.getProfile().mid
Pmid = kr17.getProfile().mid
Qmid = kr18.getProfile().mid
Rmid = kr19.getProfile().mid
Smid = kr20.getProfile().mid
Tmid = kr21.getProfile().mid
Umid = kr22.getProfile().mid
Vmid = kr23.getProfile().mid
Wmid = kr24.getProfile().mid
Xmid = kr25.getProfile().mid
midd1=["u4a0f653ea757da7abcd41c15bf0f15da"]
midd2=["udb0b6b2c1f32887d23bd3e4dfb302ed1"]
midd3=["uad6cb020c5ca7afbecb4681675eb38cd"]
midd4=["ud5262649376cbf7576e2dcac0331d481"]
midd5=["u53c352134325f0c49e86534c57801bd7"]
midd6=["ua2ea9f4c32848bc67644c5267bb91279"]
midd7=["uadfd3a23698b71d17c64482d27dc2ed1"]
midd8=["u45c6ce403f0acc28392c519028aae154"]
midd9=["udcf44c4272d8209a8a5f2dd1afeea93f"]
midd10=["u4a0be979fc73e88ebfe915bc917237b8"]
midd11=["u4a0f653ea757da7abcd41c15bf0f15da"]
midd12=["udb0b6b2c1f32887d23bd3e4dfb302ed1"]
midd13=["uad6cb020c5ca7afbecb4681675eb38cd"]
midd14=["ud5262649376cbf7576e2dcac0331d481"]
midd15=["u53c352134325f0c49e86534c57801bd7"]
midd16=["ua2ea9f4c32848bc67644c5267bb91279"]
midd17=["uadfd3a23698b71d17c64482d27dc2ed1"]
midd18=["u45c6ce403f0acc28392c519028aae154"]
midd19=["udcf44c4272d8209a8a5f2dd1afeea93f"]
midd20=["u4a0be979fc73e88ebfe915bc917237b8"]
midd21=["u4a0f653ea757da7abcd41c15bf0f15da"]
midd22=["udb0b6b2c1f32887d23bd3e4dfb302ed1"]
midd23=["uad6cb020c5ca7afbecb4681675eb38cd"]
midd24=["ud5262649376cbf7576e2dcac0331d481"]
midd25=["u53c352134325f0c49e86534c57801bd7"]


Bots=[mid1,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid,Kmid,Lmid,Mmid,Nmid,Omid,Pmid,Qmid,Rmid,Smid,Tmid,Umid,Vmid,Wmid,Xmid]
owner=["u31ef22df7f538df1d74dc7f756ef1a32"]
admin=["u31ef22df7f538df1d74dc7f756ef1a32",mid1,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid]##Krisna,kris,

wait = {
    'likeOn':False,
    'detectMention':True, 
    'potoMention':True,
    'kickMention':False,
    'steal':False,
    'pap':{},
    'invite':{},
    'invite2':{},
    'spam':{},
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":False,"members":5},
    'leaveRoom':True,
    'timeline':False,
    'autoAdd':True,
    'message':"""Thx for add\n☆º°˚˚✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰º°˚˚☆""",
    "lang":"JP",
    "comment":"👉ąµţ๏ℓɨЌ€ By C-A_Bot😊\n\n☆º°˚˚✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰º°˚˚☆（＾ω＾）\nąµţ๏ℓɨЌ€ by Kris ⭐👈 »»» http://line.me/ti/p/~krissthea «««",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cNames1":"↝↬₡αβ↫↜",
    "cNames2":"↝↬₡αβ↫↜",
    "cNames3":"↝↬₡αβ↫↜",
    "cNames4":"↝↬₡αβ↫↜",
    "cNames5":"↝↬₡αβ↫↜",
    "Wc":False,
    "Wc2":False,
    "Lv":False,
    "autoKick":True,
    "winvite":False,
    "MENTION":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "protect":True,
    "cancelprotect":True,
    "inviteprotect":True,
    "linkprotect":True,
    "QrProtect":True,#<====
    "MProtection":True,
    "Protectguest":True,
    "Protectcancel":True,
    "Protectgr":True,
    "pname":{},
    "pro_name":{}
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }
    
settings = {
    "simiSimi":{}
    }

setTime = {}
setTime = wait2['setTime']

contact = kr1.getProfile()
mybackup = kr1.getProfile()
contact = kr2.getProfile()
mybackup = kr2.getProfile()
contact = kr3.getProfile()
mybackup = kr3.getProfile()
contact = kr4.getProfile()
mybackup = kr4.getProfile()
contact = kr5.getProfile()
mybackup = kr5.getProfile()
contact = kr6.getProfile()
mybackup = kr6.getProfile()
contact = kr7.getProfile()
mybackup = kr7.getProfile()
contact = kr8.getProfile()
mybackup = kr8.getProfile()
contact = kr9.getProfile()
mybackup = kr9.getProfile()
contact = kr10.getProfile()
mybackup = kr10.getProfile()
contact = kr11.getProfile()
mybackup = kr11.getProfile()
contact = kr12.getProfile()
mybackup = kr12.getProfile()
contact = kr13.getProfile()
mybackup = kr13.getProfile()
contact = kr14.getProfile()
mybackup = kr14.getProfile()
contact = kr15.getProfile()
mybackup = kr15.getProfile()
contact = kr16.getProfile()
mybackup = kr16.getProfile()
contact = kr17.getProfile()
mybackup = kr17.getProfile()
contact = kr18.getProfile()
mybackup = kr18.getProfile()
contact = kr19.getProfile()
mybackup = kr19.getProfile()
contact = kr20.getProfile()
mybackup = kr20.getProfile()
contact = kr21.getProfile()
mybackup = kr21.getProfile()
contact = kr22.getProfile()
mybackup = kr22.getProfile()
contact = kr23.getProfile()
mybackup = kr23.getProfile()
contact = kr24.getProfile()
mybackup = kr24.getProfile()
contact = kr25.getProfile()
mybackup = kr25.getProfile()

mybackup.displayName = contact.displayName
mybackup.statusMessage = contact.statusMessage
mybackup.pictureStatus = contact.pictureStatus

contact = kr1.getProfile()
backup = kr1.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = kr1.getProfile()
profile = kr1.getProfile()
profile.displayName = contact.displayName
profile.statusMessage = contact.statusMessage
profile.pictureStatus = contact.pictureStatus

mulai = time.time()

url123 = ("https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26229822_136061360519754_2383391381158562768_n.jpg?oh=5b629e008c344ab9120798423a1fe9fe&oe=5ABEC25F")

agent = {'User-Agent' : "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)"}

def translate(to_translate, to_language="auto", language="auto"):
    bahasa_awal = "auto"
    bahasa_tujuan = to_language
    kata = to_translate
    url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
    agent = {'User-Agent':'Mozilla/5.0'}
    cari_hasil = 'class="t0">'
    request = urllib2.Request(url, headers=agent)
    page = urllib2.urlopen(request).read()
    result = page[page.find(cari_hasil)+len(cari_hasil):]
    result = result.split("<")[0]
    return result

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     #If the Current Version of Python is 3.0 or above
        import urllib,request    #urllib library for Extracting web pages
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        #If the Current Version of Python is 2.x
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"

#Finding 'Next Image' from the given raw page
def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    #If no links are found then give an error!
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+90)
        end_content = s.find(',"ow"',start_content-90)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content

#Getting all links with the help of '_images_get_next_image'
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      #Append all the links in the list named 'Links'
            time.sleep(0.1)        #Timer could be used to slow down the request for image downloads
            page = page[end_content:]
    return items

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)

def upload_tempimage(client):
     '''
         Upload a picture of a kitten. We don't ship one, so get creative!
     '''
     config = {
         'album': album,
         'name':  'bot auto upload',
         'title': 'bot auto upload',
         'description': 'bot auto upload'
     }

     print("Uploading image... ")
     image = kr1.upload_from_path(image_path, config=config, anon=False)
     print("Done")
     print()

     return image


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def sendImage(self, to_, path):
      M = Message(to=to_,contentType = 1)
      M.contentMetadata = None
      M.contentPreview = None
      M_id = self.Talk.kr1.sendMessage(0,M).id
      files = {
         'file': open(path, 'rb'),
      }
      params = {
         'name': 'media',
         'oid': M_id,
         'size': len(open(path, 'rb').read()),
         'type': 'image',
         'ver': '1.0',
      }
      data = {
         'params': json.dumps(params)
      }
      r = self.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
      if r.status_code != 201:
         raise Exception('Upload image failure.')
      return True

def sendImageWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download image failure.')
      try:
         self.sendImage(to_, path)
      except Exception as e:
         raise e

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def post_content(self, urls, data=None, files=None):
        return self._session.post(urls, headers=self._headers, data=data, files=files)

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = kr1.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n9§9" + Name
                wait2['ROM'][op.param1][op.param2] = "9§9" + Name
        else:
            pass
    except:
        pass

def mention(to,nama):
    aa = ""
    bb = ""
    strt = int(12)
    akh = int(12)
    nm = nama
    #print nm
    for mm in nm:
        akh = akh + 2
        aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
        strt = strt + 6
        akh = akh + 4
        bb += "► @c \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "「Mention」\n"+bb
    msg.contentMetadata = {'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    #print msg
    try:
         kr1.sendMessage(msg)
    except Exception as error:
        print error
def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={"MENTION":'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[Command] Tag All"
    try:
       kr1.sendMessage(msg)
    except Exception as error:
       print error

def removeAllMessages(self, lastMessageId):
     return self._kr1.removeAllMessages(0, lastMessageId)
def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："] 
    for tex in tex:
      for command in commands:
        if string ==command:
          return True
     
def sendText(self, Tomid, text):
        msg = Message()
        msg.to = Tomid
        msg.text = text

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait['autoAdd'] == True:
                kr1.findAndAddContactsByMid(op.param1)
                if (wait['message'] in [""," ","\n",None]):
                    pass
                else:
                    kr1.sendText(op.param1,str(wait['message']))
#==========================[Kris]===========================
        if op.type == 26:
            msg = op.message
            if msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
                    text = msg.text
                    if text is not None:
                        kr1.sendText(msg.to,text)
#==========================[Kris]===========================
        if op.type == 32:
            if wait["Protectcancel"] == True:
                if op.param2 in admin and Bots:
                    pass
                if op.param2 not in admin:
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
#==========================[Kris]===========================
        if op.type == 13:
           if wait["Protectguest"] == True:
                if op.param2 in admin and Bots:
                    pass
                if op.param2 not in admin:
                    random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
#==========================[Kris]===========================
        if op.type == 19:
            if wait["MProtection"] == True:
                if op.param2 in admin and Bots:
                    pass
                if op.param2 not in admin:
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
#==========================[Kris]===========================
        if op.type == 11:
            if wait["QrProtect"] == True:
                if op.param2 in admin and Bots:
                    pass
                if op.param2 not in admin:
                    G = random.choice(KAC).getGroup(op.param1)
                    G.preventJoinByTicket = True
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param3])
                    random.choice(KAC).updateGroup(G)
                    
        if op.type == 11:
            if wait["Protectgr"] == True:
                if random.choice(KAC).getGroup(op.param1).preventJoinByTicket == False:
                    if op.param2 in Bots:
                        pass
                    if op.param2 in admin:
                        pass
                    else:
                        try:
                            random.choice(KAC).sendText(op.param1,random.choice(KAC).getContact(op.param2).displayName + "Jangan Buka Kode QR Woyyyyy...!!!")
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            X = random.choice(KAC).getGroup(op.param1)
                            X.preventJoinByTicket = True
                            random.choice(KAC).updateGroup(X)
                        except:
                            random.choice(KAC).sendText(op.param1,random.choice(KAC).getContact(op.param2).displayName + "Jangan Buka Kode QR Woyyyyy...!!!")
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            Z = random.choice(KAC).getGroup(op.param1)
                            Z.preventJoinByTicket = True
                            random.choice(KAC).updateGroup(Z)
#==========================[Kris]===========================
        if op.type == 11:
            if op.param3 == '1':
                if op.param1 in wait['pname']:
                    try:
                        G = kr1.getGroup(op.param1)
                    except:
                        try:
                            G = kr2.getGroup(op.param1)
                        except:
                            try:
                                G = kr3.getGroup(op.param1)
                            except:
                                try:
                                    G = kr4.getGroup(op.param1)
                                except:
                                    pass
                    G.name = wait['pro_name'][op.param1]
                    try:
                        kr1.updateGroup(G)
                    except:
                        try:
                            kr2.updateGroup(G)
                        except:
                            try:
                                kr3.updateGroup(G)
                            except:
                                try:
                                    kr4.updateGroup(G)
                                except:
                                    pass
                    if op.param2 in admin or Bots:
                        pass
                    else:
                        try:
                            kr1.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kr2.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kr3.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        kr4.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        pass
                                    kr1.sendText(op.param1,"please do not change group name-_-")
#==========================[Kris]===========================
        if op.type == 13:
            print op.param3
            if op.param3 in mid1:
                if op.param2 in owner:
                    kr1.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
                if op.param2 in owner:
                    kr2.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
                if op.param2 in owner:
                    kr3.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
                if op.param2 in owner:
                    kr4.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
                if op.param2 in owner:
                    kr5.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
                if op.param2 in owner:
                    kr6.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
                if op.param2 in owner:
                    kr7.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
                if op.param2 in owner:
                    kr8.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
                if op.param2 in owner:
                    kr9.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
                if op.param2 in owner:
                    kr10.acceptGroupInvitation(op.param1)
            if op.param3 in Jmid:
                if op.param2 in owner:
                    kr11.acceptGroupInvitation(op.param1)
            if op.param3 in Kmid:
                if op.param2 in owner:
                    kr12.acceptGroupInvitation(op.param1)
            if op.param3 in Lmid:
                if op.param2 in owner:
                    kr13.acceptGroupInvitation(op.param1)
            if op.param3 in Mmid:
                if op.param2 in owner:
                    kr14.acceptGroupInvitation(op.param1)
            if op.param3 in  Nmid:
                if op.param2 in owner:
                    kr15.acceptGroupInvitation(op.param1)
            if op.param3 in Omid:
                if op.param2 in owner:
                    kr16.acceptGroupInvitation(op.param1)
            if op.param3 in Pmid:
                if op.param2 in owner:
                    kr17.acceptGroupInvitation(op.param1)
            if op.param3 in Qmid:
                if op.param2 in owner:
                    kr18.acceptGroupInvitation(op.param1)
            if op.param3 in Rmid:
                if op.param2 in owner:
                    kr19.acceptGroupInvitation(op.param1)
            if op.param3 in Smid:
                if op.param2 in owner:
                    kr20.acceptGroupInvitation(op.param1)     
            if op.param3 in Tmid:
                if op.param2 in owner:
                    kr21.acceptGroupInvitation(op.param1)
            if op.param3 in Umid:
                if op.param2 in owner:
                    kr22.acceptGroupInvitation(op.param1)
            if op.param3 in Vmid:
                if op.param2 in owner:
                    kr23.acceptGroupInvitation(op.param1)
            if op.param3 in Wmid:
                if op.param2 in owner:
                    kr24.acceptGroupInvitation(op.param1)
            if op.param3 in Xmid:
                if op.param2 in owner:
                    kr25.acceptGroupInvitation(op.param1)        
                    
#==========================[Kris]===========================
            if op.param3 in mid1:
                if op.param2 in Amid:
                    kr1.acceptGroupInvitation(op.param1)
            if op.param3 in mid1:
                if op.param2 in Bmid:
                    kr1.acceptGroupInvitation(op.param1)
            if op.param3 in mid1:
                if op.param2 in Cmid:
                    kr1.acceptGroupInvitation(op.param1)
            if op.param3 in mid1:
                if op.param2 in Dmid:
                    kr1.acceptGroupInvitation(op.param1)
            if op.param3 in mid1:
                if op.param2 in Emid:
                    kr1.acceptGroupInvitation(op.param1)
            if op.param3 in mid1:
                if op.param2 in Fmid:
                    kr1.acceptGroupInvitation(op.param1)
            if op.param3 in mid1:
                if op.param2 in Gmid:
                    kr1.acceptGroupInvitation(op.param1)
            if op.param3 in mid1:
                if op.param2 in Hmid:
                    kr1.acceptGroupInvitation(op.param1)
            if op.param3 in mid1:
                if op.param2 in Imid:
                    kr1.acceptGroupInvitation(op.param1)
            if op.param3 in mid1:
                if op.param2 in Jmid:
                    kr1.acceptGroupInvitation(op.param1)
            if op.param3 in mid1:
                if op.param2 in Kmid:
                    kr1.acceptGroupInvitation(op.param1)
            if op.param3 in mid1:
                if op.param2 in Lmid:
                    kr1.acceptGroupInvitation(op.param1)
            if op.param3 in mid1:
                if op.param2 in Mmid:
                    kr1.acceptGroupInvitation(op.param1)
            if op.param3 in mid1:
                if op.param2 in Nmid:
                    kr1.acceptGroupInvitation(op.param1)
            if op.param3 in mid1:
                if op.param2 in Omid:
                    kr1.acceptGroupInvitation(op.param1)
            if op.param3 in mid1:
                if op.param2 in Pmid:
                    kr1.acceptGroupInvitation(op.param1)
            if op.param3 in mid1:
                if op.param2 in Qmid:
                    kr1.acceptGroupInvitation(op.param1)
            if op.param3 in mid1:
                if op.param2 in Rmid:
                    kr1.acceptGroupInvitation(op.param1)   
            if op.param3 in mid1:
                if op.param2 in Smid:
                    kr1.acceptGroupInvitation(op.param1)
            if op.param3 in mid1:
                if op.param2 in Tmid:
                    kr1.acceptGroupInvitation(op.param1)
            if op.param3 in mid1:
                if op.param2 in Umid:
                    kr1.acceptGroupInvitation(op.param1)
            if op.param3 in mid1:
                if op.param2 in Vmid:
                    kr1.acceptGroupInvitation(op.param1)
            if op.param3 in mid1:
                if op.param2 in Wmid:
                    kr1.acceptGroupInvitation(op.param1)       
            if op.param3 in mid1:
                if op.param2 in Xmid:
                    kr1.acceptGroupInvitation(op.param1)              
               
#==========================[Kris]===========================
            if op.param3 in Amid:
                if op.param2 in mid1:
                    kr2.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
                if op.param2 in Bmid:
                    kr2.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
                if op.param2 in Cmid:
                    kr2.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
                if op.param2 in Dmid:
                    kr2.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
                if op.param2 in Emid:
                    kr2.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
                if op.param2 in Fmid:
                    kr2.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
                if op.param2 in Gmid:
                    kr2.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
                if op.param2 in Hmid:
                    kr2.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
                if op.param2 in Imid:
                    kr2.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
                if op.param2 in Jmid:
                    kr2.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
                if op.param2 in Kmid:
                    kr2.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
                if op.param2 in Lmid:
                    kr2.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
                if op.param2 in Mmid:
                    kr2.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
                if op.param2 in Nmid:
                    kr2.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
                if op.param2 in Omid:
                    kr2.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
                if op.param2 in Pmid:
                    kr2.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
                if op.param2 in Qmid:
                    kr2.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
                if op.param2 in Rmid:
                    kr2.acceptGroupInvitation(op.param1)   
            if op.param3 in Amid:
                if op.param2 in Smid:
                    kr2.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
                if op.param2 in Tmid:
                    kr2.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
                if op.param2 in Umid:
                    kr2.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
                if op.param2 in Vmid:
                    kr2.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
                if op.param2 in Wmid:
                    kr2.acceptGroupInvitation(op.param1)       
            if op.param3 in Amid:
                if op.param2 in Xmid:
                    kr2.acceptGroupInvitation(op.param1)          
#==========================[Kris]===========================
            if op.param3 in Bmid:
                if op.param2 in mid1:
                    kr3.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
                if op.param2 in Amid:
                    kr3.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
                if op.param2 in Cmid:
                    kr3.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
                if op.param2 in Dmid:
                    kr3.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
                if op.param2 in Emid:
                    kr3.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
                if op.param2 in Fmid:
                    kr3.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
                if op.param2 in Gmid:
                    kr3.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
                if op.param2 in Hmid:
                    kr3.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
                if op.param2 in Imid:
                    kr3.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
                if op.param2 in Jmid:
                    kr3.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
                if op.param2 in Kmid:
                    kr3.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
                if op.param2 in Lmid:
                    kr3.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
                if op.param2 in Mmid:
                    kr3.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
                if op.param2 in Nmid:
                    kr3.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
                if op.param2 in Omid:
                    kr3.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
                if op.param2 in Pmid:
                    kr3.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
                if op.param2 in Qmid:
                    kr3.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
                if op.param2 in Rmid:
                    kr3.acceptGroupInvitation(op.param1)   
            if op.param3 in Bmid:
                if op.param2 in Smid:
                    kr3.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
                if op.param2 in Tmid:
                    kr3.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
                if op.param2 in Umid:
                    kr3.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
                if op.param2 in Vmid:
                    kr3.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
                if op.param2 in Wmid:
                    kr3.acceptGroupInvitation(op.param1)       
            if op.param3 in Bmid:
                if op.param2 in Xmid:
                    kr3.acceptGroupInvitation(op.param1)                     
#==========================[Kris]===========================
            if op.param3 in Cmid:
                if op.param2 in mid1:
                    kr4.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
                if op.param2 in Amid:
                    kr4.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
                if op.param2 in Bmid:
                    kr4.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
                if op.param2 in Dmid:
                    kr4.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
                if op.param2 in Emid:
                    kr4.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
                if op.param2 in Fmid:
                    kr4.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
                if op.param2 in Gmid:
                    kr4.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
                if op.param2 in Hmid:
                    kr4.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
                if op.param2 in Imid:
                    kr4.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
                if op.param2 in Jmid:
                    kr4.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
                if op.param2 in Kmid:
                    kr4.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
                if op.param2 in Lmid:
                    kr4.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
                if op.param2 in Mmid:
                    kr4.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
                if op.param2 in Nmid:
                    kr4.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
                if op.param2 in Omid:
                    kr4.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
                if op.param2 in Pmid:
                    kr4.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
                if op.param2 in Qmid:
                    kr4.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
                if op.param2 in Rmid:
                    kr4.acceptGroupInvitation(op.param1)   
            if op.param3 in Cmid:
                if op.param2 in Smid:
                    kr4.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
                if op.param2 in Tmid:
                    kr4.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
                if op.param2 in Umid:
                    kr4.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
                if op.param2 in Vmid:
                    kr4.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
                if op.param2 in Wmid:
                    kr4.acceptGroupInvitation(op.param1)       
            if op.param3 in Cmid:
                if op.param2 in Xmid:
                    kr4.acceptGroupInvitation(op.param1)        
#==========================[Kris]===========================
            if op.param3 in Dmid:
                if op.param2 in mid1:
                    kr5.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
                if op.param2 in Amid:
                    kr5.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
                if op.param2 in Bmid:
                    kr5.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
                if op.param2 in Cmid:
                    kr5.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
                if op.param2 in Emid:
                    kr5.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
                if op.param2 in Fmid:
                    kr5.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
                if op.param2 in Gmid:
                    kr5.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
                if op.param2 in Hmid:
                    kr5.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
                if op.param2 in Imid:
                    kr5.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
                if op.param2 in Jmid:
                    kr5.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
                if op.param2 in Kmid:
                    kr5.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
                if op.param2 in Lmid:
                    kr5.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
                if op.param2 in Mmid:
                    kr5.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
                if op.param2 in Nmid:
                    kr5.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
                if op.param2 in Omid:
                    kr5.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
                if op.param2 in Pmid:
                    kr5.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
                if op.param2 in Qmid:
                    kr5.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
                if op.param2 in Rmid:
                    kr5.acceptGroupInvitation(op.param1)   
            if op.param3 in Dmid:
                if op.param2 in Smid:
                    kr5.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
                if op.param2 in Tmid:
                    kr5.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
                if op.param2 in Umid:
                    kr5.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
                if op.param2 in Vmid:
                    kr5.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
                if op.param2 in Wmid:
                    kr5.acceptGroupInvitation(op.param1)       
            if op.param3 in Dmid:
                if op.param2 in Xmid:
                    kr5.acceptGroupInvitation(op.param1)            
#==========================[Kris]=========================== 
            if op.param3 in Emid:
                if op.param2 in mid1:
                    kr6.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
                if op.param2 in Amid:
                    kr6.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
                if op.param2 in Bmid:
                    kr6.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
                if op.param2 in Cmid:
                    kr6.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
                if op.param2 in Dmid:
                    kr6.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
                if op.param2 in Fmid:
                    kr6.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
                if op.param2 in Gmid:
                    kr6.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
                if op.param2 in Hmid:
                    kr6.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
                if op.param2 in Imid:
                    kr6.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
                if op.param2 in Jmid:
                    kr6.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
                if op.param2 in Kmid:
                    kr6.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
                if op.param2 in Lmid:
                    kr6.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
                if op.param2 in Mmid:
                    kr6.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
                if op.param2 in Nmid:
                    kr6.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
                if op.param2 in Omid:
                    kr6.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
                if op.param2 in Pmid:
                    kr6.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
                if op.param2 in Qmid:
                    kr6.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
                if op.param2 in Rmid:
                    kr6.acceptGroupInvitation(op.param1)   
            if op.param3 in Emid:
                if op.param2 in Smid:
                    kr6.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
                if op.param2 in Tmid:
                    kr6.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
                if op.param2 in Umid:
                    kr2.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
                if op.param2 in Vmid:
                    kr6.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
                if op.param2 in Wmid:
                    kr6.acceptGroupInvitation(op.param1)       
            if op.param3 in Emid:
                if op.param2 in Xmid:
                    kr6.acceptGroupInvitation(op.param1)           
#==========================[Kris]=========================== 
            if op.param3 in Fmid:
                if op.param2 in mid1:
                    kr7.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
                if op.param2 in Amid:
                    kr7.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
                if op.param2 in Bmid:
                    kr7.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
                if op.param2 in Cmid:
                    kr7.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
                if op.param2 in Dmid:
                    kr7.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
                if op.param2 in Emid:
                    kr7.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
                if op.param2 in Gmid:
                    kr7.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
                if op.param2 in Hmid:
                    kr7.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
                if op.param2 in Imid:
                    kr7.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
                if op.param2 in Jmid:
                    kr7.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
                if op.param2 in Kmid:
                    kr7.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
                if op.param2 in Lmid:
                    kr7.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
                if op.param2 in Mmid:
                    kr7.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
                if op.param2 in Nmid:
                    kr7.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
                if op.param2 in Omid:
                    kr7.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
                if op.param2 in Pmid:
                    kr7.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
                if op.param2 in Qmid:
                    kr7.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
                if op.param2 in Rmid:
                    kr7.acceptGroupInvitation(op.param1)   
            if op.param3 in Fmid:
                if op.param2 in Smid:
                    kr7.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
                if op.param2 in Tmid:
                    kr7.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
                if op.param2 in Umid:
                    kr7.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
                if op.param2 in Vmid:
                    kr7.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
                if op.param2 in Wmid:
                    kr7.acceptGroupInvitation(op.param1)       
            if op.param3 in Fmid:
                if op.param2 in Xmid:
                    kr7.acceptGroupInvitation(op.param1)        
#==========================[Kris]=========================== 
            if op.param3 in Gmid:
                if op.param2 in mid1:
                    kr8.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
                if op.param2 in Amid:
                    kr8.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
                if op.param2 in Bmid:
                    kr8.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
                if op.param2 in Cmid:
                    kr8.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
                if op.param2 in Dmid:
                    kr8.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
                if op.param2 in Emid:
                    kr8.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
                if op.param2 in Fmid:
                    kr8.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
                if op.param2 in Hmid:
                    kr8.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
                if op.param2 in Imid:
                    kr8.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
                if op.param2 in Jmid:
                    kr8.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
                if op.param2 in Kmid:
                    kr8.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
                if op.param2 in Lmid:
                    kr8.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
                if op.param2 in Mmid:
                    kr8.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
                if op.param2 in Nmid:
                    kr8.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
                if op.param2 in Omid:
                    kr8.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
                if op.param2 in Pmid:
                    kr8.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
                if op.param2 in Qmid:
                    kr8.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
                if op.param2 in Rmid:
                    kr8.acceptGroupInvitation(op.param1)   
            if op.param3 in Gmid:
                if op.param2 in Smid:
                    kr8.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
                if op.param2 in Tmid:
                    kr8.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
                if op.param2 in Umid:
                    kr8.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
                if op.param2 in Vmid:
                    kr8.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
                if op.param2 in Wmid:
                    kr8.acceptGroupInvitation(op.param1)       
            if op.param3 in Gmid:
                if op.param2 in Xmid:
                    kr8.acceptGroupInvitation(op.param1)        
#==========================[Kris]=========================== 
            if op.param3 in Hmid:
                if op.param2 in mid1:
                    kr9.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
                if op.param2 in Amid:
                    kr9.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
                if op.param2 in Bmid:
                    kr9.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
                if op.param2 in Cmid:
                    kr9.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
                if op.param2 in Dmid:
                    kr9.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
                if op.param2 in Emid:
                    kr9.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
                if op.param2 in Fmid:
                    kr9.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
                if op.param2 in Gmid:
                    kr9.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
                if op.param2 in Imid:
                    kr9.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
                if op.param2 in Jmid:
                    kr9.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
                if op.param2 in Kmid:
                    kr9.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
                if op.param2 in Lmid:
                    kr9.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
                if op.param2 in Mmid:
                    kr9.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
                if op.param2 in Nmid:
                    kr9.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
                if op.param2 in Omid:
                    kr9.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
                if op.param2 in Pmid:
                    kr9.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
                if op.param2 in Qmid:
                    kr9.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
                if op.param2 in Rmid:
                    kr9.acceptGroupInvitation(op.param1)   
            if op.param3 in Hmid:
                if op.param2 in Smid:
                    kr9.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
                if op.param2 in Tmid:
                    kr9.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
                if op.param2 in Umid:
                    kr9.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
                if op.param2 in Vmid:
                    kr9.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
                if op.param2 in Wmid:
                    kr9.acceptGroupInvitation(op.param1)       
            if op.param3 in Hmid:
                if op.param2 in Xmid:
                    kr9.acceptGroupInvitation(op.param1)        
#==========================[Kris]=========================== 
            if op.param3 in Imid:
                if op.param2 in mid1:
                    kr10.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
                if op.param2 in Amid:
                    kr10.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
                if op.param2 in Bmid:
                    kr10.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
                if op.param2 in Cmid:
                    kr10.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
                if op.param2 in Dmid:
                    kr10.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
                if op.param2 in Emid:
                    kr10.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
                if op.param2 in Fmid:
                    kr10.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
                if op.param2 in Gmid:
                    kr10.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
                if op.param2 in Hmid:
                    kr10.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
                if op.param2 in Jmid:
                    kr10.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
                if op.param2 in Kmid:
                    kr10.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
                if op.param2 in Lmid:
                    kr10.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
                if op.param2 in Mmid:
                    kr10.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
                if op.param2 in Nmid:
                    kr10.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
                if op.param2 in Omid:
                    kr10.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
                if op.param2 in Pmid:
                    kr10.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
                if op.param2 in Qmid:
                    kr10.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
                if op.param2 in Rmid:
                    kr10.acceptGroupInvitation(op.param1)   
            if op.param3 in Imid:
                if op.param2 in Smid:
                    kr10.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
                if op.param2 in Tmid:
                    kr10.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
                if op.param2 in Umid:
                    kr10.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
                if op.param2 in Vmid:
                    kr10.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
                if op.param2 in Wmid:
                    kr10.acceptGroupInvitation(op.param1)       
            if op.param3 in Imid:
                if op.param2 in Xmid:
                    kr10.acceptGroupInvitation(op.param1)        
#------------------------------------------             
            if op.param3 in Jmid:
                if op.param2 in mid1:
                    kr11.acceptGroupInvitation(op.param1)
            if op.param3 in Jmid:
                if op.param2 in Amid:
                    kr11.acceptGroupInvitation(op.param1)
            if op.param3 in Jmid:
                if op.param2 in Bmid:
                    kr11.acceptGroupInvitation(op.param1)
            if op.param3 in Jmid:
                if op.param2 in Cmid:
                    kr11.acceptGroupInvitation(op.param1)
            if op.param3 in Jmid:
                if op.param2 in Dmid:
                    kr11.acceptGroupInvitation(op.param1)
            if op.param3 in Jmid:
                if op.param2 in Emid:
                    kr11.acceptGroupInvitation(op.param1)
            if op.param3 in Jmid:
                if op.param2 in Fmid:
                    kr11.acceptGroupInvitation(op.param1)
            if op.param3 in Jmid:
                if op.param2 in Gmid:
                    kr11.acceptGroupInvitation(op.param1)
            if op.param3 in Jmid:
                if op.param2 in Hmid:
                    kr11.acceptGroupInvitation(op.param1)
            if op.param3 in Jmid:
                if op.param2 in Imid:
                    kr11.acceptGroupInvitation(op.param1)
            if op.param3 in Jmid:
                if op.param2 in Kmid:
                    kr11.acceptGroupInvitation(op.param1)
            if op.param3 in Jmid:
                if op.param2 in Lmid:
                    kr11.acceptGroupInvitation(op.param1)
            if op.param3 in Jmid:
                if op.param2 in Mmid:
                    kr11.acceptGroupInvitation(op.param1)
            if op.param3 in Jmid:
                if op.param2 in Nmid:
                    kr11.acceptGroupInvitation(op.param1)
            if op.param3 in Jmid:
                if op.param2 in Omid:
                    kr11.acceptGroupInvitation(op.param1)
            if op.param3 in Jmid:
                if op.param2 in Pmid:
                    kr11.acceptGroupInvitation(op.param1)
            if op.param3 in Jmid:
                if op.param2 in Qmid:
                    kr11.acceptGroupInvitation(op.param1)
            if op.param3 in Jmid:
                if op.param2 in Rmid:
                    kr11.acceptGroupInvitation(op.param1)   
            if op.param3 in Jmid:
                if op.param2 in Smid:
                    kr11.acceptGroupInvitation(op.param1)
            if op.param3 in Jmid:
                if op.param2 in Tmid:
                    kr11.acceptGroupInvitation(op.param1)
            if op.param3 in Jmid:
                if op.param2 in Umid:
                    kr11.acceptGroupInvitation(op.param1)
            if op.param3 in Jmid:
                if op.param2 in Vmid:
                    kr11.acceptGroupInvitation(op.param1)
            if op.param3 in Jmid:
                if op.param2 in Wmid:
                    kr11.acceptGroupInvitation(op.param1)       
            if op.param3 in Jmid:
                if op.param2 in Xmid:
                    kr11.acceptGroupInvitation(op.param1)        
                    
#==========================[Kris]=========================== 
            if op.param3 in Kmid:
                if op.param2 in mid1:
                    kr12.acceptGroupInvitation(op.param1)
            if op.param3 in Kmid:
                if op.param2 in Amid:
                    kr12.acceptGroupInvitation(op.param1)
            if op.param3 in Kmid:
                if op.param2 in Bmid:
                    kr12.acceptGroupInvitation(op.param1)
            if op.param3 in Kmid:
                if op.param2 in Cmid:
                    kr12.acceptGroupInvitation(op.param1)
            if op.param3 in Kmid:
                if op.param2 in Dmid:
                    kr12.acceptGroupInvitation(op.param1)
            if op.param3 in Kmid:
                if op.param2 in Emid:
                    kr12.acceptGroupInvitation(op.param1)
            if op.param3 in Kmid:
                if op.param2 in Fmid:
                    kr12.acceptGroupInvitation(op.param1)
            if op.param3 in Kmid:
                if op.param2 in Gmid:
                    kr12.acceptGroupInvitation(op.param1)
            if op.param3 in Kmid:
                if op.param2 in Hmid:
                    kr12.acceptGroupInvitation(op.param1)
            if op.param3 in Kmid:
                if op.param2 in Jmid:
                    kr12.acceptGroupInvitation(op.param1)
            if op.param3 in Kmid:
                if op.param2 in Imid:
                    kr12.acceptGroupInvitation(op.param1)
            if op.param3 in Kmid:
                if op.param2 in Lmid:
                    kr12.acceptGroupInvitation(op.param1)
            if op.param3 in Kmid:
                if op.param2 in Mmid:
                    kr12.acceptGroupInvitation(op.param1)
            if op.param3 in Kmid:
                if op.param2 in Nmid:
                    kr12.acceptGroupInvitation(op.param1)
            if op.param3 in Kmid:
                if op.param2 in Omid:
                    kr12.acceptGroupInvitation(op.param1)
            if op.param3 in Kmid:
                if op.param2 in Pmid:
                    kr12.acceptGroupInvitation(op.param1)
            if op.param3 in Kmid:
                if op.param2 in Qmid:
                    kr12.acceptGroupInvitation(op.param1)
            if op.param3 in Kmid:
                if op.param2 in Rmid:
                    kr12.acceptGroupInvitation(op.param1)   
            if op.param3 in Kmid:
                if op.param2 in Smid:
                    kr12.acceptGroupInvitation(op.param1)
            if op.param3 in Kmid:
                if op.param2 in Tmid:
                    kr12.acceptGroupInvitation(op.param1)
            if op.param3 in Kmid:
                if op.param2 in Umid:
                    kr12.acceptGroupInvitation(op.param1)
            if op.param3 in Kmid:
                if op.param2 in Vmid:
                    kr12.acceptGroupInvitation(op.param1)
            if op.param3 in Kmid:
                if op.param2 in Wmid:
                    kr12.acceptGroupInvitation(op.param1)       
            if op.param3 in Kmid:
                if op.param2 in Xmid:
                    kr12.acceptGroupInvitation(op.param1)        
                    
#==========================[Kris]=========================== 
            if op.param3 in Lmid:
                if op.param2 in mid1:
                    kr13.acceptGroupInvitation(op.param1)
            if op.param3 in Lmid:
                if op.param2 in Amid:
                    kr13.acceptGroupInvitation(op.param1)
            if op.param3 in Lmid:
                if op.param2 in Bmid:
                    kr13.acceptGroupInvitation(op.param1)
            if op.param3 in Lmid:
                if op.param2 in Cmid:
                    kr13.acceptGroupInvitation(op.param1)
            if op.param3 in Lmid:
                if op.param2 in Dmid:
                    kr13.acceptGroupInvitation(op.param1)
            if op.param3 in Lmid:
                if op.param2 in Emid:
                    kr13.acceptGroupInvitation(op.param1)
            if op.param3 in Lmid:
                if op.param2 in Fmid:
                    kr13.acceptGroupInvitation(op.param1)
            if op.param3 in Lmid:
                if op.param2 in Gmid:
                    kr13.acceptGroupInvitation(op.param1)
            if op.param3 in Lmid:
                if op.param2 in Hmid:
                    kr13.acceptGroupInvitation(op.param1)
            if op.param3 in Lmid:
                if op.param2 in Jmid:
                    kr13.acceptGroupInvitation(op.param1)
            if op.param3 in Lmid:
                if op.param2 in Kmid:
                    kr13.acceptGroupInvitation(op.param1)
            if op.param3 in Lmid:
                if op.param2 in Imid:
                    kr13.acceptGroupInvitation(op.param1)
            if op.param3 in Lmid:
                if op.param2 in Mmid:
                    kr13.acceptGroupInvitation(op.param1)
            if op.param3 in Lmid:
                if op.param2 in Nmid:
                    kr13.acceptGroupInvitation(op.param1)
            if op.param3 in Lmid:
                if op.param2 in Omid:
                    kr13.acceptGroupInvitation(op.param1)
            if op.param3 in Lmid:
                if op.param2 in Pmid:
                    kr13.acceptGroupInvitation(op.param1)
            if op.param3 in Lmid:
                if op.param2 in Qmid:
                    kr13.acceptGroupInvitation(op.param1)
            if op.param3 in Lmid:
                if op.param2 in Rmid:
                    kr13.acceptGroupInvitation(op.param1)   
            if op.param3 in Lmid:
                if op.param2 in Smid:
                    kr13.acceptGroupInvitation(op.param1)
            if op.param3 in Lmid:
                if op.param2 in Tmid:
                    kr13.acceptGroupInvitation(op.param1)
            if op.param3 in Lmid:
                if op.param2 in Umid:
                    kr13.acceptGroupInvitation(op.param1)
            if op.param3 in Lmid:
                if op.param2 in Vmid:
                    kr13.acceptGroupInvitation(op.param1)
            if op.param3 in Lmid:
                if op.param2 in Wmid:
                    kr13.acceptGroupInvitation(op.param1)       
            if op.param3 in Lmid:
                if op.param2 in Xmid:
                    kr13.acceptGroupInvitation(op.param1)        
              
#==========================[Kris]=========================== 
            if op.param3 in Mmid:
                if op.param2 in mid1:
                    kr14.acceptGroupInvitation(op.param1)
            if op.param3 in Mmid:
                if op.param2 in Amid:
                    kr14.acceptGroupInvitation(op.param1)
            if op.param3 in Mmid:
                if op.param2 in Bmid:
                    kr14.acceptGroupInvitation(op.param1)
            if op.param3 in Mmid:
                if op.param2 in Cmid:
                    kr14.acceptGroupInvitation(op.param1)
            if op.param3 in Mmid:
                if op.param2 in Dmid:
                    kr14.acceptGroupInvitation(op.param1)
            if op.param3 in Mmid:
                if op.param2 in Emid:
                    kr14.acceptGroupInvitation(op.param1)
            if op.param3 in Mmid:
                if op.param2 in Fmid:
                    kr14.acceptGroupInvitation(op.param1)
            if op.param3 in Mmid:
                if op.param2 in Gmid:
                    kr14.acceptGroupInvitation(op.param1)
            if op.param3 in Mmid:
                if op.param2 in Hmid:
                    kr14.acceptGroupInvitation(op.param1)
            if op.param3 in Mmid:
                if op.param2 in Jmid:
                    kr14.acceptGroupInvitation(op.param1)
            if op.param3 in Mmid:
                if op.param2 in Kmid:
                    kr14.acceptGroupInvitation(op.param1)
            if op.param3 in Mmid:
                if op.param2 in Lmid:
                    kr14.acceptGroupInvitation(op.param1)
            if op.param3 in Mmid:
                if op.param2 in Imid:
                    kr14.acceptGroupInvitation(op.param1)
            if op.param3 in Mmid:
                if op.param2 in Nmid:
                    kr14.acceptGroupInvitation(op.param1)
            if op.param3 in Mmid:
                if op.param2 in Omid:
                    kr14.acceptGroupInvitation(op.param1)
            if op.param3 in Mmid:
                if op.param2 in Pmid:
                    kr14.acceptGroupInvitation(op.param1)
            if op.param3 in Mmid:
                if op.param2 in Qmid:
                    kr14.acceptGroupInvitation(op.param1)
            if op.param3 in Mmid:
                if op.param2 in Rmid:
                    kr14.acceptGroupInvitation(op.param1)   
            if op.param3 in Mmid:
                if op.param2 in Smid:
                    kr14.acceptGroupInvitation(op.param1)
            if op.param3 in Mmid:
                if op.param2 in Tmid:
                    kr14.acceptGroupInvitation(op.param1)
            if op.param3 in Mmid:
                if op.param2 in Umid:
                    kr14.acceptGroupInvitation(op.param1)
            if op.param3 in Mmid:
                if op.param2 in Vmid:
                    kr14.acceptGroupInvitation(op.param1)
            if op.param3 in Mmid:
                if op.param2 in Wmid:
                    kr14.acceptGroupInvitation(op.param1)       
            if op.param3 in Mmid:
                if op.param2 in Xmid:
                    kr14.acceptGroupInvitation(op.param1)        
                    
#==========================[Kris]=========================== 
            if op.param3 in Nmid:
                if op.param2 in mid1:
                    kr15.acceptGroupInvitation(op.param1)
            if op.param3 in Nmid:
                if op.param2 in Amid:
                    kr15.acceptGroupInvitation(op.param1)
            if op.param3 in Nmid:
                if op.param2 in Bmid:
                    kr15.acceptGroupInvitation(op.param1)
            if op.param3 in Nmid:
                if op.param2 in Cmid:
                    kr15.acceptGroupInvitation(op.param1)
            if op.param3 in Nmid:
                if op.param2 in Dmid:
                    kr15.acceptGroupInvitation(op.param1)
            if op.param3 in Nmid:
                if op.param2 in Emid:
                    kr15.acceptGroupInvitation(op.param1)
            if op.param3 in Nmid:
                if op.param2 in Fmid:
                    kr15.acceptGroupInvitation(op.param1)
            if op.param3 in Nmid:
                if op.param2 in Gmid:
                    kr15.acceptGroupInvitation(op.param1)
            if op.param3 in Nmid:
                if op.param2 in Hmid:
                    kr15.acceptGroupInvitation(op.param1)
            if op.param3 in Nmid:
                if op.param2 in Jmid:
                    kr15.acceptGroupInvitation(op.param1)
            if op.param3 in Nmid:
                if op.param2 in Kmid:
                    kr15.acceptGroupInvitation(op.param1)
            if op.param3 in Nmid:
                if op.param2 in Lmid:
                    kr15.acceptGroupInvitation(op.param1)
            if op.param3 in Nmid:
                if op.param2 in Mmid:
                    kr15.acceptGroupInvitation(op.param1)
            if op.param3 in Nmid:
                if op.param2 in Imid:
                    kr15.acceptGroupInvitation(op.param1)
            if op.param3 in Nmid:
                if op.param2 in Omid:
                    kr15.acceptGroupInvitation(op.param1)
            if op.param3 in Nmid:
                if op.param2 in Pmid:
                    kr15.acceptGroupInvitation(op.param1)
            if op.param3 in Nmid:
                if op.param2 in Qmid:
                    kr15.acceptGroupInvitation(op.param1)
            if op.param3 in Nmid:
                if op.param2 in Rmid:
                    kr15.acceptGroupInvitation(op.param1)   
            if op.param3 in Nmid:
                if op.param2 in Smid:
                    kr15.acceptGroupInvitation(op.param1)
            if op.param3 in Nmid:
                if op.param2 in Tmid:
                    kr15.acceptGroupInvitation(op.param1)
            if op.param3 in Nmid:
                if op.param2 in Umid:
                    kr15.acceptGroupInvitation(op.param1)
            if op.param3 in Nmid:
                if op.param2 in Vmid:
                    kr15.acceptGroupInvitation(op.param1)
            if op.param3 in Nmid:
                if op.param2 in Wmid:
                    kr15.acceptGroupInvitation(op.param1)       
            if op.param3 in Nmid:
                if op.param2 in Xmid:
                    kr15.acceptGroupInvitation(op.param1)        
                    
#==========================[Kris]=========================== 
            if op.param3 in Omid:
                if op.param2 in mid1:
                    kr16.acceptGroupInvitation(op.param1)
            if op.param3 in Omid:
                if op.param2 in Amid:
                    kr16.acceptGroupInvitation(op.param1)
            if op.param3 in Omid:
                if op.param2 in Bmid:
                    kr16.acceptGroupInvitation(op.param1)
            if op.param3 in Omid:
                if op.param2 in Cmid:
                    kr16.acceptGroupInvitation(op.param1)
            if op.param3 in Omid:
                if op.param2 in Dmid:
                    kr16.acceptGroupInvitation(op.param1)
            if op.param3 in Omid:
                if op.param2 in Emid:
                    kr16.acceptGroupInvitation(op.param1)
            if op.param3 in Omid:
                if op.param2 in Fmid:
                    kr16.acceptGroupInvitation(op.param1)
            if op.param3 in Omid:
                if op.param2 in Gmid:
                    kr16.acceptGroupInvitation(op.param1)
            if op.param3 in Omid:
                if op.param2 in Hmid:
                    kr16.acceptGroupInvitation(op.param1)
            if op.param3 in Omid:
                if op.param2 in Jmid:
                    kr16.acceptGroupInvitation(op.param1)
            if op.param3 in Omid:
                if op.param2 in Kmid:
                    kr16.acceptGroupInvitation(op.param1)
            if op.param3 in Omid:
                if op.param2 in Lmid:
                    kr16.acceptGroupInvitation(op.param1)
            if op.param3 in Omid:
                if op.param2 in Mmid:
                    kr16.acceptGroupInvitation(op.param1)
            if op.param3 in Omid:
                if op.param2 in Nmid:
                    kr16.acceptGroupInvitation(op.param1)
            if op.param3 in Omid:
                if op.param2 in Imid:
                    kr16.acceptGroupInvitation(op.param1)
            if op.param3 in Omid:
                if op.param2 in Pmid:
                    kr16.acceptGroupInvitation(op.param1)
            if op.param3 in Omid:
                if op.param2 in Qmid:
                    kr16.acceptGroupInvitation(op.param1)
            if op.param3 in Omid:
                if op.param2 in Rmid:
                    kr16.acceptGroupInvitation(op.param1)   
            if op.param3 in Omid:
                if op.param2 in Smid:
                    kr16.acceptGroupInvitation(op.param1)
            if op.param3 in Omid:
                if op.param2 in Tmid:
                    kr16.acceptGroupInvitation(op.param1)
            if op.param3 in Omid:
                if op.param2 in Umid:
                    kr16.acceptGroupInvitation(op.param1)
            if op.param3 in Omid:
                if op.param2 in Vmid:
                    kr16.acceptGroupInvitation(op.param1)
            if op.param3 in Omid:
                if op.param2 in Wmid:
                    kr16.acceptGroupInvitation(op.param1)       
            if op.param3 in Omid:
                if op.param2 in Xmid:
                    kr16.acceptGroupInvitation(op.param1)        
                   
#==========================[Kris]=========================== 
            if op.param3 in Pmid:
                if op.param2 in mid1:
                    kr17.acceptGroupInvitation(op.param1)
            if op.param3 in Pmid:
                if op.param2 in Amid:
                    kr17.acceptGroupInvitation(op.param1)
            if op.param3 in Pmid:
                if op.param2 in Bmid:
                    kr17.acceptGroupInvitation(op.param1)
            if op.param3 in Pmid:
                if op.param2 in Cmid:
                    kr17.acceptGroupInvitation(op.param1)
            if op.param3 in Pmid:
                if op.param2 in Dmid:
                    kr17.acceptGroupInvitation(op.param1)
            if op.param3 in Pmid:
                if op.param2 in Emid:
                    kr17.acceptGroupInvitation(op.param1)
            if op.param3 in Pmid:
                if op.param2 in Fmid:
                    kr17.acceptGroupInvitation(op.param1)
            if op.param3 in Pmid:
                if op.param2 in Gmid:
                    kr17.acceptGroupInvitation(op.param1)
            if op.param3 in Pmid:
                if op.param2 in Hmid:
                    kr17.acceptGroupInvitation(op.param1)
            if op.param3 in Pmid:
                if op.param2 in Jmid:
                    kr17.acceptGroupInvitation(op.param1)
            if op.param3 in Pmid:
                if op.param2 in Kmid:
                    kr17.acceptGroupInvitation(op.param1)
            if op.param3 in Pmid:
                if op.param2 in Lmid:
                    kr17.acceptGroupInvitation(op.param1)
            if op.param3 in Pmid:
                if op.param2 in Mmid:
                    kr17.acceptGroupInvitation(op.param1)
            if op.param3 in Pmid:
                if op.param2 in Nmid:
                    kr17.acceptGroupInvitation(op.param1)
            if op.param3 in Pmid:
                if op.param2 in Omid:
                    kr17.acceptGroupInvitation(op.param1)
            if op.param3 in Pmid:
                if op.param2 in Imid:
                    kr17.acceptGroupInvitation(op.param1)
            if op.param3 in Pmid:
                if op.param2 in Qmid:
                    kr17.acceptGroupInvitation(op.param1)
            if op.param3 in Pmid:
                if op.param2 in Rmid:
                    kr17.acceptGroupInvitation(op.param1)   
            if op.param3 in Pmid:
                if op.param2 in Smid:
                    kr17.acceptGroupInvitation(op.param1)
            if op.param3 in Pmid:
                if op.param2 in Tmid:
                    kr17.acceptGroupInvitation(op.param1)
            if op.param3 in Pmid:
                if op.param2 in Umid:
                    kr17.acceptGroupInvitation(op.param1)
            if op.param3 in Pmid:
                if op.param2 in Vmid:
                    kr17.acceptGroupInvitation(op.param1)
            if op.param3 in Pmid:
                if op.param2 in Wmid:
                    kr17.acceptGroupInvitation(op.param1)       
            if op.param3 in Pmid:
                if op.param2 in Xmid:
                    kr17.acceptGroupInvitation(op.param1)        
              
#==========================[Kris]=========================== 
            if op.param3 in Qmid:
                if op.param2 in mid1:
                    kr18.acceptGroupInvitation(op.param1)
            if op.param3 in Qmid:
                if op.param2 in Amid:
                    kr18.acceptGroupInvitation(op.param1)
            if op.param3 in Qmid:
                if op.param2 in Bmid:
                    kr18.acceptGroupInvitation(op.param1)
            if op.param3 in Qmid:
                if op.param2 in Cmid:
                    kr18.acceptGroupInvitation(op.param1)
            if op.param3 in Qmid:
                if op.param2 in Dmid:
                    kr18.acceptGroupInvitation(op.param1)
            if op.param3 in Qmid:
                if op.param2 in Emid:
                    kr18.acceptGroupInvitation(op.param1)
            if op.param3 in Qmid:
                if op.param2 in Fmid:
                    kr18.acceptGroupInvitation(op.param1)
            if op.param3 in Qmid:
                if op.param2 in Gmid:
                    kr18.acceptGroupInvitation(op.param1)
            if op.param3 in Qmid:
                if op.param2 in Hmid:
                    kr18.acceptGroupInvitation(op.param1)
            if op.param3 in Qmid:
                if op.param2 in Jmid:
                    kr18.acceptGroupInvitation(op.param1)
            if op.param3 in Qmid:
                if op.param2 in Kmid:
                    kr18.acceptGroupInvitation(op.param1)
            if op.param3 in Qmid:
                if op.param2 in Lmid:
                    kr18.acceptGroupInvitation(op.param1)
            if op.param3 in Qmid:
                if op.param2 in Mmid:
                    kr18.acceptGroupInvitation(op.param1)
            if op.param3 in Qmid:
                if op.param2 in Nmid:
                    kr18.acceptGroupInvitation(op.param1)
            if op.param3 in Qmid:
                if op.param2 in Omid:
                    kr18.acceptGroupInvitation(op.param1)
            if op.param3 in Qmid:
                if op.param2 in Pmid:
                    kr18.acceptGroupInvitation(op.param1)
            if op.param3 in Qmid:
                if op.param2 in Imid:
                    kr18.acceptGroupInvitation(op.param1)
            if op.param3 in Qmid:
                if op.param2 in Rmid:
                    kr18.acceptGroupInvitation(op.param1)   
            if op.param3 in Qmid:
                if op.param2 in Smid:
                    kr18.acceptGroupInvitation(op.param1)
            if op.param3 in Qmid:
                if op.param2 in Tmid:
                    kr18.acceptGroupInvitation(op.param1)
            if op.param3 in Qmid:
                if op.param2 in Umid:
                    kr18.acceptGroupInvitation(op.param1)
            if op.param3 in Qmid:
                if op.param2 in Vmid:
                    kr18.acceptGroupInvitation(op.param1)
            if op.param3 in Qmid:
                if op.param2 in Wmid:
                    kr18.acceptGroupInvitation(op.param1)       
            if op.param3 in Qmid:
                if op.param2 in Xmid:
                    kr18.acceptGroupInvitation(op.param1)        
             
#==========================[Kris]=========================== 
            if op.param3 in Rmid:
                if op.param2 in mid1:
                    kr19.acceptGroupInvitation(op.param1)
            if op.param3 in Rmid:
                if op.param2 in Amid:
                    kr19.acceptGroupInvitation(op.param1)
            if op.param3 in Rmid:
                if op.param2 in Bmid:
                    kr19.acceptGroupInvitation(op.param1)
            if op.param3 in Rmid:
                if op.param2 in Cmid:
                    kr19.acceptGroupInvitation(op.param1)
            if op.param3 in Rmid:
                if op.param2 in Dmid:
                    kr19.acceptGroupInvitation(op.param1)
            if op.param3 in Rmid:
                if op.param2 in Emid:
                    kr19.acceptGroupInvitation(op.param1)
            if op.param3 in Rmid:
                if op.param2 in Fmid:
                    kr19.acceptGroupInvitation(op.param1)
            if op.param3 in Rmid:
                if op.param2 in Gmid:
                    kr19.acceptGroupInvitation(op.param1)
            if op.param3 in Rmid:
                if op.param2 in Hmid:
                    kr19.acceptGroupInvitation(op.param1)
            if op.param3 in Rmid:
                if op.param2 in Jmid:
                    kr19.acceptGroupInvitation(op.param1)
            if op.param3 in Rmid:
                if op.param2 in Kmid:
                    kr19.acceptGroupInvitation(op.param1)
            if op.param3 in Rmid:
                if op.param2 in Lmid:
                    kr19.acceptGroupInvitation(op.param1)
            if op.param3 in Rmid:
                if op.param2 in Mmid:
                    kr19.acceptGroupInvitation(op.param1)
            if op.param3 in Rmid:
                if op.param2 in Nmid:
                    kr19.acceptGroupInvitation(op.param1)
            if op.param3 in Rmid:
                if op.param2 in Omid:
                    kr19.acceptGroupInvitation(op.param1)
            if op.param3 in Rmid:
                if op.param2 in Pmid:
                    kr19.acceptGroupInvitation(op.param1)
            if op.param3 in Rmid:
                if op.param2 in Qmid:
                    kr19.acceptGroupInvitation(op.param1)
            if op.param3 in Rmid:
                if op.param2 in Imid:
                    kr19.acceptGroupInvitation(op.param1)   
            if op.param3 in Rmid:
                if op.param2 in Smid:
                    kr19.acceptGroupInvitation(op.param1)
            if op.param3 in Rmid:
                if op.param2 in Tmid:
                    kr19.acceptGroupInvitation(op.param1)
            if op.param3 in Rmid:
                if op.param2 in Umid:
                    kr19.acceptGroupInvitation(op.param1)
            if op.param3 in Rmid:
                if op.param2 in Vmid:
                    kr19.acceptGroupInvitation(op.param1)
            if op.param3 in Rmid:
                if op.param2 in Wmid:
                    kr19.acceptGroupInvitation(op.param1)       
            if op.param3 in Rmid:
                if op.param2 in Xmid:
                    kr19.acceptGroupInvitation(op.param1)        
               
#==========================[Kris]=========================== 
            if op.param3 in Smid:
                if op.param2 in mid1:
                    kr20.acceptGroupInvitation(op.param1)
            if op.param3 in Smid:
                if op.param2 in Amid:
                    kr20.acceptGroupInvitation(op.param1)
            if op.param3 in Smid:
                if op.param2 in Bmid:
                    kr20.acceptGroupInvitation(op.param1)
            if op.param3 in Smid:
                if op.param2 in Cmid:
                    kr20.acceptGroupInvitation(op.param1)
            if op.param3 in Smid:
                if op.param2 in Dmid:
                    kr20.acceptGroupInvitation(op.param1)
            if op.param3 in Smid:
                if op.param2 in Emid:
                    kr20.acceptGroupInvitation(op.param1)
            if op.param3 in Smid:
                if op.param2 in Fmid:
                    kr20.acceptGroupInvitation(op.param1)
            if op.param3 in Smid:
                if op.param2 in Gmid:
                    kr20.acceptGroupInvitation(op.param1)
            if op.param3 in Smid:
                if op.param2 in Hmid:
                    kr20.acceptGroupInvitation(op.param1)
            if op.param3 in Smid:
                if op.param2 in Jmid:
                    kr20.acceptGroupInvitation(op.param1)
            if op.param3 in Smid:
                if op.param2 in Kmid:
                    kr20.acceptGroupInvitation(op.param1)
            if op.param3 in Smid:
                if op.param2 in Lmid:
                    kr20.acceptGroupInvitation(op.param1)
            if op.para3 in Smid:
                if op.param2 in Mmid:
                    kr20.acceptGroupInvitation(op.param1)
            if op.param3 in Smid:
                if op.param2 in Nmid:
                    kr20.acceptGroupInvitation(op.param1)
            if op.param3 in Smid:
                if op.param2 in Omid:
                    kr20.acceptGroupInvitation(op.param1)
            if op.param3 in Smid:
                if op.param2 in Pmid:
                    kr20.acceptGroupInvitation(op.param1)
            if op.param3 in Smid:
                if op.param2 in Qmid:
                    kr20.acceptGroupInvitation(op.param1)
            if op.param3 in Smid:
                if op.param2 in Rmid:
                    kr20.acceptGroupInvitation(op.param1)   
            if op.param3 in Smid:
                if op.param2 in Tmid:
                    kr20.acceptGroupInvitation(op.param1)
            if op.param3 in Smid:
                if op.param2 in Imid:
                    kr20.acceptGroupInvitation(op.param1)
            if op.param3 in Smid:
                if op.param2 in Umid:
                    kr20.acceptGroupInvitation(op.param1)
            if op.param3 in Smid:
                if op.param2 in Vmid:
                    kr20.acceptGroupInvitation(op.param1)
            if op.param3 in Smid:
                if op.param2 in Wmid:
                    kr20.acceptGroupInvitation(op.param1)       
            if op.param3 in Smid:
                if op.param2 in Xmid:
                    kr20.acceptGroupInvitation(op.param1)        
             
#==========================[Kris]=========================== 
            if op.param3 in Tmid:
                if op.param2 in mid1:
                    kr21.acceptGroupInvitation(op.param1)
            if op.param3 in Tmid:
                if op.param2 in Amid:
                    kr21.acceptGroupInvitation(op.param1)
            if op.param3 in Tmid:
                if op.param2 in Bmid:
                    kr21.acceptGroupInvitation(op.param1)
            if op.param3 in Tmid:
                if op.param2 in Cmid:
                    kr21.acceptGroupInvitation(op.param1)
            if op.param3 in Tmid:
                if op.param2 in Dmid:
                    kr21.acceptGroupInvitation(op.param1)
            if op.param3 in Tmid:
                if op.param2 in Emid:
                    kr21.acceptGroupInvitation(op.param1)
            if op.param3 in Tmid:
                if op.param2 in Fmid:
                    kr21.acceptGroupInvitation(op.param1)
            if op.param3 in Tmid:
                if op.param2 in Gmid:
                    kr21.acceptGroupInvitation(op.param1)
            if op.param3 in Tmid:
                if op.param2in Hmid:
                    kr21.acceptGroupInvitation(op.param1)
            if op.param3 in Tmid:
                if op.param2 in Jmid:
                    kr21.acceptGroupInvitation(op.param1)
            if op.param3 in Tmid:
                if op.param2 in Kmid:
                    kr21.acceptGroupInvitation(op.param1)
            if op.param3 in Tmid:
                if op.param2 in Lmid:
                    kr21.acceptGroupInvitation(op.param1)
            if op.param3 in Tmid:
                if op.param2 in Mmid:
                    kr21.acceptGroupInvitation(op.param1)
            if op.param3 in Tmid:
                if op.param2 in Nmid:
                    kr21.acceptGroupInvitation(op.param1)
            if op.param3 in Tmid:
                if op.param2 in Omid:
                    kr21.acceptGroupInvitation(op.param1)
            if op.param3 in Tmid:
                if op.param2 in Pmid:
                    kr21.acceptGroupInvitation(op.param1)
            if op.param3 in Tmid:
                if op.param2 in Qmid:
                    kr21.acceptGroupInvitation(op.param1)
            if op.param3 in Tmid:
                if op.param2 in Rmid:
                    kr21.acceptGroupInvitation(op.param1)   
            if op.param3 in Tmid:
                if op.param2 in Smid:
                    kr21.acceptGroupInvitation(op.param1)
            if op.param3 in Tmid:
                if op.param2 in Umid:
                    kr21.acceptGroupInvitation(op.param1)
            if op.param3 in Tmid:
                if op.param2 in Imid:
                    kr21.acceptGroupInvitation(op.param1)
            if op.param3 in Tmid:
                if op.param2 in Vmid:
                    kr21.acceptGroupInvitation(op.param1)
            if op.param3 in Tmid:
                if op.param2 in Wmid:
                    kr21.acceptGroupInvitation(op.param1)       
            if op.param3 in Tmid:
                if op.param2 in Xmid:
                    kr21.acceptGroupInvitation(op.param1)        
                
#==========================[Kris]=========================== 
            if op.param3 in Umid:
                if op.pa2ram2 in mid1:
                    kr22.acceptGroupInvitation(op.param1)
            if op.param3 in Umid:
                if op.param2 in Amid:
                    kr22.acceptGroupInvitation(op.param1)
            if op.param3 in Umid:
                if op.param2 in Bmid:
                    kr22.acceptGroupInvitation(op.param1)
            if op.param3 in Umid:
                if op.param2 in Cmid:
                    kr22.acceptGroupInvitation(op.param1)
            if op.param3 in Umid:
                if op.param2 in Dmid:
                    kr22.acceptGroupInvitation(op.param1)
            if op.param3 in Umid:
                if op.param2 in Emid:
                    kr22.acceptGroupInvitation(op.param1)
            if op.param3 in Umid:
                if op.param2 in Fmid:
                    kr22.acceptGroupInvitation(op.param1)
            if op.param3 in Umid:
                if op.param2 in Gmid:
                    kr22.acceptGroupInvitation(op.param1)
            if op.param3 in Umid:
                if op.param2in Hmid:
                    kr22.acceptGroupInvitation(op.param1)
            if op.param3 in Umid:
                if op.param2 in Jmid:
                    kr22.acceptGroupInvitation(op.param1)
            if op.param3 in Umid:
                if op.param2 in Kmid:
                    kr22.acceptGroupInvitation(op.param1)
            if op.param3 in Umid:
                if op.param2 in Lmid:
                    kr22.acceptGroupInvitation(op.param1)
            if op.param3 in Umid:
                if op.param2 in Mmid:
                    kr22.acceptGroupInvitation(op.param1)
            if op.param3 in Umid:
                if op.param2 in Nmid:
                    kr22.acceptGroupInvitation(op.param1)
            if op.param3 in Umid:
                if op.param2 in Omid:
                    kr22.acceptGroupInvitation(op.param1)
            if op.param3 in Umid:
                if op.param2 in Pmid:
                    kr22.acceptGroupInvitation(op.param1)
            if op.param3 in Umid:
                if op.param2 in Qmid:
                    kr22.acceptGroupInvitation(op.param1)
            if op.param3 in Umid:
                if op.param2 in Rmid:
                    kr22.acceptGroupInvitation(op.param1)   
            if op.param3 in Umid:
                if op.param2 in Smid:
                    kr22.acceptGroupInvitation(op.param1)
            if op.param3 in Umid:
                if op.param2 in Tmid:
                    kr22.acceptGroupInvitation(op.param1)
            if op.param3 in Umid:
                if op.param2 in Imid:
                    kr22.acceptGroupInvitation(op.param1)
            if op.param3 in Umid:
                if op.param2 in Vmid:
                    kr22.acceptGroupInvitation(op.param1)
            if op.param3 in Umid:
                if op.param2 in Wmid:
                    kr22.acceptGroupInvitation(op.param1)       
            if op.param3 in Umid:
                if op.param2 in Xmid:
                    kr22.acceptGroupInvitation(op.param1)        
               
#==========================[Kris]=========================== 
            if op.param3 in Vmid:
                if op.param2 in mid1:
                    kr23.acceptGroupInvitation(op.param1)
            if op.param3 in Vmid:
                if op.param2 in Amid:
                    kr23.acceptGroupInvitation(op.param1)
            if op.param3 in Vmid:
                if op.param2 in Bmid:
                    kr23.acceptGroupInvitation(op.param1)
            if op.param3 in Vmid:
                if op.param2 in Cmid:
                    kr23.acceptGroupInvitation(op.param1)
            if op.param3 in Vmid:
                if op.param2 in Dmid:
                    kr23.acceptGroupInvitation(op.param1)
            if op.param3 in Vmid:
                if op.param2 in Emid:
                    kr23.acceptGroupInvitation(op.param1)
            if op.param3 in Vmid:
                if op.param2 in Fmid:
                    kr23.acceptGroupInvitation(op.param1)
            if op.param3 in Vmid:
                if op.param2 in Gmid:
                    kr23.acceptGroupInvitation(op.param1)
            if op.param3 in Vmid:
                if op.param2in Hmid:
                    kr23.acceptGroupInvitation(op.param1)
            if op.param3 in Vmid:
                if op.param2 in Jmid:
                    kr23.acceptGroupInvitation(op.param1)
            if op.param3 in Vmid:
                if op.param2 in Kmid:
                    kr23.acceptGroupInvitation(op.param1)
            if op.param3 in Vmid:
                if op.param2 in Lmid:
                    kr23.acceptGroupInvitation(op.param1)
            if op.param3 in Vmid:
                if op.param2 in Mmid:
                    kr23.acceptGroupInvitation(op.param1)
            if op.param3 in Vmid:
                if op.param2 in Nmid:
                    kr23.acceptGroupInvitation(op.param1)
            if op.param3 in Vmid:
                if op.param2 in Omid:
                    kr23.acceptGroupInvitation(op.param1)
            if op.param3 in Vmid:
                if op.param2 in Pmid:
                    kr23.acceptGroupInvitation(op.param1)
            if op.param3 in Vmid:
                if op.param2 in Qmid:
                    kr23.acceptGroupInvitation(op.param1)
            if op.param3 in Vmid:
                if op.param2 in Rmid:
                    kr23.acceptGroupInvitation(op.param1)   
            if op.param3 in Vmid:
                if op.param2 in Smid:
                    kr23.acceptGroupInvitation(op.param1)
            if op.param3 in Vmid:
                if op.param2 in Tmid:
                    kr23.acceptGroupInvitation(op.param1)
            if op.param3 in Vmid:
                if op.param2 in Imid:
                    kr23.acceptGroupInvitation(op.param1)
            if op.param3 in Vmid:
                if op.param2 in Umid:
                    kr23.acceptGroupInvitation(op.param1)
            if op.param3 in Vmid:
                if op.param2 in Wmid:
                    kr23.acceptGroupInvitation(op.param1)       
            if op.param3 in Vmid:
                if op.param2 in Xmid:
                    kr23.acceptGroupInvitation(op.param1)        
                 
#==========================[Kris]=========================== 
            if op.param3 in Wmid:
                if op.param2 in mid1:
                    kr24.acceptGroupInvitation(op.param1)
            if op.param3 in Wmid:
                if op.param2 in Amid:
                    kr24.acceptGroupInvitation(op.param1)
            if op.param3 in Wmid:
                if op.param2 in Bmid:
                    kr24.acceptGroupInvitation(op.param1)
            if op.param3 in Wmid:
                if op.param2 in Cmid:
                    kr24.acceptGroupInvitation(op.param1)
            if op.param3 in Wmid:
                if op.param2 in Dmid:
                    kr24.acceptGroupInvitation(op.param1)
            if op.param3 in Wmid:
                if op.param2 in Emid:
                    kr24.accptGroupInvitation(op.param1)
            if op.param3 in Wmid:
                if op.param2 in Fmid:
                    kr24.accWeptGroupInvitation(op.param1)
            if op.param3 in Wmid:
                if op.param2 in Gmid:
                    kr24.acceptGroupInvitation(op.param1)
            if op.param3 in Wmid:
                if op.param2in Hmid:
                    kr24.acceptGroupInvitation(op.param1)
            if op.param3 in Wmid:
                if op.param2 in Jmid:
                    kr24.acceptGroupInvitation(op.param1)
            if op.param3 in Wmid:
                if op.param2 in Kmid:
                    kr24.acceptGroupInvitation(op.param1)
            if op.param3 in Wmid:
                if op.param2 in Lmid:
                    kr24.acceptGroupInvitation(op.param1)
            if op.param3 in Wmid:
                if op.param2 in Mmid:
                    kr24.acceptGroupInvitation(op.param1)
            if op.param3 in Wmid:
                if op.param2 in Nmid:
                    kr24.acceptGroupInvitation(op.param1)
            if op.param3 in Wmid:
                if op.param2 in Omid:
                    kr24.acceptGroupInvitation(op.param1)
            if op.param3 in Wmid:
                if op.param2 in Pmid:
                    kr24.acceptGroupInvitation(op.param1)
            if op.param3 in Wmid:
                if op.param2 in Qmid:
                    kr24.acceptGroupInvitation(op.param1)
            if op.param3 in Wmid:
                if op.param2 in Rmid:
                    kr24.acceptGroupInvitation(op.param1)   
            if op.param3 in Wmid:
                if op.param2 in Smid:
                    kr24.acceptGroupInvitation(op.param1)
            if op.param3 in Wmid:
                if op.param2 in Tmid:
                    kr24.acceptGroupInvitation(op.param1)
            if op.param3 in Wmid:
                if op.param2 in Imid:
                    kr24.acceptGroupInvitation(op.param1)
            if op.param3 in Wmid:
                if op.param2 in Vmid:
                    kr24.acceptGroupInvitation(op.param1)
            if op.param3 in Wmid:
                if op.param2 in Umid:
                    kr24.acceptGroupInvitation(op.param1)       
            if op.param3 in Wmid:
                if op.param2 in Xmid:
                    kr24.acceptGroupInvitation(op.param1)        
             
#==========================[Kris]=========================== 
            if op.param3 in Xmid:
                if op.param2 in mid1:
                    kr25.acceptGroupInvitation(op.param1)
            if op.param3 in Xmid:
                if op.param2 in Amid:
                    kr25.acceptGroupInvitation(op.param1)
            if op.param3 in Xmid:
                if op.param2 in Bmid:
                    kr25.acceptGroupInvitation(op.param1)
            if op.param3 in Xmid:
                if op.param2 in Cmid:
                    kr25.acceptGroupInvitation(op.param1)
            if op.param3 in Xmid:
                if op.param2 in Dmid:
                    kr25.acceptGroupInvitation(op.param1)
            if op.param3 in Xmid:
                if op.param2 in Emid:
                    kr25.acceptGroupInvitation(op.param1)
            if op.param3 in Xmid:
                if op.param2 in Fmid:
                    kr25.acceptGroupInvitation(op.param1)
            if op.param3 in Xmid:
                if op.param2 in Gmid:
                    kr25.acceptGroupInvitation(op.param1)
            if op.param3 in Xmid:
                if op.param2in Hmid:
                    kr25.acceptGroupInvitation(op.param1)
            if op.param3 in Xmid:
                if op.param2 in Jmid:
                    kr25.acceptGroupInvitation(op.param1)
            if op.param3 in Xmid:
                if op.param2 in Kmid:
                    kr25.acceptGroupInvitation(op.param1)
            if op.param3 in Xmid:
                if op.param2 in Lmid:
                    kr25.acceptGroupInvitation(op.param1)
            if op.param3 in Xmid:
                if op.param2 in Mmid:
                    kr25.acceptGroupInvitation(op.param1)
            if op.param3 in Xmid:
                if op.param2 in Nmid:
                    kr25.acceptGroupInvitation(op.param1)
            if op.param3 in Xmid:
                if op.param2 in Omid:
                    kr25.acceptGroupInvitation(op.param1)
            if op.param3 in Xmid:
                if op.param2 in Pmid:
                    kr25.acceptGroupInvitation(op.param1)
            if op.param3 in Xmid:
                if op.param2 in Qmid:
                    kr25.acceptGroupInvitation(op.param1)
            if op.param3 in Xmid:
                if op.param2 in Rmid:
                    kr25.acceptGroupInvitation(op.param1)   
            if op.param3 in Xmid:
                if op.param2 in Smid:
                    kr25.acceptGroupInvitation(op.param1)
            if op.param3 in Xmid:
                if op.param2 in Tmid:
                    kr25.acceptGroupInvitation(op.param1)
            if op.param3 in Xmid:
                if op.param2 in Imid:
                    kr25.acceptGroupInvitation(op.param1)
            if op.param3 in Xmid:
                if op.param2 in Vmid:
                    kr25.acceptGroupInvitation(op.param1)
            if op.param3 in Xmid:
                if op.param2 in Wmid:
                    kr25.acceptGroupInvitation(op.param1)       
            if op.param3 in Xmid:
                if op.param2 in Umid:
                    kr25.acceptGroupInvitation(op.param1)        

#==========================[Kris]=========================== 
        if op.type == 13:
            if mid1 in op.param3:
                if wait['autoJoin'] == True:
                    if op.param2 in Bots or owner:
                        kr1.acceptGroupInvitation(op.param1)
                    else:
                        kr1.acceptGroupInvitation(op.param1)
                        kr1.kickoutFromGroup(op.param1,[op.param2])
                        kr1.leaveGroup(op.param1)
                else:
                    print "autoJoin is Off"
                
            if Amid in op.param3:
                if wait['autoJoin'] == True:
                    if op.param2 in Bots or owner:
                        kr2.acceptGroupInvitation(op.param1)
                    else:
                        kr2.acceptGroupInvitation(op.param1)
                        kr2.kickoutFromGroup(op.param1,[op.param2])
                        kr2.leaveGroup(op.param1)
                else:
                    print "autoJoin is Off"
                
            if Bmid in op.param3:
                if wait['autoJoin'] == True:
                    if op.param2 in Bots or owner:
                        kr3.acceptGroupInvitation(op.param1)
                    else:
                        kr3.acceptGroupInvitation(op.param1)
                        kr3.kickoutFromGroup(op.param1,[op.param2])
                        kr3.leaveGroup(op.param1)
                else:
                    print "autoJoin is Off"
                
            if Cmid in op.param3:
                if wait['autoJoin'] == True:
                    if op.param2 in Bots or owner:
                        kr4.acceptGroupInvitation(op.param1)
                    else:
                        kr4.acceptGroupInvitation(op.param1)
                        kr4.kickoutFromGroup(op.param1,[op.param2])
                        kr4.leaveGroup(op.param1)
                else:
                    print "autoJoin is Off"
                
            if Dmid in op.param3:
                if wait['autoJoin'] == True:
                    if op.param2 in Bots or owner:
                        kr5.acceptGroupInvitation(op.param1)
                    else:
                        kr5.acceptGroupInvitation(op.param1)
                        kr5.kickoutFromGroup(op.param1,[op.param2])
                        kr5.leaveGroup(op.param1)
                else:
                    print "autoJoin is Off"
                    
            if Emid in op.param3:
                if wait['autoJoin'] == True:
                    if op.param2 in Bots or owner:
                        kr6.acceptGroupInvitation(op.param1)
                    else:
                        kr6.acceptGroupInvitation(op.param1)
                        kr6.kickoutFromGroup(op.param1,[op.param2])
                        kr6.leaveGroup(op.param1)
                else:
                    print "autoJoin is Off"
                    
            if Fmid in op.param3:
                if wait['autoJoin'] == True:
                    if op.param2 in Bots or owner:
                        kr7.acceptGroupInvitation(op.param1)
                    else:
                        kr7.acceptGroupInvitation(op.param1)
                        kr7.kickoutFromGroup(op.param1,[op.param2])
                        kr7.leaveGroup(op.param1)
                else:
                    print "autoJoin is Off"
                    
            if Gmid in op.param3:
                if wait['autoJoin'] == True:
                    if op.param2 in Bots or owner:
                        kr8.acceptGroupInvitation(op.param1)
                    else:
                        kr8.acceptGroupInvitation(op.param1)
                        kr8.kickoutFromGroup(op.param1,[op.param2])
                        kr8.leaveGroup(op.param1)
                else:
                    print "autoJoin is Off"
                    
            if Hmid in op.param3:
                if wait['autoJoin'] == True:
                    if op.param2 in Bots or owner:
                        kr9.acceptGroupInvitation(op.param1)
                    else:
                        kr9.acceptGroupInvitation(op.param1)
                        kr9.kickoutFromGroup(op.param1,[op.param2])
                        kr9.leaveGroup(op.param1)
                else:
                    print "autoJoin is Off"
                    
            if Imid in op.param3:
                if wait['autoJoin'] == True:
                    if op.param2 in Bots or owner:
                        kr10.acceptGroupInvitation(op.param1)
                    else:
                        kr10.acceptGroupInvitation(op.param1)
                        kr10.kickoutFromGroup(op.param1,[op.param2])
                        kr10.leaveGroup(op.param1)
                else:
                    print "autoJoin is Off"
#==========================[Kris]===========================
        if op.type == 19:
            if wait["autoKick"] == True:
                if op.param2 in admin or Bots:
                    pass
                else:
                    try:
                        kr3.kickoutFromGroup(op.param1,[op.param2])
                        kr8.kickoutFromGroup(op.param1,[op.param2])
                        kr1.inviteIntoGroup(op.param1,[op.param3])
                        kr5.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                if op.param2 in wait["blacklist"]:
                    pass
                else:
                    if op.param2 in admin or Bots:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
#==========================[Kris]===========================
            if mid1 in op.param3:
                if op.param2 in Bots or admin:
                    pass
                else:
                    try:
                        kr2.kickoutFromGroup(op.param1,[op.param2])
                        kr3.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
                            if op.param2 in Bots:
                                pass
                            else:
                                wait["blacklist"][op.param2] = True
                    G = kr3.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    kr3.updateGroup(G)
                    Ti = kr3.reissueGroupTicket(op.param1)
                    kr1.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr2.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr3.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr4.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr5.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr6.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr7.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr8.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr9.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr10.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr11.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr12.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr13.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr14.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr15.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr16.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr17.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr18.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr19.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr20.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr21.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr22.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr23.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr24.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr25.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kr1.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kr1.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
                        if op.param2 in Bots:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

            if Amid in op.param3:
                if op.param2 in Bots or admin:
                    pass
                else:
                    try:
                        kr3.kickoutFromGroup(op.param1,[op.param2])
                        kr4.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
                            if op.param2 in Bots:
                                pass
                            else:
                                wait["blacklist"][op.param2] = True
                    G = kr4.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    kr4.updateGroup(G)
                    Ti = kr4.reissueGroupTicket(op.param1)
                    kr1.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr2.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr3.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr4.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr5.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr6.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr7.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr8.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr9.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr10.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr11.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr12.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr13.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr14.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr15.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr16.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr17.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr18.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr19.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr20.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr21.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr22.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr23.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr24.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr25.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kr2.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kr2.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
                        if op.param2 in Bots:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

            if Bmid in op.param3:
                if op.param2 in Bots or admin:
                    pass
                else:
                    try:
                        kr4.kickoutFromGroup(op.param1,[op.param2])
                        kr5.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
                            if op.param2 in Bots:
                                pass
                            else:
                                wait["blacklist"][op.param2] = True
                    G = kr5.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    kr5.updateGroup(G)
                    Ti = kr5.reissueGroupTicket(op.param1)
                    kr1.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr2.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr3.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr4.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr5.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr6.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr7.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr8.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr9.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr10.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr11.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr12.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr13.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr14.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr15.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr16.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr17.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr18.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr19.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr20.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr21.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr22.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr23.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr24.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr25.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kr3.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kr3.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
                        if op.param2 in Bots:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

            if Cmid in op.param3:
                if op.param2 in Bots or admin:
                    pass
                else:
                    try:
                        kr5.kickoutFromGroup(op.param1,[op.param2])
                        kr6.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
                            if op.param2 in Bots:
                                pass
                            else:
                                wait["blacklist"][op.param2] = True
                    G = kr6.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    kr6.updateGroup(G)
                    Ti = kr6.reissueGroupTicket(op.param1)
                    kr1.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr2.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr3.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr4.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr5.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr6.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr7.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr8.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr9.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr10.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr11.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr12.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr13.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr14.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr15.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr16.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr17.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr18.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr19.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr20.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr21.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr22.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr23.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr24.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr25.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kr4.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kr4.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
                        if op.param2 in Bots:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

            if Dmid in op.param3:
                if op.param2 in Bots or admin:
                    pass
                else:
                    try:
                        kr6.kickoutFromGroup(op.param1,[op.param2])
                        kr7.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
                            if op.param2 in Bots:
                                pass
                            else:
                                wait["blacklist"][op.param2] = True
                    G = kr7.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    kr7.updateGroup(G)
                    Ti = kr7.reissueGroupTicket(op.param1)
                    kr1.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr2.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr3.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr4.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr5.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr6.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr7.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr8.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr9.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr10.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr11.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr12.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr13.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr14.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr15.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr16.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr17.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr18.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr19.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr20.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr21.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr22.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr23.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr24.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr25.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kr5.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kr5.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
                        if op.param2 in Bots:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

            if Emid in op.param3:
                if op.param2 in Bots or admin:
                    pass
                else:
                    try:
                        kr7.kickoutFromGroup(op.param1,[op.param2])
                        kr8.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
                            if op.param2 in Bots:
                                pass
                            else:
                                wait["blacklist"][op.param2] = True
                    G = kr8.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    kr8.updateGroup(G)
                    Ti = kr8.reissueGroupTicket(op.param1)
                    kr1.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr2.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr3.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr4.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr5.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr6.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr7.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr8.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr9.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr10.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr11.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr12.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr13.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr14.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr15.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr16.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr17.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr18.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr19.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr20.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr21.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr22.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr23.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr24.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr25.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kr6.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kr6.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
                        if op.param2 in Bots:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
            if Fmid in op.param3:
                if op.param2 in Bots or admin:
                    pass
                else:
                    try:
                        kr8.kickoutFromGroup(op.param1,[op.param2])
                        kr9.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
                            if op.param2 in Bots:
                                pass
                            else:
                                wait["blacklist"][op.param2] = True
                    G = kr9.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    kr9.updateGroup(G)
                    Ti = kr9.reissueGroupTicket(op.param1)
                    kr1.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr2.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr3.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr4.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr5.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr6.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr7.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr8.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr9.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr10.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr11.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr12.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr13.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr14.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr15.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr16.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr17.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr18.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr19.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr20.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr21.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr22.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr23.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr24.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr25.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kr7.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kr7.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
                        if op.param2 in Bots:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

            if Gmid in op.param3:
                if op.param2 in Bots or admin:
                    pass
                else:
                    try:
                        kr9.kickoutFromGroup(op.param1,[op.param2])
                        kr10.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
                            if op.param2 in Bots:
                                pass
                            else:
                                wait["blacklist"][op.param2] = True
                    G = kr10.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    kr10.updateGroup(G)
                    Ti = kr10.reissueGroupTicket(op.param1)
                    kr1.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr2.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr3.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr4.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr5.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr6.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr7.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr8.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr9.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr10.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr11.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr12.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr13.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr14.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr15.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr16.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr17.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr18.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr19.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr20.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr21.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr22.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr23.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr24.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr25.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kr8.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kr8.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
                        if op.param2 in Bots:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

            if Hmid in op.param3:
                if op.param2 in Bots or admin:
                    pass
                else:
                    try:
                        kr10.kickoutFromGroup(op.param1,[op.param2])
                        kr11.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
                            if op.param2 in Bots:
                                pass
                            else:
                                wait["blacklist"][op.param2] = True
                    G = kr11.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    kr11.updateGroup(G)
                    Ti = kr11.reissueGroupTicket(op.param1)
                    kr1.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr2.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr3.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr4.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr5.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr6.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr7.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr8.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr9.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr10.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr11.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr12.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr13.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr14.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr15.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr16.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr17.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr18.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr19.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr20.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr21.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr22.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr23.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr24.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr25.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kr9.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kr9.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
                        if op.param2 in Bots:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

            if Imid in op.param3:
                if op.param2 in Bots or admin:
                    pass
                else:
                    try:
                        kr11.kickoutFromGroup(op.param1,[op.param2])
                        kr12.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
                            if op.param2 in Bots:
                                pass
                            else:
                                wait["blacklist"][op.param2] = True
                    G = kr12.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    kr12.updateGroup(G)
                    Ti = kr12.reissueGroupTicket(op.param1)
                    kr1.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr2.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr3.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr4.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr5.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr6.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr7.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr8.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr9.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr10.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr11.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr12.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr13.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr14.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr15.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr16.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr17.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr18.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr19.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr20.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr21.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr22.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr23.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr24.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr25.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kr10.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kr10.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
                        if op.param2 in Bots:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
            if Jmid in op.param3:
                if op.param2 in Bots or admin:
                    pass
                else:
                    try:
                        kr12.kickoutFromGroup(op.param1,[op.param2])
                        kr13.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
                            if op.param2 in Bots:
                                pass
                            else:
                                wait["blacklist"][op.param2] = True
                    G = kr13.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    kr13.updateGroup(G)
                    Ti = kr13.reissueGroupTicket(op.param1)
                    kr1.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr2.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr3.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr4.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr5.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr6.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr7.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr8.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr9.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr10.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr11.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr12.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr13.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr14.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr15.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr16.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr17.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr18.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr19.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr20.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr21.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr22.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr23.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr24.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr25.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kr11.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kr11.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
                        if op.param2 in Bots:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True    
            if Kmid in op.param3:
                if op.param2 in Bots or admin:
                    pass
                else:
                    try:
                        kr13.kickoutFromGroup(op.param1,[op.param2])
                        kr14.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
                            if op.param2 in Bots:
                                pass
                            else:
                                wait["blacklist"][op.param2] = True
                    G = kr14.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    kr14.updateGroup(G)
                    Ti = kr14.reissueGroupTicket(op.param1)
                    kr1.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr2.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr3.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr4.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr5.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr6.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr7.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr8.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr9.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr10.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr11.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr12.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr13.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr14.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr15.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr16.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr17.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr18.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr19.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr20.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr21.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr22.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr23.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr24.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr25.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kr12.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kr12.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
                        if op.param2 in Bots:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True                              
                            
            if Lmid in op.param3:
                if op.param2 in Bots or admin:
                    pass
                else:
                    try:
                        kr14.kickoutFromGroup(op.param1,[op.param2])
                        kr15.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
                            if op.param2 in Bots:
                                pass
                            else:
                                wait["blacklist"][op.param2] = True
                    G = kr15.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    kr13.updateGroup(G)
                    Ti = kr15.reissueGroupTicket(op.param1)
                    kr1.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr2.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr3.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr4.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr5.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr6.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr7.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr8.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr9.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr10.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr11.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr12.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr13.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr14.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr15.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr16.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr17.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr18.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr19.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr20.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr21.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr22.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr23.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr24.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr25.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kr13.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kr13.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
                        if op.param2 in Bots:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True               
            if Mmid in op.param3:
                if op.param2 in Bots or admin:
                    pass
                else:
                    try:
                        kr15.kickoutFromGroup(op.param1,[op.param2])
                        kr16.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
                            if op.param2 in Bots:
                                pass
                            else:
                                wait["blacklist"][op.param2] = True
                    G = kr16.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    kr16.updateGroup(G)
                    Ti = kr16.reissueGroupTicket(op.param1)
                    kr1.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr2.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr3.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr4.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr5.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr6.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr7.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr8.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr9.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr10.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr11.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr12.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr13.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr14.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr15.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr16.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr17.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr18.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr19.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr20.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr21.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr22.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr23.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr24.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr25.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kr14.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kr14.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
                        if op.param2 in Bots:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True               
                            
            if Nmid in op.param3:
                if op.param2 in Bots or admin:
                    pass
                else:
                    try:
                        kr16.kickoutFromGroup(op.param1,[op.param2])
                        kr17.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
                            if op.param2 in Bots:
                                pass
                            else:
                                wait["blacklist"][op.param2] = True
                    G = kr17.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    kr17.updateGroup(G)
                    Ti = kr17.reissueGroupTicket(op.param1)
                    kr1.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr2.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr3.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr4.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr5.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr6.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr7.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr8.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr9.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr10.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr11.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr12.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr13.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr14.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr15.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr16.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr17.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr18.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr19.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr20.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr21.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr22.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr23.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr24.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr25.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kr15.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kr15.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
                        if op.param2 in Bots:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True               
                            
            if Omid in op.param3:
                if op.param2 in Bots or admin:
                    pass
                else:
                    try:
                        kr17.kickoutFromGroup(op.param1,[op.param2])
                        kr18.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
                            if op.param2 in Bots:
                                pass
                            else:
                                wait["blacklist"][op.param2] = True
                    G = kr18.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    kr18.updateGroup(G)
                    Ti = kr18.reissueGroupTicket(op.param1)
                    kr1.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr2.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr3.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr4.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr5.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr6.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr7.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr8.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr9.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr10.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr11.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr12.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr13.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr14.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr15.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr16.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr17.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr18.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr19.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr20.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr21.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr22.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr23.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr24.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr25.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kr16.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kr16.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
                        if op.param2 in Bots:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True                              
            if Pmid in op.param3:
                if op.param2 in Bots or admin:
                    pass
                else:
                    try:
                        kr18.kickoutFromGroup(op.param1,[op.param2])
                        kr19.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
                            if op.param2 in Bots:
                                pass
                            else:
                                wait["blacklist"][op.param2] = True
                    G = kr19.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    kr19.updateGroup(G)
                    Ti = kr19.reissueGroupTicket(op.param1)
                    kr1.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr2.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr3.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr4.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr5.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr6.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr7.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr8.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr9.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr10.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr11.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr12.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr13.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr14.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr15.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr16.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr17.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr18.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr19.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr20.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr21.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr22.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr23.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr24.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr25.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kr17.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kr17.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
                        if op.param2 in Bots:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True               
            if Qmid in op.param3:
                if op.param2 in Bots or admin:
                    pass
                else:
                    try:
                        kr19.kickoutFromGroup(op.param1,[op.param2])
                        kr20.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
                            if op.param2 in Bots:
                                pass
                            else:
                                wait["blacklist"][op.param2] = True
                    G = kr20.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    kr20.updateGroup(G)
                    Ti = kr20.reissueGroupTicket(op.param1)
                    kr1.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr2.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr3.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr4.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr5.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr6.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr7.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr8.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr9.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr10.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr11.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr12.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr13.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr14.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr15.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr16.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr17.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr18.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr19.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr20.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr21.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr22.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr23.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr24.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr25.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kr18.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kr18.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
                        if op.param2 in Bots:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True               
                            
            if Rmid in op.param3:
                if op.param2 in Bots or admin:
                    pass
                else:
                    try:
                        kr20.kickoutFromGroup(op.param1,[op.param2])
                        kr21.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
                            if op.param2 in Bots:
                                pass
                            else:
                                wait["blacklist"][op.param2] = True
                    G = kr21.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    kr21.updateGroup(G)
                    Ti = kr21.reissueGroupTicket(op.param1)
                    kr1.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr2.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr3.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr4.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr5.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr6.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr7.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr8.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr9.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr10.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr11.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr12.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr13.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr14.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr15.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr16.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr17.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr18.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr19.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr20.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr21.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr22.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr23.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr24.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr25.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kr19.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kr19.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
                        if op.param2 in Bots:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True                               
            if Smid in op.param3:
                if op.param2 in Bots or admin:
                    pass
                else:
                    try:
                        kr21.kickoutFromGroup(op.param1,[op.param2])
                        kr22.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
                            if op.param2 in Bots:
                                pass
                            else:
                                wait["blacklist"][op.param2] = True
                    G = kr22.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    kr22.updateGroup(G)
                    Ti = kr22.reissueGroupTicket(op.param1)
                    kr1.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr2.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr3.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr4.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr5.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr6.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr7.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr8.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr9.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr10.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr11.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr12.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr13.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr14.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr15.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr16.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr17.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr18.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr19.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr20.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr21.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr22.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr23.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr24.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr25.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kr20.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kr20.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
                        if op.param2 in Bots:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True           
                            
            if Tmid in op.param3:
                if op.param2 in Bots or admin:
                    pass
                else:
                    try:
                        kr22.kickoutFromGroup(op.param1,[op.param2])
                        kr23.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
                            if op.param2 in Bots:
                                pass
                            else:
                                wait["blacklist"][op.param2] = True
                    G = kr23.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    kr23.updateGroup(G)
                    Ti = kr23.reissueGroupTicket(op.param1)
                    kr1.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr2.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr3.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr4.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr5.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr6.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr7.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr8.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr9.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr10.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr11.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr12.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr13.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr14.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr15.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr16.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr17.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr18.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr19.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr20.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr21.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr22.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr23.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr24.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr25.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kr21.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kr21.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
                        if op.param2 in Bots:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True           
                      
            if Umid in op.param3:
                if op.param2 in Bots or admin:
                    pass
                else:
                    try:
                        kr23.kickoutFromGroup(op.param1,[op.param2])
                        kr24.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
                            if op.param2 in Bots:
                                pass
                            else:
                                wait["blacklist"][op.param2] = True
                    G = kr24.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    kr24.updateGroup(G)
                    Ti = kr24.reissueGroupTicket(op.param1)
                    kr1.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr2.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr3.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr4.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr5.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr6.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr7.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr8.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr9.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr10.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr11.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr12.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr13.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr14.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr15.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr16.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr17.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr18.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr19.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr20.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr21.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr22.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr23.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr24.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr25.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kr22.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kr22.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
                        if op.param2 in Bots:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True    
            if Vmid in op.param3:
                if op.param2 in Bots or admin:
                    pass
                else:
                    try:
                        kr24.kickoutFromGroup(op.param1,[op.param2])
                        kr25.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
                            if op.param2 in Bots:
                                pass
                            else:
                                wait["blacklist"][op.param2] = True
                    G = kr25.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    kr25.updateGroup(G)
                    Ti = kr25.reissueGroupTicket(op.param1)
                    kr1.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr2.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr3.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr4.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr5.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr6.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr7.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr8.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr9.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr10.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr11.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr12.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr13.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr14.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr15.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr16.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr17.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr18.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr19.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr20.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr21.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr22.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr23.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr24.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr25.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kr23.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kr23.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
                        if op.param2 in Bots:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True            
                            
            if Wmid in op.param3:
                if op.param2 in Bots or admin:
                    pass
                else:
                    try:
                        kr25.kickoutFromGroup(op.param1,[op.param2])
                        kr1.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
                            if op.param2 in Bots:
                                pass
                            else:
                                wait["blacklist"][op.param2] = True
                    G = kr1.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    kr1.updateGroup(G)
                    Ti = kr1.reissueGroupTicket(op.param1)
                    kr1.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr2.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr3.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr4.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr5.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr6.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr7.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr8.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr9.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr10.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr11.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr12.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr13.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr14.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr15.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr16.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr17.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr18.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr19.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr20.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr21.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr22.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr23.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr24.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr25.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kr24.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kr24.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
                        if op.param2 in Bots:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True                  
                                         
            if Xmid in op.param3:
                if op.param2 in Bots or admin:
                    pass
                else:
                    try:
                        kr1.kickoutFromGroup(op.param1,[op.param2])
                        kr2.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
                            if op.param2 in Bots:
                                pass
                            else:
                                wait["blacklist"][op.param2] = True
                    G = kr2.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    kr2.updateGroup(G)
                    Ti = kr2.reissueGroupTicket(op.param1)
                    kr1.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr2.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr3.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr4.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr5.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr6.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr7.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr8.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr9.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr10.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr11.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr12.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr13.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr14.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr15.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr16.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr17.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr18.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr19.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr20.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr21.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr22.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr23.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr24.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr25.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kr25.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kr25.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
                        if op.param2 in Bots:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True                         
#==========================[Kris]===========================
        if op.type == 19:
            if op.param3 in admin:
                if op.param2 not in admin:
                    try:
                        kr3.kickoutFromGroup(op.param1,[op.param2])
                        kr1.inviteIntoGroup(op.param1,[op.param3])
                        wait["blacklist"][op.param2] = True
                    except:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        wait["blacklist"][op.param2] = True
                                
            if op.param3 not in admin:
                if op.param2 not in admin:
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        
            if op.param3 in admin:
                if op.param2 in admin:
                    try:
                        kr1.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])

        if op.type == 19:
            if op.param3 in Bots:
                if op.param2 not in admin:
                    try:
                        kr3.kickoutFromGroup(op.param1,[op.param2])
                        mid1=["u4a0f653ea757da7abcd41c15bf0f15da"]
                        midd1 = (mid1)
                        kr2.findAndAddContactsByMid(midd1)
                        kr2.inviteIntoGroup(op.param1,[midd1])
                        kr1.acceptGroupInvitation(op.param1)
                    except:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        mid1=["u4a0f653ea757da7abcd41c15bf0f15da"]
                        midd1 = (mid1)
                        random.choice(KAC).findAndAddContactsByMid(midd1)
                        random.choice(KAC).inviteIntoGroup(op.param1,[midd1])
                        kr1.acceptGroupInvitation(op.param1)
                    
            if op.param3 in Bots:
                if op.param2 not in admin:
                    try:
                        kr4.kickoutFromGroup(op.param1,[op.param2])        
                        Amid=["udb0b6b2c1f32887d23bd3e4dfb302ed1"]
                        midd2 = (Amid)
                        kr3.findAndAddContactsByMid(midd2)
                        kr3.inviteIntoGroup(op.param1,[midd2])
                        kr2.acceptGroupInvitation(op.param1)
                    except:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])        
                        Amid=["udb0b6b2c1f32887d23bd3e4dfb302ed1"]
                        midd2 = (Amid)
                        random.choice(KAC).findAndAddContactsByMid(midd2)
                        random.choice(KAC).inviteIntoGroup(op.param1,[midd2])
                        kr2.acceptGroupInvitation(op.param1)
                        
            if op.param3 in Bots:
                if op.param2 not in admin:
                    try:
                        kr5.kickoutFromGroup(op.param1,[op.param2])
                        Bmid=["uad6cb020c5ca7afbecb4681675eb38cd"]
                        midd3 = (Bmid)
                        kr4.findAndAddContactsByMid(midd3)
                        kr4.inviteIntoGroup(op.param1,[midd3])
                        kr3.acceptGroupInvitation(op.param1)
                    except:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        Bmid=["uad6cb020c5ca7afbecb4681675eb38cd"]
                        midd3 = (Bmid)
                        random.choice(KAC).findAndAddContactsByMid(midd3)
                        random.choice(KAC).inviteIntoGroup(op.param1,[midd3])
                        kr3.acceptGroupInvitation(op.param1)
                    
            if op.param3 in Bots:
                if op.param2 not in admin:
                    try:
                        kr6.kickoutFromGroup(op.param1,[op.param2])
                        Cmid=["ud5262649376cbf7576e2dcac0331d481"]
                        midd4 = (Cmid)
                        kr5.findAndAddContactsByMid(midd4)
                        kr5.inviteIntoGroup(op.param1,[midd4])
                        kr4.acceptGroupInvitation(op.param1)
                    except:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        Cmid=["ud5262649376cbf7576e2dcac0331d481"]
                        midd4 = (Cmid)
                        random.choice(KAC).findAndAddContactsByMid(midd4)
                        random.choice(KAC).inviteIntoGroup(op.param1,[midd4])
                        kr4.acceptGroupInvitation(op.param1)
                    
            if op.param3 in Bots:
                if op.param2 not in admin:
                    try:
                        kr7.kickoutFromGroup(op.param1,[op.param2])
                        Dmid=["u53c352134325f0c49e86534c57801bd7"]
                        midd5 = (Dmid)
                        kr6.findAndAddContactsByMid(midd5)
                        kr6.inviteIntoGroup(op.param1,[midd5])
                        kr5.acceptGroupInvitation(op.param1)
                    except:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        Dmid=["u53c352134325f0c49e86534c57801bd7"]
                        midd5 = (Dmid)
                        random.choice(KAC).findAndAddContactsByMid(midd5)
                        random.choice(KAC).inviteIntoGroup(op.param1,[midd5])
                        kr5.acceptGroupInvitation(op.param1)
                    
            if op.param3 in Bots:
                if op.param2 not in admin:
                    try:
                        kr8.kickoutFromGroup(op.param1,[op.param2])
                        Emid=["ua2ea9f4c32848bc67644c5267bb91279"]
                        midd6 = (Emid)
                        kr7.findAndAddContactsByMid(midd6)
                        kr7.inviteIntoGroup(op.param1,[midd6])
                        kr6.acceptGroupInvitation(op.param1)
                    except:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        Emid=["ua2ea9f4c32848bc67644c5267bb91279"]
                        midd6 = (Emid)
                        random.choice(KAC).findAndAddContactsByMid(midd6)
                        random.choice(KAC).inviteIntoGroup(op.param1,[midd6])
                        kr6.acceptGroupInvitation(op.param1)
                    
            if op.param3 in Bots:
                if op.param2 not in admin:
                    try:
                        kr9.kickoutFromGroup(op.param1,[op.param2])
                        Fmid=["uadfd3a23698b71d17c64482d27dc2ed1"]
                        midd7 = (Fmid)
                        kr8.findAndAddContactsByMid(midd7)
                        kr8.inviteIntoGroup(op.param1,[midd7])
                        kr7.acceptGroupInvitation(op.param1)
                    except:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        Fmid=["uadfd3a23698b71d17c64482d27dc2ed1"]
                        midd7 = (Fmid)
                        random.choice(KAC).findAndAddContactsByMid(midd7)
                        random.choice(KAC).inviteIntoGroup(op.param1,[midd7])
                        kr7.acceptGroupInvitation(op.param1)
                    
            if op.param3 in Bots:
                if op.param2 not in admin:
                    try:
                        kr10.kickoutFromGroup(op.param1,[op.param2])
                        Gmid=["u45c6ce403f0acc28392c519028aae154"]
                        midd8 = (Gmid)
                        kr9.findAndAddContactsByMid(midd8)
                        kr9.inviteIntoGroup(op.param1,[midd8])
                        kr8.acceptGroupInvitation(op.param1)
                    except:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        Gmid=["u45c6ce403f0acc28392c519028aae154"]
                        midd8 = (Gmid)
                        random.choice(KAC).findAndAddContactsByMid(midd8)
                        random.choice(KAC).inviteIntoGroup(op.param1,[midd8])
                        kr8.acceptGroupInvitation(op.param1)
                    
            if op.param3 in Bots:
                if op.param2 not in admin:
                    try:
                        kr11.kickoutFromGroup(op.param1,[op.param2])
                        Hmid=["udcf44c4272d8209a8a5f2dd1afeea93f"]
                        midd9 = (Hmid)
                        kr10.findAndAddContactsByMid(midd9)
                        kr10.inviteIntoGroup(op.param1,[midd9])
                        kr9.acceptGroupInvitation(op.param1)
                    except:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        Hmid=["udcf44c4272d8209a8a5f2dd1afeea93f"]
                        midd9 = (Hmid)
                        random.choice(KAC).findAndAddContactsByMid(midd9)
                        random.choice(KAC).inviteIntoGroup(op.param1,[midd9])
                        kr9.acceptGroupInvitation(op.param1)
                    
            if op.param3 in Bots:
                if op.param2 not in admin:
                    try:
                        kr12.kickoutFromGroup(op.param1,[op.param2])
                        Imid=["u4a0be979fc73e88ebfe915bc917237b8"]
                        midd10 = (Imid)
                        kr11.findAndAddContactsByMid(midd10)
                        kr11.inviteIntoGroup(op.param1,[midd10])
                        kr10.acceptGroupInvitation(op.param1)
                    except:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        Imid=["u4a0be979fc73e88ebfe915bc917237b8"]
                        midd10 = (Imid)
                        random.choice(KAC).findAndAddContactsByMid(midd10)
                        random.choice(KAC).inviteIntoGroup(op.param1,[midd10])
                        kr10.acceptGroupInvitation(op.param1)
                                    
            if op.param3 in Bots:
                if op.param2 not in admin:
                    try:
                        kr13.kickoutFromGroup(op.param1,[op.param2])
                        Jmid=["u4a0be979fc73e88ebfe915bc917237b8"]
                        midd11 = (Jmid)
                        kr12.findAndAddContactsByMid(midd11)
                        kr12.inviteIntoGroup(op.param1,[midd11])
                        kr11.acceptGroupInvitation(op.param1)
                    except:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        Jmid=["u4a0be979fc73e88ebfe915bc917237b8"]
                        midd11 = (Jmid)
                        random.choice(KAC).findAndAddContactsByMid(midd11)
                        random.choice(KAC).inviteIntoGroup(op.param1,[midd11])
                        kr11.acceptGroupInvitation(op.param1)            
                        
            if op.param3 in Bots:
                if op.param2 not in admin:
                    try:
                        kr14.kickoutFromGroup(op.param1,[op.param2])
                        Kmid=["u4a0be979fc73e88ebfe915bc917237b8"]
                        midd12 = (Kmid)
                        kr13.findAndAddContactsByMid(midd12)
                        kr13.inviteIntoGroup(op.param1,[midd12])
                        kr12.acceptGroupInvitation(op.param1)
                    except:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        Kmid=["u4a0be979fc73e88ebfe915bc917237b8"]
                        midd12 = (Kmid)
                        random.choice(KAC).findAndAddContactsByMid(midd12)
                        random.choice(KAC).inviteIntoGroup(op.param1,[midd12])
                        kr12.acceptGroupInvitation(op.param1)           
            if op.param3 in Bots:
                if op.param2 not in admin:
                    try:
                        kr15.kickoutFromGroup(op.param1,[op.param2])
                        Lmid=["u4a0be979fc73e88ebfe915bc917237b8"]
                        midd13 = (Lmid)
                        kr14.findAndAddContactsByMid(midd13)
                        kr14.inviteIntoGroup(op.param1,[midd13])
                        kr13.acceptGroupInvitation(op.param1)
                    except:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        Lmid=["u4a0be979fc73e88ebfe915bc917237b8"]
                        midd13 = (Lmid)
                        random.choice(KAC).findAndAddContactsByMid(midd13)
                        random.choice(KAC).inviteIntoGroup(op.param1,[midd13])
                        kr13.acceptGroupInvitation(op.param1)                   
                        
            if op.param3 in Bots:
                if op.param2 not in admin:
                    try:
                        kr16.kickoutFromGroup(op.param1,[op.param2])
                        Mmid=["u4a0be979fc73e88ebfe915bc917237b8"]
                        midd14 = (Mmid)
                        kr15.findAndAddContactsByMid(midd14)
                        kr15.inviteIntoGroup(op.param1,[midd14])
                        kr14.acceptGroupInvitation(op.param1)
                    except:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        Mmid=["u4a0be979fc73e88ebfe915bc917237b8"]
                        midd14 = (Mmid)
                        random.choice(KAC).findAndAddContactsByMid(midd14)
                        random.choice(KAC).inviteIntoGroup(op.param1,[midd14])
                        kr14.acceptGroupInvitation(op.param1)                    
                        
            if op.param3 in Bots:
                if op.param2 not in admin:
                    try:
                        kr17.kickoutFromGroup(op.param1,[op.param2])
                        Nmid=["u4a0be979fc73e88ebfe915bc917237b8"]
                        midd15 = (Nmid)
                        kr16.findAndAddContactsByMid(midd15)
                        kr16.inviteIntoGroup(op.param1,[midd15])
                        kr15.acceptGroupInvitation(op.param1)
                    except:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        Nmid=["u4a0be979fc73e88ebfe915bc917237b8"]
                        midd15 = (Nmid)
                        random.choice(KAC).findAndAddContactsByMid(midd15)
                        random.choice(KAC).inviteIntoGroup(op.param1,[midd15])
                        kr15.acceptGroupInvitation(op.param1)           
                        
            if op.param3 in Bots:
                if op.param2 not in admin:
                    try:
                        kr18.kickoutFromGroup(op.param1,[op.param2])
                        Omid=["u4a0be979fc73e88ebfe915bc917237b8"]
                        midd16 = (Omid)
                        kr17.findAndAddContactsByMid(midd16)
                        kr17.inviteIntoGroup(op.param1,[midd16])
                        kr16.acceptGroupInvitation(op.param1)
                    except:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        Omid=["u4a0be979fc73e88ebfe915bc917237b8"]
                        midd16 = (Omid)
                        random.choice(KAC).findAndAddContactsByMid(midd16)
                        random.choice(KAC).inviteIntoGroup(op.param1,[midd16])
                        kr16.acceptGroupInvitation(op.param1)                  
                        
            if op.param3 in Bots:
                if op.param2 not in admin:
                    try:
                        kr19.kickoutFromGroup(op.param1,[op.param2])
                        Pmid=["u4a0be979fc73e88ebfe915bc917237b8"]
                        midd17 = (Pmid)
                        kr18.findAndAddContactsByMid(midd17)
                        kr18.inviteIntoGroup(op.param1,[midd17])
                        kr17.acceptGroupInvitation(op.param1)
                    except:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        Pmid=["u4a0be979fc73e88ebfe915bc917237b8"]
                        midd17 = (Pmid)
                        random.choice(KAC).findAndAddContactsByMid(midd17)
                        random.choice(KAC).inviteIntoGroup(op.param1,[midd17])
                        kr17.acceptGroupInvitation(op.param1)        
                        
            if op.param3 in Bots:
                if op.param2 not in admin:
                    try:
                        kr20.kickoutFromGroup(op.param1,[op.param2])
                        Qmid=["u4a0be979fc73e88ebfe915bc917237b8"]
                        midd18 = (Qmid)
                        kr19.findAndAddContactsByMid(midd18)
                        kr19.inviteIntoGroup(op.param1,[midd18])
                        kr18.acceptGroupInvitation(op.param1)
                    except:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        Qmid=["u4a0be979fc73e88ebfe915bc917237b8"]
                        midd18 = (Qmid)
                        random.choice(KAC).findAndAddContactsByMid(midd18)
                        random.choice(KAC).inviteIntoGroup(op.param1,[midd18])
                        kr18.acceptGroupInvitation(op.param1)            
                        
            if op.param3 in Bots:
                if op.param2 not in admin:
                    try:
                        kr21.kickoutFromGroup(op.param1,[op.param2])
                        Rmid=["u4a0be979fc73e88ebfe915bc917237b8"]
                        midd19 = (Rmid)
                        kr20.findAndAddContactsByMid(midd19)
                        kr20.inviteIntoGroup(op.param1,[midd19])
                        kr19.acceptGroupInvitation(op.param1)
                    except:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        Rmid=["u4a0be979fc73e88ebfe915bc917237b8"]
                        midd19 = (Rmid)
                        random.choice(KAC).findAndAddContactsByMid(midd19)
                        random.choice(KAC).inviteIntoGroup(op.param1,[midd19])
                        kr19.acceptGroupInvitation(op.param1)            
                        
            if op.param3 in Bots:
                if op.param2 not in admin:
                    try:
                        kr22.kickoutFromGroup(op.param1,[op.param2])
                        Smid=["u4a0be979fc73e88ebfe915bc917237b8"]
                        midd20 = (Smid)
                        kr21.findAndAddContactsByMid(midd20)
                        kr21.inviteIntoGroup(op.param1,[midd20])
                        kr20.acceptGroupInvitation(op.param1)
                    except:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        Smid=["u4a0be979fc73e88ebfe915bc917237b8"]
                        midd20 = (Smid)
                        random.choice(KAC).findAndAddContactsByMid(midd20)
                        random.choice(KAC).inviteIntoGroup(op.param1,[midd20])
                        kr20.acceptGroupInvitation(op.param1)            
                                     
            if op.param3 in Bots:
                if op.param2 not in admin:
                    try:
                        kr23.kickoutFromGroup(op.param1,[op.param2])
                        Tmid=["u4a0be979fc73e88ebfe915bc917237b8"]
                        midd21 = (Tmid)
                        kr22.findAndAddContactsByMid(midd21)
                        kr22.inviteIntoGroup(op.param1,[midd21])
                        kr21.acceptGroupInvitation(op.param1)
                    except:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        Tmid=["u4a0be979fc73e88ebfe915bc917237b8"]
                        midd21 = (Tmid)
                        random.choice(KAC).findAndAddContactsByMid(midd21)
                        random.choice(KAC).inviteIntoGroup(op.param1,[midd21])
                        kr21.acceptGroupInvitation(op.param1)         
                        
            if op.param3 in Bots:
                if op.param2 not in admin:
                    try:
                        kr24.kickoutFromGroup(op.param1,[op.param2])
                        Umid=["u4a0be979fc73e88ebfe915bc917237b8"]
                        midd22 = (Umid)
                        kr23.findAndAddContactsByMid(midd22)
                        kr23.inviteIntoGroup(op.param1,[midd22])
                        kr22.acceptGroupInvitation(op.param1)
                    except:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        Umid=["u4a0be979fc73e88ebfe915bc917237b8"]
                        midd22 = (Umid)
                        random.choice(KAC).findAndAddContactsByMid(midd22)
                        random.choice(KAC).inviteIntoGroup(op.param1,[midd22])
                        kr22.acceptGroupInvitation(op.param1)                 
                        
            if op.param3 in Bots:
                if op.param2 not in admin:
                    try:
                        kr25.kickoutFromGroup(op.param1,[op.param2])
                        Vmid=["u4a0be979fc73e88ebfe915bc917237b8"]
                        midd23 = (Vmid)
                        kr24.findAndAddContactsByMid(midd23)
                        kr24.inviteIntoGroup(op.param1,[midd23])
                        kr23.acceptGroupInvitation(op.param1)
                    except:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        Vmid=["u4a0be979fc73e88ebfe915bc917237b8"]
                        midd23 = (Vmid)
                        random.choice(KAC).findAndAddContactsByMid(midd23)
                        random.choice(KAC).inviteIntoGroup(op.param1,[midd23])
                        kr23.acceptGroupInvitation(op.param1)     
                        
            if op.param3 in Bots:
                if op.param2 not in admin:
                    try:
                        kr1.kickoutFromGroup(op.param1,[op.param2])
                        Wmid=["u4a0be979fc73e88ebfe915bc917237b8"]
                        midd24 = (Wmid)
                        kr25.findAndAddContactsByMid(midd24)
                        kr25.inviteIntoGroup(op.param1,[midd24])
                        kr24.acceptGroupInvitation(op.param1)
                    except:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        Wmid=["u4a0be979fc73e88ebfe915bc917237b8"]
                        midd24 = (Wmid)
                        random.choice(KAC).findAndAddContactsByMid(midd24)
                        random.choice(KAC).inviteIntoGroup(op.param1,[midd24])
                        kr24.acceptGroupInvitation(op.param1)                      
                        
            if op.param3 in Bots:
                if op.param2 not in admin:
                    try:
                        kr2.kickoutFromGroup(op.param1,[op.param2])
                        Xmid=["u4a0be979fc73e88ebfe915bc917237b8"]
                        midd25 = (Xmid)
                        kr1.findAndAddContactsByMid(midd25)
                        kr1.inviteIntoGroup(op.param1,[midd25])
                        kr25.acceptGroupInvitation(op.param1)
                    except:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        Xmid=["u4a0be979fc73e88ebfe915bc917237b8"]
                        midd25 = (Xmid)
                        random.choice(KAC).findAndAddContactsByMid(midd25)
                        random.choice(KAC).inviteIntoGroup(op.param1,[midd25])
                        kr25.acceptGroupInvitation(op.param1)                        
#==========================[Kris]===========================
        if op.type == 19:
            if mid1 in op.param3:
                wait["blacklist"][op.param2] = True
#==========================[Kris]===========================
        if op.type == 22:
            if wait['leaveRoom'] == True:
                kr1.leaveRoom(op.param1)
                kr2.leaveRoom(op.param1)
                kr3.leaveRoom(op.param1)
                kr4.leaveRoom(op.param1)
                kr5.leaveRoom(op.param1)
                kr6.leaveRoom(op.param1)
                kr7.leaveRoom(op.param1)
                kr8.leaveRoom(op.param1)
                kr9.leaveRoom(op.param1)
                kr10.leaveRoom(op.param1)
                kr11.leaveRoom(op.param1)
                kr12.leaveRoom(op.param1)
                kr13.leaveRoom(op.param1)
                kr14.leaveRoom(op.param1)
                kr15.leaveRoom(op.param1)
                kr16.leaveRoom(op.param1)
                kr17.leaveRoom(op.param1)
                kr18.leaveRoom(op.param1)
                kr19.leaveRoom(op.param1)
                kr20.leaveRoom(op.param1)
                kr21.leaveRoom(op.param1)
                kr22.leaveRoom(op.param1)
                kr23.leaveRoom(op.param1)
                kr24.leaveRoom(op.param1)
                kr25.leaveRoom(op.param1)
#==========================[Kris]===========================
        if op.type == 24:
            if wait['leaveRoom'] == True:
                kr1.leaveRoom(op.param1)
                kr2.leaveRoom(op.param1)
                kr3.leaveRoom(op.param1)
                kr4.leaveRoom(op.param1)
                kr5.leaveRoom(op.param1)
                kr6.leaveRoom(op.param1)
                kr7.leaveRoom(op.param1)
                kr8.leaveRoom(op.param1)
                kr9.leaveRoom(op.param1)
                kr10.leaveRoom(op.param1)
                kr11.leaveRoom(op.param1)
                kr12.leaveRoom(op.param1)
                kr13.leaveRoom(op.param1)
                kr14.leaveRoom(op.param1)
                kr15.leaveRoom(op.param1)
                kr16.leaveRoom(op.param1)
                kr17.leaveRoom(op.param1)
                kr18.leaveRoom(op.param1)
                kr19.leaveRoom(op.param1)
                kr20.leaveRoom(op.param1)
                kr21.leaveRoom(op.param1)
                kr22.leaveRoom(op.param1)
                kr23.leaveRoom(op.param1)
                kr24.leaveRoom(op.param1)
                kr25.leaveRoom(op.param1) 
#==========================[Kris]===========================
        if op.type == 26:
            msg = op.message

            if msg.toType == 1:
                if wait['leaveRoom'] == True:
                    kr1.leaveRoom(msg.to)
                    kr2.leaveRoom(msg.to)
                    kr3.leaveRoom(msg.to)
                    kr4.leaveRoom(msg.to)
                    kr5.leaveRoom(msg.to)
                    kr6.leaveRoom(msg.to)
                    kr7.leaveRoom(msg.to)
                    kr8.leaveRoom(msg.to)
                    kr9.leaveRoom(msg.to)
                    kr10.leaveRoom(msg.to)
                    kr11.leaveRoom(msg.to)
                    kr12.leaveRoom(msg.to)
                    kr13.leaveRoom(msg.to)
                    kr14.leaveRoom(msg.to)
                    kr15.leaveRoom(msg.to)
                    kr16.leaveRoom(msg.to)
                    kr17.leaveRoom(msg.to)
                    kr18.leaveRoom(msg.to)
                    kr19.leaveRoom(msg.to)
                    kr20.leaveRoom(msg.to)
                    kr21.leaveRoom(msg.to)
                    kr22.leaveRoom(msg.to)
                    kr23.leaveRoom(msg.to)
                    kr24.leaveRoom(msg.to)
                    kr25.leaveRoom(msg.to)
#==========================[Kris]===========================
            if msg.contentType == 16:
                url = msg.contentMetadata["postEndUrl"]
                kr1.like(url[25:58], url[66:], likeType=1001)
#==========================[Kris]===========================
        if op.type == 26:
            msg = op.message
            if msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
                    text = msg.text
                    if text is not None:
                        kr1.sendText(msg.to,text)
#==========================[Kris]===========================
        if op.type == 26:
            msg = op.message
            if msg.to in settings["simiSimi"]:
                if settings["simiSimi"][msg.to] == True:
                    if msg.text is not None:
                        text = msg.text
                        r = requests.get("http://api.ntcorp.us/chatbot/v1/?text=" + text.replace(" ","+") + "&key=beta1.nt")
                        data = r.text
                        data = json.loads(data)
                        if data["status"] == 200:
                            if data['result']['result'] == 100:
                                kr1.sendText(msg.to, "[From Simi]\n" + data['result']['response'].encode('utf-8'))
#==========================[Kris]===========================
#            if "MENTION" in msg.contentMetadata.keys() != None:
#                if wait['detectMention'] == True:
#                    contact = kr1.getContact(msg.from_)
#                    cName = contact.displayName
#                    balas = [cName + "Kangenkah sampai ngetag mulu?",cName + " nah mending pc aja klo penting..!", "kenapa, ", cName + " kangen ya?","kangen bilang, gak usah ngetag mulu, " + cName, "sekali lagi ngetag, bayar ya..!!! " + cName, "Tuh kan" + cName + "ngetag lagi, mojok aja yux...!!!"]
#                    ret_ = "[Auto Respon] " + random.choice(balas)
#                    name = re.findall(r'@(\w+)', msg.text)
#                    mention = ast.literal_eval(msg.contentMetadata["MENTION"])
#                    mentionees = mention['MENTIONEES']
#                    for mention in mentionees:
#                        if mention['M'] in Bots:
#                            kr1.sendText(msg.to,ret_)
#                            msg.contentType = 7
#                            msg.text = None
#                            msg.contentMetadata = {
#                                                        "STKID": "11866873",
#                                                        "STKPKGID": "1293049",
#                                                        "STKVER": "1" }
#                            kr1.sendMessage(msg)
#                            break            
#==========================[Kris]===========================
#            if "MENTION" in msg.contentMetadata.keys() != None:
#                 if wait['potoMention'] == True:
#                     contact = kr1.getContact(msg.from_)
#                     cName = contact.pictureStatus
#                     balas = ["http://dl.profile.line-cdn.net/" + cName]
#                     ret_ = random.choice(balas)
#                     mention = ast.literal_eval(msg.contentMetadata["MENTION"])
#                     mentionees = mention["MENTIONEES"]
#                     for mention in mentionees:
#                           if mention["M"] in Bots:
#                                  kr1.sendImageWithURL(msg.to,ret_)
#                                  break  
#==========================[Kris]===========================
            if "MENTION" in msg.contentMetadata.keys() != None:
                 if wait['kickMention'] == True:
                     contact = kr1.getContact(msg.from_)
                     cName = contact.displayName
                     balas = [cName + "Kangenkah sampai ngetag mulu?",cName + " nah mending pc aja klo penting..!", "kenapa, ", cName + " kangen ya?","kangen bilang, gak usah ngetag mulu, " + cName, "sekali lagi ngetag, bayar ya..!!! " + cName, "Tuh kan" + cName + "ngetag lagi, mojok aja yux...!!!"]
                     ret_ = "[Auto Respon] " + random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  kr1.sendText(msg.to,ret_)
                                  kr1.kickoutFromGroup(msg.to,[msg.from_])
                                  kr1.inviteIntoGroup(msg.to, admin)
                                  break
#==========================[Kris]===========================
            if msg.contentType == 13:
                if wait['invite'] == True:
                     _name = msg.contentMetadata["displayName"]
                     invite = msg.contentMetadata["mid"]
                     groups = kr1.getGroup(msg.to)
                     pending = groups.invitee
                     targets = []
                     for s in groups.members:
                         if _name in s.displayName:
                             kr1.sendText(msg.to, _name + " Berada DiGrup Ini")
                         else:
                             targets.append(invite)
                     if targets == []:
                         pass
                     else:
                         for target in targets:
                             try:
                                 kr1.findAndAddContactsByMid(target)
                                 kr1.inviteIntoGroup(msg.to,[target])
                                 kr1.sendText(msg.to,"Invite " + _name)
                                 wait['invite'] = False
                                 break                              
                             except:             
                                      kr1.sendText(msg.to,"Error")
                                      wait['invite'] = False
                                      break
            if msg.contentType == 13:
                if wait['invite2'] == True:
                     _name = msg.contentMetadata["displayName"]
                     invite = msg.contentMetadata["mid"]
                     groups = random.choice(KAC).getGroup(msg.to)
                     pending = groups.invitee
                     targets = []
                     for s in groups.members:
                         if _name in s.displayName:
                             random.choice(KAC).sendText(msg.to, _name + " Berada DiGrup Ini")
                         else:
                             targets.append(invite)
                     if targets == []:
                         pass
                     else:
                         for target in targets:
                             try:
                                 random.choice(KAC).findAndAddContactsByMid(target)
                                 random.choice(KAC).inviteIntoGroup(msg.to,[target])
                                 random.choice(KAC).sendText(msg.to,"Invite2 " + _name)
                                 wait['invite2'] = False
                                 break                              
                             except:             
                                      random.choice(KAC).sendText(msg.to,"Error")
                                      wait['invite2'] = False
                                      break
#==========================[Kris]===========================
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
                if wait["winvite"] == True:
                    if msg.from_ in admin or owner:
                        _name = msg.contentMetadata["displayName"]
                        invite = msg.contentMetadata["mid"]
                        groups = kr1.getGroup(msg.to)
                        pending = groups.invitee
                        targets = []
                        for s in groups.members:
                            if _name in s.displayName:
                                kr1.sendText(msg.to,"-> " + _name + " ada di room ini")
                                break
                            elif invite in wait["blacklist"]:
                                kr1.sendText(msg.to,"Maaf, " + _name + " kena Blacklist")
                                kr1.sendText(msg.to,"hubungi owner kami ya !, \n➡Unban: " + invite)
                                break
                            else:
                                targets.append(invite)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    kr1.findAndAddContactsByMid(target)
                                    kr1.inviteIntoGroup(msg.to,[target])
                                    kr1.sendText(msg.to,"Selesai di Invite : \n➡" + _name)
                                    wait["winvite"] = False
                                    break
                                except:
                                    try:
                                        kr1.findAndAddContactsByMid(invite)
                                        kr1.inviteIntoGroup(op.param1,[invite])
                                        wait["winvite"] = False
                                    except:
                                        kr1.sendText(msg.to,"Negative, Error detected")
                                        wait["winvite"] = False
                                        break
#==========================[Kris]===========================
                    if msg.from_ in admin or owner:
                        _name = msg.contentMetadata["displayName"]
                        invite = msg.contentMetadata["mid"]
                        groups = kr2.getGroup(msg.to)
                        pending = groups.invitee
                        targets = []
                        for s in groups.members:
                            if _name in s.displayName:
                                kr2.sendText(msg.to,"-> " + _name + " ada di room ini")
                                break
                            elif invite in wait["blacklist"]:
                                kr2.sendText(msg.to,"Maaf, " + _name + " kena Blacklist")
                                kr2.sendText(msg.to,"hubungi owner kami ya !, \n➡Unban: " + invite)
                                break
                            else:
                                targets.append(invite)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    kr2.findAndAddContactsByMid(target)
                                    kr2.inviteIntoGroup(msg.to,[target])
                                    kr2.sendText(msg.to,"Selesai di Invite : \n➡" + _name)
                                    wait["winvite"] = False
                                    break
                                except:
                                    try:
                                        kr2.findAndAddContactsByMid(invite)
                                        kr2.inviteIntoGroup(op.param1,[invite])
                                        wait["winvite"] = False
                                    except:
                                        kr2.sendText(msg.to,"Negative, Error detected")
                                        wait["winvite"] = False
                                        break
#==========================[Kris]===========================
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
#==========================[Kris]===========================
                if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        kr1.sendText(msg.to,"In Blacklist")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        kr1.sendText(msg.to,"Nothing")
#==========================[Kris]===========================
                elif wait["dblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        kr1.sendText(msg.to,"Done")
                        wait["dblack"] = False
                    else:
                        wait["dblack"] = False
                        kr1.sendText(msg.to,"Not in Blacklist")
#==========================[Kris]===========================
                elif wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        kr1.sendText(msg.to,"In Blacklist")
                        wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        kr1.sendText(msg.to,"Done")
#==========================[Kris]===========================
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        kr1.sendText(msg.to,"Done")
                        wait["dblacklist"] = False
                    else:
                        wait["dblacklist"] = False
                        kr1.sendText(msg.to,"Done")
#==========================[Kris]===========================
                elif wait['contact'] == True:
                    msg.contentType = 0
                    kr1.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = kr1.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = kr1.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        kr1.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = kr1.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = kr1.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        kr1.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
#==========================[Kris]===========================
            elif msg.contentType == 16:
                if wait['timeline'] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "menempatkan URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = msg.contentMetadata["postEndUrl"]
                    kr1.sendText(msg.to,msg.text)
#==========================[Kris]===========================
            elif msg.text is None:
                return
#==========================[Kris]===========================
            elif msg.text.lower() == 'help':
                if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        kr1.sendText(msg.to,helpmsg)
                    else:
                        kr1.sendText(msg.to,helpmsg)
#==========================[Kris]===========================
            elif msg.text.lower() == 'keybot':
                if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        kr1.sendText(msg.to,keymsg)
                    else:
                        kr1.sendText(msg.to,keymsg)
#==========================[Kris]===========================
            elif msg.text.lower() == 'keypro':
                if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        kr1.sendText(msg.to,helppro)
                    else:
                        kr1.sendText(msg.to,helppro)
#==========================[Kris]===========================
            elif msg.text.lower() == 'keyself':
                if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        kr1.sendText(msg.to,helpself)
                    else:
                        kr1.sendText(msg.to,helpself)
#==========================[Kris]===========================
            elif msg.text.lower() == 'keygrup':
                if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        kr1.sendText(msg.to,helpgrup)
                    else:
                        kr1.sendText(msg.to,helpgrup)
#==========================[Kris]===========================
            elif msg.text.lower() == 'keyset':
                if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        kr1.sendText(msg.to,helpset)
                    else:
                        kr1.sendText(msg.to,helpset)
#==========================[Kris]===========================
#            elif msg.text.lower() == 'keytran':
#                if msg.from_ in admin:
#                    if wait["lang"] == "JP":
#                        kr1.sendText(msg.to,helptranslate)
#                    else:
#                        kr1.sendText(msg.to,helptranslate)
#==========================[Kris]===========================
            elif msg.text.lower() == 'keyrhs':
                if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        kr1.sendText(msg.to,helprhs)
                    else:
                        kr1.sendText(msg.to,helprhs)
#==========================[Kris]===========================
            elif msg.text in ["Sp","Speed","speed"]:
                if msg.from_ in admin:
                    start = time.time()
                    kr1.sendText(msg.to, "❂➣Proses.....")
                    elapsed_time = time.time() - start
                    kr1.sendText(msg.to, "%sseconds" % (elapsed_time))
#==========================[Kris]===========================
            elif msg.text.lower() == '#crash':
                if msg.from_ in admin:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u1f41296217e740650e0448b96851a3e2',"}
                    kr1.sendMessage(msg)
                    kr2.sendMessage(msg)
                    kr3.sendMessage(msg)
                    kr4.sendMessage(msg)
#==========================[Kris]===========================
            elif msg.text.lower() == 'me':
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}
                kr1.sendMessage(msg)
#==========================[Kris]===========================
            elif msg.text.lower() == 'bot':
                if msg.from_ in admin:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': mid1}
                    kr1.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': Amid}
                    kr2.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': Bmid}
                    kr3.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': Cmid}
                    kr4.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': Dmid}
                    kr5.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': Emid}
                    kr6.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': Fmid}
                    kr7.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': Gmid}
                    kr8.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': Hmid}
                    kr9.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': Imid}
                    kr10.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': Jmid}
                    kr11.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': Kmid}
                    kr12.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': Lmid}
                    kr13.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': Mmid}
                    kr14.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': Nmid}
                    kr15.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': Omid}
                    kr16.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': Pmid}
                    kr17.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': Qmid}
                    kr18.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': Rmid}
                    kr19.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': Smid}
                    kr20.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': Tid1}
                    kr21.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': Umid}
                    kr22.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': Vmid}
                    kr23.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': Wmid}
                    kr24.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': Xmid}
                    kr25.sendMessage(msg)
                    random.choice(KAC).sendImageWithURL(msg.to, url123)
                    random.choice(KAC).sendText(msg.to,"↥↥↥↥↥↪ Owner Bots ↩↥↥↥↥↥")
#==========================[Kris]===========================
            elif msg.text.lower() == 'mode on':
                if msg.from_ in admin:
                    if wait["protect"] == True:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Protecion Already On")
                        else:
                            kr1.sendText(msg.to,"Protecion Already On")
                    else:
                        wait["protect"] = True
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Protecion Already On")
                        else:
                            kr1.sendText(msg.to,"Protecion Already On")
                    if wait["linkprotect"] == True:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Protection Qr already On")
                        else:
                            kr1.sendText(msg.to,"Protection Qr already On")
                    else:
                        wait["linkprotect"] = True
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Protection Qr already On")
                        else:
                            kr1.sendText(msg.to,"Protection Qr already On")
                    if wait["inviteprotect"] == True:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Protection Invite already On")
                        else:
                            kr1.sendText(msg.to,"Protection Invite already On")
                    else:
                        wait["inviteprotect"] = True
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"ρяσтє¢тισи ιиνιтє ѕєт тσ σи")
                        else:
                            kr1.sendText(msg.to,"ρяσтє¢тισи ιиνιтє αℓяєα∂у σи")
                    if wait["cancelprotect"] == True:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"¢αи¢єℓ ρяσтє¢тισи ѕєт тσ σи")
                        else:
                            kr1.sendText(msg.to,"¢αи¢єℓ ρяσтє¢тισи αℓяєα∂у σи")
                    else:
                        wait["cancelprotect"] = True
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"¢αи¢єℓ ρяσтє¢тισи ѕєт тσ σи")
                        else:
                            kr1.sendText(msg.to,"¢αи¢єℓ ρяσтє¢тισи αℓяєα∂у σи")
                    if wait["QrProtect"] == True:#<==========
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Protect QR On")
                        else:
                            kr1.sendText(msg.to,"done")
                    else:
                        wait["QrProtect"] = True
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Protect QR On")
                        else:
                            kr1.sendText(msg.to,"done")
                    if wait["MProtection"] == True:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Member Protection On")
                        else:
                            kr1.sendText(msg.to,"done")
                    else:
                        wait["MProtection"] = True
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Member Protection On")
                        else:
                            kr1.sendText(msg.to,"done")
                    if msg.to in wait['pname']:
                        kr1.sendText(msg.to,"TURN ON")
                    else:
                        kr1.sendText(msg.to,"ALREADY ON")
                        wait['pname'][msg.to] = True
                        wait['pro_name'][msg.to] = kr1.getGroup(msg.to).name
                    if wait["Protectcancel"] == True:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"proтecт cancel on")
                    else:
                        wait["Protectcancel"] = True
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"already on")
                    if wait["autoKick"] == True:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Kick on")
                    else:
                        wait["autoKick"] = True
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"already on")
                    if wait["Protectguest"] == True:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Guest Stranger On")
                        else:
                            kr1.sendText(msg.to,"done")
                    else:
                        wait["Protectguest"] = True
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Guest Stranger On")
                        else:
                            kr1.sendText(msg.to,"done")
                    if wait["Protectgr"] == True:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Protect Link On")
                        else:
                            kr1.sendText(msg.to,"done")
                    else:
                        wait["Protectgr"] = True
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Protect Link On")
                        else:
                            kr1.sendText(msg.to,"done")
#==========================[Kris]===========================
            elif msg.text.lower() == 'mode off':
                if msg.from_ in admin:
                    if wait["protect"] == False:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Protection already Off")
                        else:
                            kr1.sendText(msg.to,"Protection already Off")
                    else:
                        wait["protect"] = False
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"ρяσтє¢тισи ѕєт тσ σff")
                        else:
                            kr1.sendText(msg.to,"ρяσтє¢тισи αℓяєα∂у σff")
                    if wait["linkprotect"] == False:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Protection Qr already off")
                        else:
                            kr1.sendText(msg.to,"Protection Qr already off")
                    else:
                        wait["linkprotect"] = False
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Protection Qr already Off")
                        else:
                            kr1.sendText(msg.to,"Protection Qr already Off")
                    if wait["inviteprotect"] == False:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Protection Invite already Off")
                        else:
                            kr1.sendText(msg.to,"Protection Invite already Off")
                    else:
                        wait["inviteprotect"] = False
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Protection Invite already Off")
                        else:
                            kr1.sendText(msg.to,"Protection Invite already Off")
                    if wait["cancelprotect"] == False:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Protection Cancel already Off")
                        else:
                            kr1.sendText(msg.to,"Protection Cancel already Off")
                    else:
                        wait["cancelprotect"] = False
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Protection Cancel already Off")
                        else:
                            kr1.sendText(msg.to,"Protection Cancel already Off")
                    if wait["QrProtect"] == False:#<===
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Protect QR Off")
                        else:
                            kr1.sendText(msg.to,"done")
                    else:
                        wait["QrProtect"] = False
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Protect QR Off")
                        else:
                            kr1.sendText(msg.to,"done")
                    if wait["MProtection"] == False:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Member Protection Off")
                        else:
                            kr1.sendText(msg.to,"done")
                    else:
                        wait["MProtection"] = False
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Member Protection Off")
                        else:
                            kr1.sendText(msg.to,"done")
                    if msg.to in wait['pname']:
                        kr1.sendText(msg.to,"TURN OFF")
                        del wait['pname'][msg.to]
                    else:
                        kr1.sendText(msg.to,"ALREADY OFF")
                    if wait["Protectcancel"] == False:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"proтecт cancel oғғ")
                    else:
                        wait["Protectcancel"] = False
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Protect already oғғ")
                    if wait["autoKick"] == False:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Kick oғғ")
                    else:
                        wait["autoKick"] = False
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Kick already oғғ")
                    if wait["Protectguest"] == False:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Guest Stranger Off")
                        else:
                            kr1.sendText(msg.to,"done")
                    else:
                        wait["Protectguest"] = False
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Guest Stranger Off")
                        else:
                            kr1.sendText(msg.to,"done")
                    if wait["Protectgr"] == False:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Protect Link Off")
                        else:
                            kr1.sendText(msg.to,"done")
                    else:
                        wait["Protectgr"] = False
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Protect Link Off")
                        else:
                            kr1.sendText(msg.to,"done")
#==========================[Kris]===========================
            elif msg.text.lower() == 'contact on':
                if msg.from_ in admin:
                    if wait['contact'] == True:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"ɕσηϯαɕϯ ςεϯ ϯσ ση")
                        else:
                            kr1.sendText(msg.to,"ɕσηϯαɕϯ ςεϯ ϯσ ση")
                    else:
                        wait['contact'] = True
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"ɕσηϯαɕϯ ςεϯ ϯσ ση")
                        else:
                            kr1.sendText(msg.to,"ɕσηϯαɕϯ ςεϯ ϯσ ση")
            elif msg.text.lower() == 'contact off':
                if msg.from_ in admin:
                    if wait['contact'] == False:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"ɕσηϯαɕϯ ςεϯ ϯσ σƒƒ")
                        else:
                            kr1.sendText(msg.to,"ɕσηϯαɕϯ αʆɾεαδψ σƒƒ")
                    else:
                        wait['contact'] = False
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"ɕσηϯαɕϯ ςεϯ ϯσ σƒƒ")
                        else:
                            kr1.sendText(msg.to,"ɕσηϯαɕϯ αʆɾεαδψ σƒƒ")
#==========================[Kris]===========================
            elif msg.text.lower() == 'protect on':
                if msg.from_ in admin:
                    if wait["protect"] == True:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Protecion Already On")
                        else:
                            kr1.sendText(msg.to,"Protecion Already On")
                    else:
                        wait["protect"] = True
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Protecion Already On")
                        else:
                            kr1.sendText(msg.to,"Protecion Already On")
#==========================[Kris]===========================
            elif msg.text.lower() == 'qr on':
                if msg.from_ in admin:
                    if wait["linkprotect"] == True:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Protection Qr already On")
                        else:
                            kr1.sendText(msg.to,"Protection Qr already On")
                    else:
                        wait["linkprotect"] = True
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Protection Qr already On")
                        else:
                            kr1.sendText(msg.to,"Protection Qr already On")
#==========================[Kris]===========================
            elif msg.text.lower() == 'invite on':
                if msg.from_ in admin:
                    if wait["inviteprotect"] == True:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Protection Invite already On")
                        else:
                            kr1.sendText(msg.to,"Protection Invite already On")
                    else:
                        wait["inviteprotect"] = True
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"ρяσтє¢тισи ιиνιтє ѕєт тσ σи")
                        else:
                            kr1.sendText(msg.to,"ρяσтє¢тισи ιиνιтє αℓяєα∂у σи")
#==========================[Kris]===========================
            elif msg.text.lower() == 'cancel on':
                if msg.from_ in admin:
                    if wait["cancelprotect"] == True:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"¢αи¢єℓ ρяσтє¢тισи ѕєт тσ σи")
                        else:
                            kr1.sendText(msg.to,"¢αи¢єℓ ρяσтє¢тισи αℓяєα∂у σи")
                    else:
                        wait["cancelprotect"] = True
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"¢αи¢єℓ ρяσтє¢тισи ѕєт тσ σи")
                        else:
                            kr1.sendText(msg.to,"¢αи¢єℓ ρяσтє¢тισи αℓяєα∂у σи")
#==========================[Kris]===========================
            elif msg.text.lower() == 'autojoin on':
                if msg.from_ in admin:
                    if wait['autoJoin'] == True:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"αυтσʝσιи ѕєт тσ σи")
                        else:
                            kr1.sendText(msg.to,"αυтσʝσιи αℓяєα∂у σи")
                    else:
                        wait['autoJoin'] = True
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"αυтσʝσιи ѕєт тσ σи")
                        else:
                            kr1.sendText(msg.to,"αυтσʝσιи αℓяєα∂у σи")
#==========================[Kris]===========================
            elif msg.text.lower() == 'autojoin off':
                if msg.from_ in admin:
                    if wait['autoJoin'] == False:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"αυтσʝσιи ѕєт тσ σff")
                        else:
                            kr1.sendText(msg.to,"αυтσʝσιи αℓяєα∂у σff")
                    else:
                        wait['autoJoin'] = False
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"αυтσʝσιи ѕєт тσ σff")
                        else:
                            kr1.sendText(msg.to,"αυтσʝσιи αℓяєα∂у σff")
#==========================[Kris]===========================
            elif msg.text.lower() == 'protect off':
                if msg.from_ in admin:
                    if wait["protect"] == False:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Protection already Off")
                        else:
                            kr1.sendText(msg.to,"Protection already Off")
                    else:
                        wait["protect"] = False
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"ρяσтє¢тισи ѕєт тσ σff")
                        else:
                            kr1.sendText(msg.to,"ρяσтє¢тισи αℓяєα∂у σff")
#==========================[Kris]===========================
            elif msg.text.lower() == 'qr off':
                if msg.from_ in admin:
                    if wait["linkprotect"] == False:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Protection Qr already off")
                        else:
                            kr1.sendText(msg.to,"Protection Qr already off")
                    else:
                        wait["linkprotect"] = False
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Protection Qr already Off")
                        else:
                            kr1.sendText(msg.to,"Protection Qr already Off")
#==========================[Kris]===========================
            elif msg.text.lower() == 'invit off':
                if msg.from_ in admin:
                    if wait["inviteprotect"] == False:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Protection Invite already Off")
                        else:
                            kr1.sendText(msg.to,"Protection Invite already Off")
                    else:
                        wait["inviteprotect"] = False
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Protection Invite already Off")
                        else:
                            kr1.sendText(msg.to,"Protection Invite already Off")
#==========================[Kris]===========================
            elif msg.text.lower() == 'cancel off':
                if msg.from_ in admin:
                    if wait["cancelprotect"] == False:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Protection Cancel already Off")
                        else:
                            kr1.sendText(msg.to,"Protection Cancel already Off")
                    else:
                        wait["cancelprotect"] = False
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Protection Cancel already Off")
                        else:
                            kr1.sendText(msg.to,"Protection Cancel already Off")
#==========================[Kris]===========================
            elif "Grup cancel:" in msg.text:
                if msg.from_ in admin:
                    try:
                        strnum = msg.text.replace("Grup cancel:","")
                        if strnum == "off":
                            wait['autoCancel']["on"] = False
                            if wait["lang"] == "JP":
                                kr1.sendText(msg.to,"Itu off undangan ditolak??\nSilakan kirim dengan menentukan jumlah orang ketika Anda menghidupkan")
                            else:
                                kr1.sendText(msg.to,"Off undangan ditolak??Sebutkan jumlah terbuka ketika Anda ingin mengirim")
                        else:
                            num =  int(strnum)
                            wait['autoCancel']["on"] = True
                            if wait["lang"] == "JP":
                                kr1.sendText(msg.to,strnum + "Kelompok berikut yang diundang akan ditolak secara otomatis")
                            else:
                                kr1.sendText(msg.to,strnum + "The team declined to create the following automatic invitation")
                    except:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Nilai tidak benar")
                        else:
                            kr1.sendText(msg.to,"Weird value")
#==========================[Kris]===========================
            elif msg.text.lower() == 'autoleave on':
                if msg.from_ in admin:
                    if wait['leaveRoom'] == True:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Auto Leave room set to on")
                        else:
                            kr1.sendText(msg.to,"Auto Leave room already on")
                    else:
                        wait['leaveRoom'] = True
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Auto Leave room set to on")
                        else:
                            kr1.sendText(msg.to,"Auto Leave room already on")
            elif msg.text.lower() == 'autoleave off':
                if msg.from_ in admin:
                    if wait['leaveRoom'] == False:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Auto Leave room set to off")
                        else:
                            kr1.sendText(msg.to,"Auto Leave room already off")
                    else:
                        wait['leaveRoom'] = False
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Auto Leave room set to off")
                        else:
                            kr1.sendText(msg.to,"Auto Leave room already off")

#==========================[Kris]===========================
            elif msg.text.lower() == 'Bot':
                random.choice(KAC).sendImageWithURL(msg.to, url123)
                random.choice(KAC).sendText(msg.to,"↥↥↥↥↥↪ Pembuat Bots ↩↥↥↥↥↥")
            elif msg.text.lower() == 'share off':
                if msg.from_ in admin:
                    if wait['timeline'] == False:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Share set to off")
                        else:
                            kr1.sendText(msg.to,"Share already off")
                    else:
                        wait['timeline'] = False
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Share set to off")
                        else:
                            kr1.sendText(msg.to,"Share already off")
#==========================[Kris]===========================
            elif msg.text.lower() == "status":
                if msg.from_ in admin:
                    md = """╔═════════════\n"""
                    if wait['contact'] == True: md+="╠❂➣Contact:on [✅]\n"
                    else: md+="╠❂➣Contact:off [❌]\n"
                    if wait['autoJoin'] == True: md+="╠❂➣Auto Join:on [✅]\n"
                    else: md +="╠❂➣Auto Join:off [❌]\n"
                    if wait['autoCancel']["on"] == True:md+="╠❂➣Auto cancel:" + str(wait['autoCancel']["members"]) + "[✅]\n"
                    else: md+= "╠❂➣Group cancel:off [❌]\n"
                    if wait['leaveRoom'] == True: md+="╠❂➣Auto leave:on [✅]\n"
                    else: md+="╠❂➣Auto leave:off [❌]\n"
                    if wait['timeline'] == True: md+="╠❂➣Share:on [✅]\n"
                    else:md+="╠❂➣Share:off [❌]\n"
                    if wait['autoAdd'] == True: md+="╠❂➣Auto add:on [✅]\n"
                    else:md+="╠❂➣Auto add:off [❌]\n"
                    if wait["protect"] == True: md+="╠❂➣Protect:on [✅]\n"
                    else:md+="╠❂➣Protect:off [❌]\n"
                    if wait["linkprotect"] == True: md+="╠❂➣Link Protect:on [✅]\n"
                    else:md+="╠❂➣Link Protect:off [❌]\n"
                    if wait["inviteprotect"] == True: md+="╠❂➣Invitation Protect:on [✅]\n"
                    else:md+="╠❂➣Invitation Protect:off [❌]\n"
                    if wait["cancelprotect"] == True: md+="╠❂➣Cancel Protect:on [✅]\n"
                    else:md+="╠❂➣Cancel Protect:off [❌]\n╚═════════════"
                    kr1.sendText(msg.to,md)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u31ef22df7f538df1d74dc7f756ef1a32"}
                    kr1.sendMessage(msg)
#==========================[Kris]===========================
            elif cms(msg.text,["creator","Creator"]):
                msg.contentType = 13
                msg.contentMetadata = {'mid': "u31ef22df7f538df1d74dc7f756ef1a32"}
                kr1.sendMessage(msg)
                kr1.sendText(msg.to,'❂➣ Creator yang manis kalem  􀜁􀄯􏿿')
#==========================[Kris]===========================
            elif msg.text.lower() == 'autoadd on':
                if msg.from_ in admin:
                    if wait['autoAdd'] == True:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Auto add set to on")
                        else:
                            kr1.sendText(msg.to,"Auto add already on")
                    else:
                        wait['autoAdd'] = True
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Auto add set to on")
                        else:
                            kr1.sendText(msg.to,"Auto add already on")
            elif msg.text.lower() == 'autoadd off':
                if msg.from_ in admin:
                    if wait['autoAdd'] == False:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Auto add set to off")
                        else:
                            kr1.sendText(msg.to,"Auto add already off")
                    else:
                        wait['autoAdd'] = False
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Auto add set to off")
                        else:
                            kr1.sendText(msg.to,"Auto add already off")
#==========================[Kris]===========================
            elif "Pesan set:" in msg.text:
                if msg.from_ in admin:
                    wait['message'] = msg.text.replace("Pesan set:","")
                    kr1.sendText(msg.to,"We changed the message")
#==========================[Kris]===========================
            elif msg.text.lower() == 'pesan cek':
                if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        kr1.sendText(msg.to,"Pesan tambahan otomatis telah ditetapkan sebagai berikut \n\n" + wait['message'])
                    else:
                        kr1.sendText(msg.to,"Pesan tambahan otomatis telah ditetapkan sebagai berikut \n\n" + wait['message'])
#==========================[Kris]===========================
            elif "Coment Set:" in msg.text:
                if msg.from_ in admin:
                    c = msg.text.replace("Coment Set:","")
                    if c in [""," ","\n",None]:
                        kr1.sendText(msg.to,"Merupakan string yang tidak bisa diubah")
                    else:
                        wait["comment"] = c
                        kr1.sendText(msg.to,"Ini telah diubah\n\n" + c)
#==========================[Kris]===========================
            elif msg.text in ["Comment on"]:
                if msg.from_ in admin:
                    if wait["commentOn"] == True:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Aku berada di")
                        else:
                            kr1.sendText(msg.to,"To open")
                    else:
                        wait["commentOn"] = True
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Comment Actived")
                        else:
                            kr1.sendText(msg.to,"Comment Has Been Active")
            elif msg.text in ["Comment off"]:
                if msg.from_ in admin:
                    if wait["commentOn"] == False:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Hal ini sudah off")
                        else:
                            kr1.sendText(msg.to,"It is already turned off")
                    else:
                        wait["commentOn"] = False
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Off")
                        else:
                            kr1.sendText(msg.to,"To turn off")
#==========================[Kris]===========================
            elif msg.text in ["Com","Comment"]:
                if msg.from_ in admin:
                    kr1.sendText(msg.to,"Auto komentar saat ini telah ditetapkan sebagai berikut:??\n\n" + str(wait["comment"]))
            elif msg.text in ["Com Bl"]:
                if msg.from_ in admin:
                    wait["wblack"] = True
                    kr1.sendText(msg.to,"Please send contacts from the person you want to add to the blacklist")
            elif msg.text in ["Com hapus Bl"]:
                if msg.from_ in admin:
                    wait["dblack"] = True
                    kr1.sendText(msg.to,"Please send contacts from the person you want to add from the blacklist")
            elif msg.text in ["Com Bl cek"]:
                if msg.from_ in admin:
                    if wait["commentBlack"] == {}:
                        kr1.sendText(msg.to,"Nothing in the blacklist")
                    else:
                        kr1.sendText(msg.to,"The following is a blacklist")
                        mc = ""
                        for mi_d in wait["commentBlack"]:
                            mc += "ãƒ»" +kr1.getContact(mi_d).displayName + "\n"
                        kr1.sendText(msg.to,mc)

#==========================[Kris]===========================
            elif "Spamcontact @" in msg.text:
                if msg.from_ in owner:
                    _name = msg.text.replace("Spamcontact @","")
                    _nametarget = _name.rstrip(' ')
                    gs = kr1.getGroup(msg.to)
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(msg.to, "Selesai di Spam")
                            print " Spammed !"

#==========================[Kris]===========================
            elif msg.text in ["Invite"]:
                if msg.from_ in admin:
                    wait["invite"] = True
                    kr1.sendText(msg.to,"Kirim Contact")
#==========================[Kris]===========================
            elif msg.text in ["Jepit"]:
                if msg.from_ in admin:
                    wait["invite2"] = True
                    random.choice(KAC).sendText(msg.to,"Kirim Contact")
#==========================[Kris]===========================
            elif msg.text in ["Undang"]:
                if msg.from_ in admin:
                    wait["winvite"] = True
                    kr2.sendText(msg.to,"Kirim Contact")

#==========================[Kris]===========================
            elif msg.text in ["Tag2 on","tag2 on"]:
                if msg.from_ in admin:
                    wait['kickMention'] = True
                    kr1.sendText(msg.to,"Auto Kick tag ON")
#==========================[Kris]=========================== 
            elif msg.text in ["Tag2 off","tag2 off"]:
                if msg.from_ in admin:
                    wait['kickMention'] = False
                    kr1.sendText(msg.to,"Auto Kick tag OFF")
#==========================[Kris]===========================
            elif "Time" in msg.text:
                if msg.toType == 2:
                    kr1.sendText(msg.to,datetime.today().strftime('%H:%M:%S'))
#==========================[Kris]===========================
            elif ".bubar99" in msg.text:
                if msg.from_ in owner:
                    if msg.toType == 2:
                        if msg.toType == 2:
                            print "ok"
                            _name = msg.text.replace(".bubar99","")
                            gs = kr1.getGroup(msg.to)
                            gs = kr2.getGroup(msg.to)
                            gs = kr3.getGroup(msg.to)
                            gs = kr4.getGroup(msg.to)
                            gs = kr5.getGroup(msg.to)
                            gs = kr6.getGroup(msg.to)
                            gs = kr7.getGroup(msg.to)
                            gs = kr8.getGroup(msg.to)
                            gs = kr9.getGroup(msg.to)
                            gs = kr10.getGroup(msg.to)
                            gs = kr11.getGroup(msg.to)
                            gs = kr12.getGroup(msg.to)
                            gs = kr13.getGroup(msg.to)
                            gs = kr14.getGroup(msg.to)
                            gs = kr15.getGroup(msg.to)
                            gs = kr16.getGroup(msg.to)
                            gs = kr17.getGroup(msg.to)
                            gs = kr18.getGroup(msg.to)
                            gs = kr19.getGroup(msg.to)
                            gs = kr20.getGroup(msg.to)
                            gs = kr21.getGroup(msg.to)
                            gs = kr22.getGroup(msg.to)
                            gs = kr23.getGroup(msg.to)
                            gs = kr24.getGroup(msg.to)
                            kr1.sendText(msg.to,"Jangan panik, santai aja ya ô")
                            kr25.sendText(msg.to,"Group di bersihkan...!!")
                            targets = []
                            for g in gs.members:
                                if _name in g.displayName:
                                    targets.append(g.mid)
                            if targets == []:
                                kr1.sendText(msg.to,"Tidak di temukan")
                                kr2.sendText(msg.to,"Tidak di temukan")
                            else:
                                for target in targets:
                                    if target not in admin:
                                        try:
                                            klist=[kr1,kr2,kr3,kr4,kr5,kr6,kr7,kr8,kr9]
                                            kicker=random.choice(klist)
                                            kicker.kickoutFromGroup(msg.to,[target])
                                            print (msg.to,[g.mid])
                                        except:
                                            kr1.sendText(msg.to,"Group Bersih")
                                            kr2.sendText(msg.to,"Group Bersih")
#==========================[Kris]===========================
            elif msg.text in ["#bubar99"]:
                if msg.from_ in owner:
                    kr1.sendText(msg.to,"السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                    kr2.sendText(msg.to,"Assalamu'alaikum")
                    kr3.sendText(msg.to,"وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِوَبَرَكَاتُهُ")
                    kr4.sendText(msg.to,"Wa'alaikumsallam.Wr,Wb")
                    if msg.toType == 2:
                        print "ok"
                        _name = msg.text.replace("#bubar99","")
                        gs = kr1.getGroup(msg.to)
                        gs = kr2.getGroup(msg.to)
                        gs = kr3.getGroup(msg.to)
                        gs = kr4.getGroup(msg.to)
                        gs = kr5.getGroup(msg.to)
                        gs = kr6.getGroup(msg.to)
                        gs = kr7.getGroup(msg.to)
                        gs = kr8.getGroup(msg.to)
                        gs = kr9.getGroup(msg.to)
                        kr1.sendText(msg.to,"maaf kalo gak sopan")
                        kr2.sendText(msg.to,"Qo salamnya gak ada yang jawab ya..!!")
                        kr3.sendText(msg.to,"hehehhehe")
                        targets = []
                        for g in gs.members:
                            if _name in g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            kr1.sendText(msg.to,"Tidak di temukan")
                        else:
                            for target in targets:
                                if target not in admin:
                                    try:
                                        klist=[kr1,kr2,kr3,kr4,kr5,kr6,kr7,kr8,kr9]
                                        kicker=random.choice(klist)
                                        kicker.kickoutFromGroup(msg.to,[target])
                                        print (msg.to,[g.mid])
                                    except:
                                        kr1.sendText(msg.to,"السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                                        kr2.sendText(msg.to,"وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِوَبَرَكَاتُهُ")
                                        kr3.sendText(msg.to,"Nah salamnya jawab sendiri jadinya wkwkwk..!!")
#==========================[Kris]===========================
            elif ("#kick " in msg.text):
                if msg.from_ in admin:
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"] [0] ["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           kr1.kickoutFromGroup(msg.to,[target])
                       except:
                           kr1.sendText(msg.to,"Error")
#==========================[Kris]===========================
            elif ("#cium " in msg.text):
                if msg.from_ in admin:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"] [0] ["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        if target not in admin:
                            try:
                                kr1.kickoutFromGroup(msg.to,[target])
                                #kr1.inviteIntoGroup(msg.to,[admin])
                                kr1.cancelGroupInvitation(msg.to,[target])
                            except:
                                kr1.sendText(msg.to,"Error")

            elif "#kick: " in msg.text:
                if msg.from_ in admin:
                    midd = msg.text.replace("Kick: ","")
                    kr1.kickoutFromGroup(msg.to,[midd])
#==========================[Kris]===========================
            elif 'invite ' in msg.text.lower():
                if msg.from_ in admin:
                    key = msg.text[-33:]
                    kr1.findAndAddContactsByMid(key)
                    kr1.inviteIntoGroup(msg.to, [key])
                    contact = kr1.getContact(key)
#==========================[Kris]===========================
            elif msg.text.lower() == 'cancel':
                if msg.from_ in admin:
                    if msg.toType == 2:
                        group = kr1.getGroup(msg.to)
                        if group.invitee is not None:
                            gInviMids = [contact.mid for contact in group.invitee]
                            kr1.cancelGroupInvitation(msg.to, gInviMids)
                        else:
                            if wait["lang"] == "JP":
                                kr1.sendText(msg.to,"Tidak ada undangan")
                            else:
                                kr1.sendText(msg.to,"Invitan tidak ada")
                    else:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Tidak ada undangan")
                        else:
                            kr1.sendText(msg.to,"Invitan tidak ada")
#==========================[Kris]===========================
            elif msg.text.lower() == 'link on':
                if msg.from_ in admin:
                    if msg.toType == 2:
                        group = kr1.getGroup(msg.to)
                        group.preventJoinByTicket = False
                        kr1.updateGroup(group)
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"URL open")
                        else:
                            kr1.sendText(msg.to,"URL open")
                    else:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"It can not be used outside the group")
                        else:
                            kr1.sendText(msg.to,"Can not be used for groups other than")
#==========================[Kris]===========================
            elif msg.text.lower() == 'link off':
                if msg.from_ in admin:
                    if msg.toType == 2:
                        group = kr1.getGroup(msg.to)
                        group.preventJoinByTicket = True
                        kr1.updateGroup(group)
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"URL close")
                        else:
                            kr1.sendText(msg.to,"URL close")
                    else:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"It can not be used outside the group")
                        else:
                            kr1.sendText(msg.to,"Can not be used for groups other than")
#==========================[Kris]===========================
            elif msg.text in ["Url","Gurl"]:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        g = kr1.getGroup(msg.to)
                        if g.preventJoinByTicket == True:
                            g.preventJoinByTicket = False
                            kr1.updateGroup(g)
                        gurl = kr1.reissueGroupTicket(msg.to)
                        kr1.sendText(msg.to,"line://ti/g/" + gurl)
#==========================[Kris]===========================   
            elif "Gcreator" == msg.text:
                try:
                    group = kr1.getGroup(msg.to)
                    GS = group.creator.mid
                    M = Message()
                    M.to = msg.to
                    M.contentType = 13
                    M.contentMetadata = {'mid': GS}
                    kr1.sendMessage(M)
                except:
                    W = group.members[0].mid
                    M = Message()
                    M.to = msg.to
                    M.contentType = 13
                    M.contentMetadata = {'mid': W}
                    kr1.sendMessage(M)
                    kr1.sendText(msg.to,"Creator Grup")
#==========================[Kris]===========================
            elif msg.text.lower() == 'invite:gcreator':
                if msg.from_ in admin:
                    if msg.toType == 2:
                           ginfo = kr1.getGroup(msg.to)
                           try:
                               gcmid = ginfo.creator.mid
                           except:
                               gcmid = "Error"
                           if wait["lang"] == "JP":
                               kr1.inviteIntoGroup(msg.to,[gcmid])
                           else:
                               kr1.inviteIntoGroup(msg.to,[gcmid])
#==========================[Kris]===========================  
            elif ("Gname: " in msg.text):
                if msg.from_ in admin:
                    if msg.toType == 2:
                        X = kr1.getGroup(msg.to)
                        X.name = msg.text.replace("Gname: ","")
                        kr1.updateGroup(X)
#==========================[Kris]===========================  
            elif msg.text.lower() == 'infogrup':
                if msg.from_ in admin:
                    group = kr1.getGroup(msg.to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Error"
                    md = "[Nama Grup : ]\n" + group.name + "\n\n[Id Grup : ]\n" + group.id + "\n\n[Pembuat Grup :]\n" + gCreator + "\n\n[Gambar Grup : ]\nhttp://dl.profile.line-cdn.net/" + group.pictureStatus
                    if group.preventJoinByTicket is False: md += "\n\nKode Url : Diizinkan"
                    else: md += "\n\nKode Url : Diblokir"
                    if group.invitee is None: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : 0 Orang"
                    else: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : " + str(len(group.invitee)) + " Orang"
                    kr1.sendText(msg.to,md)
#==========================[Kris]===========================
            elif msg.text.lower() == 'grup id':
                if msg.from_ in owner:
                    gid = kr1.getGroupIdsJoined()
                    h = ""
                    for i in gid:
                        h += "[%s]:%s\n" % (kr1.getGroup(i).name,i)
                    kr1.sendText(msg.to,h)
#==========================[Kris]===========================
            elif msg.text in ["Glist"]:
                if msg.from_ in admin:
                    gid = kr1.getGroupIdsJoined()
                    h = ""
                    for i in gid:
                        h += "%s\n" % (kr1.getGroup(i).name +" ? ["+str(len(kr1.getGroup(i).members))+"]")
                    kr1.sendText(msg.to,"-- List Groups --\n\n"+ h +"\nTotal groups =" +" ["+str(len(gid))+"]")
#==========================[Kris]===========================
            elif msg.text.lower() == 'gcancel':
                if msg.from_ in admin:
                    gid = kr1.getGroupIdsInvited()
                    for i in gid:
                        kr1.rejectGroupInvitation(i)
                    if wait["lang"] == "JP":
                        kr1.sendText(msg.to,"Aku menolak semua undangan")
                    else:
                        kr1.sendText(msg.to,"He declined all invitations")
#==========================[Kris]===========================  
            elif "Auto add" in msg.text:
                if msg.from_ in admin:
                    thisgroup = kr1.getGroups([msg.to])
                    Mids = [contact.mid for contact in thisgroup[0].members]
                    mi_d = Mids[:33]
                    kr1.findAndAddContactsByMids(mi_d)
                    kr1.sendText(msg.to,"Success Add all")
#==========================[Kris]===========================
            elif "Admin add @" in msg.text:
              if msg.from_ in owner:
                print "[Command]Staff add executing"
                _name = msg.text.replace("Admin add @","")
                _nametarget = _name.rstrip('  ')
                gs = kr1.getGroup(msg.to)
                gs = kr2.getGroup(msg.to)
                gs = kr3.getGroup(msg.to)
                gs = kr4.getGroup(msg.to)
                gs = kr5.getGroup(msg.to)
                gs = kr6.getGroup(msg.to)
                gs = kr7.getGroup(msg.to)
                gs = kr8.getGroup(msg.to)
                gs = kr9.getGroup(msg.to)
                gs = kr10.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact not found")
                else:
                   for target in targets:
                        try:
                            admin.append(target)
                            kr1.sendText(msg.to,"Admin Ditambahkan")
                        except:
                            pass
                print "[Command]Staff add executed"
              else:
                kr1.sendText(msg.to,"Perintah Ditolak.")
                kr1.sendText(msg.to,"Hanya Owner Yang bisa Gunain Perintah ini.")
#==========================[Kris]===========================
            elif "Admin remove @" in msg.text:
              if msg.from_ in owner:
                print "[Command]Staff remove executing"
                _name = msg.text.replace("Admin remove @","")
                _nametarget = _name.rstrip('  ')
                gs = kr1.getGroup(msg.to)
                gs = kr2.getGroup(msg.to)
                gs = kr3.getGroup(msg.to)
                gs = kr4.getGroup(msg.to)
                gs = kr5.getGroup(msg.to)
                gs = kr6.getGroup(msg.to)
                gs = kr7.getGroup(msg.to)
                gs = kr8.getGroup(msg.to)
                gs = kr9.getGroup(msg.to)
                gs = kr10.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact not found")
                else:
                   for target in targets:
                        try:
                            admin.remove(target)
                            kr1.sendText(msg.to,"Admin Dihapus")
                        except:
                            pass
                print "[Command]Staff remove executed"
              else:
                kr1.sendText(msg.to,"Perintah Ditolak.")
                kr1.sendText(msg.to,"Hanya Owner Yang bisa Gunain Perintah ini.")
#==========================[Kris]=========================== 
            elif msg.text in ["Adminlist","adminlist"]:
              if admin == []:
                  kr1.sendText(msg.to,"The stafflist is empty")
              else:
                  kr1.sendText(msg.to,"Tunggu...")
                  mc = "╔═════════════\n║Admin ✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰\n╠═════════════\n"
                  for mi_d in admin:
                      mc += "║••>" +kr1.getContact(mi_d).displayName + "\n╠═════════════\n"
                  kr1.sendText(msg.to,mc)
                  print "[Command]Stafflist executed"
#==========================[Kris]===========================
            elif msg.text in [".join","asup"]: #Panggil Semua Bot
                if msg.from_ in owner:
                    G = kr1.getGroup(msg.to)
                    ginfo = kr1.getGroup(msg.to)
                    G.preventJoinByTicket = False
                    kr1.updateGroup(G)
                    invsend = 0
                    Ticket = kr1.reissueGroupTicket(msg.to)
                    kr2.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.01)
                    kr3.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.01)
                    kr4.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.01)
                    kr5.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.01)
                    kr6.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.01)
                    kr7.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.01)
                    kr8.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.01)
                    kr9.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.01)
                    kr10.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.01)
                    kr11.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.01)
                    kr12.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.01)
                    kr13.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.01)
                    kr14.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.01)
                    kr15.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.01)
                    kr16.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.01)
                    kr17.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.01)
                    kr18.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.01)
                    kr19.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.01)
                    kr20.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.01)
                    kr21.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.01)
                    kr22.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.01)
                    kr23.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.01)
                    kr24.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.01)
                    kr25.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.01)
                    G = kr1.getGroup(msg.to)
                    ginfo = kr1.getGroup(msg.to)
                    G.preventJoinByTicket = True
                    kr1.updateGroup(G)
                    kr5.sendText(msg.to,"Hallo...!!! " + str(ginfo.name) + "\n\nSemoga Selalu Bahagia...!!!")
                    print "Semua Sudah Lengkap"
#==========================[Kris]=========================== 
            elif msg.text in [".."]: #Panggil Semua Bot
                if msg.from_ in owner:
                    G = kr1.getGroup(msg.to)
                    ginfo = kr1.getGroup(msg.to)
                    midd2 = msg.text.replace("..","udb0b6b2c1f32887d23bd3e4dfb302ed1")
                    midd3 = msg.text.replace("..","uad6cb020c5ca7afbecb4681675eb38cd")
                    midd4 = msg.text.replace("..","ud5262649376cbf7576e2dcac0331d481")
                    midd5 = msg.text.replace("..","u53c352134325f0c49e86534c57801bd7")
                    midd6 = msg.text.replace("..","ua2ea9f4c32848bc67644c5267bb91279")
                    midd7 = msg.text.replace("..","uadfd3a23698b71d17c64482d27dc2ed1")
                    midd8 = msg.text.replace("..","u45c6ce403f0acc28392c519028aae154")
                    midd9 = msg.text.replace("..","udcf44c4272d8209a8a5f2dd1afeea93f")
                    midd10 = msg.text.replace("..","u4a0be979fc73e88ebfe915bc917237b8")
                    midd11 = msg.text.replace("..","u4a0be979fc73e88ebfe915bc917237b8")
                    midd12 = msg.text.replace("..","udb0b6b2c1f32887d23bd3e4dfb302ed1")
                    midd13 = msg.text.replace("..","uad6cb020c5ca7afbecb4681675eb38cd")
                    midd14 = msg.text.replace("..","ud5262649376cbf7576e2dcac0331d481")
                    midd15 = msg.text.replace("..","u53c352134325f0c49e86534c57801bd7")
                    midd16 = msg.text.replace("..","ua2ea9f4c32848bc67644c5267bb91279")
                    midd17 = msg.text.replace("..","uadfd3a23698b71d17c64482d27dc2ed1")
                    midd18 = msg.text.replace("..","u45c6ce403f0acc28392c519028aae154")
                    midd19 = msg.text.replace("..","udcf44c4272d8209a8a5f2dd1afeea93f")
                    midd20 = msg.text.replace("..","u4a0be979fc73e88ebfe915bc917237b8")
                    midd21 = msg.text.replace("..","u4a0be979fc73e88ebfe915bc917237b8")
                    midd22 = msg.text.replace("..","udb0b6b2c1f32887d23bd3e4dfb302ed1")
                    midd23 = msg.text.replace("..","uad6cb020c5ca7afbecb4681675eb38cd")
                    midd24 = msg.text.replace("..","ud5262649376cbf7576e2dcac0331d481")
                    midd25 = msg.text.replace("..","u53c352134325f0c49e86534c57801bd7")
                    kr1.findAndAddContactsByMid(midd2)
                    kr1.findAndAddContactsByMid(midd3)
                    kr1.findAndAddContactsByMid(midd4)
                    kr1.findAndAddContactsByMid(midd5)
                    kr1.findAndAddContactsByMid(midd6)
                    kr1.findAndAddContactsByMid(midd7)
                    kr1.findAndAddContactsByMid(midd8)
                    kr1.findAndAddContactsByMid(midd9)
                    kr1.findAndAddContactsByMid(midd10)
                    kr1.findAndAddContactsByMid(midd11)
                    kr1.findAndAddContactsByMid(midd12)
                    kr1.findAndAddContactsByMid(midd13)
                    kr1.findAndAddContactsByMid(midd14)
                    kr1.findAndAddContactsByMid(midd15)
                    kr1.findAndAddContactsByMid(midd16)
                    kr1.findAndAddContactsByMid(midd17)
                    kr1.findAndAddContactsByMid(midd18)
                    kr1.findAndAddContactsByMid(midd19)
                    kr1.findAndAddContactsByMid(midd20)
                    kr1.findAndAddContactsByMid(midd21)
                    kr1.findAndAddContactsByMid(midd22)
                    kr1.findAndAddContactsByMid(midd23)
                    kr1.findAndAddContactsByMid(midd24)
                    kr1.findAndAddContactsByMid(midd25)
                    kr1.inviteIntoGroup(msg.to,[midd2])
                    kr1.inviteIntoGroup(msg.to,[midd3])
                    kr1.inviteIntoGroup(msg.to,[midd4])
                    kr1.inviteIntoGroup(msg.to,[midd5])
                    kr1.inviteIntoGroup(msg.to,[midd6])
                    kr1.inviteIntoGroup(msg.to,[midd7])
                    kr1.inviteIntoGroup(msg.to,[midd8])
                    kr1.inviteIntoGroup(msg.to,[midd9])
                    kr1.inviteIntoGroup(msg.to,[midd11])
                    kr1.inviteIntoGroup(msg.to,[midd10])
                    kr1.inviteIntoGroup(msg.to,[midd12])
                    kr1.inviteIntoGroup(msg.to,[midd13])
                    kr1.inviteIntoGroup(msg.to,[midd14])
                    kr1.inviteIntoGroup(msg.to,[midd15])
                    kr1.inviteIntoGroup(msg.to,[midd16])
                    kr1.inviteIntoGroup(msg.to,[midd17])
                    kr1.inviteIntoGroup(msg.to,[midd18])
                    kr1.inviteIntoGroup(msg.to,[midd19])
                    kr1.inviteIntoGroup(msg.to,[midd20])
                    kr1.inviteIntoGroup(msg.to,[midd21])
                    kr1.inviteIntoGroup(msg.to,[midd22])
                    kr1.inviteIntoGroup(msg.to,[midd23])
                    kr1.inviteIntoGroup(msg.to,[midd24])
                    kr1.inviteIntoGroup(msg.to,[midd25])
                    kr2.acceptGroupInvitation(msg.to)
                    kr3.acceptGroupInvitation(msg.to)
                    kr4.acceptGroupInvitation(msg.to)
                    kr5.acceptGroupInvitation(msg.to)
                    kr6.acceptGroupInvitation(msg.to)
                    kr7.acceptGroupInvitation(msg.to)
                    kr8.acceptGroupInvitation(msg.to)
                    kr9.acceptGroupInvitation(msg.to)
                    kr10.acceptGroupInvitation(msg.to)
                    kr11.acceptGroupInvitation(msg.to)
                    kr12.acceptGroupInvitation(msg.to)
                    kr13.acceptGroupInvitation(msg.to)
                    kr14.acceptGroupInvitation(msg.to)
                    kr15.acceptGroupInvitation(msg.to)
                    kr16.acceptGroupInvitation(msg.to)
                    kr17.acceptGroupInvitation(msg.to)
                    kr18.acceptGroupInvitation(msg.to)
                    kr19.acceptGroupInvitation(msg.to)
                    kr20.acceptGroupInvitation(msg.to)
                    kr21.acceptGroupInvitation(msg.to)
                    kr22.acceptGroupInvitation(msg.to)
                    kr23.acceptGroupInvitation(msg.to)
                    kr24.acceptGroupInvitation(msg.to)
                    kr25.acceptGroupInvitation(msg.to)
                    kr10.sendText(msg.to,"Hallo...!!! " + str(ginfo.name) + "\n\nSemoga Selalu Bahagia...!!!")
                    print "Semua Sudah Lengkap"
            elif msg.text in ["."]: #Panggil Bot induk
                if msg.from_ in owner:
                    G = kr2.getGroup(msg.to)
                    G = kr3.getGroup(msg.to)
                    G = kr4.getGroup(msg.to)
                    G = kr5.getGroup(msg.to)
                    G = kr6.getGroup(msg.to)
                    G = kr7.getGroup(msg.to)
                    G = kr8.getGroup(msg.to)
                    G = kr9.getGroup(msg.to)
                    G = kr10.getGroup(msg.to)
                    G = kr11.getGroup(msg.to)
                    G = kr12.getGroup(msg.to)
                    G = kr13.getGroup(msg.to)
                    G = kr14.getGroup(msg.to)
                    G = kr15.getGroup(msg.to)
                    G = kr16.getGroup(msg.to)
                    G = kr17.getGroup(msg.to)
                    G = kr18.getGroup(msg.to)
                    G = kr19.getGroup(msg.to)
                    G = kr20.getGroup(msg.to)
                    G = kr21.getGroup(msg.to)
                    G = kr22.getGroup(msg.to)
                    G = kr23.getGroup(msg.to)
                    G = kr24.getGroup(msg.to)
                    G = kr25.getGroup(msg.to)
                    ginfo = kr2.getGroup(msg.to)
                    ginfo = kr3.getGroup(msg.to)
                    ginfo = kr4.getGroup(msg.to)
                    ginfo = kr5.getGroup(msg.to)
                    ginfo = kr6.getGroup(msg.to)
                    ginfo = kr7.getGroup(msg.to)
                    ginfo = kr8.getGroup(msg.to)
                    ginfo = kr9.getGroup(msg.to)
                    ginfo = kr10.getGroup(msg.to)
                    ginfo = kr11.getGroup(msg.to)
                    ginfo = kr12.getGroup(msg.to)
                    ginfo = kr13.getGroup(msg.to)
                    ginfo = kr14.getGroup(msg.to)
                    ginfo = kr15.getGroup(msg.to)
                    ginfo = kr16.getGroup(msg.to)
                    ginfo = kr17.getGroup(msg.to)
                    ginfo = kr18.getGroup(msg.to)
                    ginfo = kr19.getGroup(msg.to)
                    ginfo = kr20.getGroup(msg.to)
                    ginfo = kr21.getGroup(msg.to)
                    ginfo = kr22.getGroup(msg.to)
                    ginfo = kr23.getGroup(msg.to)
                    ginfo = kr24.getGroup(msg.to)
                    ginfo = kr25.getGroup(msg.to)
                    midd1 = msg.text.replace(".","u4a0f653ea757da7abcd41c15bf0f15da")
                    random.choice(KAC).findAndAddContactsByMid(midd1)
                    random.choice(KAC).inviteIntoGroup(msg.to,[midd1])
                    kr1.acceptGroupInvitation(msg.to)
                    print "Induk Sudah Masuk"
#==========================[Kris]===========================
            elif msg.text in ["Kabur all","Kr kabur"]:#keluar semua bots
                if msg.from_ in owner:
                    if msg.toType == 2:
                        ginfo = kr1.getGroup(msg.to)
                        ginfo = kr2.getGroup(msg.to)
                        ginfo = kr3.getGroup(msg.to)
                        ginfo = kr4.getGroup(msg.to)
                        ginfo = kr5.getGroup(msg.to)
                        ginfo = kr6.getGroup(msg.to)
                        ginfo = kr7.getGroup(msg.to)
                        ginfo = kr8.getGroup(msg.to)
                        ginfo = kr9.getGroup(msg.to)
                        ginfo = kr10.getGroup(msg.to)
                        ginfo = kr11.getGroup(msg.to)
                        ginfo = kr12.getGroup(msg.to)
                        ginfo = kr13.getGroup(msg.to)
                        ginfo = kr14.getGroup(msg.to)
                        ginfo = kr15.getGroup(msg.to)
                        ginfo = kr16.getGroup(msg.to)
                        ginfo = kr17.getGroup(msg.to)
                        ginfo = kr18.getGroup(msg.to)
                        ginfo = kr19.getGroup(msg.to)
                        ginfo = kr20.getGroup(msg.to)
                        ginfo = kr21.getGroup(msg.to)
                        ginfo = kr22.getGroup(msg.to)
                        ginfo = kr23.getGroup(msg.to)
                        ginfo = kr24.getGroup(msg.to)
                        ginfo = kr25.getGroup(msg.to)
                        try:
                            kr10.sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nJangan Lupa Bahagia...!!!")
                            kr25.leaveGroup(msg.to)
                            kr24.leaveGroup(msg.to)
                            kr23.leaveGroup(msg.to)
                            kr22.leaveGroup(msg.to)
                            kr21.leaveGroup(msg.to)
                            kr20.leaveGroup(msg.to)
                            kr19.leaveGroup(msg.to)
                            kr18.leaveGroup(msg.to)
                            kr17.leaveGroup(msg.to)
                            kr16.leaveGroup(msg.to)
                            kr15.leaveGroup(msg.to)
                            kr14.leaveGroup(msg.to)
                            kr13.leaveGroup(msg.to)
                            kr12.leaveGroup(msg.to)
                            kr11.leaveGroup(msg.to)
                            kr10.leaveGroup(msg.to)
                            kr9.leaveGroup(msg.to)
                            kr8.leaveGroup(msg.to)
                            kr7.leaveGroup(msg.to)
                            kr6.leaveGroup(msg.to)
                            kr5.leaveGroup(msg.to)
                            kr4.leaveGroup(msg.to)
                            kr3.leaveGroup(msg.to)
                            kr2.leaveGroup(msg.to)
                            kr1.leaveGroup(msg.to)
                        except:
                            pass
#==========================[Kris]===========================
            elif msg.text in [".bye"]:#keluar bot kecuali bot induk
                if msg.from_ in owner:
                    if msg.toType == 2:
                        ginfo = kr1.getGroup(msg.to)
                        ginfo = kr2.getGroup(msg.to)
                        ginfo = kr3.getGroup(msg.to)
                        ginfo = kr4.getGroup(msg.to)
                        ginfo = kr5.getGroup(msg.to)
                        ginfo = kr6.getGroup(msg.to)
                        ginfo = kr7.getGroup(msg.to)
                        ginfo = kr8.getGroup(msg.to)
                        ginfo = kr9.getGroup(msg.to)
                        ginfo = kr10.getGroup(msg.to)
                        ginfo = kr11.getGroup(msg.to)
                        ginfo = kr12.getGroup(msg.to)
                        ginfo = kr13.getGroup(msg.to)
                        ginfo = kr14.getGroup(msg.to)
                        ginfo = kr15.getGroup(msg.to)
                        ginfo = kr16.getGroup(msg.to)
                        ginfo = kr17.getGroup(msg.to)
                        ginfo = kr18.getGroup(msg.to)
                        ginfo = kr19.getGroup(msg.to)
                        ginfo = kr20.getGroup(msg.to)
                        ginfo = kr21.getGroup(msg.to)
                        ginfo = kr22.getGroup(msg.to)
                        ginfo = kr23.getGroup(msg.to)
                        ginfo = kr24.getGroup(msg.to)
                        ginfo = kr25.getGroup(msg.to)
                        try:
                            kr20.sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nJangan Lupa Bahagia...!!!")     
                            kr25.leaveGroup(msg.to)
                            kr24.leaveGroup(msg.to)
                            kr23.leaveGroup(msg.to)
                            kr22.leaveGroup(msg.to)
                            kr21.leaveGroup(msg.to)
                            kr20.leaveGroup(msg.to)
                            kr19.leaveGroup(msg.to)
                            kr18.leaveGroup(msg.to)
                            kr17.leaveGroup(msg.to)
                            kr16.leaveGroup(msg.to)
                            kr15.leaveGroup(msg.to)
                            kr14.leaveGroup(msg.to)
                            kr13.leaveGroup(msg.to)
                            kr12.leaveGroup(msg.to)
                            kr11.leaveGroup(msg.to)
                            kr10.leaveGroup(msg.to)
                            kr9.leaveGroup(msg.to)
                            kr8.leaveGroup(msg.to)
                            kr7.leaveGroup(msg.to)
                            kr6.leaveGroup(msg.to)
                            kr5.leaveGroup(msg.to)
                            kr4.leaveGroup(msg.to)
                            kr3.leaveGroup(msg.to)
                            kr2.leaveGroup(msg.to)
                            #kr1.leaveGroup(msg.to)
                        except:
                            pass
#==========================[Kris]===========================
            elif "hai" == msg.text.lower():
                if msg.from_ in admin:
                    group = kr1.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                    if jml <= 100:
                        summon(msg.to, nama)
                    if jml > 100 and jml < 200:
                        for i in range(0, 99):
                            nm1 += [nama[i]]
                        summon(msg.to, nm1)
                        for j in range(100, len(nama)-1):
                            nm2 += [nama[j]]
                        summon(msg.to, nm2)
                    if jml > 200  and jml < 500:
                        for i in range(0, 99):
                            nm1 += [nama[i]]
                        summon(msg.to, nm1)
                        for j in range(100, 199):
                            nm2 += [nama[j]]
                        summon(msg.to, nm2)
                        for k in range(200, 299):
                            nm3 += [nama[k]]
                        summon(msg.to, nm3)
                        for l in range(300, 399):
                            nm4 += [nama[l]]
                        summon(msg.to, nm4)
                        for m in range(400, len(nama)-1):
                            nm5 += [nama[m]]
                        summon(msg.to, nm5)
                    if jml > 500:
                         print "Terlalu Banyak Men 500+"
                    cnt = Message()
                    cnt.text = "Jumlah:\n" + str(jml) +  " Members"
                    cnt.to = msg.to
                    kr1.sendMessage(cnt)
#==========================[Kris]===========================
            elif "sepi" == msg.text.lower():
                if msg.from_ in admin:
                    group = kr1.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                    if jml <= 100:
                        summon(msg.to, nama)
                    if jml > 100 and jml < 200:
                        for i in range(0, 99):
                            nm1 += [nama[i]]
                        summon(msg.to, nm1)
                        for j in range(100, len(nama)-1):
                            nm2 += [nama[j]]
                        summon(msg.to, nm2)
                    if jml > 200  and jml < 500:
                        for i in range(0, 99):
                            nm1 += [nama[i]]
                        summon(msg.to, nm1)
                        for j in range(100, 199):
                            nm2 += [nama[j]]
                        summon(msg.to, nm2)
                        for k in range(200, 299):
                            nm3 += [nama[k]]
                        summon(msg.to, nm3)
                        for l in range(300, 399):
                            nm4 += [nama[l]]
                        summon(msg.to, nm4)
                        for m in range(400, len(nama)-1):
                            nm5 += [nama[m]]
                        summon(msg.to, nm5)
                    if jml > 500:
                         print "Terlalu Banyak Men 500+"
                    cnt = Message()
                    cnt.text = "Jumlah:\n" + str(jml) +  " Members"
                    cnt.to = msg.to
                    kr1.sendMessage(cnt)

#==========================[Kris]===========================
            elif msg.text.lower() == 'Bot':
                random.choice(KAC).sendImageWithURL(msg.to, url123)
                random.choice(KAC).sendText(msg.to,"↥↥↥↥↥↪ Pembuat Bots ↩↥↥↥↥↥")
                    
#==========================[Kris]===========================
            elif "Gbroadcast: " in msg.text:
                if msg.from_ in owner:
                    bc = msg.text.replace("Gbroadcast: ","")
                    gid = kr1.getGroupIdsJoined()
                    for i in gid:
                        kr1.sendText(i, bc)
#==========================[Kris]=========================== 
            elif "Cbroadcast: " in msg.text:
                if msg.from_ in owner:
                    bc = msg.text.replace("Cbroadcast: ","")
                    gid = kr1.getAllContactIds()
                    for i in gid:
                        kr1.sendText(i, bc)

#==========================[Kris]===========================
            elif "Spamtag @" in msg.text:
                if msg.from_ in admin:
                    _name = msg.text.replace("Spamtag @","")
                    _nametarget = _name.rstrip(' ')
                    gs = kr1.getGroup(msg.to)
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            xname = g.displayName
                            xlen = str(len(xname)+1)
                            msg.contentType = 0
                            msg.text = "@"+xname+" "
                            msg.contentMetadata ={"MENTION":'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(g.mid)+'}]}','EMTVER':'4'}
                            kr1.sendMessage(msg)
                            kr1.sendMessage(msg)
                            kr1.sendMessage(msg)
                            kr1.sendMessage(msg)
                            kr1.sendMessage(msg)
                            kr1.sendMessage(msg)
                            kr1.sendMessage(msg)
                            kr1.sendMessage(msg)
                            kr1.sendMessage(msg)
                            kr1.sendMessage(msg)
                            kr1.sendMessage(msg)
                            kr1.sendMessage(msg)
                            kr1.sendMessage(msg)
                            kr1.sendMessage(msg)
                            kr1.sendMessage(msg)
                            kr1.sendMessage(msg)
                            kr1.sendMessage(msg)
                            kr1.sendMessage(msg)
                            kr1.sendMessage(msg)
                            kr1.sendMessage(msg)
                        else:
                            pass

            elif msg.text.lower() == 'mymid':
                kr1.sendText(msg.to,mid)
#==========================[Kris]===========================
            elif "Namebot: " in msg.text:
                if msg.from_ in owner:
                    string = msg.text.replace("Namebot: ","")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = kr1.getProfile()
                        profile.displayName = string
                        kr1.updateProfile(profile)
                        kr1.sendText(msg.to,"Changed " + string + "")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = kr2.getProfile()
                        profile.displayName = string
                        kr2.updateProfile(profile)
                        kr2.sendText(msg.to,"Changed " + string + "")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = kr3.getProfile()
                        profile.displayName = string
                        kr3.updateProfile(profile)
                        kr3.sendText(msg.to,"Changed " + string + "")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = kr4.getProfile()
                        profile.displayName = string
                        kr4.updateProfile(profile)
                        kr4.sendText(msg.to,"Changed " + string + "")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = kr5.getProfile()
                        profile.displayName = string
                        kr5.updateProfile(profile)
                        kr5.sendText(msg.to,"Changed " + string + "")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = kr6.getProfile()
                        profile.displayName = string
                        kr6.updateProfile(profile)
                        kr6.sendText(msg.to,"Changed " + string + "")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = kr7.getProfile()
                        profile.displayName = string
                        kr7.updateProfile(profile)
                        kr7.sendText(msg.to,"Changed " + string + "")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = kr8.getProfile()
                        profile.displayName = string
                        kr8.updateProfile(profile)
                        kr8.sendText(msg.to,"Changed " + string + "")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = kr9.getProfile()
                        profile.displayName = string
                        kr9.updateProfile(profile)
                        kr9.sendText(msg.to,"Changed " + string + "")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = kr10.getProfile()
                        profile.displayName = string
                        kr10.updateProfile(profile)
                        kr10.sendText(msg.to,"Changed " + string + "")
#==========================[Kris]===========================
            elif "Namebot1: " in msg.text:
                if msg.from_ in owner:
                    string = msg.text.replace("Namebot1: ","")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = kr1.getProfile()
                        profile.displayName = string
                        kr1.updateProfile(profile)
                        kr1.sendText(msg.to,"Changed " + string + "")
            elif "Namebot2: " in msg.text:
                if msg.from_ in owner:
                    string = msg.text.replace("Namebot2: ","")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = kr2.getProfile()
                        profile.displayName = string
                        kr2.updateProfile(profile)
                        kr2.sendText(msg.to,"Changed " + string + "")
            elif "Namebot3: " in msg.text:
                if msg.from_ in owner:
                    string = msg.text.replace("Namebot3: ","")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = kr3.getProfile()
                        profile.displayName = string
                        kr3.updateProfile(profile)
                        kr3.sendText(msg.to,"Changed " + string + "")
            elif "Namebot4: " in msg.text:
                if msg.from_ in owner:
                    string = msg.text.replace("Namebot4: ","")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = kr4.getProfile()
                        profile.displayName = string
                        kr4.updateProfile(profile)
                        kr4.sendText(msg.to,"Changed " + string + "")
            elif "Namebot5: " in msg.text:
                if msg.from_ in owner:
                    string = msg.text.replace("Namebot5: ","")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = kr5.getProfile()
                        profile.displayName = string
                        kr5.updateProfile(profile)
                        kr5.sendText(msg.to,"Changed " + string + "")
            elif "Namebot6: " in msg.text:
                if msg.from_ in owner:
                    string = msg.text.replace("Namebot6: ","")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = kr6.getProfile()
                        profile.displayName = string
                        kr6.updateProfile(profile)
                        kr6.sendText(msg.to,"Changed " + string + "")
            elif "Namebot7: " in msg.text:
                if msg.from_ in owner:
                    string = msg.text.replace("Namebot7: ","")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = kr7.getProfile()
                        profile.displayName = string
                        kr7.updateProfile(profile)
                        kr7.sendText(msg.to,"Changed " + string + "")
            elif "Namebot8: " in msg.text:
                if msg.from_ in owner:
                    string = msg.text.replace("Namebot8: ","")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = kr8.getProfile()
                        profile.displayName = string
                        kr8.updateProfile(profile)
                        kr8.sendText(msg.to,"Changed " + string + "")
            elif "Namebot9: " in msg.text:
                if msg.from_ in owner:
                    string = msg.text.replace("Namebot9: ","")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = kr9.getProfile()
                        profile.displayName = string
                        kr9.updateProfile(profile)
                        kr9.sendText(msg.to,"Changed " + string + "")
            elif "Namebot10: " in msg.text:
                if msg.from_ in owner:
                    string = msg.text.replace("Namebot10: ","")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = kr10.getProfile()
                        profile.displayName = string
                        kr10.updateProfile(profile)
                        kr10.sendText(msg.to,"Changed " + string + "")
#==========================[Kris]===========================
            elif "Biobot: " in msg.text:
                if msg.from_ in owner:
                    string = msg.text.replace("Biobot: ","")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = kr1.getProfile()
                        profile.statusMessage = string
                        kr1.updateProfile(profile)
                        kr1.sendText(msg.to,"Changed " + string)
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = kr2.getProfile()
                        profile.statusMessage = string
                        kr2.updateProfile(profile)
                        kr2.sendText(msg.to,"Changed " + string)
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = kr3.getProfile()
                        profile.statusMessage = string
                        kr3.updateProfile(profile)
                        kr3.sendText(msg.to,"Changed " + string)
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = kr4.getProfile()
                        profile.statusMessage = string
                        kr4.updateProfile(profile)
                        kr4.sendText(msg.to,"Changed " + string)
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = kr5.getProfile()
                        profile.statusMessage = string
                        kr5.updateProfile(profile)
                        kr5.sendText(msg.to,"Changed " + string)
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = kr6.getProfile()
                        profile.statusMessage = string
                        kr6.updateProfile(profile)
                        kr6.sendText(msg.to,"Changed " + string)
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = kr7.getProfile()
                        profile.statusMessage = string
                        kr7.updateProfile(profile)
                        kr7.sendText(msg.to,"Changed " + string)
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = kr8.getProfile()
                        profile.statusMessage = string
                        kr8.updateProfile(profile)
                        kr8.sendText(msg.to,"Changed " + string)
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = kr9.getProfile()
                        profile.statusMessage = string
                        kr9.updateProfile(profile)
                        kr9.sendText(msg.to,"Changed " + string)
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = kr10.getProfile()
                        profile.statusMessage = string
                        kr10.updateProfile(profile)
                        kr10.sendText(msg.to,"Changed " + string)
#==========================[Kris]===========================
            elif msg.text in ["Myname"]:
                    h = kr1.getContact(mid)
                    kr1.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
            elif msg.text in ["Mybot"]:
                    h = kr1.getContact(mid)
                    h = kr2.getContact(Amid)
                    h = kr3.getContact(Bmid)
                    h = kr4.getContact(Cmid)
                    h = kr5.getContact(Dmid)
                    h = kr6.getContact(Emid)
                    h = kr7.getContact(Fmid)
                    h = kr8.getContact(Gmid)
                    h = kr9.getContact(Hmid)
                    h = kr10.getContact(Imid)
                    h = kr11.getContact(Jmid)
                    h = kr12.getContact(Kmid)
                    h = kr13.getContact(Lmid)
                    h = kr14.getContact(Mmid)
                    h = kr15.getContact(Nmid)
                    h = kr16.getContact(Omid)
                    h = kr17.getContact(Pmid)
                    h = kr18.getContact(Qmid)
                    h = kr19.getContact(Rmid)
                    h = kr20.getContact(Smid)
                    h = kr21.getContact(Tmid)
                    h = kr22.getContact(Umid)
                    h = kr23.getContact(Vmid)
                    h = kr24.getContact(Wmid)
                    h = kr25.getContact(Xmid)
                    kr1.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
                    kr2.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
                    kr3.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
                    kr4.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
                    kr5.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
                    kr6.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
                    kr7.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
                    kr8.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
                    kr9.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
                    kr10.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
                    kr11.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
                    kr12.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
                    kr13.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
                    kr14.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
                    kr15.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
                    kr16.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
                    kr17.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
                    kr18.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
                    kr19.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
                    kr20.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
                    kr21.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
                    kr22.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
                    kr23.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
                    kr24.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
                    kr25.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
            elif msg.text in ["Mybio"]:
                    h = kr1.getContact(mid)
                    kr1.sendText(msg.to,"═══[StatusMessage]═══\n" + h.statusMessage)
            elif msg.text in ["Mypict"]:
                    h = kr1.getContact(mid)
                    kr1.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in ["Myvid"]:
                    h = kr1.getContact(mid)
                    kr1.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in ["Urlpict"]:
                    h = kr1.getContact(mid)
                    kr1.sendText(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text.lower() == 'Bot':
                random.choice(KAC).sendImageWithURL(msg.to, url123)
                random.choice(KAC).sendText(msg.to,"↥↥↥↥↥↪ Pembuat Bots ↩↥↥↥↥↥")
            elif msg.text in ["Mycover"]:
                    h = kr1.getContact(mid)
                    cu = kr1.channel.getCover(mid)          
                    path = str(cu)
                    kr1.sendImageWithURL(msg.to, path)
            elif msg.text in ["Urlcover"]:
                    h = kr1.getContact(mid)
                    cu = kr1.channel.getCover(mid)          
                    path = str(cu)
                    kr1.sendText(msg.to, path)
           
            elif msg.text in ["Absen","absen"]:
                if msg.from_ in admin:
                    kr1.sendText(msg.to,"👉★1★√")
                    kr2.sendText(msg.to,"👉★2★√")
                    kr3.sendText(msg.to,"👉★3★√")
                    kr4.sendText(msg.to,"👉★4★√")
                    kr5.sendText(msg.to,"👉★5★√")
                    kr6.sendText(msg.to,"👉★6★√")
                    kr7.sendText(msg.to,"👉★7★√")
                    kr8.sendText(msg.to,"👉★8★√")
                    kr9.sendText(msg.to,"👉★9★√")
                    kr10.sendText(msg.to,"👉★10★√")
                    kr11.sendText(msg.to,"👉★11★√")
                    kr12.sendText(msg.to,"👉★12★√")
                    kr13.sendText(msg.to,"👉★13★√")
                    kr14.sendText(msg.to,"👉★14★√")
                    kr15.sendText(msg.to,"👉★15★√")
                    kr16.sendText(msg.to,"👉★16★√")
                    kr17.sendText(msg.to,"👉★17★√")
                    kr18.sendText(msg.to,"👉★18★√")
                    kr19.sendText(msg.to,"👉★19★√")
                    kr20.sendText(msg.to,"👉★20★√")
                    kr21.sendText(msg.to,"👉★21★√")
                    kr22.sendText(msg.to,"👉★22★√")
                    kr23.sendText(msg.to,"👉★23★√")
                    kr24.sendText(msg.to,"👉★24★√")
                    kr25.sendText(msg.to,"👉★25★√")
                    kr12.sendText(msg.to,"👉Semua Hadir Boss...!!!\n\n[✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰]")
#==========================[Kris]===========================
            elif "Bcast " in msg.text:
                if msg.from_ in owner:
                    bc = msg.text.replace("Bcast ","")
                    gid = kr1.getGroupIdsJoined()
                    for i in gid:
                        kr1.sendText(i,"●▬▬▬▬ஜ۩[BROADCAST]۩ஜ▬▬▬▬●\n\n"+bc+"\n\n#BROADCAST!!")
      
#==========================[Kris]===========================
            elif "Restart" in msg.text:
                if msg.from_ in owner:
                    print "[Command]Restart"
                    try:
                        kr1.sendText(msg.to,"Restarting...")
                        kr1.sendText(msg.to,"Restart Success")
                        restart_program()
                    except:
                        kr1.sendText(msg.to,"Please wait")
                        restart_program()
                        pass
#==========================[Kris]===========================
            elif "Kr turn off" in msg.text:
                if msg.from_ in owner:
                    try:
                        import sys
                        sys.exit()
                    except:
                        pass
#==========================[Kris]===========================
            elif msg.text.lower() == 'runtime':
                if msg.from_ in admin:
                    eltime = time.time() - mulai
                    van = "Bot has been active "+waktu(eltime)
                    kr1.sendText(msg.to,van)
#==========================[Kris]===========================
            elif msg.text in ["Kr kemari"]: # Keluar Dari Semua Group Yang Di dalem nya  ada bot(Kalo Bot Kalian Nyangkut di Group lain :D)
                if msg.from_ in owner:
                    gid = kr1.getGroupIdsJoined()
                    gid = kr2.getGroupIdsJoined()
                    gid = kr3.getGroupIdsJoined()
                    gid = kr4.getGroupIdsJoined()
                    gid = kr5.getGroupIdsJoined()
                    gid = kr6.getGroupIdsJoined()
                    gid = kr7.getGroupIdsJoined()
                    gid = kr8.getGroupIdsJoined()
                    gid = kr9.getGroupIdsJoined()
                    gid = kr10.getGroupIdsJoined()
                    gid = kr11.getGroupIdsJoined()
                    gid = kr12.getGroupIdsJoined()
                    gid = kr13.getGroupIdsJoined()
                    gid = kr14.getGroupIdsJoined()
                    gid = kr15.getGroupIdsJoined()
                    gid = kr16.getGroupIdsJoined()
                    gid = kr17.getGroupIdsJoined()
                    gid = kr18.getGroupIdsJoined()
                    gid = kr19.getGroupIdsJoined()
                    gid = kr20.getGroupIdsJoined()
                    gid = kr21.getGroupIdsJoined()
                    gid = kr22.getGroupIdsJoined()
                    gid = kr23.getGroupIdsJoined()
                    gid = kr24.getGroupIdsJoined()
                    gid = kr25.getGroupIdsJoined()
                    for i in gid:
                        kr1.sendText(i,"Bye~Bye " + str(ginfo.name) + "\n\nBots Dipaksa Keluar oleh Owner Bots...!!!\nMakasih...!!!")
                        kr1.leaveGroup(i)
                        kr2.leaveGroup(i)
                        kr3.leaveGroup(i)
                        kr4.leaveGroup(i)
                        kr5.leaveGroup(i)
                        kr6.leaveGroup(i)
                        kr7.leaveGroup(i)
                        kr8.leaveGroup(i)
                        kr9.leaveGroup(i)
                        kr10.leaveGroup(i)
                        kr11.leaveGroup(i)
                        kr12.leaveGroup(i)
                        kr13.leaveGroup(i)
                        kr14.leaveGroup(i)
                        kr15.leaveGroup(i)
                        kr16.leaveGroup(i)
                        kr17.leaveGroup(i)
                        kr18.leaveGroup(i)
                        kr19.leaveGroup(i)
                        kr20.leaveGroup(i)
                        kr21.leaveGroup(i)
                        kr22.leaveGroup(i)
                        kr23.leaveGroup(i)
                        kr24.leaveGroup(i)
                        kr25.leaveGroup(i)
                    if wait["lang"] == "JP":
                        kr1.sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nBots Dipaksa Keluar oleh Owner Bots...!!!\nMakasih...!!!")
                    else:
                        kr1.sendText(msg.to,"He declined all invitations")

            elif msg.text in ["Team","Logo"]:
                if msg.from_ in admin:
                    url = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26168676_131451404314083_3952554270011807487_n.jpg?oh=6e90aa78daaf5e06b1078bbf15d5aa0f&oe=5AB9882D"
                    url1 = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26165506_131451400980750_8433498092579272217_n.jpg?oh=c85beaa35a6f5babd638edeaac9bccaa&oe=5AF760B2"
                    url2 = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26168227_131451417647415_680587542176648285_n.jpg?oh=e714a97fec8d8c1e178ab6c0a3ca39cf&oe=5AC96AD3"
                    url3 = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26195387_131462840979606_8781956575640573461_n.jpg?oh=27ba5e875917c20df7dd8916bdd64847&oe=5ABB27F4"
                    url4 = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26111928_131462844312939_2544207656543605714_n.jpg?oh=0fac796564e963d8b573826263bbc6c7&oe=5AFA67A8"
                    url5 = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26219732_131462837646273_1213898565647052451_n.jpg?oh=c5a8bcce115cdab488bde1b8e981e5dd&oe=5AC3A96E"
                    url6 = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26167549_131462897646267_3496884138024907307_n.jpg?oh=edc63b98f790e9bf2cbb57dce7df9b25&oe=5AB0DDF6"
                    url7 = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26111931_131462894312934_151942458148573227_n.jpg?oh=2b0473a6caf4446df430180a47ca3355&oe=5AC37B56"
                    kr1.sendImageWithURL(msg.to, url)
                    kr1.sendImageWithURL(msg.to, url1)
                    kr1.sendImageWithURL(msg.to, url2)
                    kr1.sendImageWithURL(msg.to, url3)
                    kr1.sendImageWithURL(msg.to, url4)
                    kr1.sendImageWithURL(msg.to, url5)
                    kr1.sendImageWithURL(msg.to, url6)
                    kr1.sendImageWithURL(msg.to, url7)
                
            elif msg.text in ["Kibar","kibar"]:
                if msg.from_ in admin:
                    url = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26168676_131451404314083_3952554270011807487_n.jpg?oh=6e90aa78daaf5e06b1078bbf15d5aa0f&oe=5AB9882D"
                    url1 = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26165506_131451400980750_8433498092579272217_n.jpg?oh=c85beaa35a6f5babd638edeaac9bccaa&oe=5AF760B2"
                    url6 = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26167549_131462897646267_3496884138024907307_n.jpg?oh=edc63b98f790e9bf2cbb57dce7df9b25&oe=5AB0DDF6"
                    url7 = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26111931_131462894312934_151942458148573227_n.jpg?oh=2b0473a6caf4446df430180a47ca3355&oe=5AC37B56"
                    kr1.sendImageWithURL(msg.to, url)
                    kr1.sendImageWithURL(msg.to, url1)
                    kr1.sendImageWithURL(msg.to, url6)
                    kr1.sendImageWithURL(msg.to, url7)
#==========================[Kris]===========================
            elif cms(msg.text,["creator","Creator"]):
                msg.contentType = 13
                msg.contentMetadata = {'mid': "u31ef22df7f538df1d74dc7f756ef1a32"}
                kr1.sendMessage(msg)
#==========================[Kris]===========================
            elif "Checkmid: " in msg.text:
                if msg.from_ in admin:
                    saya = msg.text.replace("Checkmid: ","")
                    msg.contentType = 13
                    msg.contentMetadata = {"mid":saya}
                    kr1.sendMessage(msg)
                    contact = kr1.getContact(saya)
                    cu = kr1.channel.getCover(saya)
                    path = str(cu)
                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    try:
                        kr1.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                        kr1.sendText(msg.to,"Profile Picture " + contact.displayName)
                        kr1.sendImageWithURL(msg.to,image)
                        kr1.sendText(msg.to,"Cover " + contact.displayName)
                        kr1.sendImageWithURL(msg.to,path)
                    except:
                        pass
#==========================[Kris]===========================
            elif "Checkid: " in msg.text:
                if msg.from_ in admin:
                    saya = msg.text.replace("Checkid: ","")
                    gid = kr1.getGroupIdsJoined()
                    for i in gid:
                        h = kr1.getGroup(i).id
                        group = kr1.getGroup(i)
                        if h == saya:
                            try:
                                creator = group.creator.mid 
                                msg.contentType = 13
                                msg.contentMetadata = {'mid': creator}
                                md = "Nama Grup :\n" + group.name + "\n\nID Grup :\n" + group.id
                                if group.preventJoinByTicket is False: md += "\n\nKode Url : Diizinkan"
                                else: md += "\n\nKode Url : Diblokir"
                                if group.invitee is None: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : 0 Orang"
                                else: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : " + str(len(group.invitee)) + " Orang"
                                kr1.sendText(msg.to,md)
                                kr1.sendMessage(msg)
                                kr1.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ group.pictureStatus)
                            except:
                                creator = "Error"
#==========================[Kris]===========================
            elif msg.text in ["Friendlist"]:
                if msg.from_ in owner:
                    contactlist = kr1.getAllContactIds()
                    kontak = kr1.getContacts(contactlist)
                    num=1
                    msgs="═════════List Friend═════════"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.displayName)
                        num=(num+1)
                    msgs+="\n═════════List Friend═════════\n\nTotal Friend : %i" % len(kontak)
                    kr1.sendText(msg.to, msgs)
#==========================[Kris]===========================
            elif msg.text in ["Memlist"]:
                if msg.from_ in owner:
                    kontak = kr1.getGroup(msg.to)
                    group = kontak.members
                    num=1
                    msgs="═════════List Member═════════-"
                    for ids in group:
                        msgs+="\n[%i] %s" % (num, ids.displayName)
                        num=(num+1)
                    msgs+="\n═════════List Member═════════\n\nTotal Members : %i" % len(group)
                    kr1.sendText(msg.to, msgs)
#==========================[Kris]===========================
            elif "Friendinfo: " in msg.text:
                if msg.from_ in owner:
                    saya = msg.text.replace('Friendinfo: ','')
                    gid = kr1.getAllContactIds()
                    for i in gid:
                        h = kr1.getContact(i).displayName
                        contact = kr1.getContact(i)
                        cu = kr1.channel.getCover(i)
                        path = str(cu)
                        image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                        if h == saya:
                            kr1.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                            kr1.sendText(msg.to,"Profile Picture " + contact.displayName)
                            kr1.sendImageWithURL(msg.to,image)
                            kr1.sendText(msg.to,"Cover " + contact.displayName)
                            kr1.sendImageWithURL(msg.to,path)
#==========================[Kris]===========================
            elif "Friendpict: " in msg.text:
                if msg.from_ in owner:
                    saya = msg.text.replace('Friendpict: ','')
                    gid = kr1.getAllContactIds()
                    for i in gid:
                        h = kr1.getContact(i).displayName
                        gna = kr1.getContact(i)
                        if h == saya:
                            kr1.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)
#==========================[Kris]===========================
            elif msg.text in ["Friendlistmid"]:
                if msg.from_ in owner:
                    gruplist = kr1.getAllContactIds()
                    kontak = kr1.getContacts(gruplist)
                    num=1
                    msgs="═════════ʆίςϯ ƒɾίεηδʍίδ═════════"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.mid)
                        num=(num+1)
                    msgs+="\n═════════ʆίςϯ ƒɾίεηδʍίδ═════════\n\nTotal Friend : %i" % len(kontak)
                    kr1.sendText(msg.to, msgs)
#==========================[Kris]===========================
            elif msg.text in ["Blocklist"]:
                if msg.from_ in admin:
                    blockedlist = kr1.getBlockedContactIds()
                    kontak = kr1.getContacts(blockedlist)
                    num=1
                    msgs="═════════List Blocked═════════"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.displayName)
                        num=(num+1)
                    msgs+="\n═════════List Blocked═════════\n\nTotal Blocked : %i" % len(kontak)
                    kr1.sendText(msg.to, msgs)
#==========================[Kris]===========================
            elif msg.text in ["Gruplist"]:
                if msg.from_ in admin:
                    gruplist = kr1.getGroupIdsJoined()
                    kontak = kr1.getGroups(gruplist)
                    num=1
                    msgs="═════════List Grup═════════"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.name)
                        num=(num+1)
                    msgs+="\n═════════List Grup═════════\n\nTotal Grup : %i" % len(kontak)
                    kr1.sendText(msg.to, msgs)
#==========================[Kris]===========================
            elif msg.text in ["Gruplistmid"]:
                if msg.from_ in owner:
                    gruplist = kr1.getGroupIdsJoined()
                    kontak = kr1.getGroups(gruplist)
                    num=1
                    msgs="═════════List GrupMid═════════"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.id)
                        num=(num+1)
                    msgs+="\n═════════List GrupMid═════════\n\nTotal Grup : %i" % len(kontak)
                    kr1.sendText(msg.to, msgs)
#==========================[Kris]===========================  
            elif "Grupimage: " in msg.text:
                if msg.from_ in admin:
                    saya = msg.text.replace('Grupimage: ','')
                    gid = kr1.getGroupIdsJoined()
                    for i in gid:
                        h = kr1.getGroup(i).name
                        gna = kr1.getGroup(i)
                        if h == saya:
                            kr1.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)
#==========================[Kris]===========================  
            elif "Grupname" in msg.text:
                if msg.from_ in admin:
                    saya = msg.text.replace('Grupname','')
                    gid = kr1.getGroup(msg.to)
                    kr1.sendText(msg.to, "[Nama Grup : ]\n" + gid.name)
#==========================[Kris]=========================== 
            elif "Grupid" in msg.text:
                if msg.from_ in admin:
                    saya = msg.text.replace('Grupid','')
                    gid = kr1.getGroup(msg.to)
                    kr1.sendText(msg.to, "[ID Grup : ]\n" + gid.id)
#==========================[Kris]===========================      
            elif "Grupinfo: " in msg.text:
                if msg.from_ in admin:
                    saya = msg.text.replace('Grupinfo: ','')
                    gid = kr1.getGroupIdsJoined()
                    for i in gid:
                        h = kr1.getGroup(i).name
                        group = kr1.getGroup(i)
                        if h == saya:
                            try:
                                creator = group.creator.mid 
                                msg.contentType = 13
                                msg.contentMetadata = {'mid': creator}
                                md = "Nama Grup :\n" + group.name + "\n\nID Grup :\n" + group.id
                                if group.preventJoinByTicket is False: md += "\n\nKode Url : Diizinkan"
                                else: md += "\n\nKode Url : Diblokir"
                                if group.invitee is None: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : 0 Orang"
                                else: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : " + str(len(group.invitee)) + " Orang"
                                kr1.sendText(msg.to,md)
                                kr1.sendMessage(msg)
                                kr1.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ group.pictureStatus)
                            except:
                                creator = "Error"
#==========================[Kris]===========================
            elif msg.text in ["Gcreator:inv"]:
                if msg.from_ in admin:
                    ginfo = kr1.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                       kr1.findAndAddContactsByMid(gCreator)
                       kr1.inviteIntoGroup(msg.to,[gCreator])
                       print "success inv gCreator"
                    except:
                       pass
#==========================[Kris]===========================
            elif msg.text in ["Gcreator:kick"]:
                if msg.from_ in admin:
                    ginfo = kr1.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                       kr1.findAndAddContactsByMid(gCreator)
                       kr1.kickoutFromGroup(msg.to,[gCreator])
                       print "success inv gCreator"
                    except:
                       pass 
#==========================[Kris]===========================   
            elif "reinvite" in msg.text.split():
                if msg.from_ in admin:
                    if msg.toType == 2:
                        group = kr1.getGroup(msg.to)
                        if group.invitee is not None:
                            try:
                                grCans = [contact.mid for contact in group.invitee]
                                kr1.findAndAddContactByMid(msg.to, grCans)
                                kr1.cancelGroupInvitation(msg.to, grCans)
                                kr1.inviteIntoGroup(msg.to, grCans)
                            except Exception as error:
                                print error
                        else:
                            if wait["lang"] == "JP":
                                kr1.sendText(msg.to,"No Invited")
                            else:
                                kr1.sendText(msg.to,"Error")
                    else:
                        pass

#==========================[Kris]===========================	
            elif msg.text in ["#aah","#Aah"]:
                if msg.from_ in owner:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "ua7fb5762d5066629323d113e1266e8ca',"}
                    kr1.sendMessage(msg)
                    kr1.sendMessage(msg)
                    kr1.sendMessage(msg)
                    kr1.sendMessage(msg)
                    kr1.sendMessage(msg)
                    kr1.sendMessage(msg)
                    kr1.sendMessage(msg)
                    kr1.sendMessage(msg)
                    kr1.sendMessage(msg)
                    kr1.sendMessage(msg)
                    kr1.sendMessage(msg)
                    kr1.sendMessage(msg)
                    kr1.sendMessage(msg)
                    kr1.sendMessage(msg)
#==========================[Kris]===========================
            elif msg.text.lower() == '###':
                if msg.from_ in owner:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "ua7fb5762d5066629323d113e1266e8ca',"}
                    kr1.sendMessage(msg)    
#==========================[Kris]===========================
            elif "Ban @" in msg.text:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        _name = msg.text.replace("Ban @","")
                        _nametarget = _name.rstrip()
                        gs = kr1.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            kr1.sendText(msg.to,_nametarget + " Not Found")
                        else:
                            for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    kr1.sendText(msg.to,_nametarget + " Succes Add to Blacklist")
                                except:
                                    kr1.sendText(msg.to,"Error")
#==========================[Kris]===========================
            elif "Unban @" in msg.text:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        _name = msg.text.replace("Unban @","")
                        _nametarget = _name.rstrip()
                        gs = kr1.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            kr1.sendText(msg.to,_nametarget + " Not Found")
                        else:
                            for target in targets:
                                try:
                                    del wait["blacklist"][target]
                                    kr1.sendText(msg.to,_nametarget + " Delete From Blacklist")
                                except:
                                    kr1.sendText(msg.to,_nametarget + " Not In Blacklist")
#==========================[Kris]===========================
            elif "Ban:" in msg.text:
                if msg.from_ in admin:
                    nk0 = msg.text.replace("Ban:","")
                    nk1 = nk0.lstrip()
                    nk2 = nk1.replace("","")
                    nk3 = nk2.rstrip()
                    _name = nk3
                    gs = kr1.getGroup(msg.to)
                    targets = []
                    for s in gs.members:
                        if _name in s.displayName:
                            targets.append(s.mid)
                    if targets == []:
                        sendMessage(msg.to,"user does not exist")
                        pass
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                kr1.sendText(msg.to,_name + " Succes Add to Blacklist")
                            except:
                                kr1.sendText(msg.to,"Error")
#==========================[Kris]===========================
            elif "Unban:" in msg.text:
                if msg.from_ in admin:
                    nk0 = msg.text.replace("Unban:","")
                    nk1 = nk0.lstrip()
                    nk2 = nk1.replace("","")
                    nk3 = nk2.rstrip()
                    _name = nk3
                    gs = kr1.getGroup(msg.to)
                    targets = []
                    for s in gs.members:
                        if _name in s.displayName:
                            targets.append(s.mid)
                    if targets == []:
                        sendMessage(msg.to,"user does not exist")
                        pass
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                kr1.sendText(msg.to,_name + " Delete From Blacklist")
                            except:
                                kr1.sendText(msg.to,_name + " Not In Blacklist")
#==========================[Kris]===========================
            elif msg.text in ["Clear"]:
                if msg.from_ in admin:
                    wait["blacklist"] = {}
                    kr1.sendText(msg.to,"Blacklist Telah Dibersihkan")
#==========================[Kris]===========================
            elif msg.text in ["Ban:on"]:
                if msg.from_ in admin:
                    wait["wblacklist"] = True
                    kr1.sendText(msg.to,"Send Contact")
#==========================[Kris]===========================
            elif msg.text in ["Unban:on"]:
                if msg.from_ in admin:
                    wait["dblacklist"] = True
                    kr1.sendText(msg.to,"Send Contact")
#==========================[Kris]===========================
            elif msg.text in ["Banlist"]:
                if msg.from_ in admin:
                    if wait["blacklist"] == {}:
                        kr1.sendText(msg.to,"Tidak Ada Blacklist")
                    else:
                        kr1.sendText(msg.to,"Daftar Banlist")
                        num=1
                        msgs="*Blacklist*"
                        for mi_d in wait["blacklist"]:
                            msgs+="\n[%i] %s" % (num, kr1.getContact(mi_d).displayName)
                            num=(num+1)
                        msgs+="\n*Blacklist*\n\nTotal Blacklist : %i" % len(wait["blacklist"])
                        kr1.sendText(msg.to, msgs)
#==========================[Kris]===========================
            elif msg.text in ["Conban","Contactban","Contact ban"]:
                if msg.from_ in admin:
                    if wait["blacklist"] == {}:
                        kr1.sendText(msg.to,"Tidak Ada Blacklist")
                    else:
                        kr1.sendText(msg.to,"Daftar Blacklist")
                        h = ""
                        for i in wait["blacklist"]:
                            h = kr1.getContact(i)
                            M = Message()
                            M.to = msg.to
                            M.contentType = 13
                            M.contentMetadata = {'mid': i}
                            kr1.sendMessage(M)
#==========================[Kris]===========================
            elif msg.text in ["Midban","Mid ban"]:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        group = kr1.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        num=1
                        cocoa = "══════════List Blacklist═════════"
                        for mm in matched_list:
                            cocoa+="\n[%i] %s" % (num, mm)
                            num=(num+1)
                            cocoa+="\n═════════List Blacklist═════════\n\nTotal Blacklist : %i" % len(matched_list)
                        kr1.sendText(msg.to,cocoa)
#==========================[Kris]===========================
            elif msg.text.lower() == 'scan blacklist':
                if msg.from_ in admin:
                    if msg.toType == 2:
                        group = kr1.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            kr1.sendText(msg.to,"Tidak ada Daftar Blacklist")
                            return
                        for jj in matched_list:
                            try:
                                kr1.kickoutFromGroup(msg.to,[jj])
                                print (msg.to,[jj])
                            except:
                                pass       
#==========================[Kris]===========================
            elif "spamtag @" in msg.text:
                if msg.from_ in owner:
                    _name = msg.text.replace("Kr spamtag @","")
                    _nametarget = _name.rstrip(' ')
                    gs = kr1.getGroup(msg.to)
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            xname = g.displayName
                            xlen = str(len(xname)+1)
                            msg.contentType = 0
                            msg.text = "@"+xname+" "
                            msg.contentMetadata ={"MENTION":'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(g.mid)+'}]}','EMTVER':'4'}
                            kr1.sendMessage(msg)
                            kr1.sendMessage(msg)
                            kr1.sendMessage(msg)
                            kr1.sendMessage(msg)
                            kr1.sendMessage(msg)
                            kr1.sendMessage(msg)
                            kr1.sendMessage(msg)
                            kr1.sendMessage(msg)
                            kr1.sendMessage(msg)
                            kr1.sendMessage(msg)
                            kr1.sendMessage(msg)
                            kr1.sendMessage(msg)
                            kr1.sendMessage(msg)
                            kr1.sendMessage(msg)
                            kr1.sendMessage(msg)
                            kr1.sendMessage(msg)
                            kr1.sendMessage(msg)
                            kr1.sendMessage(msg)
                            kr1.sendMessage(msg)
                            kr1.sendMessage(msg)
                        else:
                            pass
#==========================[Kris]===========================
            elif ("#cium " in msg.text):
                if msg.from_ in owner:
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"] [0] ["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           kr1.kickoutFromGroup(msg.to,[target])
                           #kr1.inviteIntoGroup(msg.to,[target])
                           kr1.cancelGroupInvitation(msg.to,[target])
                       except:
                           kr1.sendText(msg.to,"Error")
                           
            elif ("##Aah " in msg.text):
                if msg.from_ in owner:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"] [0] ["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            msg.contentType = 13
                            msg.contentMetadata = {'mid': "ua7fb5762d5066629323d113e1266e8ca',"}
                            kr1.sendMessage(msg)
                            kr1.kickoutFromGroup(msg.to,[target])
                            #kr1.inviteIntoGroup(msg.to,[target])
                            kr1.cancelGroupInvitation(msg.to,[target])
                        except:
                            kr1.sendText(msg.to,"Error")
                           
                    
#==========================[Kris]===========================
            elif msg.text in ["glist"]: #Melihat List Group
                if msg.from_ in owner:
                    gids = kr1.getGroupIdsJoined()
                    h = ""
                    for i in gids:
                      #####gn = kr1.getGroup(i).name
                      h += "[•]%s Member\n" % (kr1.getGroup(i).name   +"👉"+str(len(kr1.getGroup(i).members)))
                      kr1.sendText(msg.to,"=======[List Group]======\n"+ h +"Total Group :"+str(len(gids)))
                
            elif msg.text in ["glist2"]: 
                if msg.from_ in owner:
                    gid = kr1.getGroupIdsJoined()
                    h = ""
                    for i in gid:
                      h += "[%s]:%s\n" % (kr1.getGroup(i).name,i)
                      kr1.sendText(msg.to,h)
#==========================[Kris]===========================
            elif "#asupka " in msg.text:
                if msg.from_ in owner:
                    gid = msg.text.replace("Kr asupka ","")
                    if gid == "":
                        kr1.sendText(msg.to,"Invalid group id")
                    else:
                        try:
                            kr1.findAndAddContactsByMid(msg.from_)
                            kr1.inviteIntoGroup(gid,[msg.from_])
                            kr1.sendText(msg.to,"succes di invite boss, silahkan masuk...!!")
                        except:
                            kr1.sendText(msg.to,"Mungkin saya tidak di dalaam grup itu")
#==========================[Kris]===========================
            elif "##megs " in msg.text:
                if msg.from_ in owner:
                    gName = msg.text.replace("##megs ","")
                    ap = kr1.getGroups([msg.to])
                    semua = [contact.mid for contact in ap[0].members]
                    nya = ap[0].members
                    for a in nya:
                        Mi_d = str(a.mid)
                        kr1.createGroup(gName, semua)
                        kr1.createGroup(gName, semua)
                        kr1.createGroup(gName, semua)
                        kr1.createGroup(gName, semua)
                        kr1.createGroup(gName, semua)
                        kr1.createGroup(gName, semua)
                        kr1.createGroup(gName, semua)
#==========================[Kris]===========================
            elif "#megs " in msg.text:
                if msg.from_ in owner:
                    gName = msg.text.replace("#megs ","")
                    ap = kr1.getGroups([msg.to])
                    semua = findAndAddContactsByMid(Mi_d)
                    nya = ap[0].members
                    for a in nya:
                        Mi_d = str(a.mid)
                        klis=[kr]
                        team=random.choice(klis)
                        kr1.findAndAddContactsByMid(Mi_d)
                        kr1.createGroup(gName, semua)
                        kr1.createGroup(gName, semua)
                        kr1.createGroup(gName, semua)
                        kr1.createGroup(gName, semua)
                        kr1.createGroup(gName, semua)
                        kr1.createGroup(gName, semua)
                        team.findAndAddContactsByMid(Mi_d)
                        team.createGroup(gName, semua)
                        team.createGroup(gName, semua)
                        team.createGroup(gName, semua)
                        team.createGroup(gName, semua)
                        team.createGroup(gName, semua)
                        team.createGroup(gName, semua)
#==========================[Kris]===========================
            elif "recover" in msg.text:
                if msg.from_ in owner:
                    thisgroup = kr1.getGroups([msg.to])
                    Mids = [contact.mid for contact in thisgroup[0].members]
                    mi_d = Mids[:33]
                    kr1.createGroup("recover", mi_d)
                    kr1.sendText(msg.to,"Success recover")
#==========================[Kris]===========================
            elif msg.text in ["Remove all chat"]:
                if msg.from_ in owner:
                    kr1.removeAllMessages(op.param2)
                    kr1.removeAllMessages(op.param2)
                    kr1.sendText(msg.to,"Removed all chat Finish")
#==========================[Kris]===========================
        if op.type == 17:
            if op.param2 not in admin:
                if op.param2 in Bots or admin:
                    pass
            if wait["protect"] == True:
                if wait["blacklist"][op.param2] == True:
                    try:
                        kr1.kickoutFromGroup(op.param1,[op.param2])
                        G = kr1.getGroup(op.param1)
                        G.preventJoinByTicket = True
                        kr1.updateGroup(G)
                    except:
                        try:
                            kr1.kickoutFromGroup(op.param1,[op.param2])
                            G = kr1.getGroup(op.param1)
                            G.preventJoinByTicket = True
                            kr1.updateGroup(G)
                        except:
                            pass
        if op.type == 19:
            if op.param2 not in admin:
                if op.param2 in Bots or admin:
                    pass
                elif wait["protect"] == True:
                    wait ["blacklist"][op.param2] = True
                    kr1.kickoutFromGroup(op.param1,[op.param2])
                    kr1.inviteIntoGroup(op.param1,[op.param2])
        if op.type == 13:
            if op.param2 not in admin:
                if op.param2 in Bots or admin:
                    pass
                elif wait["inviteprotect"] == True:
                    wait ["blacklist"][op.param2] = True
                    kr1.kickoutFromGroup(op.param1,[op.param2])
                    if op.param2 not in admin:
                        if op.param2 in Bots or admin:
                            pass
                        elif wait["inviteprotect"] == True:
                            wait ["blacklist"][op.param2] = True
                            kr1.cancelGroupInvitation(op.param1,[op.param3])
                            if op.param2 not in admin:
                                if op.param2 in Bots or admin:
                                    pass
                                elif wait["cancelprotect"] == True:
                                    wait ["blacklist"][op.param2] = True
                                    kr1.cancelGroupInvitation(op.param1,[op.param3])
        if op.type == 11:
            if op.param2 not in admin:
                if op.param2 in Bots or admin:
                    pass
                elif wait["linkprotect"] == True:
                    wait ["blacklist"][op.param2] = True
                    G = kr1.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kr1.updateGroup(G)
                    kr1.kickoutFromGroup(op.param1,[op.param2])
        if op.type == 5:
            if wait['autoAdd'] == True:
                if (wait['message'] in [""," ","\n",None]):
                    pass
                else:
                    kr1.sendText(op.param1,str(wait['message']))
        if op.type == 11:
            if wait["linkprotect"] == True:
                if op.param2 not in Bots:
                    G = kr1.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kr1.kickoutFromGroup(op.param1,[op.param2])
                    kr1.updateGroup(G)
       
#------------------------------------------------------------------------------#
        
        if op.type == 59:
            print op
    
    
    except Exception as error:
        print error


while True:
    try:
        Ops = kr1.fetchOps(kr1.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(kr1.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            kr1.Poll.rev = max(kr1.Poll.rev, Op.revision)
            bot(Op)
