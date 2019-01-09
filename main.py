#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

# 自分の環境ではpipのインストール先のpathが通っていなかったのでpathを追加しました.

# ---
import sys
sys.path.append("/usr/local/lib/python2.7/site-packages")
# ---

import nfc
import re
import time

# message_write
## 書き込み
def message_write(sttr):
  f = open('attend.txt', 'a')
  f.write(sttr + "\n")
  f.close()

# on_connect
## fekicaのセットアップ時に発火
def on_startup(target):
  def on_startup(targets):
    print("on_startup()")
    print targets
    #return targets

# on_connect
## felicaにタッチした時に発火
def on_connected(tag):
  for line in tag.dump(): 
    pattern = r"0000: 30"
    matchLine = re.search(pattern, line)
    if matchLine:
      uId = line.split('|')      
      message = '{ \"time\" : \"' + time.ctime() + '\", \"uId\" : \"' + uId[1][4:14] + '\" }'
      message_write(message)
      print "学籍番号 : " + uId[1][4:14] + " の出席を確認しました！"
      break

  time.sleep(2)
  print('学生証をかざしてください：')

# on-release
## felicaを離した時に発火
def on_released(tag):
  #print(tag)
  print('学生証をかざしてください：')

  time.sleep(2)
  
# main
## 
def main():
  
  rdwr_options = {
    #'on-startup': on_startup,
    'on-connect': on_connected,
    'on-release': on_released
  }

  # usb devise との接続を行う
  clf = nfc.ContactlessFrontend('usb')
  print(clf)

  print "学生証をかざしてください："

  if clf:
    while clf.connect(rdwr=rdwr_options):
      pass

if __name__ == '__main__':
  main()