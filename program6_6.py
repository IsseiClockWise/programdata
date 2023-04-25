import urllib.request
url = 'https://www.google.co.jp/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png'
saveimage = 'logo.png'

urllib.request.urlretrieve(url, saveimage)
print("保存完了しました")
