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
kr1.login(token="isi token disini") #1 => akun utama
kr1.loginResult()

#kr2 = KRIS.LINE()
#kr2.login(qr=True)
#kr2.login(token="")#2 => asist
#kr2.loginResult()

#kr3 = KRIS.LINE()
#kr3.login(qr=True)
#kr3.login(token="")#3 => asist
#kr3.loginResult()
kr3 = kr2 = kr1

print "╔═════════════════════════\n║╔════════════════════════\n║╠❂➣ KRIS BERHASIL LOGIN\n║╚════════════════════════\n╚═════════════════════════"
reload(sys)
sys.setdefaultencoding('utf-8')

keymsg ="""
╔═════════════
║ ✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰
╠═════════════
║ Owner : Kris
╠═════════════
║╔════════════
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
║╠❂➣Intip on/off
║╚════════════
╚═════════════"""

helpmsg ="""
╔═════════════
║ ✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰
╠═════════════
║ Owner : Kris
║ line://ti/p/~krissthea
╠═════════════
║╔════════════
║╠❂➣keyself
║╠❂➣keygrup
║╠❂➣keyset
║╠❂➣keytran
║╠❂➣keybot
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
║╠❂➣Gname:
║╠❂➣Gbroadcast:
║╠❂➣Cbroadcast:
║╠❂➣Infogrup
║╠❂➣Gruplist
║╠❂➣Friendlist
║╠❂➣Contact ban
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
╠═════════════
║╔════════════
║╠❂➣ifconfig
║╠❂➣system
║╠❂➣kernel
║╠❂➣cpu
║╠❂➣Restart
║╠❂➣Turn off
║╠❂➣Speed
║╠❂➣Spamcontact @
║╠❂➣Spamtag @
║╠❂➣Kibar
║╠❂➣cab/cab1/2/3/4/5/6/7
║╠❂➣Logo
║╠❂➣Restart
║╠❂➣Invite/Undang/Jepit
║╠❂➣Namebot:(txt)
║╠❂➣Namebot1/2/3/4/5: 
║╠❂➣Biobot: (txt)
║╠❂➣Kr spamtag @
║╠❂➣Kr glist
║╠❂➣Kr glist2
║╠❂➣Kr bye
║╠❂➣recover
║╠❂➣Kr spin
║╠❂➣Remove all chat
║╚════════════
╚═════════════"""

KAC=[kr1,kr2,kr3]
mid = kr1.getProfile().mid
Amid = kr2.getProfile().mid
Bmid = kr3.getProfile().mid

midd1=["ua573bd78c11cc00f773645d1b83b5c63"]
#midd2=["u9cc2323f5b84f9df880c33aa9f9e3ae1"]
#midd3=["uece14c5ae46691f48f03c4fd331c3fd8"]

Bots=[mid,Amid,Bmid]
owner=["ua573bd78c11cc00f773645d1b83b5c63"]
admin=["ua573bd78c11cc00f773645d1b83b5c63","u31ef22df7f538df1d74dc7f756ef1a32",mid,Amid,Bmid]##Krisna,kris,

wait = {
    'likeOn':False,
    'detectMention':True, 
    'potoMention':False,
    'kickMention':False,
    'steal':False,
    'stiker':False,
    'pap':{},
    'invite':{},
    'invite2':{},
    'spam':{},
    'contact':False,
    'autoJoin':False,
    #'autoCancel':{"on":False,"members":5},
    'leaveRoom':False,
    #'timeline':False,
    #'autoAdd':False,
    #'message':,
    "lang":"JP",
    #"comment":"",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cNames1":"↝↬₡αβ↫↜",
    "cNames2":"↝↬₡αβ↫↜",
    "cNames3":"↝↬₡αβ↫↜",
    "Wc":False,
    "Wc2":False,
    "Lv":False,
    "autoKick":False,
    "winvite":False,
    "MENTION":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "protect":False,
    "cancelprotect":False,
    "inviteprotect":False,
    "linkprotect":False,
    "QrProtect":False,#<====
    "MProtection":False,
    "Protectguest":False,
    "Protectcancel":False,
    "Protectgr":False,
    "Sider":{},
    "intipp":{},
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

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
    }

ngintip = {
    "intip":{},
    "target":{},
    "toong":{}
    }

setTime = {}
setTime = wait2['setTime']

contact = kr1.getProfile()
mybackup = kr1.getProfile()
contact = kr2.getProfile()
mybackup = kr2.getProfile()
contact = kr3.getProfile()
mybackup = kr3.getProfile()
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


def yt(query):
    with requests.session() as s:
         isi = []
         if query == "":
             query = "S1B tanysyz"
         s.headers['user-agent'] = 'Mozilla/5.0'
         url    = 'http://www.youtube.com/results'
         params = {'search_query': query}
         r    = s.get(url, params=params)
         soup = BeautifulSoup(r.content, 'html5lib')
         for a in soup.select('.yt-lockup-title > a[title]'):
            if '&list=' not in a['href']:
                if 'watch?v' in a['href']:
                    b = a['href'].replace('watch?v=', '')
                    isi += ['youtu.be' + b]
         return isi

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
def sendMessage(self, Tomid, msg):
        msg = Message()
        msg.to = Tomid
        msg.msg = msg

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
        if op.type == 25:
            msg = op.message
            if msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
                    text = msg.text
                    if text is not None:
                        kr1.sendText(msg.to,text)

#==========================[Kris]===========================
        if op.type == 13:
            print op.param3
            if op.param3 in mid:
                if op.param2 in admin or owner:
                    kr1.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
                if op.param2 in admin or owner:
                    kr2.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
                if op.param2 in admin or owner:
                    kr3.acceptGroupInvitation(op.param1)
#==========================[Kris]===========================
            if op.param3 in mid:
                if op.param2 in Amid:
                    kr1.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
                if op.param2 in Bmid:
                    kr1.acceptGroupInvitation(op.param1)
#==========================[Kris]===========================
            if op.param3 in Amid:
                if op.param2 in mid:
                    kr2.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
                if op.param2 in Bmid:
                    kr2.acceptGroupInvitation(op.param1)
#==========================[Kris]===========================
            if op.param3 in Bmid:
                if op.param2 in mid:
                    kr3.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
                if op.param2 in Amid:
                    kr3.acceptGroupInvitation(op.param1)
#==========================[Kris]===========================
        if op.type == 13:
            if mid in op.param3:
                if wait['autoJoin'] == True:
                    if op.param2 in admin or owner:
                        kr1.acceptGroupInvitation(op.param1)
                    else:
                        kr1.rejectGroupInvitation(op.param1)
                else:
                    print "autoJoin is Off"
                
            if Amid in op.param3:
                if wait['autoJoin'] == True:
                    if op.param2 in admin or owner:
                        kr2.acceptGroupInvitation(op.param1)
                    else:
                        kr2.acceptGroupInvitation(op.param1)
                        kr2.kickoutFromGroup(op.param1,[op.param2])
                        kr2.leaveGroup(op.param1)
                else:
                    print "autoJoin is Off"
                
            if Bmid in op.param3:
                if wait['autoJoin'] == True:
                    if op.param2 in admin or owner:
                        kr3.acceptGroupInvitation(op.param1)
                    else:
                        kr3.acceptGroupInvitation(op.param1)
                        kr3.kickoutFromGroup(op.param1,[op.param2])
                        kr3.leaveGroup(op.param1)
                else:
                    print "autoJoin is Off"
                
        if op.type == 19:
            if mid in op.param3:
                wait["blacklist"][op.param2] = True
#==========================[Kris]===========================
        if op.type == 22:
            if wait['leaveRoom'] == True:
                kr1.leaveRoom(op.param1)
                kr2.leaveRoom(op.param1)
                kr3.leaveRoom(op.param1)
#==========================[Kris]===========================
        if op.type == 24:
            if wait['leaveRoom'] == True:
                kr1.leaveRoom(op.param1)
                kr2.leaveRoom(op.param1)
                kr3.leaveRoom(op.param1)
#==========================[Kris]===========================
        if op.type == 25:
            msg = op.message

            if msg.toType == 1:
                if wait['leaveRoom'] == True:
                    kr1.leaveRoom(msg.to)
                    kr2.leaveRoom(msg.to)
                    kr3.leaveRoom(msg.to)
#==========================[Kris]===========================
            if msg.contentType == 16:
                url = msg.contentMetadata["postEndUrl"]
                kr1.like(url[25:58], url[66:], likeType=1001)
#==========================[Kris]===========================
        if op.type == 25:
            msg = op.message
            if msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
                    text = msg.text
                    if text is not None:
                        kr1.sendText(msg.to,text)
                        
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
        if op.type in [26,25]:
            msg = op.message
            if msg.contentType == 7:
                if wait['stiker'] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    filler = "[Stiker Check] \nSTKID : %s\nSTKPKGID : %s \nSTKVER : %s\n =>> Link...\nline://shopdetail/%s"%(stk_id,pkg_id,stk_ver,pkg_id)
                    kr1.sendText(msg.to, filler)
                else:
                    pass
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
                            #msg.contentType = 7
                            #msg.text = None
                            #msg.contentMetadata = {
                            #    "STKID": "22926163",
                            #    "STKPKGID": "9800",
                            #    "STKVER": "1" }
                            #kr1.sendMessage(msg)
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
#            if "MENTION" in msg.contentMetadata.keys() != None:
#                 if wait['kickMention'] == True:
#                     contact = kr1.getContact(msg.from_)
#                     cName = contact.displayName
#                     balas = [cName + "Kangenkah sampai ngetag mulu?",cName + " nah mending pc aja klo penting..!", "kenapa, ", cName + " kangen ya?","kangen bilang, gak usah ngetag mulu, " + cName, "sekali lagi ngetag, bayar ya..!!! " + cName, "Tuh kan" + cName + "ngetag lagi, mojok aja yux...!!!"]
#                    ret_ = "[Auto Respon] " + random.choice(balas)
#                     name = re.findall(r'@(\w+)', msg.text)
#                     mention = ast.literal_eval(msg.contentMetadata["MENTION"])
#                     mentionees = mention['MENTIONEES']
#                     for mention in mentionees:
#                           if mention['M'] in Bots:
#                                  kr1.sendText(msg.to,ret_)
#                                  kr1.kickoutFromGroup(msg.to,[msg.from_])
#                                  kr1.inviteIntoGroup(msg.to, admin)
#                                  break
#==========================[Kris]===========================
        if op.type in [26,25]:
            msg = op.message
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
        if op.type in [26,25]:
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
        if op.type == 25:
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
            elif msg.text in ["help","Help"]:
                #if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        kr1.sendText(msg.to,helpmsg)
                    else:
                        kr1.sendText(msg.to,helpmsg)
