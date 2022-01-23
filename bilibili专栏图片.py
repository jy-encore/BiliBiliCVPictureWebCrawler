import http
import requests
import urllib.request
from bs4 import BeautifulSoup
from tkinter import *
import tkinter.filedialog

def getDir():
    dir=tkinter.filedialog.askdirectory()
    return dir

def getMoviesImg():
    inurl=str(input('输入哔哩哔哩专栏地址：'))
    #输入url
    url = requests.get(inurl)
    #获取网站数据
    html = url.text
    #解析网页
    soup = BeautifulSoup(html,'html.parser')
    #获取所有的img标签
    movie = soup.find_all('img')
    #获取本地路径
    dir=getDir()
    x = 1
    for i in movie:
        # 获取src路径
        imgsrc = i.get('data-src')
        #确认地址是否完整，不完整则补全
        if 'https:' in imgsrc:
            httpsimgsrc = imgsrc
        else:
            httpsimgsrc = 'https:'+ imgsrc
        #本地保存路径
        filename = dir+'/%s.jpg'%x
        urllib.request.urlretrieve(httpsimgsrc , filename)#下载保存
        print(httpsimgsrc)
        print('下载第%d张' % x)
        x += 1

    print('**下载完成!**')

getMoviesImg()
