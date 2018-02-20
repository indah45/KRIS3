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
from googletrans import Translator

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
kr11.login(token="")#kicker1 ''cab'''
kr11.loginResult()

kr12 = KRIS.LINE()
#kr12.login(qr=True)
kr12.login(token="")#kicker2 
kr12.loginResult()

kr12 = kr11
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
║╠❂➣Cipok
║╠❂➣Gcreator
║╠❂➣time
║╠❂➣Salam1/Salam2
║╠❂➣Creator
║╠❂➣Kalender/waktu
║╠❂➣Gift8
║╠❂➣Gift/Gift1/2/3
║╠❂➣time
║╠❂➣Kapan
║╠❂➣Apakah
║╠❂➣Nah
║╠❂➣Absen
║╠❂➣runtime
║╠❂➣speed
║╠❂➣mode on/off
║╠❂➣key1
║╠❂➣key2
║╠❂➣key3
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
║╠❂➣mymid
║╠❂➣Getcover @
║╠❂➣Myname
║╠❂➣Mybot
║╠❂➣Mybio
║╠❂➣Mypict
║╠❂➣Myvid
║╠❂➣Getmid @
║╠❂➣spam txt/on/jml
║╠❂➣Gurl
║╠❂➣Grup cancel:
║╠❂➣Respoto on/off
║╠❂➣Sambut on/off
║╠❂➣Sambut2 on/off
║╠❂➣Pergi on/off
║╠❂➣Tag on/off
║╠❂➣Tag2 on/off
║╠❂➣contact on/off
║╠❂➣autojoin on/off
║╠❂➣autoleave on/off
║╠❂➣link on/off
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
║╠❂➣Infogrup
║╠❂➣Gruplist
║╠❂➣Friendlist
║╠❂➣Blacklist
║╠❂➣Banlist
║╠❂➣Contact ban
║╠❂➣Midban
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
║╠❂➣Asup/Masuk/Reinvite
║╠❂➣Kabur all
║╠❂➣Kr bye
║╠❂➣cipok/crot (tagall)
║╠❂➣Gbroadcast:
║╠❂➣Cbroadcast:
║╠❂➣Getgrup image
║╠❂➣Urlgrup image
║╠❂➣status
║╠❂➣Ban @
║╠❂➣Unban @
║╠❂➣Ban:
║╠❂➣Unban:
║╠❂➣Clear/Clearban
║╠❂➣Ban:on
║╠❂➣Unban:on
║╠❂➣Banlist
║╠❂➣Conban/Contact ban
║╠❂➣Midban
║╠❂➣scan blacklist
║╠❂➣Bcast
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
║╠❂➣Attack
║╠❂➣Spamcontact @
║╠❂➣Spamtag @
║╠❂➣Kibar
║╠❂➣Kr kemari
║╠❂➣cab
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

KAC=[kr1,kr2,kr3,kr4,kr5,kr6,kr7,kr8,kr9,kr10]
IND=[kr1]
AST=[kr2,kr3,kr4,kr5,kr6,kr7,kr8,kr9,kr10]
KIK=[kr11,kr12]
mid = kr1.getProfile().mid
mid2 = kr2.getProfile().mid
mid3 = kr3.getProfile().mid
mid4 = kr4.getProfile().mid
mid5 = kr5.getProfile().mid
mid6 = kr6.getProfile().mid
mid7 = kr7.getProfile().mid
mid8 = kr8.getProfile().mid
mid9 = kr9.getProfile().mid
mid10 = kr10.getProfile().mid
mid11 = kr11.getProfile().mid
mid12 = kr12.getProfile().mid

Bots=[mid,mid2,mid3,mid4,mid5,mid6,mid7,mid8,mid9,mid10,mid11,mid12]
induk=[mid]
asist=[mid2,mid3,mid4,mid5,mid6,mid7,mid8,mid9,mid10]
satpam=[mid11,mid12]
owner=["u31ef22df7f538df1d74dc7f756ef1a32","u9cc2323f5b84f9df880c33aa9f9e3ae1"]
admin=["u31ef22df7f538df1d74dc7f756ef1a32","u9cc2323f5b84f9df880c33aa9f9e3ae1","uece14c5ae46691f48f03c4fd331c3fd8","uc70b2f7f85d13c96e0f28ded3b3b13d6","ua4f5b3c2ac79b488c70d08112a3097c5","u8a8c4e247a92f3a29c709abd6e2ad30d","u60694eabf6ae04073739b4c95777d04a","ud3065a5bd9cf0d6961d9c046a124761c","uc545f6498513e4c8bc7004920e037ff3","uc06a9b75c93e5b4b726d9d3c9889b699","u9d4b18194ce5b48d86fa27e5fac1d606","u183bff92d294ed24000efe36e8b2c474","u241b9b83d51b93c77c982e8330139cdd","u15d0c7b52ea7731e5245531c2f543d50","u28c833c6d623e47cf130cb32457c6b3b","u0e881fcbda6a0d82974a775f8015f4fe","ue19cf2484197083712939e81005b57a0","u425365a1a944365b986e3034418eee30","ue0afa260c2e038d74587911771a48dc4","udd468875ae063c026e58c4a7a82b4782","ua8b707e4382fc47b4df318c7c9aa1f3e","u7f94f517d3f2d97718f4f49258a7ef7c","ud55745480bb2c5665e6a21df2a68155e","u6908b4803bf3e267cf659ddda91d5fa4","u60335d94c7a3ca3a3c3685f515724145","uc92d7e39d7259174dba7d8028c7ef4b2","uc1ba312554b4ee025039f54ff44c7c7f","ud74066bb0bc042125f6da564f576d683","u7b8ce44a6f9d630388280e817775111f","uf1850996231087975161942c551f3ac9","u412728dbaf91158d3787b7de2aaf5be8","uaa4d57483fe9bc48d6b904dac88d8ef5","u43ee16d1d2a4a38f894f41aabb7b6714","u51fdb21d7eaa491cd792d5316d8ae416",mid,mid2,mid3,mid4,mid5,mid6,mid7,mid8,mid9,mid10,mid11,mid12]##Krisna,kris,
wait = {
    'detectMention':False, 
    'potoMention':False,
    'kickMention':False,
    'invite':{},
    'invite2':{},
    'spam':{},
    'contact':False,
    'autoJoin':False,
    'autoCancel':{"on":False,"members":5},
    'leaveRoom':True,
    'autoAdd':False,
    'message':"""Thx for add\n☆º°˚˚✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰º°˚˚☆""",
    "lang":"JP",
    "comment":"👉ąµţ๏ℓɨЌ€ By C-A_Bot😊\n\n☆º°˚˚✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰º°˚˚☆（＾ω＾）\nąµţ๏ℓɨЌ€ by Kris ⭐👈 »»» http://line.me/ti/p/~krissthea «««",
    "commentOn":False,
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cNames1":"↝↬₡αβ↫↜",
    "cNames2":"↝↬₡αβ↫↜",
    "cNames3":"↝↬₡αβ↫↜",
    "cNames4":"↝↬₡αβ↫↜",
    "cNames5":"↝↬₡αβ↫↜",
    "cNames6":"↝↬₡αβ↫↜",
    "cNames7":"↝↬₡αβ↫↜",
    "cNames8":"↝↬₡αβ↫↜",
    "cNames9":"↝↬₡αβ↫↜",
    "cNames10":"↝↬₡αβ↫↜",
    "Wc":False,
    "Wc2":False,
    "Lv":False,
    "winvite":False,
    "MENTION":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    #"Protect":True,
    #"cancelprotect":True,
    #"inviteprotect":True,
    #"linkprotect":True,
    "QrProtect":True,#<====
    "MProtection":True,
    "Protectguest":True,
    "Protectcancel":True,
    "Protectgr":True,
    "pname":{},
    "pro_name":{},
    "atjointicket":True
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
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
mybackup.displayName = contact.displayName
mybackup.statusMessage = contact.statusMessage
mybackup.pictureStatus = contact.pictureStatus

contact = kr1.getProfile()
backup = kr1.getProfile()
contact = kr2.getProfile()
backup = kr2.getProfile()
contact = kr3.getProfile()
backup = kr3.getProfile()
contact = kr4.getProfile()
backup = kr4.getProfile()
contact = kr5.getProfile()
backup = kr5.getProfile()
contact = kr6.getProfile()
backup = kr6.getProfile()
contact = kr7.getProfile()
backup = kr7.getProfile()
contact = kr8.getProfile()
backup = kr8.getProfile()
contact = kr9.getProfile()
backup = kr9.getProfile()
contact = kr10.getProfile()
backup = kr10.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = kr1.getProfile()
profile = kr1.getProfile()
contact = kr2.getProfile()
profile = kr2.getProfile()
contact = kr3.getProfile()
profile = kr3.getProfile()
contact = kr4.getProfile()
profile = kr4.getProfile()
contact = kr5.getProfile()
profile = kr5.getProfile()
contact = kr6.getProfile()
profile = kr6.getProfile()
contact = kr7.getProfile()
profile = kr7.getProfile()
contact = kr8.getProfile()
profile = kr8.getProfile()
contact = kr9.getProfile()
profile = kr9.getProfile()
contact = kr10.getProfile()
profile = kr10.getProfile()
profile.displayName = contact.displayName
profile.statusMessage = contact.statusMessage
profile.pictureStatus = contact.pictureStatus

mulai = time.time()

url123 = ("https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26229822_136061360519754_2383391381158562768_n.jpg?oh=5b629e008c344ab9120798423a1fe9fe&oe=5ABEC25F")

agent = {'User-Agent' : "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)"}

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

def sendAudio(self, to_, path):
        M = Message(to=to_, text=None, contentType = 3)
        M_id = self.Talk.kr1.sendMessage(0,M).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'audio',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }

        r = self.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        print r
        if r.status_code != 201:
            raise Exception('Upload audio failure.')


def sendAudioWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download audio failure.')
      try:
         self.sendAudio(to_, path)
      except Exception as e:
            raise e
def sendAudioWithURL(self, to_, url):
      path = 'pythonLiness.data'
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download Audio failure.')
      try:
         self.sendAudio(to_, path)
      except Exception as e:
         raise e

def sendVoice(self, to_, path):
        M = Message(to=to_, text=None, contentType = 3)
        M.contentPreview = None
        M_id = self._kr1.sendMessage(0,M).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'voice_message',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'audio',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload voice failure.')
        return True