#==========================[Kris]===========================
            elif msg.text in ["keybot","Keybot"]:
                #if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        kr1.sendText(msg.to,keymsg)
                    else:
                        kr1.sendText(msg.to,keymsg)
#==========================[Kris]===========================
            elif msg.text in ["keypro","Keypro"]:
                #if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        kr1.sendText(msg.to,helppro)
                    else:
                        kr1.sendText(msg.to,helppro)
#==========================[Kris]===========================
            elif msg.text in ["keyself","Keyself"]:
                #if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        kr1.sendText(msg.to,helpself)
                    else:
                        kr1.sendText(msg.to,helpself)
#==========================[Kris]===========================
            elif msg.text in ["keygrup","Keygrup"]:
                #if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        kr1.sendText(msg.to,helpgrup)
                    else:
                        kr1.sendText(msg.to,helpgrup)
#==========================[Kris]===========================
            elif msg.text in ["keyset","Keyset"]:
                #if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        kr1.sendText(msg.to,helpset)
                    else:
                        kr1.sendText(msg.to,helpset)
#==========================[Kris]===========================
            elif msg.text in ["keytran","Keytran"]:
                #if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        kr1.sendText(msg.to,helptranslate)
                    else:
                        kr1.sendText(msg.to,helptranslate)
#==========================[Kris]===========================
            elif msg.text in ["keyrhs","Keyrhs"]:
                #if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        kr1.sendText(msg.to,helprhs)
                    else:
                        kr1.sendText(msg.to,helprhs)
#==========================[Kris]===========================
            elif msg.text in ["Sp","Speed","speed"]:
                #if msg.from_ in admin:
                    start = time.time()
                    kr1.sendText(msg.to, "❂➣Proses.....")
                    elapsed_time = time.time() - start
                    kr1.sendText(msg.to, "%sseconds" % (elapsed_time))

#==========================[Kris]===========================
            elif msg.text in ["aku","Aku"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}
                kr1.sendMessage(msg)
#==========================[Kris]===========================
            elif msg.text in ["me","Me"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}
                kr1.sendMessage(msg)
#==========================[Kris]===========================
            elif msg.text in ["bot","Bot"]:
                if msg.from_ in admin:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': mid}
                    kr1.sendMessage(msg)
#==========================[Kris]===========================
            elif "facebook " in msg.text:
                #if msg.from_ in admin:
                    a = msg.text.replace("facebook ","")
                    b = urllib.quote(a)
                    kr1.sendText(msg.to,"「 Mencari 」\n" "Type:Mencari Info\nStatus: Proses")
                    kr1.sendText(msg.to, "https://www.facebook.com" + b)
                    kr1.sendText(msg.to,"「 Mencari 」\n" "Type:Mencari Info\nStatus: Sukses")    
#==========================[Kris]===========================
            elif msg.text in ["mode on","Mode on"]:
                #if msg.from_ in admin:
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
            elif msg.text in ["mode off","Mode off"]:
                #if msg.from_ in admin:
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
            elif msg.text in ["contact on","Contact on"]:
                #if msg.from_ in admin:
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
            elif msg.text in ["contact off","Contact off"]:
                #if msg.from_ in admin:
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
            elif msg.text in ["protect on","Protect on"]:
                #if msg.from_ in admin:
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
            elif msg.text in ["tikel on","Tikel on"]:
                #if msg.from_ in admin:
                    if wait['stiker'] == True:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Stiker Already On")
                        else:
                            kr1.sendText(msg.to,"Stiker Already On")
                    else:
                        wait["stiker"] = True
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Stiker Already On")
                        else:
                            kr1.sendText(msg.to,"Stiker Already On")
#==========================[Kris]===========================
            elif msg.text in ["qr on","Qr on"]:
                #if msg.from_ in admin:
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
            elif msg.text in ["invite on","Invite on"]:
                #if msg.from_ in admin:
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
            elif msg.text in ["cancel on","Cancel on"]:
                #if msg.from_ in admin:
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
            elif msg.text in ["autojoin on","Autojoin on"]:
                #if msg.from_ in admin:
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
            elif msg.text in ["autojoin off","Autojoin off"]:
                #if msg.from_ in admin:
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
            elif msg.text in ["protect off","Protect off"]:
                #if msg.from_ in admin:
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
            elif msg.text in ["tikel off","Tikel off"]:
                #if msg.from_ in admin:
                    if wait["stiker"] == False:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Stiker already Off")
                        else:
                            kr1.sendText(msg.to,"Stiker already Off")
                    else:
                        wait["stiker"] = False
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Stiker ѕєт тσ σff")
                        else:
                            kr1.sendText(msg.to,"Stiker αℓяєα∂у σff")
#==========================[Kris]===========================
            elif msg.text in ["qr off","Qr off"]:
                #if msg.from_ in admin:
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
            elif msg.text in ["invit off","Invit off"]:
                #if msg.from_ in admin:
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
            elif msg.text in ["cancel off","Cancel off"]:
                #if msg.from_ in admin:
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
                #if msg.from_ in admin:
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
            elif msg.text in ["autoleave on","Autoleave on"]:
                #if msg.from_ in admin:
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
            elif msg.text in ["autoleave off","Autoleave off"]:
                #if msg.from_ in admin:
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
            elif msg.text in ["share on","share on"]:
                #if msg.from_ in admin:
                    if wait['timeline'] == True:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Share set to on")
                        else:
                            kr1.sendText(msg.to,"Share already on")
                    else:
                        wait['timeline'] = True
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Share set to on")
                        else:
                            kr1.sendText(msg.to,"Share already on")
#==========================[Kris]===========================
            elif msg.text in ["share off","Share off"]:
                #if msg.from_ in admin:
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
            elif msg.text in ["status","Status"]:
                #if msg.from_ in admin:
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
            elif msg.text in ["autoadd on","Autoadd on"]:
                #if msg.from_ in admin:
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
            elif msg.text in ["autoadd off","autoadd off"]:
                #if msg.from_ in admin:
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
                #if msg.from_ in admin:
                    wait['message'] = msg.text.replace("Pesan set:","")
                    kr1.sendText(msg.to,"We changed the message")
#==========================[Kris]===========================
            elif msg.text in ["pesan cek","Pesan cek"]:
                #if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        kr1.sendText(msg.to,"Pesan tambahan otomatis telah ditetapkan sebagai berikut \n\n" + wait['message'])
                    else:
                        kr1.sendText(msg.to,"Pesan tambahan otomatis telah ditetapkan sebagai berikut \n\n" + wait['message'])
#==========================[Kris]===========================
            elif "Coment Set:" in msg.text:
                #if msg.from_ in admin:
                    c = msg.text.replace("Coment Set:","")
                    if c in [""," ","\n",None]:
                        kr1.sendText(msg.to,"Merupakan string yang tidak bisa diubah")
                    else:
                        wait["comment"] = c
                        kr1.sendText(msg.to,"Ini telah diubah\n\n" + c)
#==========================[Kris]===========================
            elif msg.text in ["Comment on","comment on"]:
                #if msg.from_ in admin:
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
            elif msg.text in ["Comment off","comment off"]:
                #if msg.from_ in admin:
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
            elif msg.text in ["jam on","Jam on"]:
                #if msg.from_ in admin:
                    if wait["clock"] == True:
                        kr1.sendText(msg.to,"Jam already on")
                    else:
                        wait["clock"] = True
                        now2 = datetime.now()
                        nowT = datetime.strftime(now2,"?%H:%M?")
                        profile = kr1.getProfile()
                        profile.displayName = wait["cName"] + nowT
                        kr1.updateProfile(profile)
                        kr1.sendText(msg.to,"Jam set on")
            elif msg.text in ["jam off","Jam off"]:
                #if msg.from_ in admin:
                    if wait["clock"] == False:
                        kr1.sendText(msg.to,"Jam already off")
                    else:
                        wait["clock"] = False
                        kr1.sendText(msg.to,"Jam set off")
            elif "Jam say:" in msg.text:
                #if msg.from_ in admin:
                    n = msg.text.replace("Jam say:","")
                    if len(n.decode("utf-8")) > 30:
                        kr1.sendText(msg.to,"terlalu lama")
                    else:
                        wait["cName"] = n
                        kr1.sendText(msg.to,"Nama Jam Berubah menjadi:" + n)
            elif msg.text in ["update","Update"]:
                #if msg.from_ in admin:
                    if wait["clock"] == True:
                        now2 = datetime.now()
                        nowT = datetime.strftime(now2,"?%H:%M?")
                        profile = kr1.getProfile()
                        profile.displayName = wait["cName"] + nowT
                        kr1.updateProfile(profile)
                        kr1.sendText(msg.to,"Diperbarui")
                    else:
                        kr1.sendText(msg.to,"Silahkan Aktifkan Jam")
