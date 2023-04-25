# -*- coding: utf-8 -*-
from requests_oauthlib import OAuth1Session, OAuth1
import json
import requests
import urllib
import sys
import tkinter

#tkinterでウィンドウを新規作成
window = tkinter.Tk()
window.title(u'Tweetを表示')

#APIキー情報設定
consumer_key = "自分の consumer_key"
consumer_key_secret = "自分の consumer_key_secret"
access_token = "自分の access_token"
access_token_secret = "自分の access_token_secret"

#Twitter APIアクセス
def search_tweets(event):
    word = search_form.get()
    url = "https://api.twitter.com/1.1/search/tweets.json?count=10&q=" + word
    auth = OAuth1(consumer_key, consumer_key_secret, access_token, access_token_secret)
    response = requests.get(url, auth = auth)
    data = response.json()['statuses']
    change_char = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
    
    for i, tweet in enumerate(data):
        label_array[i].configure(text = tweet["text"].translate(change_char))
        
#tkinterの入力フォーム作成
search_form = tkinter.Entry()
search_form.insert(tkinter.END,"テスト")
search_form.pack()

#tkinterの検索ボタン作成
button = tkinter.Button(text='検索', width=50)
#左クリック（<Button-1>）でsearch_tweets()関数を呼び出す
button.bind("<Button-1>",search_tweets) 
button.pack()

#tkinterのツイート表示用ラベルの作成
label_array = [tkinter.Label(window, text="ツイート{}".format(i)) for i in range(10)]
for i in range(10):
    label_array[i].pack()

window.geometry('800x600')
window.mainloop()