def sendVideoWithURL(self, to_, url):
      path = 'pythonLines.data'
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download Audio failure.')
      try:
         self.sendVideo(to_, path)
      except Exception as e:
         raise e

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
#==========================[Kris]===========================
        if op.type == 32:
            if wait["Protectcancel"] == True:
                if op.param2 in admin:
                    pass
                else:
                    G = random.choice(KAC).getGroup(op.param1)
                    G.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(G)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    kr11.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr12.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = True
                    random.choice(KAC).updateGroup(X)
                    random.choice(KIK).kickoutFromGroup(op.param1,[op.param2])
                    kr11.leaveGroup(op.param1)
                    kr12.leaveGroup(op.param1)
#==========================[Kris]===========================
        if op.type == 13:
           if wait["MProtection"] == True:
                if op.param2 in admin:
                    pass
                else:
                    random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])
                    random.choice(KAC).sendText(op.param1,"Protectnya aktif boss, Hubungi owner Bots =>line://ti/p/~krissthea for [Pro off] (-_-)")
#==========================[Kris]===========================
        if op.type == 17:
           if wait["Protectguest"] == True:
                if op.param2 in admin:
                    pass
                else:
                    G = random.choice(KAC).getGroup(op.param1)
                    G.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(G)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    kr11.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr12.acceptGroupInvitationByTicket(op.param1,Ti)
                    random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])
                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = True
                    random.choice(KAC).updateGroup(X)
                    random.choice(KIK).kickoutFromGroup(op.param1,[op.param2])
                    kr11.leaveGroup(op.param1)
                    kr12.leaveGroup(op.param1)
#==========================[Kris]===========================
        if op.type == 11:
            if wait["QrProtect"] == True:
                if op.param2 in admin:
                    pass
                else:
                    G = random.choice(KAC).getGroup(op.param1)
                    G.preventJoinByTicket = True
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    kr11.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr12.acceptGroupInvitationByTicket(op.param1,Ti)
                    random.choice(KAC).updateGroup(G)
                    random.choice(KIK).kickoutFromGroup(op.param1,[op.param2])
                    kr11.leaveGroup(op.param1)
                    kr12.leaveGroup(op.param1)
                    
        if op.type == 11:
            if wait["Protectgr"] == True:
                if random.choice(KAC).getGroup(op.param1).preventJoinByTicket == False:
                    if op.param2 in admin:
                        pass
                    else:
                        G = random.choice(KAC).getGroup(op.param1)
                        Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                        kr11.acceptGroupInvitationByTicket(op.param1,Ti)
                        kr12.acceptGroupInvitationByTicket(op.param1,Ti)
                        G = random.choice(KAC).getGroup(op.param1)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        kr11.kickoutFromGroup(op.param1,[op.param2])
                        kr12.kickoutFromGroup(op.param1,[op.param2])
                        kr11.leaveGroup(op.param1)
                        kr12.leaveGroup(op.param1)
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
                                    try:
                                        G = kr5.getGroup(op.param1)
                                    except:
                                        try:
                                            G = kr6.getGroup(op.param1)
                                        except:
                                            try:
                                                G = kr7.getGroup(op.param1)
                                            except:
                                                try:
                                                    G = kr8.getGroup(op.param1)
                                                except:
                                                    try:
                                                        G = kr9.getGroup(op.param1)
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
                                    try:
                                        kr5.updateGroup(G)
                                    except:
                                        try:
                                            kr6.updateGroup(G)
                                        except:
                                            try:
                                                kr7.updateGroup(G)
                                            except:
                                                try:
                                                    kr8.updateGroup(G)
                                                except:
                                                    try:
                                                        kr9.updateGroup(G)
                                                    except:
                                                        pass
                    if op.param2 in admin:
                        pass
                    else:
                        G = random.choice(KAC).getGroup(op.param1)
                        G.preventJoinByTicket = False
                        random.choice(KAC).updateGroup(G)
                        Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                        kr11.acceptGroupInvitationByTicket(op.param1,Ti)
                        kr12.acceptGroupInvitationByTicket(op.param1,Ti)
                        X = random.choice(KAC).getGroup(op.param1)
                        X.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(X)
                        random.choice(KAC).sendText(op.param1,"please do not change group name-_-")
                        kr11.kickoutFromGroup(op.param1,[op.param2])
                        kr12.kickoutFromGroup(op.param1,[op.param2])
                        kr11.leaveGroup(op.param1)
                        kr12.leaveGroup(op.param1)
#==========================[Kris]===========================
        if op.type == 13:
            print op.param3
            if op.param3 in mid:
                if op.param2 in owner:
                    try:
                        kr1.acceptGroupInvitation(op.param1)
                        G = kr1.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        kr1.updateGroup(G)
                        Ti = kr1.reissueGroupTicket(op.param1)
                        kr2.acceptGroupInvitationByTicket(op.param1,Ti)
                        kr3.acceptGroupInvitationByTicket(op.param1,Ti)
                        kr4.acceptGroupInvitationByTicket(op.param1,Ti)
                        kr5.acceptGroupInvitationByTicket(op.param1,Ti)
                        kr6.acceptGroupInvitationByTicket(op.param1,Ti)
                        kr7.acceptGroupInvitationByTicket(op.param1,Ti)
                        kr8.acceptGroupInvitationByTicket(op.param1,Ti)
                        kr9.acceptGroupInvitationByTicket(op.param1,Ti)
                        kr10.acceptGroupInvitationByTicket(op.param1,Ti)
                        X = kr1.getGroup(op.param1)
                        X.preventJoinByTicket = True
                        kr1.updateGroup(X)
                    except:
                        G = random.choice(KAC).getGroup(op.param1)
                        G.preventJoinByTicket = False
                        random.choice(KAC).updateGroup(G)
                        Ti = random.choice(KAC).reissueGroupTicket(op.param1)
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
                        X = random.choice(KAC).getGroup(op.param1)
                        X.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(X)
#==========================[Kris]===========================   
        if op.type == 13:
            print op.param3
            if op.param3 in mid:
                if op.param2 in owner:
                    kr1.acceptGroupInvitation(op.param1)
            if op.param3 in mid2:
                if op.param2 in owner:
                    kr2.acceptGroupInvitation(op.param1)
            if op.param3 in mid3:
                if op.param2 in owner:
                    kr3.acceptGroupInvitation(op.param1)
            if op.param3 in mid4:
                if op.param2 in owner:
                    kr4.acceptGroupInvitation(op.param1)
            if op.param3 in mid5:
                if op.param2 in owner:
                    kr5.acceptGroupInvitation(op.param1)
            if op.param3 in mid6:
                if op.param2 in owner:
                    kr6.acceptGroupInvitation(op.param1)
            if op.param3 in mid7:
                if op.param2 in owner:
                    kr7.acceptGroupInvitation(op.param1)
            if op.param3 in mid8:
                if op.param2 in owner:
                    kr8.acceptGroupInvitation(op.param1)
            if op.param3 in mid9:
                if op.param2 in owner:
                    kr9.acceptGroupInvitation(op.param1)
            if op.param3 in mid10:
                if op.param2 in owner:
                    kr10.acceptGroupInvitation(op.param1) 
#==========================[Kris]===========================                 
            if op.param3 in mid:
                if op.param2 in mid2:
                    kr1.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
                if op.param2 in mid3:
                    kr1.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
                if op.param2 in mid4:
                    kr1.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
                if op.param2 in mid5:
                    kr1.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
                if op.param2 in mid6:
                    kr1.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
                if op.param2 in mid7:
                    kr1.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
                if op.param2 in mid8:
                    kr1.acceptGroupInvitation(op.param1)       
            if op.param3 in mid:
                if op.param2 in mid9:
                    kr1.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
                if op.param2 in mid10:
                    kr1.acceptGroupInvitation(op.param1)        
#==========================[Kris]===========================
            if op.param3 in mid2:
                if op.param2 in mid:
                    kr2.acceptGroupInvitation(op.param1)
            if op.param3 in mid2:
                if op.param2 in mid3:
                    kr2.acceptGroupInvitation(op.param1)
            if op.param3 in mid2:
                if op.param2 in mid4:
                    kr2.acceptGroupInvitation(op.param1)
            if op.param3 in mid2:
                if op.param2 in mid5:
                    kr2.acceptGroupInvitation(op.param1)
            if op.param3 in mid2:
                if op.param2 in mid6:
                    kr2.acceptGroupInvitation(op.param1)
            if op.param3 in mid2:
                if op.param2 in mid7:
                    kr2.acceptGroupInvitation(op.param1)
            if op.param3 in mid2:
                if op.param2 in mid8:
                    kr2.acceptGroupInvitation(op.param1)
            if op.param3 in mid2:
                if op.param2 in mid9:
                    kr2.acceptGroupInvitation(op.param1)        
            if op.param3 in mid2:
                if op.param2 in mid10:
                    kr2.acceptGroupInvitation(op.param1)     
#==========================[Kris]===========================                
            if op.param3 in mid3:
                if op.param2 in mid:
                    kr3.acceptGroupInvitation(op.param1)
            if op.param3 in mid3:
                if op.param2 in mid2:
                    kr3.acceptGroupInvitation(op.param1)
            if op.param3 in mid3:
                if op.param2 in mid4:
                    kr3.acceptGroupInvitation(op.param1)
            if op.param3 in mid3:
                if op.param2 in mid5:
                    kr3.acceptGroupInvitation(op.param1)
            if op.param3 in mid3:
                if op.param2 in mid6:
                    kr3.acceptGroupInvitation(op.param1)
            if op.param3 in mid3:
                if op.param2 in mid7:
                    kr3.acceptGroupInvitation(op.param1)
            if op.param3 in mid3:
                if op.param2 in mid8:
                    kr3.acceptGroupInvitation(op.param1)
            if op.param3 in mid3:
                if op.param2 in mid9:
                    kr3.acceptGroupInvitation(op.param1)        
            if op.param3 in mid3:
                if op.param2 in mid10:
                    kr3.acceptGroupInvitation(op.param1)        
#==========================[Kris]===========================                      
            if op.param3 in mid4:
                if op.param2 in mid:
                    kr4.acceptGroupInvitation(op.param1)
            if op.param3 in mid4:
                if op.param2 in mid2:
                    kr4.acceptGroupInvitation(op.param1)
            if op.param3 in mid4:
                if op.param2 in mid3:
                    kr4.acceptGroupInvitation(op.param1)
            if op.param3 in mid4:
                if op.param2 in mid5:
                    kr4.acceptGroupInvitation(op.param1)
            if op.param3 in mid4:
                if op.param2 in mid6:
                    kr4.acceptGroupInvitation(op.param1)
            if op.param3 in mid4:
                if op.param2 in mid7:
                    kr4.acceptGroupInvitation(op.param1)
            if op.param3 in mid4:
                if op.param2 in mid8:
                    kr4.acceptGroupInvitation(op.param1)
            if op.param3 in mid4:
                if op.param2 in mid9:
                    kr4.acceptGroupInvitation(op.param1)        
            if op.param3 in mid4:
                if op.param2 in mid10:
                    kr4.acceptGroupInvitation(op.param1)        