#==========================[Kris]===========================
            elif "Image " in msg.text:
                #if msg.from_ in admin:
                    search = msg.text.replace("Image ","")
                    url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                    raw_html = (download_page(url))
                    items = []
                    items = items + (_images_get_all_items(raw_html))
                    path = random.choice(items)
                    print path
                    try:
                        kr1.sendImageWithURL(msg.to,path)
                    except:
                        pass
#==========================[Kris]===========================
            elif "Spam change:" in msg.text:
                #if msg.from_ in admin:
                    if msg.toType == 2:
                        wait['spam'] = msg.text.replace("Spam change:","")
                        kr1.sendText(msg.to,"spam changed")
#==========================[Kris]===========================
            elif "Spam add:" in msg.text:
                #if msg.from_ in admin:
                    if msg.toType == 2:
                        wait['spam'] = msg.text.replace("Spam add:","")
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"spam changed")
                        else:
                            kr1.sendText(msg.to,"Done")
#==========================[Kris]===========================
            elif "Spam:" in msg.text:
                #if msg.from_ in admin:
                    if msg.toType == 2:
                        strnum = msg.text.replace("Spam:","")
                        num = int(strnum)
                        for var in range(0,num):
                            kr1.sendText(msg.to, wait['spam'])
#==========================[Kris]===========================
            elif ".spam " in msg.text:
                #if msg.from_ in admin:
                    if msg.toType == 2:
                        bctxt = msg.text.replace(".spam ", "")
                        t = kr1.getAllContactIds()
                        t = 500
                        while(t):
                            kr1.sendText(msg.to, (bctxt))
#==========================[Kris]===========================
            elif "Spamcontact @" in msg.text:
                #if msg.from_ in owner:
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

            elif msg.text in ["Invite"]:
                #if msg.from_ in admin:
                    wait["invite"] = True
                    kr1.sendText(msg.to,"Kirim Contact")
#==========================[Kris]===========================
            elif msg.text in ["Jepit"]:
                #if msg.from_ in admin:
                    wait["invite2"] = True
                    random.choice(KAC).sendText(msg.to,"Kirim Contact")
#==========================[Kris]===========================
            elif msg.text in ["Undang"]:
                #if msg.from_ in admin:
                    wait["winvite"] = True
                    kr2.sendText(msg.to,"Kirim Contact")
#==========================[Kris]===========================
            elif msg.text in ["Steal contact"]:
                #if msg.from_ in admin:
                    wait['contact'] = True
                    kr1.sendText(msg.to,"Send Contact")
#==========================[Kris]===========================
            elif msg.text in ["Like:me","Like me"]: #Semua Bot Ngelike Status Akun Utama
                #if msg.from_ in admin:
                    print "[Command]Like executed"
                    kr1.sendText(msg.to,"Like Status Owner")
                    try:
                        likeme()
                    except:
                        pass
#==========================[Kris]===========================
            elif msg.text in ["Like:friend","Like friend"]: #Semua Bot Ngelike Status Teman
                #if msg.from_ in admin:
                    print "[Command]Like executed"
                    kr1.sendText(msg.to,"Like Status Teman")
                    try:
                        likefriend()
                    except:
                        pass
#==========================[Kris]===========================
            elif msg.text in ["Like:on","Like on"]:
                #if msg.from_ in admin:
                    if wait['likeOn'] == True:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Done")
                    else:
                        wait['likeOn'] = True
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Already")
#==========================[Kris]===========================  
            elif msg.text in ["Like off","Like:off"]:
                #if msg.from_ in admin:
                    if wait['likeOn'] == False:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Done")
                    else:
                        wait['likeOn'] = False
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Already")
#==========================[Kris]===========================  
            elif msg.text in ["Simisimi on","Simisimi:on"]:
                #if msg.from_ in admin:
                    settings["simiSimi"][msg.to] = True
                    kr1.sendText(msg.to,"Simi mode On")
#==========================[Kris]=========================== 
            elif msg.text in ["Simisimi off","Simisimi:off"]:
                #if msg.from_ in admin:
                    settings["simiSimi"][msg.to] = False
                    kr1.sendText(msg.to,"Simi mode Off")
#==========================[Kris]===========================  
            elif msg.text in ["Tag on","tag on"]:
                #if msg.from_ in admin:
                    wait['detectMention'] = True
                    kr1.sendText(msg.to,"Auto respon tag On")
#==========================[Kris]===========================
            elif msg.text in ["Tag off","tag off"]:
                #if msg.from_ in admin:
                    wait['detectMention'] = False
                    kr1.sendText(msg.to,"Auto respon tag Off")
#==========================[Kris]===========================
            elif msg.text in ["Respoto on","respoto on"]:
                #if msg.from_ in admin:
                    wait['potoMention'] = True
                    kr1.sendText(msg.to,"Auto respon tag poto On")
#==========================[Kris]===========================   
            elif msg.text in ["Respoto off","respoto off"]:
                #if msg.from_ in admin:
                    wait['potoMention'] = False
                    kr1.sendText(msg.to,"Auto respon tag poto Off")
#==========================[Kris]===========================
            elif msg.text in ["Tag2 on","tag2 on"]:
                #if msg.from_ in admin:
                    wait['kickMention'] = True
                    kr1.sendText(msg.to,"Auto Kick tag ON")
#==========================[Kris]=========================== 
            elif msg.text in ["Tag2 off","tag2 off"]:
                #if msg.from_ in admin:
                    wait['kickMention'] = False
                    kr1.sendText(msg.to,"Auto Kick tag OFF")
#==========================[Kris]===========================
            elif "Time" in msg.text:
                if msg.toType == 2:
                    kr1.sendText(msg.to,datetime.today().strftime('%H:%M:%S'))
