#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

# 自分の環境ではpipのインストール先のpathが通っていなかったのでpathを追加しました.

# ---
import sys
sys.path.append("/usr/local/lib/python2.7/site-packages")
# ---

import re
import time
import nfc
import binascii

def message_write(sttr):
  f = open('attend.txt', 'a')
  f.write(sttr + "\n")
  f.close()

def on_connect(tag):
  print "読み込みました！"
  for line in tag.dump(): 
    pattern = r"0000: 30"
    matchLine = re.search(pattern, line)
    if matchLine:
      uId = line.split('|')      
      message = '{ \"time\" : \"' + time.ctime() + '\", \"uId\" : \"' + uId[1][4:14] + '\" }'
      message_write(message)
      print "学籍番号 : " + uId[1][4:14] + "の出席を確認しました！"
      break
  
def main():
  print "学生証をかざしてください:"
  with nfc.ContactlessFrontend('usb') as clf:
    clf.connect(rdwr={'on-connect': on_connect})

if __name__ == '__main__':
  main()