#==========================[Kris]===========================                   
            if op.param3 in mid5:
                if op.param2 in mid:
                    kr5.acceptGroupInvitation(op.param1)
            if op.param3 in mid5:
                if op.param2 in mid2:
                    kr5.acceptGroupInvitation(op.param1)
            if op.param3 in mid5:
                if op.param2 in mid3:
                    kr5.acceptGroupInvitation(op.param1)
            if op.param3 in mid5:
                if op.param2 in mid4:
                    kr5.acceptGroupInvitation(op.param1)
            if op.param3 in mid5:
                if op.param2 in mid6:
                    kr5.acceptGroupInvitation(op.param1)
            if op.param3 in mid5:
                if op.param2 in mid7:
                    kr5.acceptGroupInvitation(op.param1)
            if op.param3 in mid5:
                if op.param2 in mid8:
                    kr5.acceptGroupInvitation(op.param1)
            if op.param3 in mid5:
                if op.param2 in mid9:
                    kr5.acceptGroupInvitation(op.param1)   
            if op.param3 in mid5:
                if op.param2 in mid10:
                    kr5.acceptGroupInvitation(op.param1)        
#==========================[Kris]===========================                
            if op.param3 in mid6:
                if op.param2 in mid:
                    kr6.acceptGroupInvitation(op.param1)
            if op.param3 in mid6:
                if op.param2 in mid2:
                    kr6.acceptGroupInvitation(op.param1)
            if op.param3 in mid6:
                if op.param2 in mid3:
                    kr6.acceptGroupInvitation(op.param1)
            if op.param3 in mid6:
                if op.param2 in mid4:
                    kr6.acceptGroupInvitation(op.param1)
            if op.param3 in mid6:
                if op.param2 in mid5:
                    kr6.acceptGroupInvitation(op.param1)
            if op.param3 in mid6:
                if op.param2 in mid7:
                    kr6.acceptGroupInvitation(op.param1)
            if op.param3 in mid6:
                if op.param2 in mid8:
                    kr6.acceptGroupInvitation(op.param1)
            if op.param3 in mid6:
                if op.param2 in mid9:
                    kr6.acceptGroupInvitation(op.param1)   
            if op.param3 in mid6:
                if op.param2 in mid10:
                    kr6.acceptGroupInvitation(op.param1)        
#==========================[Kris]===========================
            if op.param3 in mid7:
                if op.param2 in mid:
                    kr7.acceptGroupInvitation(op.param1)
            if op.param3 in mid7:
                if op.param2 in mid2:
                    kr7.acceptGroupInvitation(op.param1)
            if op.param3 in mid7:
                if op.param2 in mid3:
                    kr7.acceptGroupInvitation(op.param1)
            if op.param3 in mid7:
                if op.param2 in mid4:
                    kr7.acceptGroupInvitation(op.param1)
            if op.param3 in mid7:
                if op.param2 in mid5:
                    kr7.acceptGroupInvitation(op.param1)
            if op.param3 in mid7:
                if op.param2 in mid6:
                    kr7.acceptGroupInvitation(op.param1)
            if op.param3 in mid7:
                if op.param2 in mid8:
                    kr7.acceptGroupInvitation(op.param1)
            if op.param3 in mid7:
                if op.param2 in mid9:
                    kr7.acceptGroupInvitation(op.param1)   
            if op.param3 in mid7:
                if op.param2 in mid10:
                    kr7.acceptGroupInvitation(op.param1)        
#==========================[Kris]===========================                           
            if op.param3 in mid8:
                if op.param2 in mid:
                    kr8.acceptGroupInvitation(op.param1)
            if op.param3 in mid8:
                if op.param2 in mid2:
                    kr8.acceptGroupInvitation(op.param1)
            if op.param3 in mid8:
                if op.param2 in mid3:
                    kr8.acceptGroupInvitation(op.param1)
            if op.param3 in mid8:
                if op.param2 in mid4:
                    kr8.acceptGroupInvitation(op.param1)
            if op.param3 in mid8:
                if op.param2 in mid5:
                    kr8.acceptGroupInvitation(op.param1)
            if op.param3 in mid8:
                if op.param2 in mid6:
                    kr8.acceptGroupInvitation(op.param1)
            if op.param3 in mid8:
                if op.param2 in mid7:
                    kr8.acceptGroupInvitation(op.param1)
            if op.param3 in mid8:
                if op.param2 in mid9:
                    kr8.acceptGroupInvitation(op.param1)   
            if op.param3 in mid8:
                if op.param2 in mid10:
                    kr8.acceptGroupInvitation(op.param1)        
#==========================[Kris]===========================                                                   
            if op.param3 in mid9:
                if op.param2 in mid:
                    kr9.acceptGroupInvitation(op.param1)
            if op.param3 in mid9:
                if op.param2 in mid2:
                    kr9.acceptGroupInvitation(op.param1)
            if op.param3 in mid9:
                if op.param2 in mid3:
                    kr9.acceptGroupInvitation(op.param1)
            if op.param3 in mid9:
                if op.param2 in mid4:
                    kr9.acceptGroupInvitation(op.param1)
            if op.param3 in mid9:
                if op.param2 in mid5:
                    kr9.acceptGroupInvitation(op.param1)
            if op.param3 in mid9:
                if op.param2 in mid6:
                    kr9.acceptGroupInvitation(op.param1)
            if op.param3 in mid9:
                if op.param2 in mid7:
                    kr9.acceptGroupInvitation(op.param1)   
            if op.param3 in mid9:
                if op.param2 in mid8:
                    kr9.acceptGroupInvitation(op.param1) 
            if op.param3 in mid9:
                if op.param2 in mid10:
                    kr9.acceptGroupInvitation(op.param1)         
#==========================[Kris]===========================
            if op.param3 in mid10:
                if op.param2 in mid:
                    kr10.acceptGroupInvitation(op.param1)
            if op.param3 in mid10:
                if op.param2 in mid2:
                    kr10.acceptGroupInvitation(op.param1)
            if op.param3 in mid10:
                if op.param2 in mid3:
                    kr10.acceptGroupInvitation(op.param1)
            if op.param3 in mid10:
                if op.param2 in mid4:
                    kr10.acceptGroupInvitation(op.param1)
            if op.param3 in mid10:
                if op.param2 in mid5:
                    kr10.acceptGroupInvitation(op.param1)
            if op.param3 in mid10:
                if op.param2 in mid6:
                    kr10.acceptGroupInvitation(op.param1)
            if op.param3 in mid10:
                if op.param2 in mid7:
                    kr10.acceptGroupInvitation(op.param1)   
            if op.param3 in mid10:
                if op.param2 in mid8:
                    kr10.acceptGroupInvitation(op.param1) 
            if op.param3 in mid10:
                if op.param2 in mid9:
                    kr10.acceptGroupInvitation(op.param1)          
#==========================[Kris]=========================== 
        if op.type == 13:
            if mid in op.param3:
                if op.param2 not in admin:
                    kr1.rejectGroupInvitation(op.param1)
                
            if mid2 in op.param3:
                if op.param2 not in admin:
                    kr2.rejectGroupInvitation(op.param1)
                            
            if mid3 in op.param3:
                if op.param2 not in admin:
                    kr3.rejectGroupInvitation(op.param1)
                            
            if mid4 in op.param3:
                if op.param2 not in admin:
                    kr4.rejectGroupInvitation(op.param1)
                            
            if mid5 in op.param3:
                if op.param2 not in admin:
                    kr5.rejectGroupInvitation(op.param1)
                        
            if mid6 in op.param3:
                if op.param2 not in admin:
                    kr6.rejectGroupInvitation(op.param1)
                            
            if mid7 in op.param3:
                if op.param2 not in admin:
                    kr7.rejectGroupInvitation(op.param1)
                            
            if mid8 in op.param3:
                if op.param2 not in admin:
                    kr8.rejectGroupInvitation(op.param1)
                            
            if mid9 in op.param3:
                if op.param2 not in admin:
                    kr9.rejectGroupInvitation(op.param1)
                            
            if mid10 in op.param3:
                if op.param2 not in admin:
                    kr10.rejectGroupInvitation(op.param1)
#==========================[Kris]===========================
        if op.type == 19:
            if mid in op.param3:
                if op.param2 in admin:
                    G = kr2.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    kr2.updateGroup(G)
                    Ti = kr2.reissueGroupTicket(op.param1)
                    kr1.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kr1.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kr1.updateGroup(X)
                else:    
                    G = kr2.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    kr2.updateGroup(G)
                    Ti = kr2.reissueGroupTicket(op.param1)
                    kr11.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr1.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kr1.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kr1.updateGroup(X)
                    kr11.kickoutFromGroup(op.param1,[op.param2])
                    kr11.leaveGroup(op.param1)
#==========================[Kris]===========================
            if mid2 in op.param3:
                if op.param2 in admin:
                    G = kr3.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    kr3.updateGroup(G)
                    Ti = kr3.reissueGroupTicket(op.param1)
                    kr2.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kr2.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kr2.updateGroup(X)
                else:
                    G = kr3.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    kr3.updateGroup(G)
                    Ti = kr3.reissueGroupTicket(op.param1)
                    kr12.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr2.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kr2.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kr2.updateGroup(X)
                    kr12.kickoutFromGroup(op.param1,[op.param2])
                    kr12.leaveGroup(op.param1)
#==========================[Kris]===========================
            if mid3 in op.param3:
                if op.param2 in admin:
                    G = kr4.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    kr4.updateGroup(G)
                    Ti = kr4.reissueGroupTicket(op.param1)
                    kr3.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kr3.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kr3.updateGroup(X)
                else:
                    G = kr4.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    kr4.updateGroup(G)
                    Ti = kr4.reissueGroupTicket(op.param1)
                    kr11.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr3.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kr3.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kr3.updateGroup(X)
                    kr11.kickoutFromGroup(op.param1,[op.param2])
                    kr11.leaveGroup(op.param1)