#==========================[Kris]===========================
            elif msg.text in ["Sambut on","sambut on"]:
                #if msg.from_ in admin:
                    if wait["Wc"] == True:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"noтιғ yg joιn on")
                    else:
                        wait["Wc"] = True
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"already on")
            elif msg.text in ["Sambut off","sambut off"]:
                #if msg.from_ in admin:
                    if wait["Wc"] == False:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"noтιғ yg joιn oғғ")
                    else:
                        wait["Wc"] = False
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"already oғғ")
#==========================[Kris]===========================
            elif msg.text in ["Sambut2 on","sambut2 on"]:
                #if msg.from_ in admin:
                    if wait["Wc2"] == True:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"noтιғ yg joιn poto on")
                    else:
                        wait["Wc2"] = True
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"already on")
            elif msg.text in ["Sambut2 off","sambut2 off"]:
                #if msg.from_ in admin:
                    if wait["Wc2"] == False:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"noтιғ yg joιn poto oғғ")
                    else:
                        wait["Wc2"] = False
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"already oғғ")
#==========================[Kris]===========================
            elif msg.text in ["Pergi on","pergi on"]:
                #if msg.from_ in admin:
                    if wait["Lv"] == True:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"noтιғ yg leave on")
                    else:
                        wait["Lv"] = True
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"already on")
            elif msg.text in ["Pergi off","pergi off"]:
                #if msg.from_ in admin:
                    if wait["Lv"] == False:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"noтιғ yg leave oғғ")
                    else:
                        wait["Lv"] = False
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"already oғғ")
#==========================[Kris]===========================
            elif msg.text in ["Salam1"]:
                kr1.sendText(msg.to,"السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                kr2.sendText(msg.to,"Assalamu'alaikum")
            elif msg.text in ["Salam2"]:
                kr1.sendText(msg.to,"وَعَلَيْكُمْ السَّلاَمُرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                kr2.sendText(msg.to,"Wa'alaikumsallam.Wr,Wb")
           
#==========================[Kris]===========================
            elif "invite " in msg.text.lower():
                #if msg.from_ in admin:
                    key = msg.text[-33:]
                    kr1.findAndAddContactsByMid(key)
                    kr1.inviteIntoGroup(msg.to, [key])
                    contact = kr1.getContact(key)
#==========================[Kris]===========================
            elif msg.text in ["cancel","Cancel"]:
                #if msg.from_ in admin:
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
            elif msg.text in ["link on","Link on"]:
                #if msg.from_ in admin:
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
            elif msg.text in ["link off","Link off"]:
                #if msg.from_ in admin:
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
                #if msg.from_ in admin:
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
            elif msg.text in ["invite:gcreator"]:
                #if msg.from_ in admin:
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
                #if msg.from_ in admin:
                    if msg.toType == 2:
                        X = kr1.getGroup(msg.to)
                        X.name = msg.text.replace("Gname: ","")
                        kr1.updateGroup(X)
#==========================[Kris]===========================  
            elif msg.text in ["infogrup","Infogrup"]:
                #if msg.from_ in admin:
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
            elif msg.text in ["Botak"]:
                random.choice(KAC).sendImageWithURL(msg.to, url123)
                random.choice(KAC).sendText(msg.to,"↥↥↥↥↥↪ Pembuat Bots ↩↥↥↥↥↥")
#==========================[Kris]===========================
            elif msg.text in ["grup id","Grup id"]:
                #if msg.from_ in owner:
                    gid = kr1.getGroupIdsJoined()
                    h = ""
                    for i in gid:
                        h += "[%s]:%s\n" % (kr1.getGroup(i).name,i)
                    kr1.sendText(msg.to,h)
#==========================[Kris]===========================
            elif msg.text in ["Glist"]:
                #if msg.from_ in admin:
                    gid = kr1.getGroupIdsJoined()
                    h = ""
                    for i in gid:
                        h += "%s\n" % (kr1.getGroup(i).name +" ? ["+str(len(kr1.getGroup(i).members))+"]")
                    kr1.sendText(msg.to,"-- List Groups --\n\n"+ h +"\nTotal groups =" +" ["+str(len(gid))+"]")
#==========================[Kris]===========================
            elif msg.text in ["Glist2"]:
                #if msg.from_ in admin:
                    gid = kr2.getGroupIdsJoined()
                    h = ""
                    for i in gid:
                        h += "%s\n" % (kr2.getGroup(i).name +" ? ["+str(len(kr2.getGroup(i).members))+"]")
                    kr2.sendText(msg.to,"-- List Groups --\n\n"+ h +"\nTotal groups =" +" ["+str(len(gid))+"]")
#==========================[Kris]===========================
            elif msg.text in ["Glist3"]:
                #if msg.from_ in admin:
                    gid = kr3.getGroupIdsJoined()
                    h = ""
                    for i in gid:
                        h += "%s\n" % (kr3.getGroup(i).name +" ? ["+str(len(kr3.getGroup(i).members))+"]")
                    kr3.sendText(msg.to,"-- List Groups --\n\n"+ h +"\nTotal groups =" +" ["+str(len(gid))+"]")
#==========================[Kris]===========================
            elif msg.text in ["gcancel","Gcancel"]:
                #if msg.from_ in admin:
                    gid = kr1.getGroupIdsInvited()
                    for i in gid:
                        kr1.rejectGroupInvitation(i)
                    if wait["lang"] == "JP":
                        kr1.sendText(msg.to,"Aku menolak semua undangan")
                    else:
                        kr1.sendText(msg.to,"He declined all invitations")

#==========================[Kris]===========================
            elif msg.text in ["Kr bye"]:#keluar bot kecuali bot induk
                #if msg.from_ in owner:
                    if msg.toType == 2:
                        ginfo = kr1.getGroup(msg.to)
                        ginfo = kr2.getGroup(msg.to)
                        ginfo = kr3.getGroup(msg.to)
                        try:
                            kr3.sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nJangan Lupa Bahagia...!!!")
                            kr3.leaveGroup(msg.to)
                            #kr2.leaveGroup(msg.to)
                            #kr1.leaveGroup(msg.to)
                        except:
                            pass
#==========================[Kris]===========================
            elif "cipok" == msg.text.lower():
                #if msg.from_ in admin:
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
                #if msg.from_ in admin:
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
            elif "cctv on" == msg.text.lower():
                #if msg.from_ in admin:
                    if msg.to in wait2['readPoint']:
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        with open('sider.json', 'w') as fp:
                            json.dump(wait2, fp, sort_keys=True, indent=4)
                            kr1.sendText(msg.to,"Setpoint already on")
                    else:
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        with open('sider.json', 'w') as fp:
                            json.dump(wait2, fp, sort_keys=True, indent=4)
                            kr1.sendText(msg.to, "Set reading point:\n" + datetime.now().strftime('%H:%M:%S'))
                            print wait2
#==========================[Kris]===========================
            elif msg.text in ["Botak"]:
                random.choice(KAC).sendImageWithURL(msg.to, url123)
                random.choice(KAC).sendText(msg.to,"↥↥↥↥↥↪ Pembuat Bots ↩↥↥↥↥↥")
                    
            elif "cctv off" == msg.text.lower():
                #if msg.from_ in admin:
                    if msg.to not in wait2['readPoint']:
                        kr1.sendText(msg.to,"Setpoint already off")
                    else:
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                        except:
                             pass
                        kr1.sendText(msg.to, "Delete reading point:\n" + datetime.now().strftime('%H:%M:%S'))
#==========================[Kris]===========================
            elif msg.text in ["toong","Toong"]:
                #if msg.from_ in admin:
                    if msg.toType == 2:
                        print "\nRead aktif..."
                        if msg.to in wait2['readPoint']:
                            if wait2['ROM'][msg.to].items() == []:
                                chiya = ""
                            else:
                                chiya = ""
                                for rom in wait2['ROM'][msg.to].items():
                                    print rom
                                    chiya += rom[1] + "\n"
                            kr1.sendText(msg.to, "╔═════════════ \n╠❂➣Sider :\n╠═════════════                     %s\n╠\n╠═════════════\n╠❂➣Reader :\n╠═════════════ %s\n╠\n╠═════════════\n╠In the last seen point:\n╠[%s]\n╚═════════════" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                            print "\nReading Point Set..."
                            try:
                                del wait2['readPoint'][msg.to]
                                del wait2['readMember'][msg.to]
                            except:
                                pass
                            wait2['readPoint'][msg.to] = msg.id
                            wait2['readMember'][msg.to] = ""
                            wait2['setTime'][msg.to] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                            wait2['ROM'][msg.to] = {}
                            print "toong ready"
                            kr1.sendText(msg.to, "Auto Read Point!!" + (wait2['setTime'][msg.to]))
                        else:
                            kr1.sendText(msg.to, "Ketik [Cctv on] dulu, baru ketik [Toong]")
#==========================[Kris]===========================
            elif msg.text in ["Botak"]:
                random.choice(KAC).sendImageWithURL(msg.to, url123)
                random.choice(KAC).sendText(msg.to,"↥↥↥↥↥↪ Pembuat Bots ↩↥↥↥↥↥")
                    
            elif "intip" == msg.text.lower():
                #if msg.from_ in admin:
                    if msg.to in wait2['readPoint']:
                        if wait2['ROM'][msg.to].items() == []:
                            kr1.sendText(msg.to, "Reader:\nNone")
                        else:
                            chiya = []
                            for rom in wait2['ROM'][msg.to].items():
                                chiya.append(rom[1])
                               
                            cmem = kr1.getContacts(chiya)
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = ''
                        for x in range(len(cmem)):
                                xname = str(cmem[x].displayName)
                                pesan = ''
                                pesan2 = pesan+"@a\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                zx2.append(zx)
                                zxc += pesan2
                                msg.contentType = 0
           
                        print zxc
                        msg.text = xpesan+ zxc + "\nBefore: %s\nAfter: %s"%(wait2['setTime'][msg.to],datetime.now().strftime('%H:%M:%S'))
                        lol ={"MENTION":str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                        print lol
                        msg.contentMetadata = lol
                        try:
                            kr1.sendMessage(msg)
                        except Exception as error:
                            print error
                        pass

                    else:
                        kr1.sendText(msg.to, "Lurking has not been set.")
#==========================[Kris]===========================
            elif "Gbroadcast: " in msg.text:
                #if msg.from_ in owner:
                    bc = msg.text.replace("Gbroadcast: ","")
                    gid = kr1.getGroupIdsJoined()
                    for i in gid:
                        kr1.sendText(i, bc)
#==========================[Kris]=========================== 
            elif "Cbroadcast: " in msg.text:
                #if msg.from_ in owner:
                    bc = msg.text.replace("Cbroadcast: ","")
                    gid = kr1.getAllContactIds()
                    for i in gid:
                        kr1.sendText(i, bc)
#==========================[Kris]===========================
            elif "Spam change: " in msg.text:
                #if msg.from_ in admin:
                    wait['spam'] = msg.text.replace("Spam change: ","")
                    kr1.sendText(msg.to,"spam changed")
#==========================[Kris]===========================
            elif "Spam add: " in msg.text:
                #if msg.from_ in admin:
                    wait['spam'] = msg.text.replace("Spam add: ","")
                    if wait["lang"] == "JP":
                        kr1.sendText(msg.to,"spam changed")
                    else:
                        kr1.sendText(msg.to,"Done")
#==========================[Kris]===========================
            elif "Spam: " in msg.text:
                #if msg.from_ in admin:
                    strnum = msg.text.replace("Spam: ","")
                    num = int(strnum)
                    for var in range(0,num):
                        kr1.sendText(msg.to, wait['spam'])
#==========================[Kris]===========================
            elif "Spamtag @" in msg.text:
                #if msg.from_ in admin:
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
                #if msg.from_ in admin:
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
            elif ("Micadd " in msg.text):
                #if msg.from_ in admin:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            mimic["target"][target] = True
                            kr1.sendText(msg.to,"Target ditambahkan!")
                            break
                        except:
                            kr1.sendText(msg.to,"Fail !")
                            break
#==========================[Kris]===========================  
            elif ("Micdel " in msg.text):
                #if msg.from_ in admin:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del mimic["target"][target]
                            kr1.sendText(msg.to,"Target dihapuskan!")
                            break
                        except:
                            kr1.sendText(msg.to,"Fail !")
                            break
#==========================[Kris]=========================== 
            elif msg.text in ["Miclist"]:
                #if msg.from_ in admin:
                    if mimic["target"] == {}:
                        kr1.sendText(msg.to,"nothing")
                    else:
                        mc = "Target mimic user\n"
                        for mi_d in mimic["target"]:
                            mc += "?? "+kr1.getContact(mi_d).displayName + "\n"
                        kr1.sendText(msg.to,mc)
#==========================[Kris]===========================
            elif "Mimic target " in msg.text:
                #if msg.from_ in admin:
                    if mimic["copy"] == True:
                        siapa = msg.text.replace("Mimic target ","")
                        if siapa.rstrip(' ') == "me":
                            mimic["copy2"] = "me"
                            kr1.sendText(msg.to,"Mimic change to me")
                        elif siapa.rstrip(' ') == "target":
                            mimic["copy2"] = "target"
                            kr1.sendText(msg.to,"Mimic change to target")
                        else:
                            kr1.sendText(msg.to,"I dont know")
#==========================[Kris]===========================
            elif "Mimic " in msg.text:
                #if msg.from_ in admin:
                    cmd = msg.text.replace("Mimic ","")
                    if cmd == "on":
                        if mimic["status"] == False:
                            mimic["status"] = True
                            kr1.sendText(msg.to,"Reply Message on")
                        else:
                            kr1.sendText(msg.to,"Sudah on")
                    elif cmd == "off":
                        if mimic["status"] == True:
                            mimic["status"] = False
                            kr1.sendText(msg.to,"Reply Message off")
                        else:
                            kr1.sendText(msg.to,"Sudah off")
#==========================[Kris]===========================
            elif "Setimage: " in msg.text:
                #if msg.from_ in admin:
                    wait['pap'] = msg.text.replace("Setimage: ","")
                    kr1.sendText(msg.to, "Pap telah di Set")
            elif msg.text in ["Papimage","Papim",'pap']:
                #if msg.from_ in admin:
                    kr1.sendImageWithURL(msg.to,wait['pap'])
            elif "Setvideo: " in msg.text:
                #if msg.from_ in admin:
                    wait['pap'] = msg.text.replace("Setvideo: ","")
                    kr1.sendText(msg.to,"Video Has Ben Set To")
            elif msg.text in ["Papvideo","Papvid"]:
                #if msg.from_ in admin:
                    kr1.sendVideoWithURL(msg.to,wait['pap'])
            elif "TL:" in msg.text:
                #if msg.from_ in admin:
                    if msg.toType == 2:
                        tl_text = msg.text.replace("TL:","")
                        kr1.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+kr1.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
#==========================[Kris]===========================
            elif msg.text in ["mymid","Mymid"]:
                kr1.sendText(msg.to,mid)
#==========================[Kris]===========================
            elif "Timeline: " in msg.text:
                #if msg.from_ in admin:
                    tl_text = msg.text.replace("Timeline: ","")
                    kr1.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+kr1.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
#==========================[Kris]===========================
            elif "Namebot: " in msg.text:
                #if msg.from_ in owner:
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
#==========================[Kris]===========================
            elif "Namebot1: " in msg.text:
                #if msg.from_ in owner:
                    string = msg.text.replace("Namebot1: ","")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = kr1.getProfile()
                        profile.displayName = string
                        kr1.updateProfile(profile)
                        kr1.sendText(msg.to,"Changed " + string + "")
            elif "Namebot2: " in msg.text:
                #if msg.from_ in owner:
                    string = msg.text.replace("Namebot2: ","")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = kr2.getProfile()
                        profile.displayName = string
                        kr2.updateProfile(profile)
                        kr2.sendText(msg.to,"Changed " + string + "")
            elif "Namebot3: " in msg.text:
                #if msg.from_ in owner:
                    string = msg.text.replace("Namebot3: ","")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = kr3.getProfile()
                        profile.displayName = string
                        kr3.updateProfile(profile)
                        kr3.sendText(msg.to,"Changed " + string + "")
#==========================[Kris]===========================
            elif "Biobot: " in msg.text:
                #if msg.from_ in owner:
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
#==========================[Kris]===========================
            elif msg.text in ["Myname"]:
                    h = kr1.getContact(mid)
                    kr1.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
            elif msg.text in ["Mybot"]:
                    h = kr1.getContact(mid)
                    h = kr2.getContact(Amid)
                    h = kr3.getContact(Bmid)
                    kr1.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
                    kr2.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
                    kr3.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
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
            elif msg.text in ["Botak"]:
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
            elif msg.text in ["Intip on","intip on"]:
                #if msg.from_ in admin:
                    try:
                        del cctv['point'][msg.to]
                        del cctv['sidermem'][msg.to]
                        del cctv['cyduk'][msg.to]
                    except:
                        pass
                    cctv['point'][msg.to] = msg.id
                    cctv['sidermem'][msg.to] = ""
                    cctv['cyduk'][msg.to]=True
                    wait["Sider"] == True
                    kr1.sendText(msg.to,"Cek yang ngintip on..!!!")
                
            elif msg.text in ["Intip off","intip off"]:
                #if msg.from_ in admin:
                    if msg.to in cctv['point']:
                        cctv['cyduk'][msg.to]=False
                        wait["Sider"] = False
                        kr1.sendText(msg.to,"Cek yang ngintip off")
                    else:
                        kr1.sendText(msg.to,"Belum Di Set Boss")
#==========================[Kris]===========================
            elif msg.text in ["Toong on","toong on"]:
                #if msg.from_ in admin:
                    try:
                        del ngintip['target'][msg.to]
                        del ngintip['toong'][msg.to]
                        del ngintip['intip'][msg.to]
                    except:
                        pass
                    ngintip['target'][msg.to] = msg.id
                    ngintip['toong'][msg.to] = ""
                    ngintip['intip'][msg.to]=True
                    wait["intipp"] == True
                    kr1.sendText(msg.to,"Cek yang Cctv on..!!!")
                
            elif msg.text in ["Toong off","toong off"]:
                #if msg.from_ in admin:
                    if msg.to in ngintip['target']:
                        ngintip['intip'][msg.to]=False
                        wait["intipp"] = False
                        kr1.sendText(msg.to,"Cek yang Cctv off")
                    else:
                        kr1.sendText(msg.to,"Belum Di Set Boss")
#==========================[Kris]===========================
            elif "Getmid @" in msg.text:
                #if msg.from_ in admin:
                    _name = msg.text.replace("Getmid @","")
                    _nametarget = _name.rstrip(' ')
                    gs = kr1.getGroup(msg.to)
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            kr1.sendText(msg.to, g.mid)
                        else:
                            pass
            elif "Getinfo" in msg.text:
                #if msg.from_ in admin:
                    key = eval(msg.contentMetadata["MENTION"])
                    key1 = key["MENTIONEES"][0]["M"]
                    contact = kr1.getContact(key1)
                    cu = kr1.channel.getCover(key1)
                    try:
                        kr1.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nHeader :\n" + str(cu))
                    except:
                        kr1.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\n" + str(cu))
            elif "Getbio" in msg.text:
                #if msg.from_ in admin:
                    key = eval(msg.contentMetadata["MENTION"])
                    key1 = key["MENTIONEES"][0]["M"]
                    contact = kr1.getContact(key1)
                    cu = kr1.channel.getCover(key1)
                    try:
                        kr1.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)
                    except:
                        kr1.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)
            elif "Getname" in msg.text:
                #if msg.from_ in admin:
                    key = eval(msg.contentMetadata["MENTION"])
                    key1 = key["MENTIONEES"][0]["M"]
                    contact = kr1.getContact(key1)
                    cu = kr1.channel.getCover(key1)
                    try:
                        kr1.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)
                    except:
                        kr1.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)
            elif "Getprofile" in msg.text:
                #if msg.from_ in admin:
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
                #if msg.from_ in admin:
                    key = eval(msg.contentMetadata["MENTION"])
                    key1 = key["MENTIONEES"][0]["M"]                
                    mmid = kr1.getContact(key1)
                    msg.contentType = 13
                    msg.contentMetadata = {"mid": key1}
                    kr1.sendMessage(msg)
            elif "Getpict @" in msg.text:
                #if msg.from_ in admin:
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
                #if msg.from_ in admin:
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
                #if msg.from_ in admin:
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
                #if msg.from_ in admin:
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
                #if msg.from_ in admin:
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
                #if msg.from_ in admin:
                    group = kr1.getGroup(msg.to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    kr1.sendImageWithURL(msg.to,path)
            elif "Urlgrup image" in msg.text:
                #if msg.from_ in admin:
                    group = kr1.getGroup(msg.to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    kr1.sendText(msg.to,path)
#==========================[Kris]===========================
            elif "Mycopy @" in msg.text:
                #if msg.from_ in admin:
                    print "[COPY] Ok"
                    _name = msg.text.replace("Mycopy @","")
                    _nametarget = _name.rstrip('  ')
                    gs = kr1.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        kr1.sendText(msg.to, "Not Found...")
                    else:
                        for target in targets:
                            try:
                                kr1.CloneContactProfile(target)
                                kr1.sendText(msg.to, "Copied.")
                            except Exception as e:
                                print e
            elif msg.text in ["Mybackup","mybackup"]:
                #if msg.from_ in admin:
                    try:
                        kr1.updateDisplayPicture(backup.pictureStatus)
                        kr1.updateProfile(backup)
                        kr1.sendText(msg.to, "Refreshed.")
                    except Exception as e:
                        kr1.sendText(msg.to, str(e))
#==============================================================================#
            elif "Testext: " in msg.text:
                #if msg.from_ in admin:
                    txt = msg.text.replace("Testext: ", "")
                    kr1.kedapkedip(msg.to,txt)
                    print "[Command] Kedapkedip"
#==========================[Kris]===========================   
            elif "Translate-id " in msg.text:
                isi = msg.text.replace("Tr-id ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='id')
                A = hasil.text
                A = A.encode('utf-8')
                kr1.sendText(msg.to, A)
            elif "Translate-en " in msg.text:
                isi = msg.text.replace("Tr-en ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='en')
                A = hasil.text
                A = A.encode('utf-8')
                kr1.sendText(msg.to, A)
            elif "Translate-ar" in msg.text:
                isi = msg.text.replace("Tr-ar ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ar')
                A = hasil.text
                A = A.encode('utf-8')
                kr1.sendText(msg.to, A)
            elif "Translate-jp" in msg.text:
                isi = msg.text.replace("Tr-jp ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ja')
                A = hasil.text
                A = A.encode('utf-8')
                kr1.sendText(msg.to, A)
            elif "Translate-ko" in msg.text:
                isi = msg.text.replace("Tr-ko ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ko')
                A = hasil.text
                A = A.encode('utf-8')
                kr1.sendText(msg.to, A)
            elif msg.text in ["Botak"]:
                random.choice(KAC).sendImageWithURL(msg.to, url123)
                random.choice(KAC).sendText(msg.to,"↥↥↥↥↥↪ Pembuat Bots ↩↥↥↥↥↥")
            elif "Id@en" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'en'
                kata = msg.text.replace("Id@en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                kr1.sendText(msg.to,"**FROM ID**\n" + "" + kata + "\n**TO ENGLISH**\n" + "" + result + "\n**SUKSES**")
            elif "En@id" in msg.text:
                bahasa_awal = 'en'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("En@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                kr1.sendText(msg.to,"**FROM EN**\n" + "" + kata + "\n**TO ID**\n" + "" + result + "\n**SUKSES**")
            elif "Id@jp" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'ja'
                kata = msg.text.replace("Id@jp ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                kr1.sendText(msg.to,"**FROM ID**\n" + "" + kata + "\n**TO JP**\n" + "" + result + "\n**SUKSES**")
            elif "Jp@id" in msg.text:
                bahasa_awal = 'ja'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Jp@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                kr1.sendText(msg.to,"----FROM JP----\n" + "" + kata + "\n----TO ID----\n" + "" + result + "\n------SUKSES-----")
            elif "Id@th" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'th'
                kata = msg.text.replace("Id@th ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                kr1.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO TH----\n" + "" + result + "\n------SUKSES-----")
            elif "Th@id" in msg.text:
                bahasa_awal = 'th'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Th@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                kr1.sendText(msg.to,"----FROM TH----\n" + "" + kata + "\n----TO ID----\n" + "" + result + "\n------SUKSES-----")
            elif "Id@jp" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'ja'
                kata = msg.text.replace("Id@jp ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                kr1.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO JP----\n" + "" + result + "\n------SUKSES-----")
            elif "Id@ar" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'ar'
                kata = msg.text.replace("Id@ar ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                kr1.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO AR----\n" + "" + result + "\n------SUKSES-----")
            elif "Ar@id" in msg.text:
                bahasa_awal = 'ar'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Ar@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                kr1.sendText(msg.to,"----FROM AR----\n" + "" + kata + "\n----TO ID----\n" + "" + result + "\n------SUKSES-----")
            elif "Id@ko" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'ko'
                kata = msg.text.replace("Id@ko ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                kr1.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO KO----\n" + "" + result + "\n------SUKSES-----")
            elif "Ko@id" in msg.text:
                bahasa_awal = 'ko'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Ko@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                kr1.sendText(msg.to,"----FROM KO----\n" + "" + kata + "\n----TO ID----\n" + "" + result + "\n------SUKSES-----")
#==========================[Kris]===========================
            elif msg.text in ["welcome","Welcome","kam","Kam"]:
                ginfo = kr1.getGroup(msg.to)
                kr1.sendText(msg.to,"Selamat Datang Di Grup " + str(ginfo.name))
                jawaban1 = ("Selamat Datang Di Grup " + str(ginfo.name))
                kr1.sendText(msg.to,"Owner Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName )
                tts = gTTS(text=jawaban1, lang='id')
                tts.save('tts.mp3')
                kr1.sendAudio(msg.to,'tts.mp3')
#==========================[Kris]===========================
            elif "Say-id " in msg.text:
                say = msg.text.replace("Say-id ","")
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                kr1.sendAudio(msg.to,"hasil.mp3")
                
            elif "Say-en " in msg.text:
                say = msg.text.replace("Say-en ","")
                lang = 'en'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                kr1.sendAudio(msg.to,"hasil.mp3")
                
            elif "Say-jp " in msg.text:
                say = msg.text.replace("Say-jp ","")
                lang = 'ja'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                kr1.sendAudio(msg.to,"hasil.mp3")
                
            elif "Say-ar " in msg.text:
                say = msg.text.replace("Say-ar ","")
                lang = 'ar'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                kr1.sendAudio(msg.to,"hasil.mp3")
                
            elif "Say-ko " in msg.text:
                say = msg.text.replace("Say-ko ","")
                lang = 'ko'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                kr1.sendAudio(msg.to,"hasil.mp3")
#==========================[Kris]=========================== 
            elif "Kapan " in msg.text:
                tanya = msg.text.replace("Kapan ","")
                jawab = ("kapan kapan","besok","satu abad lagi","Hari ini","Tahun depan","Minggu depan","Bulan depan","Sebentar lagi")
                jawaban = random.choice(jawab)
                tts = gTTS(text=jawaban, lang='id')
                tts.save('tts.mp3')
                kr1.sendAudio(msg.to,'tts.mp3')
                kr1.sendText(msg.to,jawaban)
                kr2.sendText(msg.to,jawaban)
                kr2.sendText(msg.to,jawaban)
#==========================[Kris]===========================
            elif "Apakah " in msg.text:
                tanya = msg.text.replace("Apakah ","")
                jawab = ("Ya","Tidak","Mungkin","Bisa jadi")
                jawaban = random.choice(jawab)
                tts = gTTS(text=jawaban, lang='id')
                tts.save('tts.mp3')
                kr1.sendAudio(msg.to,'tts.mp3')
                kr1.sendText(msg.to,jawaban)
                kr2.sendText(msg.to,jawaban)
                kr2.sendText(msg.to,jawaban)
#==========================[Kris]=========================== 
            elif msg.text in ["Nah","nah"]:
                kr1.sendText(msg.to,"Kan")
                kr1.sendText(msg.to,"Kan")
                kr1.sendText(msg.to,"Kan")
#==========================[Kris]===========================
            elif msg.text in ["Absen","absen"]:
                #if msg.from_ in admin:
                    kr1.sendText(msg.to,"👉★★★√")
                    kr2.sendText(msg.to,"👉★★★★√")
                    kr3.sendText(msg.to,"👉★★★★★√")
                    kr1.sendText(msg.to,"👉Semua Hadir Boss...!!!\n\n[✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰]")
#==========================[Kris]===========================
            elif "Bcast " in msg.text:
                #if msg.from_ in owner:
                    bc = msg.text.replace("Bcast ","")
                    gid = kr1.getGroupIdsJoined()
                    for i in gid:
                        kr1.sendText(i,"●▬▬▬▬ஜ۩[BROADCAST]۩ஜ▬▬▬▬●\n\n"+bc+"\n\n#BROADCAST!!")
#==========================[Kris]===========================
            elif 'Youtube ' in msg.text:
                #if msg.from_ in admin:
                    try:
                        textToSearch = (msg.text).replace('Youtube ', "").strip()
                        query = urllib.quote(textToSearch)
                        url = "https://www.youtube.com/results?search_query=" + query
                        response = urllib2.urlopen(url)
                        html = response.read()
                        soup = BeautifulSoup(html, "html.parser")
                        results = soup.find(attrs={'class': 'yt-uix-tile-link'})
                        ght = ('https://www.youtube.com' + results['href'])
                        kr1.sendVideoWithURL(msg.to, ght)
                    except:
                        kr1.sendText(msg.to, "Could not find it")
            
            elif "Yt " in msg.text:
                #if msg.from_ in admin:
                    query = msg.text.replace("Yt ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'http://www.youtube.com/results'
                        params = {'search_query': query}
                        r = s.get(url, params=params)
                        soup = BeautifulSoup(r.content, 'html5lib')
                        hasil = ""
                        for a in soup.select('.yt-lockup-title > a[title]'):
                            if '&list=' not in a['href']:
                                hasil += ''.join((a['title'],'\nUrl : http://www.youtube.com' + a['href'],'\n\n'))
                        kr1.sendText(msg.to,hasil)
                        print '[Command] Youtube Search'
#==========================[Kris]=========================== 
            elif "Lirik " in msg.text:
                #if msg.from_ in admin:
                    try:
                        songname = msg.text.lower().replace("Lirik ","")
                        params = {'songname': songname}
                        r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                        data = r.text
                        data = json.loads(data)
                        for song in data:
                            hasil = 'Lyric Lagu ('
                            hasil += song[0]
                            hasil += ')\n\n'
                            hasil += song[5]
                            kr1.sendText(msg.to, hasil)
                    except Exception as wak:
                            kr1.sendText(msg.to, str(wak))
#==========================[Kris]===========================
            elif "Wikipedia " in msg.text:
                #if msg.from_ in admin:
                    try:
                        wiki = msg.text.lower().replace("Wikipedia ","")
                        wikipedia.set_lang("id")
                        pesan="Title ("
                        pesan+=wikipedia.page(wiki).title
                        pesan+=")\n\n"
                        pesan+=wikipedia.summary(wiki, sentences=1)
                        pesan+="\n"
                        pesan+=wikipedia.page(wiki).url
                        kr1.sendText(msg.to, pesan)
                    except:
                        try:
                            pesan="Over Text Limit! Please Click link\n"
                            pesan+=wikipedia.page(wiki).url
                            kr1.sendText(msg.to, pesan)
                        except Exception as e:
                            kr1.sendText(msg.to, str(e))
#==========================[Kris]===========================
            elif "Music " in msg.text:
                #if msg.from_ in admin:
                    try:
                        songname = msg.text.lower().replace("Music ","")
                        params = {'songname': songname}
                        r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                        data = r.text
                        data = json.loads(data)
                        for song in data:
                            hasil = 'This is Your Music\n'
                            hasil += 'Judul : ' + song[0]
                            hasil += '\nDurasi : ' + song[1]
                            hasil += '\nLink Download : ' + song[4]
                            kr1.sendText(msg.to, hasil)
                            kr1.sendText(msg.to, "Please Wait for audio...")
                            kr1.sendAudioWithURL(msg.to, song[4])
                    except Exception as njer:
                        kr1.sendText(msg.to, str(njer))
#==========================[Kris]===========================
            elif "Image " in msg.text:
                #if msg.from_ in admin:
                    search = msg.text.replace("Image ","")
                    url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                    raw_html = (download_page(url))
                    items = []
                    items = items + (_images_get_all_items(raw_html))
                    path = random.choice(items)
                    print path
                    try:
                        kr1.sendImageWithURL(msg.to,path)
                    except:
                        pass           
#==========================[Kris]===========================
            elif "Instagram " in msg.text:
                #if msg.from_ in admin:
                    try:
                        instagram = msg.text.replace("Instagram ","")
                        response = requests.get("https://www.instagram.com/"+instagram+"?__a=1")
                        data = response.json()
                        namaIG = str(data['user']['full_name'])
                        bioIG = str(data['user']['biography'])
                        mediaIG = str(data['user']['media']['count'])
                        verifIG = str(data['user']['is_verified'])
                        usernameIG = str(data['user']['username'])
                        followerIG = str(data['user']['followed_by']['count'])
                        profileIG = data['user']['profile_pic_url_hd']
                        privateIG = str(data['user']['is_private'])
                        followIG = str(data['user']['follows']['count'])
                        link = "Link: " + "https://www.instagram.com/" + instagram
                        text = "Name : "+namaIG+"\nUsername : "+usernameIG+"\nBiography : "+bioIG+"\nFollower : "+followerIG+"\nFollowing : "+followIG+"\nPost : "+mediaIG+"\nVerified : "+verifIG+"\nPrivate : "+privateIG+"" "\n" + link
                        kr1.sendImageWithURL(msg.to, profileIG)
                        kr1.sendText(msg.to, str(text))
                    except Exception as e:
                        kr1.sendText(msg.to, str(e))
#==========================[Kris]===========================
            elif "Kelahiran " in msg.text:
                #if msg.from_ in admin:
                    tanggal = msg.text.replace("Kelahiran ","")
                    r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                    data=r.text
                    data=json.loads(data)
                    lahir = data["data"]["lahir"]
                    usia = data["data"]["usia"]
                    ultah = data["data"]["ultah"]
                    zodiak = data["data"]["zodiak"]
                    kr1.sendText(msg.to,"============ I N F O R M A S I ============\n"+"Date Of Birth : "+lahir+"\nAge : "+usia+"\nUltah : "+ultah+"\nZodiak : "+zodiak+"\n============ I N F O R M A S I ============")
#==========================[Kris]===========================
            elif msg.text in ["Kalender"]:
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
            elif msg.text in ["Botak"]:
                random.choice(KAC).sendImageWithURL(msg.to, url123)
                random.choice(KAC).sendText(msg.to,"↥↥↥↥↥↪ Pembuat Bots ↩↥↥↥↥↥")
            elif msg.text in ["ifconfig"]:
                #if msg.from_ in admin:
                    botKernel = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE).communicate()[0]
                    kr1.sendText(msg.to, botKernel + "\n\n===SERVER INFO NetStat===")
            elif msg.text in ["system"]:
                #if msg.from_ in admin:
                    botKernel = subprocess.Popen(["df","-h"], stdout=subprocess.PIPE).communicate()[0]
                    kr1.sendText(msg.to, botKernel + "\n\n===SERVER INFO SYSTEM===")
            elif msg.text in ["kernel"]:
                #if msg.from_ in admin:
                    botKernel = subprocess.Popen(["uname","-srvmpio"], stdout=subprocess.PIPE).communicate()[0]
                    kr1.sendText(msg.to, botKernel + "\n\n===SERVER INFO KERNEL===")
            elif msg.text in ["cpu"]:
                #if msg.from_ in admin:
                    botKernel = subprocess.Popen(["cat","/proc/cpuinfo"], stdout=subprocess.PIPE).communicate()[0]
                    kr1.sendText(msg.to, botKernel + "\n\n===SERVER INFO CPU===")
#==========================[Kris]===========================
            elif "Restart" in msg.text:
                #if msg.from_ in owner:
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
                #if msg.from_ in owner:
                    try:
                        import sys
                        sys.exit()
                    except:
                        pass
#==========================[Kris]===========================
            elif msg.text in ["runtime","Runtime"]:
                #if msg.from_ in admin:
                    eltime = time.time() - mulai
                    van = "Bot has been active "+waktu(eltime)
                    kr1.sendText(msg.to,van)
#==========================[Kris]===========================
            elif msg.text in ["Kr kemari"]: # Keluar Dari Semua Group Yang Di dalem nya  ada bot(Kalo Bot Kalian Nyangkut di Group lain :D)
                #if msg.from_ in owner:
                    gid = kr1.getGroupIdsJoined()
                    gid = kr2.getGroupIdsJoined()
                    gid = kr3.getGroupIdsJoined()
                    for i in gid:
                        kr1.sendText(i,"Bye~Bye " + str(ginfo.name) + "\n\nBots Dipaksa Keluar oleh Owner Bots...!!!\nMakasih...!!!")
                        kr1.leaveGroup(i)
                        kr2.leaveGroup(i)
                        kr3.leaveGroup(i)
                    if wait["lang"] == "JP":
                        kr1.sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nBots Dipaksa Keluar oleh Owner Bots...!!!\nMakasih...!!!")
                    else:
                        kr1.sendText(msg.to,"He declined all invitations")
#==========================[Kris]=========================== 
            elif msg.text in ["cab","Cab"]:
                #if msg.from_ in admin:
                    url = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26168676_131451404314083_3952554270011807487_n.jpg?oh=6e90aa78daaf5e06b1078bbf15d5aa0f&oe=5AB9882D"
                    kr1.sendImageWithURL(msg.to, url)
                
            elif msg.text in ["cab1","Cab1"]:
                #if msg.from_ in admin:
                    url = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26165506_131451400980750_8433498092579272217_n.jpg?oh=c85beaa35a6f5babd638edeaac9bccaa&oe=5AF760B2"
                    kr1.sendImageWithURL(msg.to, url)
                
            elif msg.text in ["cab2","Cab2"]:
                #if msg.from_ in admin:
                    url = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26168227_131451417647415_680587542176648285_n.jpg?oh=e714a97fec8d8c1e178ab6c0a3ca39cf&oe=5AC96AD3"
                    kr1.sendImageWithURL(msg.to, url)
                
            elif msg.text in ["cab3","Cab3"]:
                #if msg.from_ in admin:
                    url = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26195387_131462840979606_8781956575640573461_n.jpg?oh=27ba5e875917c20df7dd8916bdd64847&oe=5ABB27F4"
                    kr1.sendImageWithURL(msg.to, url)
                
            elif msg.text in ["cab4","Cab4"]:
                #if msg.from_ in admin:
                    url = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26111928_131462844312939_2544207656543605714_n.jpg?oh=0fac796564e963d8b573826263bbc6c7&oe=5AFA67A8"
                    kr1.sendImageWithURL(msg.to, url)
                
            elif msg.text in ["cab5","Cab5"]:
                #if msg.from_ in admin:
                    url = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26219732_131462837646273_1213898565647052451_n.jpg?oh=c5a8bcce115cdab488bde1b8e981e5dd&oe=5AC3A96E"
                    kr1.sendImageWithURL(msg.to, url)
                
            elif msg.text in ["cab6","Cab6"]:
                #if msg.from_ in admin:
                    url = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26167549_131462897646267_3496884138024907307_n.jpg?oh=edc63b98f790e9bf2cbb57dce7df9b25&oe=5AB0DDF6"
                    kr1.sendImageWithURL(msg.to, url)
                
            elif msg.text in ["cab7","Cab7"]:
                #if msg.from_ in admin:
                    url = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26111931_131462894312934_151942458148573227_n.jpg?oh=2b0473a6caf4446df430180a47ca3355&oe=5AC37B56"
                    kr1.sendImageWithURL(msg.to, url)
                
            elif msg.text in ["Team","Logo"]:
                #if msg.from_ in admin:
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
                #if msg.from_ in admin:
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
            elif "friendpp: " in msg.text:
                #if msg.from_ in admin:
                    suf = msg.text.replace('friendpp: ','')
                    gid = kr1.getAllContactIds()
                    for i in gid:
                        h = kr1.getContact(i).displayName
                        gna = kr1.getContact(i)
                        if h == suf:
                            kr1.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)
#==========================[Kris]===========================
            elif "Checkmid: " in msg.text:
                #if msg.from_ in admin:
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
                #if msg.from_ in admin:
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
                #if msg.from_ in owner:
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
                #if msg.from_ in owner:
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
                #if msg.from_ in owner:
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
                #if msg.from_ in owner:
                    saya = msg.text.replace('Friendpict: ','')
                    gid = kr1.getAllContactIds()
                    for i in gid:
                        h = kr1.getContact(i).displayName
                        gna = kr1.getContact(i)
                        if h == saya:
                            kr1.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)
#==========================[Kris]===========================
            elif msg.text in ["Friendlistmid"]:
                #if msg.from_ in owner:
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
                #if msg.from_ in admin:
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
                #if msg.from_ in admin:
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
                #if msg.from_ in owner:
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
                #if msg.from_ in admin:
                    saya = msg.text.replace('Grupimage: ','')
                    gid = kr1.getGroupIdsJoined()
                    for i in gid:
                        h = kr1.getGroup(i).name
                        gna = kr1.getGroup(i)
                        if h == saya:
                            kr1.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)
#==========================[Kris]===========================  
            elif "Grupname" in msg.text:
                #if msg.from_ in admin:
                    saya = msg.text.replace('Grupname','')
                    gid = kr1.getGroup(msg.to)
                    kr1.sendText(msg.to, "[Nama Grup : ]\n" + gid.name)
#==========================[Kris]=========================== 
            elif "Grupid" in msg.text:
                #if msg.from_ in admin:
                    saya = msg.text.replace('Grupid','')
                    gid = kr1.getGroup(msg.to)
                    kr1.sendText(msg.to, "[ID Grup : ]\n" + gid.id)
#==========================[Kris]===========================      
            elif "Grupinfo: " in msg.text:
                #if msg.from_ in admin:
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

            elif 'wikipedia ' in msg.text.lower():
                #if msg.from_ in admin:
                    try:
                        wiki = msg.text.lower().replace("wikipedia ","")
                        wikipedia.set_lang("id")
                        pesan="Title ("
                        pesan+=wikipedia.page(wiki).title
                        pesan+=")\n\n"
                        pesan+=wikipedia.summary(wiki, sentences=3)
                        pesan+="\n"
                        pesan+=wikipedia.page(wiki).url
                        kr1.sendText(msg.to, pesan)
                    except:
                            try:
                                pesan="Teks nya kepanjangan! ketik link dibawah aja\n"
                                pesan+=wikipedia.page(wiki).url
                                kr1.sendText(msg.to, pesan)
                            except Exception as e:
                                kr1.sendText(msg.to, str(e))    
#==========================[Kris]===========================
            elif "say " in msg.text.lower():
                #if msg.from_ in admin:
                    say = msg.text.lower().replace("say ","")
                    lang = 'id'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    kr1.sendAudio(msg.to,"hasil.mp3")
#==========================[Kris]===========================
            elif msg.text in ["Gift 8","Gift8","gift8"]:
                #if msg.from_ in admin:
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
            elif 'lirik ' in msg.text.lower():
                #if msg.from_ in admin:
                    try:
                        songname = msg.text.lower().replace('lirik ','')
                        params = {'songname': songname}
                        r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                        data = r.text
                        data = json.loads(data)
                        for song in data:
                            hasil = 'Lyric Lagu ('
                            hasil += song[0]
                            hasil += ')\n\n'
                            hasil += song[5]
                            kr1.sendText(msg.to, hasil)
                    except Exception as wak:
                            kr1.sendText(msg.to, str(wak))       
#==========================[Kris]===========================
            elif "Getcover @" in msg.text:
                #if msg.from_ in admin:
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
            elif "idline: " in msg.text:
                #if msg.from_ in admin:
                    msgg = msg.text.replace('idline: ','')
                    conn = kr1.findContactsByUserid(msgg)
                    if True:
                        msg.contentType = 13
                        msg.contentMetadata = {'mid': conn.mid}
                        kr1.sendText(msg.to,"http://line.me/ti/p/~" + msgg)
                        kr1.sendMessage(msg)
#==========================[Kris]===========================   
            elif "reinvite" in msg.text.split():
                #if msg.from_ in admin:
                    if msg.toType == 2:
                        group = kr1.getGroup(msg.to)
                        if group.invitee is not None:
                            try:
                                grCans = [contact.mid for contact in group.invitee]
                                kr1.findAndAddContactsByMid(msg.to, grCans)
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
            elif "image " in msg.text:
                #if msg.from_ in admin:
                    search = msg.text.replace("image ","")
                    url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                    raw_html = (download_page(url))
                    items = []
                    items = items + (_images_get_all_items(raw_html))
                    path = random.choice(items)
                    print path
                    try:
                        kr1.sendImageWithURL(msg.to,path)
                    except:
                        pass
#==========================[Kris]===========================
            elif 'instagram ' in msg.text.lower():
                #if msg.from_ in admin:
                    try:
                        instagram = msg.text.lower().replace("instagram ","")
                        html = requests.get('https://www.instagram.com/' + instagram + '/?')
                        soup = BeautifulSoup(html.text, 'html5lib')
                        data = soup.find_all('meta', attrs={'property':'og:description'})
                        text = data[0].get('content').split()
                        data1 = soup.find_all('meta', attrs={'property':'og:image'})
                        text1 = data1[0].get('content').split()
                        user = "Name: " + text[-2] + "\n"
                        user1 = "Username: " + text[-1] + "\n"
                        followers = "Followers: " + text[0] + "\n"
                        following = "Following: " + text[2] + "\n"
                        post = "Post: " + text[4] + "\n"
                        link = "Link: " + "https://www.instagram.com/" + instagram
                        detail = "**INSTAGRAM INFO USER**\n"
                        details = "\n**INSTAGRAM INFO USER**"
                        kr1.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                        kr1.sendImageWithURL(msg.to, text1[0])
                    except Exception as njer:
                    	kr1.sendText(msg.to, str(njer))    
#==========================[Kris]===========================
            elif msg.text in ["Clear"]:
                #if msg.from_ in admin:
                    wait["blacklist"] = {}
                    kr1.sendText(msg.to,"Blacklist Telah Dibersihkan")
#==========================[Kris]===========================
            elif "Kr spamtag @" in msg.text:
                #if msg.from_ in owner:
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
            elif msg.text in ["Kr glist"]: #Melihat List Group
                #if msg.from_ in owner:
                    gids = kr1.getGroupIdsJoined()
                    h = ""
                    for i in gids:
                      #####gn = kr1.getGroup(i).name
                      h += "[•]%s Member\n" % (kr1.getGroup(i).name   +"👉"+str(len(kr1.getGroup(i).members)))
                      kr1.sendText(msg.to,"=======[List Group]======\n"+ h +"Total Group :"+str(len(gids)))
                
            elif msg.text in ["Kr glist2"]: 
                #if msg.from_ in owner:
                    gid = kr1.getGroupIdsJoined()
                    h = ""
                    for i in gid:
                      h += "[%s]:%s\n" % (kr1.getGroup(i).name,i)
                      kr1.sendText(msg.to,h)

#==========================[Kris]===========================
            elif "recover" in msg.text:
                #if msg.from_ in owner:
                    thisgroup = kr1.getGroups([msg.to])
                    Mids = [contact.mid for contact in thisgroup[0].members]
                    mi_d = Mids[:33]
                    kr1.createGroup("recover", mi_d)
                    kr1.sendText(msg.to,"Success recover")
#==========================[Kris]===========================
            elif "Kr spin" in msg.text:
                #if msg.from_ in owner:
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
                #if msg.from_ in owner:
                    kr1.removeAllMessages(op.param2)
                    kr1.removeAllMessages(op.param2)
                    kr1.sendText(msg.to,"Removed all chat Finish")
#==========================[Kris]===========================
        if op.type == 5:
            if wait['autoAdd'] == True:
                if (wait['message'] in [""," ","\n",None]):
                    pass
                else:
                    kr1.sendText(op.param1.str(wait['message']))
        
        if op.type == 17:
           if wait["Wc"] == True:
               if op.param2 in Bots:
                 return
               ginfo = kr1.getGroup(op.param1)
               kr1.sendText(op.param1, "╔═════════════\n║Selamat Datang Di  " + str(ginfo.name) + "\n╠═════════════\n" + "║owner =>>> " + str(ginfo.name) + " :\n║" + ginfo.creator.displayName + "\n╠═════════════\n" + "║😊Semoga Betah Kak 😘 \n╚═════════════")
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
            
        
        if op.type == 55:
            try:
                if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = kr1.getContact(op.param2).displayName
                            Np = kr1.getContact(op.param2).pictureStatus
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n• " + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        kr1.sendText(op.param1, "Hallo.. " + "☞ " + nick[0] + " ☜" + "\nNah jangan ngintip mulu 😁. . .\nGabung Chat yux 😉")
                                        kr1.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net/" + Np)
                                    else:
                                        kr1.sendText(op.param1, "Hallo.. " + "☞ " + nick[1] + " ☜" + "\nJangan ngintip.. 😏. . .\nMasuk  ayox... 😆😂😛")
                                        kr1.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net/" + Np)
                                else:
                                    kr1.sendText(op.param1, "hallo.. " + "☞ " + Name + " ☜" + "\nJangan ngintip aja\nMasuk gabung chat ya...😋 😝")
                                    kr1.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net/" + Np)
                        else:
                            pass
                else:
                    pass
            except:
                pass
        else:
            pass
    
        if op.type == 55:
            try:
                if ngintip['intip'][op.param1]==True:
                        if op.param1 in ngintip['target']:
                            Name = kr1.getContact(op.param2).displayName
                            if Name in ngintip['toong'][op.param1]:
                                pass
                            else:
                                ngintip['toong'][op.param1] += "\n• " + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        kr1.sendText(op.param1, "Hallo.. " + "☞ " + nick[0] + " ☜" + "\nNah jangan ngintip mulu 😁. . .\nGabung Chat yux 😉")
                                    else:
                                        kr1.sendText(op.param1, "Hallo.. " + "☞ " + nick[1] + " ☜" + "\nJangan ngintip.. 😏. . .\nMasuk  ayox... 😆😂😛")
                                else:
                                    kr1.sendText(op.param1, "hallo.. " + "☞ " + Name + " ☜" + "\nJangan ngintip aja\nMasuk gabung chat ya...😋 😝")
                        else:
                            pass
                else:
                    pass
            except:
                pass
        else:
            pass
        
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