#==========================[Kris]===========================
            if mid4 in op.param3:
                if op.param2 in admin:
                    G = kr5.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    kr5.updateGroup(G)
                    Ti = kr5.reissueGroupTicket(op.param1)
                    kr4.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kr4.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kr4.updateGroup(X)
                else:
                    G = kr5.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    kr5.updateGroup(G)
                    Ti = kr5.reissueGroupTicket(op.param1)
                    kr4.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr12.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kr4.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kr4.updateGroup(X)
                    kr12.kickoutFromGroup(op.param1,[op.param2])
                    kr12.leaveGroup(op.param1)
#==========================[Kris]===========================
            if mid5 in op.param3:
                if op.param2 in admin:
                    G = kr6.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    kr6.updateGroup(G)
                    Ti = kr6.reissueGroupTicket(op.param1)
                    kr5.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kr5.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kr5.updateGroup(X)
                else:
                    G = kr6.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    kr6.updateGroup(G)
                    Ti = kr6.reissueGroupTicket(op.param1)
                    kr5.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr11.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kr5.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kr5.updateGroup(X)
                    kr11.kickoutFromGroup(op.param1,[op.param2])
                    kr11.leaveGroup(op.param1)
#==========================[Kris]===========================
            if mid6 in op.param3:
                if op.param2 in admin:
                    G = kr7.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    kr7.updateGroup(G)
                    Ti = kr7.reissueGroupTicket(op.param1)
                    kr6.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kr6.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kr6.updateGroup(X)
                else:
                    G = kr7.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    kr7.updateGroup(G)
                    Ti = kr7.reissueGroupTicket(op.param1)
                    kr6.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr12.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kr6.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kr6.updateGroup(X)
                    kr12.kickoutFromGroup(op.param1,[op.param2])
                    kr12.leaveGroup(op.param1)
#==========================[Kris]===========================
            if mid7 in op.param3:
                if op.param2 in admin:
                    G = kr8.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    kr8.updateGroup(G)
                    Ti = kr8.reissueGroupTicket(op.param1)
                    kr7.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kr7.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kr7.updateGroup(X)
                else:
                    G = kr8.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    kr8.updateGroup(G)
                    Ti = kr8.reissueGroupTicket(op.param1)
                    kr7.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr11.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kr7.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kr7.updateGroup(X)
                    kr11.kickoutFromGroup(op.param1,[op.param2])
                    kr11.leaveGroup(op.param1)
#==========================[Kris]===========================
            if mid8 in op.param3:
                if op.param2 in admin:
                    G = kr9.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    kr9.updateGroup(G)
                    Ti = kr9.reissueGroupTicket(op.param1)
                    kr8.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kr8.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kr8.updateGroup(X)
                else:
                    G = kr9.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    kr9.updateGroup(G)
                    Ti = kr9.reissueGroupTicket(op.param1)
                    kr8.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr12.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kr8.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kr8.updateGroup(X)
                    kr12.kickoutFromGroup(op.param1,[op.param2])
                    kr12.leaveGroup(op.param1)
#==========================[Kris]===========================
            if mid9 in op.param3:
                if op.param2 in admin:
                    G = kr10.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    kr10.updateGroup(G)
                    Ti = kr10.reissueGroupTicket(op.param1)
                    kr9.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kr9.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kr9.updateGroup(X)
                else:
                    G = kr10.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    kr10.updateGroup(G)
                    Ti = kr10.reissueGroupTicket(op.param1)
                    kr9.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr11.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kr9.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kr9.updateGroup(X)
                    kr11.kickoutFromGroup(op.param1,[op.param2])
                    kr11.leaveGroup(op.param1)
#==========================[Kris]===========================
            if mid10 in op.param3:
                if op.param2 in admin:
                    G = kr1.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    kr1.updateGroup(G)
                    Ti = kr1.reissueGroupTicket(op.param1)
                    kr10.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kr10.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kr10.updateGroup(X)
                else:
                    G = kr1.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    kr1.updateGroup(G)
                    Ti = kr1.reissueGroupTicket(op.param1)
                    kr10.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr12.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kr10.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kr10.updateGroup(X)
                    kr12.kickoutFromGroup(op.param1,[op.param2])
                    kr12.leaveGroup(op.param1)
#==========================[Kris]===========================
        if op.type == 19:
            if op.param3 not in admin:
                if op.param2 in admin:
                    pass
                if op.param2 not in admin:
                    G = random.choice(KAC).getGroup(op.param1)
                    G.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(G)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    kr11.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr12.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = True
                    random.choice(KAC).updateGroup(X)
                    random.choice(KIK).kickoutFromGroup(op.param1,[op.param2])
                    kr11.leaveGroup(op.param1)
                    kr12.leaveGroup(op.param1)
        if op.type == 19:
            if op.param3 in owner:
                if op.param2 not in admin:
                    G = random.choice(KAC).getGroup(op.param1)
                    G.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(G)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    kr11.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr12.acceptGroupInvitationByTicket(op.param1,Ti)
                    random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = True
                    random.choice(KAC).updateGroup(X)
                    random.choice(KIK).kickoutFromGroup(op.param1,[op.param2])
                    kr11.leaveGroup(op.param1)
                    kr12.leaveGroup(op.param1)
                else:
                    random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
#==========================[Kris]===========================  
        if op.type == 19:
            if mid in op.param3:
                if op.param2 in admin:
                    pass
                else:
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
#==========================[Kris]===========================
        if op.type == 26:
            msg = op.message

            if "MENTION" in msg.contentMetadata.keys() != None:
                if wait['detectMention'] == True:
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
                            break            
#==========================[Kris]===========================
            if "MENTION" in msg.contentMetadata.keys() != None:
                if wait['potoMention'] == True:
                    contact = kr1.getContact(msg.from_)
                    cName = contact.pictureStatus
                    balas = ["http://dl.profile.line-cdn.net/" + cName]
                    ret_ = random.choice(balas)
                    mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                    mentionees = mention["MENTIONEES"]
                    for mention in mentionees:
                        if mention["M"] in Bots:
                            kr1.sendImageWithURL(msg.to,ret_)
                            break  
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
            elif msg.text.lower() == 'key1':
                if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        kr1.sendText(msg.to,helpself)
                    else:
                        kr1.sendText(msg.to,helpself)
#==========================[Kris]===========================
            elif msg.text.lower() == 'key2':
                if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        kr1.sendText(msg.to,helpgrup)
                    else:
                        kr1.sendText(msg.to,helpgrup)
#==========================[Kris]===========================
            elif msg.text.lower() == 'key3':
                if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        kr1.sendText(msg.to,helprhs)
                    else:
                        kr1.sendText(msg.to,helprhs)
#==========================[Kris]===========================
            elif msg.text in ["Sp","Speed","speed","sp"]:
                if msg.from_ in admin:
                    start = time.time()
                    kr1.sendText(msg.to, "❂➣Proses.....")
                    elapsed_time = time.time() - start
                    kr1.sendText(msg.to, "%sseconds" % (elapsed_time))
#==========================[Kris]===========================
            elif msg.text.lower() == 'crash':
                if msg.from_ in admin:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u1f41296217e740650e0448b96851a3e2',"}
                    kr1.sendMessage(msg)
                    kr1.sendMessage(msg)
                    kr2.sendMessage(msg)
                    kr2.sendMessage(msg)
#==========================[Kris]===========================
            elif msg.text.lower() == 'me':
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}
                kr1.sendMessage(msg)
#==========================[Kris]===========================
            elif msg.text.lower() == 'bot':
                if msg.from_ in admin:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': mid}
                    kr1.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': mid2}
                    kr2.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': mid3}
                    kr3.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': mid4}
                    kr4.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': mid5}
                    kr5.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': mid6}
                    kr6.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': mid7}
                    kr7.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': mid8}
                    kr8.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': mid9}
                    kr9.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': mid10}
                    kr10.sendMessage(msg)
                    random.choice(KAC).sendImageWithURL(msg.to, url123)
                    random.choice(KAC).sendText(msg.to,"↥↥↥↥↥↪ Owner Bots ↩↥↥↥↥↥")
#==========================[Kris]===========================
            elif msg.text.lower() == 'mode on':
                if msg.from_ in admin:
                    #wait["Protect"] = True
                    #wait["linkprotect"] = True
                    #wait["inviteprotect"] = True
                    #wait["cancelprotect"] = True
                    wait["QrProtect"] = True#<=====
                    wait["MProtection"] = True
                    wait["Protectcancel"] = True
                    wait["Protectguest"] = True
                    wait["Protectgr"] = True
                    wait['pname'][msg.to] = True
                    wait['pro_name'][msg.to] = kr1.getGroup(msg.to).name
                    if wait["lang"] == "JP":
                        kr1.sendText(msg.to,"All Protect On")
                else:
                    kr1.sendText(msg.to,"Perintah di tolak, Khusus admin/owner")
#==========================[Kris]===========================
            elif msg.text.lower() == 'mode off':
                if msg.from_ in admin:
                    #wait["Protect"] == False
                    #wait["linkprotect"] == False
                    #wait["inviteprotect"] == False
                    #wait["cancelprotect"] == False
                    wait["QrProtect"] = False#<===
                    wait["MProtection"] = False
                    wait["Protectcancel"] = False
                    wait["Protectguest"] = False
                    wait["Protectgr"] = False
                    wait['pname'][msg.to] = False
                    if wait["lang"] == "JP":
                        kr1.sendText(msg.to,"All Protect Off")
                else:
                    kr1.sendText(msg.to,"Perintah di tolak, Khusus admin/owner")
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
                    if wait['MProtection'] == True: md+="╠❂➣MProtection:on [✅]\n"
                    else: md+="╠❂➣MProtection:off [❌]\n"
                    if wait['Protectguest'] == True: md+="╠❂➣Protectguest:on [✅]\n"
                    else: md+="╠❂➣Protectguest:off [❌]\n"
                    if wait['Protectcancel'] == True: md+="╠❂➣Protectcancel:on [✅]\n"
                    else: md+="╠❂➣Protectcancel:off [❌]\n"
                    if wait['Protectgr'] == True: md+="╠❂➣Protectgr:on [✅]\n"
                    else: md+="╠❂➣Protectgr:off [❌]\n"
                    #if wait["Protect"] == True: md+="╠❂➣Protect:on [✅]\n"
                    #else:md+="╠❂➣Protect:off [❌]\n"
                    #if wait["linkprotect"] == True: md+="╠❂➣Link Protect:on [✅]\n"
                    #else:md+="╠❂➣Link Protect:off [❌]\n"
                    #if wait["inviteprotect"] == True: md+="╠❂➣Invitation Protect:on [✅]\n"
                    #else:md+="╠❂➣Invitation Protect:off [❌]\n"
                    #if wait["cancelprotect"] == True: md+="╠❂➣Cancel Protect:on [✅]\n"
                    #else:md+="╠❂➣Cancel Protect:off [❌]\n╚═════════════"
                    if wait["QrProtect"] == True: md+="╠❂➣QrProtect:on [✅]\n"
                    else:md+="╠❂➣QrProtect:off [❌]\n╚═════════════"
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
            elif "Spamcontact @" in msg.text:
                if msg.from_ in owner:
                    _name = msg.text.replace("Spamcontact @","")
                    _nametarget = _name.rstrip(' ')
                    gs = kr1.getGroup(msg.to)
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            kr1.sendText(msg.to, "Spam di Proses....!!!")
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
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr2.sendText(g.mid,'spam')
                            kr1.sendText(msg.to, "Selesai di Spam")
                            kr2.sendText(msg.to, "Selesai di Spam")
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
            elif msg.text in ["Tag on","tag on"]:
                if msg.from_ in admin:
                    wait['detectMention'] = True
                    kr1.sendText(msg.to,"Auto respon tag On")
#==========================[Kris]===========================
            elif msg.text in ["Tag off","tag off"]:
                if msg.from_ in admin:
                    wait['detectMention'] = False
                    kr1.sendText(msg.to,"Auto respon tag Off")
#==========================[Kris]===========================
            elif msg.text in ["Respoto on","respoto on"]:
                if msg.from_ in admin:
                    wait['potoMention'] = True
                    kr1.sendText(msg.to,"Auto respon tag poto On")
#==========================[Kris]===========================   
            elif msg.text in ["Respoto off","respoto off"]:
                if msg.from_ in admin:
                    wait['potoMention'] = False
                    kr1.sendText(msg.to,"Auto respon tag poto Off")
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
            elif '/ti/g/' in msg.text.lower():
                link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                links = link_re.findall(msg.text)
                n_links=[]
                for l in links:
                    if l not in n_links:
                        n_links.append(l)
                for ticket_id in n_links:
                    if wait["atjointicket"] == True:
                        group=kr1.findGroupByTicket(ticket_id)
                        group=kr2.findGroupByTicket(ticket_id)
                        group=kr3.findGroupByTicket(ticket_id)
                        group=kr4.findGroupByTicket(ticket_id)
                        group=kr5.findGroupByTicket(ticket_id)
                        group=kr6.findGroupByTicket(ticket_id)
                        group=kr7.findGroupByTicket(ticket_id)
                        group=kr8.findGroupByTicket(ticket_id)
                        group=kr9.findGroupByTicket(ticket_id)
                        group=kr10.findGroupByTicket(ticket_id)
                        kr1.acceptGroupInvitationByTicket(group.mid,ticket_id)
                        kr2.acceptGroupInvitationByTicket(group.mid,ticket_id)
                        kr3.acceptGroupInvitationByTicket(group.mid,ticket_id)
                        kr4.acceptGroupInvitationByTicket(group.mid,ticket_id)
                        kr5.acceptGroupInvitationByTicket(group.mid,ticket_id)
                        kr6.acceptGroupInvitationByTicket(group.mid,ticket_id)
                        kr7.acceptGroupInvitationByTicket(group.mid,ticket_id)
                        kr8.acceptGroupInvitationByTicket(group.mid,ticket_id)
                        kr9.acceptGroupInvitationByTicket(group.mid,ticket_id)
                        kr10.acceptGroupInvitationByTicket(group.mid,ticket_id)
#==========================[Kris]===========================
#            elif msg.text in ["Pro on","pro on"]:
#                if msg.from_ in admin:
#                    if wait["Protectmem"] == True:
#                        if wait["lang"] == "JP":
#                            kr1.sendText(msg.to,"Protect join on")
#                    else:
#                        wait["Protectmem"] = True
#                        if wait["lang"] == "JP":
#                            kr1.sendText(msg.to,"already on")
#            elif msg.text in ["Pro off","pro off"]:
#                if msg.from_ in admin:
#                    if wait["Protectmem"] == False:
#                        if wait["lang"] == "JP":
#                            kr1.sendText(msg.to,"Protect joιn oғғ")
#                    else:
#                        wait["Protectmem"] = False
#                        if wait["lang"] == "JP":
#                            kr1.sendText(msg.to,"already oғғ")
#==========================[Kris]===========================
            elif msg.text in ["Sambut on","sambut on"]:
                if msg.from_ in admin:
                    if wait["Wc"] == True:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"noтιғ yg joιn on")
                    else:
                        wait["Wc"] = True
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"already on")
            elif msg.text in ["Sambut off","sambut off"]:
                if msg.from_ in admin:
                    if wait["Wc"] == False:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"noтιғ yg joιn oғғ")
                    else:
                        wait["Wc"] = False
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"already oғғ")
#==========================[Kris]===========================
            elif msg.text in ["Sambut2 on","sambut2 on"]:
                if msg.from_ in admin:
                    if wait["Wc2"] == True:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"noтιғ yg joιn poto on")
                    else:
                        wait["Wc2"] = True
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"already on")
            elif msg.text in ["Sambut2 off","sambut2 off"]:
                if msg.from_ in admin:
                    if wait["Wc2"] == False:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"noтιғ yg joιn poto oғғ")
                    else:
                        wait["Wc2"] = False
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"already oғғ")
#==========================[Kris]===========================
            elif msg.text in ["Pergi on","pergi on"]:
                if msg.from_ in admin:
                    if wait["Lv"] == True:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"noтιғ yg leave on")
                    else:
                        wait["Lv"] = True
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"already on")
            elif msg.text in ["Pergi off","pergi off"]:
                if msg.from_ in admin:
                    if wait["Lv"] == False:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"noтιғ yg leave oғғ")
                    else:
                        wait["Lv"] = False
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"already oғғ")
#==========================[Kris]===========================
            elif "Dadas" in msg.text:
                if msg.from_ in owner:
                    if msg.toType == 2:
                        if msg.toType == 2:
                            print "ok"
                            _name = msg.text.replace("Dadas","")
                            gs = kr1.getGroup(msg.to)
                            gs = kr2.getGroup(msg.to)
                            gs = kr3.getGroup(msg.to)
                            gs = kr4.getGroup(msg.to)
                            gs = kr5.getGroup(msg.to)
                            gs = kr6.getGroup(msg.to)
                            gs = kr7.getGroup(msg.to)
                            gs = kr8.getGroup(msg.to)
                            gs = kr9.getGroup(msg.to)
                            kr1.sendText(msg.to,"Jangan panik, santai aja ya ô")
                            kr2.sendText(msg.to,"Group di bersihkan...!!")
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
            elif msg.text in ["Salam1"]:
                kr1.sendText(msg.to,"السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                kr2.sendText(msg.to,"Assalamu'alaikum")
            elif msg.text in ["Salam2"]:
                kr1.sendText(msg.to,"وَعَلَيْكُمْ السَّلاَمُرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                kr2.sendText(msg.to,"Wa'alaikumsallam.Wr,Wb")
            elif msg.text in ["Salam3"]:
                if msg.from_ in owner:
                    kr1.sendText(msg.to,"السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                    kr2.sendText(msg.to,"Assalamu'alaikum")
                    kr3.sendText(msg.to,"وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِوَبَرَكَاتُهُ")
                    kr4.sendText(msg.to,"Wa'alaikumsallam.Wr,Wb")
                    if msg.toType == 2:
                        print "ok"
                        _name = msg.text.replace("Salam3","")
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
            elif "Tajong " in msg.text:
                if msg.from_ in admin:
                    nk0 = msg.text.replace("Tajong ","")
                    nk1 = nk0.lstrip()
                    nk2 = nk1.replace("@","")
                    nk3 = nk2.rstrip()
                    _name = nk3
                    gs = kr1.getGroup(msg.to)
                    ginfo = kr1.getGroup(msg.to)
                    gs.preventJoinByTicket = False
                    kr1.updateGroup(gs)
                    invsend = 0
                    Ticket = kr1.reissueGroupTicket(msg.to)
                    kr11.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.01)
                    kr12.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.01)
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
                                random.choice(KIK).kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                kr11.leaveGroup(msg.to)
                                kr12.leaveGroup(msg.to)
                                gs = kr1.getGroup(msg.to)
                                gs.preventJoinByTicket = True
                                kr1.updateGroup(gs)
                                gs.preventJoinByTicket(gs)
                                kr1.updateGroup(gs)
#==========================[Kris]===========================
            elif ("Kick " in msg.text):
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
            elif ("Cium " in msg.text):
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
#==========================[Kris]===========================
            elif "Kick: " in msg.text:
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
                if msg.from_ in admin:
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
            elif msg.text in ["Reinvite","reinvite"]: #Panggil Semua Bot
                if msg.from_ in owner:
                    try:
                        X = kr1.getGroup(msg.to)
                        ginfo = kr1.getGroup(msg.to)
                        X.preventJoinByTicket = False
                        kr1.updateGroup(X)
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
                        G = kr1.getGroup(msg.to)
                        ginfo = kr1.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        kr1.updateGroup(G)
                        print "Semua Sudah Lengkap"
                    except:
                        try:
                            X = kr2.getGroup(msg.to)
                            ginfo = kr2.getGroup(msg.to)
                            X.preventJoinByTicket = False
                            kr2.updateGroup(X)
                            invsend = 0
                            Ticket = kr2.reissueGroupTicket(msg.to)
                            kr1.acceptGroupInvitationByTicket(msg.to,Ticket)
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
                            G = kr2.getGroup(msg.to)
                            ginfo = kr2.getGroup(msg.to)
                            G.preventJoinByTicket = True
                            kr2.updateGroup(G)
                            print "Semua Sudah Lengkap"
                        except:
                            try:
                                X = kr3.getGroup(msg.to)
                                ginfo = kr3.getGroup(msg.to)
                                X.preventJoinByTicket = False
                                kr3.updateGroup(X)
                                invsend = 0
                                Ticket = kr3.reissueGroupTicket(msg.to)
                                kr1.acceptGroupInvitationByTicket(msg.to,Ticket)
                                time.sleep(0.01)
                                kr2.acceptGroupInvitationByTicket(msg.to,Ticket)
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
                                G = kr3.getGroup(msg.to)
                                ginfo = kr3.getGroup(msg.to)
                                G.preventJoinByTicket = True
                                kr3.updateGroup(G)
                                print "Semua Sudah Lengkap"
                            except:
                                pass
#==========================[Kris]=========================== 
            elif msg.text in ["Masuk","masuk"]: #Panggil Semua Bot
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
                    kr1.findAndAddContactsByMid(midd2)
                    kr1.inviteIntoGroup(msg.to,[midd2])
                    kr2.acceptGroupInvitation(msg.to)
                    
                    G = kr2.getGroup(msg.to)
                    ginfo = kr2.getGroup(msg.to)
                    midd3 = msg.text.replace("..","uad6cb020c5ca7afbecb4681675eb38cd")
                    kr2.findAndAddContactsByMid(midd3)
                    kr2.inviteIntoGroup(msg.to,[midd3])
                    kr3.acceptGroupInvitation(msg.to)
                    
                    G = kr3.getGroup(msg.to)
                    ginfo = kr3.getGroup(msg.to)
                    midd4 = msg.text.replace("..","ud5262649376cbf7576e2dcac0331d481")
                    kr3.findAndAddContactsByMid(midd4)
                    kr3.inviteIntoGroup(msg.to,[midd4])
                    kr4.acceptGroupInvitation(msg.to)
                    
                    G = kr4.getGroup(msg.to)
                    ginfo = kr4.getGroup(msg.to)
                    midd5 = msg.text.replace("..","u53c352134325f0c49e86534c57801bd7")
                    kr4.findAndAddContactsByMid(midd5)
                    kr4.inviteIntoGroup(msg.to,[midd5])
                    kr5.acceptGroupInvitation(msg.to)
                    
                    G = kr5.getGroup(msg.to)
                    ginfo = kr5.getGroup(msg.to)
                    midd6 = msg.text.replace("..","ua2ea9f4c32848bc67644c5267bb91279")
                    kr5.findAndAddContactsByMid(midd6)
                    kr5.inviteIntoGroup(msg.to,[midd6])
                    kr6.acceptGroupInvitation(msg.to)
                    
                    G = kr6.getGroup(msg.to)
                    ginfo = kr6.getGroup(msg.to)
                    midd7 = msg.text.replace("..","uadfd3a23698b71d17c64482d27dc2ed1")
                    kr6.findAndAddContactsByMid(midd7)
                    kr6.inviteIntoGroup(msg.to,[midd7])
                    kr7.acceptGroupInvitation(msg.to)
                    
                    G = kr7.getGroup(msg.to)
                    ginfo = kr7.getGroup(msg.to)
                    midd8 = msg.text.replace("..","u45c6ce403f0acc28392c519028aae154")
                    kr7.findAndAddContactsByMid(midd8)
                    kr7.inviteIntoGroup(msg.to,[midd8])
                    kr8.acceptGroupInvitation(msg.to)
                    
                    G = kr8.getGroup(msg.to)
                    ginfo = kr8.getGroup(msg.to)
                    midd9 = msg.text.replace("..","udcf44c4272d8209a8a5f2dd1afeea93f")
                    kr8.findAndAddContactsByMid(midd9)
                    kr8.inviteIntoGroup(msg.to,[midd9])
                    kr9.acceptGroupInvitation(msg.to)
                    
                    G = kr9.getGroup(msg.to)
                    ginfo = kr9.getGroup(msg.to)
                    midd10 = msg.text.replace("..","u4a0be979fc73e88ebfe915bc917237b8")
                    kr9.findAndAddContactsByMid(midd10)
                    kr9.inviteIntoGroup(msg.to,[midd10])
                    kr10.acceptGroupInvitation(msg.to)
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
                    ginfo = kr2.getGroup(msg.to)
                    ginfo = kr3.getGroup(msg.to)
                    ginfo = kr4.getGroup(msg.to)
                    ginfo = kr5.getGroup(msg.to)
                    ginfo = kr6.getGroup(msg.to)
                    ginfo = kr7.getGroup(msg.to)
                    ginfo = kr8.getGroup(msg.to)
                    ginfo = kr9.getGroup(msg.to)
                    ginfo = kr10.getGroup(msg.to)
                    midd1 = msg.text.replace(".","u4a0f653ea757da7abcd41c15bf0f15da")
                    random.choice(KAC).findAndAddContactsByMid(midd1)
                    random.choice(KAC).inviteIntoGroup(msg.to,[midd1])
                    kr1.acceptGroupInvitation(msg.to)
                    print "Induk Sudah Masuk"
                    
            elif msg.text in ["N masuk"]: #Panggil Semua Bot
                if msg.from_ in owner:
                    G = kr1.getGroup(msg.to)
                    ginfo = kr1.getGroup(msg.to)
                    midd = msg.text.replace("N masuk","uc6a6ba43d1ce45e5c78fc7fb37afd17e")
                    kr1.findAndAddContactsByMid(midd)
                    kr1.inviteIntoGroup(msg.to,[midd])
                    print "Mengundang N"
                else:
                    pass
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
                        try:
                            kr10.sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nJangan Lupa Bahagia...!!!")
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
                        
            elif msg.text in ["1bye","1 bye"]:#keluar semua bots
                if msg.from_ in owner:
                    if msg.toType == 2:
                        ginfo = kr1.getGroup(msg.to)
                        try:
                            kr1.sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nJangan Lupa Bahagia...!!!")
                            kr1.leaveGroup(msg.to)
                        except:
                            pass
#==========================[Kris]===========================
            elif msg.text in ["Kr bye"]:#keluar bot kecuali bot induk
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
                        try:
                            kr10.sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nJangan Lupa Bahagia...!!!")
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
            elif "cipok" == msg.text.lower():
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
            elif "crot" == msg.text.lower():
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
#==========================[Kris]=========================== 
            elif "Spam " in msg.text:
                if msg.from_ in admin:
                    txt = msg.text.split(" ")
                    jmlh = int(txt[2])
                    teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                    tulisan = jmlh * (teks+"\n")
                    if txt[1] == "on":
                        if jmlh <= 100000:
                           for x in range(jmlh):
                               kr1.sendText(msg.to, teks)
                        else:
                           kr1.sendText(msg.to, "Out of Range!")
                    elif txt[1] == "off":
                        if jmlh <= 100000:
                            kr1.sendText(msg.to, tulisan)
                        else:
                            kr1.sendText(msg.to, "Out Of Range!")
#==========================[Kris]===========================  
            elif msg.text.lower() == 'mymid':
                if msg.from_ in admin:
                    kr1.sendText(msg.to,msg.from_)
#==========================[Kris]===========================
            elif msg.text.lower() == 'mid bot':
                if msg.from_ in owner:
                    kr1.sendText(msg.to,mid)
                    kr2.sendText(msg.to,mid2)
                    kr3.sendText(msg.to,mid3)
                    kr4.sendText(msg.to,mid4)
                    kr5.sendText(msg.to,mid5)
                    kr6.sendText(msg.to,mid6)
                    kr7.sendText(msg.to,mid7)
                    kr8.sendText(msg.to,mid8)
                    kr9.sendText(msg.to,mid9)
                    kr10.sendText(msg.to,mid10)
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
                    h1 = kr2.getContact(mid2)
                    h2 = kr3.getContact(mid3)
                    h3 = kr4.getContact(mid4)
                    h4 = kr5.getContact(mid5)
                    h5 = kr6.getContact(mid6)
                    h6 = kr7.getContact(mid7)
                    h7 = kr8.getContact(mid8)
                    h8 = kr9.getContact(mid9)
                    h9 = kr10.getContact(mid10)
                    kr1.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
                    kr2.sendText(msg.to,"═══[DisplayName]═══\n" + h1.displayName)
                    kr3.sendText(msg.to,"═══[DisplayName]═══\n" + h2.displayName)
                    kr4.sendText(msg.to,"═══[DisplayName]═══\n" + h3.displayName)
                    kr5.sendText(msg.to,"═══[DisplayName]═══\n" + h4.displayName)
                    kr6.sendText(msg.to,"═══[DisplayName]═══\n" + h5.displayName)
                    kr7.sendText(msg.to,"═══[DisplayName]═══\n" + h6.displayName)
                    kr8.sendText(msg.to,"═══[DisplayName]═══\n" + h7.displayName)
                    kr9.sendText(msg.to,"═══[DisplayName]═══\n" + h8.displayName)
                    kr10.sendText(msg.to,"═══[DisplayName]═══\n" + h9.displayName)
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
#==========================[Kris]===========================
            elif "Getmid @" in msg.text:
                if msg.from_ in admin:
                    _name = msg.text.replace("Getmid @","")
                    _nametarget = _name.rstrip(' ')
                    gs = kr1.getGroup(msg.to)
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            kr1.sendText(msg.to, g.mid)
                        else:
                            pass
            elif "Getinfo" in msg.text:
                if msg.from_ in admin:
                    key = eval(msg.contentMetadata["MENTION"])
                    key1 = key["MENTIONEES"][0]["M"]
                    contact = kr1.getContact(key1)
                    cu = kr1.channel.getCover(key1)
                    try:
                        kr1.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nHeader :\n" + str(cu))
                    except:
                        kr1.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\n" + str(cu))
            elif "Getbio" in msg.text:
                if msg.from_ in admin:
                    key = eval(msg.contentMetadata["MENTION"])
                    key1 = key["MENTIONEES"][0]["M"]
                    contact = kr1.getContact(key1)
                    cu = kr1.channel.getCover(key1)
                    try:
                        kr1.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)
                    except:
                        kr1.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)
            elif "Getname" in msg.text:
                if msg.from_ in admin:
                    key = eval(msg.contentMetadata["MENTION"])
                    key1 = key["MENTIONEES"][0]["M"]
                    contact = kr1.getContact(key1)
                    cu = kr1.channel.getCover(key1)
                    try:
                        kr1.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)
                    except:
                        kr1.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)
            elif "Getprofile" in msg.text:
                if msg.from_ in admin:
                    key = eval(msg.contentMetadata["MENTION"])
                    key1 = key["MENTIONEES"][0]["M"]
                    contact = kr1.getContact(key1)
                    cu = kr1.channel.getCover(key1)
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
            elif "Getcontact" in msg.text:
                if msg.from_ in admin:
                    key = eval(msg.contentMetadata["MENTION"])
                    key1 = key["MENTIONEES"][0]["M"]                
                    mmid = kr1.getContact(key1)
                    msg.contentType = 13
                    msg.contentMetadata = {"mid": key1}
                    kr1.sendMessage(msg)
            elif "Getpict @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]dp executing"
                    _name = msg.text.replace("Getpict @","")
                    _nametarget = _name.rstrip('  ')
                    gs = kr1.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        kr1.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                contact = kr1.getContact(target)
                                path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                kr1.sendImageWithURL(msg.to, path)
                            except Exception as e:
                                raise e
                    print "[Command]dp executed"
            elif "Getvid @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]dp executing"
                    _name = msg.text.replace("Getvid @","")
                    _nametarget = _name.rstrip('  ')
                    gs = kr1.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        kr1.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                contact = kr1.getContact(target)
                                path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                kr1.sendVideoWithURL(msg.to, path)
                            except Exception as e:
                                raise e
                    print "[Command]dp executed"
            elif "Picturl @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]dp executing"
                    _name = msg.text.replace("Picturl @","")
                    _nametarget = _name.rstrip('  ')
                    gs = kr1.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        kr1.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                contact = kr1.getContact(target)
                                path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                kr1.sendText(msg.to, path)
                            except Exception as e:
                                raise e
                    print "[Command]dp executed"
            elif "Getcover @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]cover executing"
                    _name = msg.text.replace("Getcover @","")    
                    _nametarget = _name.rstrip('  ')
                    gs = kr1.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        kr1.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                contact = kr1.getContact(target)
                                cu = kr1.channel.getCover(target)          
                                path = str(cu)
                                kr1.sendImageWithURL(msg.to, path)
                            except Exception as e:
                                raise e
                    print "[Command]cover executed"
            elif "Coverurl @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]cover executing"
                    _name = msg.text.replace("Coverurl @","")    
                    _nametarget = _name.rstrip('  ')
                    gs = kr1.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        kr1.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                contact = kr1.getContact(target)
                                cu = kr1.channel.getCover(target)          
                                path = str(cu)
                                kr1.sendText(msg.to, path)
                            except Exception as e:
                                raise e
                    print "[Command]cover executed"
            elif "Getgrup image" in msg.text:
                if msg.from_ in admin:
                    group = kr1.getGroup(msg.to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    kr1.sendImageWithURL(msg.to,path)
            elif "Urlgrup image" in msg.text:
                if msg.from_ in admin:
                    group = kr1.getGroup(msg.to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    kr1.sendText(msg.to,path)
#==========================[Kris]===========================
            elif msg.text.lower() == 'welcome':
                ginfo = kr1.getGroup(msg.to)
                kr1.sendText(msg.to,"Selamat Datang Di Grup " + str(ginfo.name))
                jawaban1 = ("Selamat Datang Di Grup " + str(ginfo.name))
                kr1.sendText(msg.to,"Owner Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName )
                tts = gTTS(text=jawaban1, lang='id')
                tts.save('tts.mp3')
                kr1.sendAudio(msg.to,'tts.mp3')
#==========================[Kris]===========================
            elif msg.text in ["Absen","absen"]:
                if msg.from_ in admin:
                    kr1.sendText(msg.to,"👉★★★√")
                    kr2.sendText(msg.to,"👉★★★★√")
                    kr3.sendText(msg.to,"👉★★★★★√")
                    kr4.sendText(msg.to,"👉★★★★★★√")
                    kr5.sendText(msg.to,"👉★★★★★★★√")
                    kr6.sendText(msg.to,"👉★★★★★★★★√")
                    kr7.sendText(msg.to,"👉★★★★★★★★★√")
                    kr8.sendText(msg.to,"👉★★★★★★★★★★√")
                    kr9.sendText(msg.to,"👉★★★★★★★★★★★√")
                    kr10.sendText(msg.to,"👉★★★★★★★★★★★★√")
                    kr10.sendText(msg.to,"👉Semua Hadir Boss...!!!\n\n[✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰]")
#==========================[Kris]===========================
            elif "Bcast " in msg.text:
                if msg.from_ in owner:
                    bc = msg.text.replace("Bcast ","")
                    gid = kr1.getGroupIdsJoined()
                    for i in gid:
                        kr1.sendText(i,"●▬▬▬▬ஜ۩[BROADCAST]۩ஜ▬▬▬▬●\n\n"+bc+"\n\n#BROADCAST!!")
#==========================[Kris]===========================
            elif msg.text.lower() == 'ifconfig':
                if msg.from_ in admin:
                    botKernel = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE).communicate()[0]
                    kr1.sendText(msg.to, botKernel + "\n\n===SERVER INFO NetStat===")
            elif msg.text.lower() == 'system':
                if msg.from_ in admin:
                    botKernel = subprocess.Popen(["df","-h"], stdout=subprocess.PIPE).communicate()[0]
                    kr1.sendText(msg.to, botKernel + "\n\n===SERVER INFO SYSTEM===")
            elif msg.text.lower() == 'kernel':
                if msg.from_ in admin:
                    botKernel = subprocess.Popen(["uname","-srvmpio"], stdout=subprocess.PIPE).communicate()[0]
                    kr1.sendText(msg.to, botKernel + "\n\n===SERVER INFO KERNEL===")
            elif msg.text.lower() == 'cpu':
                if msg.from_ in admin:
                    botKernel = subprocess.Popen(["cat","/proc/cpuinfo"], stdout=subprocess.PIPE).communicate()[0]
                    kr1.sendText(msg.to, botKernel + "\n\n===SERVER INFO CPU===")
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
                    if wait["lang"] == "JP":
                        kr1.sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nBots Dipaksa Keluar oleh Owner Bots...!!!\nMakasih...!!!")
                    else:
                        kr1.sendText(msg.to,"He declined all invitations")
#==========================[Kris]=========================== 
            elif msg.text in ["cab","Cab"]:
                if msg.from_ in admin:
                    url = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26168676_131451404314083_3952554270011807487_n.jpg?oh=6e90aa78daaf5e06b1078bbf15d5aa0f&oe=5AB9882D"
                    kr1.sendImageWithURL(msg.to, url)
                
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
                if msg.from_ in owner:
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
            elif msg.text in ["Blocklist2"]:
                if msg.from_ in owner:
                    blockedlist = kr2.getBlockedContactIds()
                    kontak = kr2.getContacts(blockedlist)
                    num=1
                    msgs="═════════List Blocked═════════"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.displayName)
                        num=(num+1)
                    msgs+="\n═════════List Blocked═════════\n\nTotal Blocked : %i" % len(kontak)
                    kr2.sendText(msg.to, msgs)
#==========================[Kris]===========================
            elif msg.text in ["Blocklist3"]:
                if msg.from_ in admin:
                    blockedlist = kr3.getBlockedContactIds()
                    kontak = kr3.getContacts(blockedlist)
                    num=1
                    msgs="═════════List Blocked═════════"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.displayName)
                        num=(num+1)
                    msgs+="\n═════════List Blocked═════════\n\nTotal Blocked : %i" % len(kontak)
                    kr3.sendText(msg.to, msgs)
#==========================[Kris]===========================
            elif msg.text in ["Blocklist4"]:
                if msg.from_ in admin:
                    blockedlist = kr4.getBlockedContactIds()
                    kontak = kr4.getContacts(blockedlist)
                    num=1
                    msgs="═════════List Blocked═════════"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.displayName)
                        num=(num+1)
                    msgs+="\n═════════List Blocked═════════\n\nTotal Blocked : %i" % len(kontak)
                    kr4.sendText(msg.to, msgs)
#==========================[Kris]===========================
            elif msg.text in ["Blocklist5"]:
                if msg.from_ in admin:
                    blockedlist = kr5.getBlockedContactIds()
                    kontak = kr5.getContacts(blockedlist)
                    num=1
                    msgs="═════════List Blocked═════════"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.displayName)
                        num=(num+1)
                    msgs+="\n═════════List Blocked═════════\n\nTotal Blocked : %i" % len(kontak)
                    kr5.sendText(msg.to, msgs)
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
            elif msg.text in ["Gift 8","Gift8","gift8"]:
                if msg.from_ in admin:
                    msg.contentType = 9
                    msg.contentMetadata={'PRDID': 'ae3d9165-fab2-4e70-859b-c14a9d4137c4',
                                        'PRDTYPE': 'THEME',
                                        'MSGTPL': '8'}
                    msg.text = None
                    kr1.sendMessage(msg)
                    kr1.sendMessage(msg)
                    
                    msg.contentType = 9
                    msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                        'PRDTYPE': 'THEME',
                                        'MSGTPL': '5'}
                    msg.text = None
                    kr1.sendMessage(msg)
                    kr1.sendMessage(msg)

                    msg.contentType = 9
                    msg.contentMetadata={'PRDID': '696d7046-843b-4ed0-8aac-3113ed6c0733',
                                        'PRDTYPE': 'THEME',
                                        'MSGTPL': '6'}
                    msg.text = None
                    kr1.sendMessage(msg)
                    kr1.sendMessage(msg)

                    msg.contentType = 9
                    msg.contentMetadata={'PRDID': '8fe8cdab-96f3-4f84-95f1-6d731f0e273e',
                                        'PRDTYPE': 'THEME',
                                        'MSGTPL': '7'}
                    msg.text = None
                    kr1.sendMessage(msg)
                    kr1.sendMessage(msg)
    #==========================[Kris]===========================
            elif msg.text in ["Gift","gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                kr1.sendMessage(msg)


            elif msg.text in ["Gift1"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '696d7046-843b-4ed0-8aac-3113ed6c0733',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '6'}
                msg.text = None
                kr1.sendMessage(msg)

            elif msg.text in ["Gift2"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '8fe8cdab-96f3-4f84-95f1-6d731f0e273e',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '7'}
                msg.text = None
                kr1.sendMessage(msg)

            elif msg.text in ["Gift3"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'ae3d9165-fab2-4e70-859b-c14a9d4137c4',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '8'}
                msg.text = None
                kr1.sendMessage(msg)
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
            elif "Getcover @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]dp executing"
                    _name = msg.text.replace("Getcover @","")
                    _nametarget = _name.rstrip('  ')
                    gs = kr1.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        kr2.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                contact = kr1.getContact(target)
                                cu = kr1.channel.getCover(target)
                                path = str(cu)
                                kr1.sendImageWithURL(msg.to, path)
                            except:
                                pass
                    print "[Command]dp executed"
#==========================[Kris]===========================
            elif msg.text in ["Waktu"]:
                timeNow = datetime.now()
                timeHours = datetime.strftime(timeNow,"(%H:%M)")
                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                inihari = datetime.today()
                hr = inihari.strftime('%A')
                bln = inihari.strftime('%m')
                for i in range(len(day)):
                    if hr == day[i]: hasil = hari[i]
                for k in range(0, len(bulan)):
                    if bln == str(k): bln = bulan[k-1]
                rst = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + "\nJam : [ " + inihari.strftime('%H:%M:%S') + " ]"
                kr1.sendText(msg.to, rst)
#==========================[Kris]=========================== 
            elif msg.text in ["aah","Aah"]:
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
            elif msg.text.lower() == '...':
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
            elif msg.text in ["Clear","Clearban"]:
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
            elif "Kr spamtag @" in msg.text:
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
            elif ("Kr cium " in msg.text):
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
                           
            elif ("Aah " in msg.text):
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
            elif msg.text in ["Kr glist"]: #Melihat List Group
                if msg.from_ in owner:
                    gids = kr1.getGroupIdsJoined()
                    h = ""
                    for i in gids:
                      #####gn = kr1.getGroup(i).name
                      h += "[•]%s Member\n" % (kr1.getGroup(i).name   +"👉"+str(len(kr1.getGroup(i).members)))
                      kr1.sendText(msg.to,"=======[List Group]======\n"+ h +"Total Group :"+str(len(gids)))
                
            elif msg.text in ["Kr glist2"]: 
                if msg.from_ in owner:
                    gid = kr1.getGroupIdsJoined()
                    h = ""
                    for i in gid:
                      h += "[%s]:%s\n" % (kr1.getGroup(i).name,i)
                      kr1.sendText(msg.to,h)
#==========================[Kris]===========================
            elif "Kr asupka " in msg.text:
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
            elif "Kr megs " in msg.text:
                if msg.from_ in owner:
                    gName = msg.text.replace("Kr megs ","")
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
                        klis=[kr1]
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
            elif "Kr spin" in msg.text:
                if msg.from_ in owner:
                    thisgroup = kr1.getGroups([msg.to])
                    Mids = [contact.mid for contact in thisgroup[0].members]
                    mi_d = Mids[:33]
                    kr1.createGroup("Nah kan", mi_d)
                    kr1.createGroup("Nah kan", mi_d)
                    kr1.createGroup("Nah kan", mi_d)
                    kr1.createGroup("Nah kan", mi_d)
                    kr1.createGroup("Nah kan", mi_d)
                    kr1.createGroup("Nah kan", mi_d)
                    kr1.createGroup("Nah kan", mi_d)
                    kr1.createGroup("Nah kan", mi_d)
                    kr1.createGroup("Nah kan", mi_d)
                    kr1.createGroup("Nah kan", mi_d)
                    kr1.sendText(msg.to,"Success...!!!!")
#==========================[Kris]===========================
            elif msg.text in ["Remove all chat"]:
                if msg.from_ in owner:
                    kr1.removeAllMessages(op.param2)
                    kr2.removeAllMessages(op.param2)
                    kr3.removeAllMessages(op.param2)
                    kr4.removeAllMessages(op.param2)
                    kr5.removeAllMessages(op.param2)
                    kr6.removeAllMessages(op.param2)
                    kr7.removeAllMessages(op.param2)
                    kr8.removeAllMessages(op.param2)
                    kr9.removeAllMessages(op.param2)
                    kr10.removeAllMessages(op.param2)
                    kr1.sendText(msg.to,"Removed all chat Finish")
#==========================[Kris]===========================
            elif msg.text in ["Kr muach"]:
                if msg.from_ in owner:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "ua7fb5762d5066629323d113e1266e8ca',"}
                    kr1.sendMessage(msg)
#==========================[Kris]===========================
#        if op.type == 17:
#            if wait["protect"] == True:
#                if wait["blacklist"][op.param2] == True:
#                    if op.param2 in admin:
#                        pass
#                    if op.param2 not in admin:
#                        try:
#                            X = random.choice(KAC).getGroup(op.param1)
#                            X.preventJoinByTicket = True
#                            random.choice(KAC).updateGroup(X)
#                            Ti = random.choice(KAC).reissueGroupTicket(op.param1)
#                            kr11.acceptGroupInvitationByTicket(op.param1,Ti)
#                            kr12.acceptGroupInvitationByTicket(op.param1,Ti)
#                            kr11.kickoutFromGroup(op.param1,[op.param2])
#                            kr12.kickoutFromGroup(op.param1,[op.param2])
#                            kr11.leaveGroup(op.param1)
#                            kr12.leaveGroup(op.param1)
#                            G = random.choice(KAC).getGroup(op.param1)
#                            G.preventJoinByTicket = True
#                            random.choice(KAC).updateGroup(G)
#                        except:
#                            try:
#                                kr1.kickoutFromGroup(op.param1,[op.param2])
#                                G = kr1.getGroup(op.param1)
#                                G.preventJoinByTicket = True
#                                kr1.updateGroup(G)
#                            except:
#                                pass
#        if op.type == 19:
#            if wait["protect"] == True:
#                wait ["blacklist"][op.param2] = True
#                if op.param2 in admin:
#                    pass
#                if op.param2 not in admin:
#                    X = random.choice(KAC).getGroup(op.param1)
#                    X.preventJoinByTicket = False
#                    random.choice(KAC).updateGroup(X)
#                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
#                    kr11.acceptGroupInvitationByTicket(op.param1,Ti)
#                    kr12.acceptGroupInvitationByTicket(op.param1,Ti)
#                    kr11.kickoutFromGroup(op.param1,[op.param2])
#                    kr12.kickoutFromGroup(op.param1,[op.param2])
#                    kr11.leaveGroup(op.param1)
#                    kr12.leaveGroup(op.param1)
#                    G = random.choice(KAC).getGroup(op.param1)
#                    G.preventJoinByTicket = True
#                    random.choice(KAC).updateGroup(G)
#                    #random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
#        if op.type == 13:
#            if wait["inviteprotect"] == True:
#                wait ["blacklist"][op.param2] = True
#                if op.param2 in admin:
#                    pass
#                if op.param2 not in admin:
#                    random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])
#                    X = random.choice(KAC).getGroup(op.param1)
#                    X.preventJoinByTicket = False
#                    random.choice(KAC).updateGroup(X)
#                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
#                    kr11.acceptGroupInvitationByTicket(op.param1,Ti)
#                    kr12.acceptGroupInvitationByTicket(op.param1,Ti)
#                    kr11.kickoutFromGroup(op.param1,[op.param2])
#                    kr12.kickoutFromGroup(op.param1,[op.param2])
#                    kr11.leaveGroup(op.param1)
#                    kr12.leaveGroup(op.param1)
#                    G = random.choice(KAC).getGroup(op.param1)
#                    G.preventJoinByTicket = True
#                    random.choice(KAC).updateGroup(G)
#                    if wait["inviteprotect"] == True:
#                        wait ["blacklist"][op.param2] = True
#                        if op.param2 in admin:
#                                pass
#                        if op.param2 not in admin:
#                            kr1.cancelGroupInvitation(op.param1,[op.param3])
#                            X = random.choice(KAC).getGroup(op.param1)
#                            X.preventJoinByTicket = False
#                            random.choice(KAC).updateGroup(X)
#                            Ti = random.choice(KAC).reissueGroupTicket(op.param1)
#                            kr11.acceptGroupInvitationByTicket(op.param1,Ti)
#                            kr12.acceptGroupInvitationByTicket(op.param1,Ti)
#                            kr11.kickoutFromGroup(op.param1,[op.param2])
#                            kr12.kickoutFromGroup(op.param1,[op.param2])
#                            kr11.leaveGroup(op.param1)
#                            kr12.leaveGroup(op.param1)
#                            G = random.choice(KAC).getGroup(op.param1)
#                            G.preventJoinByTicket = True
#                            random.choice(KAC).updateGroup(G)
#                            if wait["cancelprotect"] == True:
#                                wait ["blacklist"][op.param2] = True
#                                kr2.cancelGroupInvitation(op.param1,[op.param3])
#        if op.type == 11:
#            if wait["linkprotect"] == True:
#                if op.param2 in admin:
#                    pass
#                if op.param2 not in admin:
#                    X = random.choice(KAC).getGroup(op.param1)
#                    X.preventJoinByTicket = True
#                    random.choice(KAC).updateGroup(X)
#                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
#                    kr11.acceptGroupInvitationByTicket(op.param1,Ti)
#                    kr12.acceptGroupInvitationByTicket(op.param1,Ti)
#                    kr11.kickoutFromGroup(op.param1,[op.param2])
#                    kr12.kickoutFromGroup(op.param1,[op.param2])
#                    kr11.leaveGroup(op.param1)
#                    kr12.leaveGroup(op.param1)
#                    G = random.choice(KAC).getGroup(op.param1)
#                    G.preventJoinByTicket = True
#                    random.choice(KAC).updateGroup(G)
        if op.type == 17:
           if wait["Wc"] == True:
               if op.param2 in Bots:
                 return
               ginfo = kr1.getGroup(op.param1)
               kr1.sendText(op.param1, "╔═════════════\n║Selamat Datang Di  " + str(ginfo.name) + "\n╠═════════════\n" + "║Founder =>>> " + str(ginfo.name) + " :\n║" + ginfo.creator.displayName + "\n╠═════════════\n" + "║😊Semoga Betah Kak 😘 \n╚═════════════")
               print "MEMBER HAS JOIN THE GROUP"
        if op.type == 17:
            if wait["Wc2"] == True:
                if op.param2 in Bots:
                    return
                G = kr1.getGroup(op.param1)
                h = kr1.getContact(op.param2)
                kr1.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net/" + h.pictureStatus)
                print "MEMBER HAS JOIN THE GROUP"
        if op.type == 15:
            if wait["Lv"] == True:
                if op.param2 in Bots:
                    return
                kr1.sendText(op.param1, "╔═════════════\n║Baper Tuh Orang :v \n║Semoga Bahagia ya 😊 \n╚═════════════")
                print "MEMBER HAS LEFT THE GROUP"
#------------------------------------------------------------------------------#

        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
           
                    if op.param2 in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += op.param2
                    wait2['ROM'][op.param1][op.param2] = op.param2
                    with open('sider.json', 'w') as fp:
                     json.dump(wait2, fp, sort_keys=True, indent=4)
                else:
                    pass
            except:
                pass           
            
        
        if op.type == 59:
            print op
    
    except Exception as error:
        print error

time.sleep(0.60)

while True:
    try:
        Ops = kr1.fetchOps(kr1.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(kr1.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            kr1.Poll.rev = max(kr1.Poll.rev, Op.revision)
            bot(Op)
