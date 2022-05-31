import tkinter as tk
from gettext import find
from multiprocessing.sharedctypes import Value
from os import link, name
from tkinter import N
from typing import final
import urllib  
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import requests
import easygui
import os
import urllib.request
import xurls
from lxml import html
import lxml
import bs4
from lxml.html.soupparser import parse
from bdownload import BDownloader
from urlextract import URLExtract
import tldextract
from urllib.parse import urlparse, urljoin
import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("iOS Image Downloader-Bilawal")
        #setting window size
        width=500
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GMessage_120=tk.Message(root)
        GMessage_120["bg"] = "#393d49"
        ft = tkFont.Font(family='Times',size=10)
        GMessage_120["font"] = ft
        GMessage_120["fg"] = "#90f090"
        GMessage_120["justify"] = "center"
        GMessage_120["text"] = ""
        GMessage_120.place(x=0,y=0,width=500,height=500)

        GLabel_286=tk.Label(root)
        GLabel_286["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=24)
        GLabel_286["font"] = ft
        GLabel_286["fg"] = "#cc0000"
        GLabel_286["justify"] = "center"
        GLabel_286["text"] = "iOS Image Downloader"
        GLabel_286.place(x=0,y=80,width=505,height=67)

        GButton_722=tk.Button(root)
        GButton_722["bg"] = "#ff4500"
        ft = tkFont.Font(family='Times',size=28)
        GButton_722["font"] = ft
        GButton_722["fg"] = "#000000"
        GButton_722["justify"] = "center"
        GButton_722["text"] = "iPhone"
        GButton_722.place(x=60,y=260,width=150,height=150)
        GButton_722["command"] = self.GButton_722_command

        GButton_136=tk.Button(root)
        GButton_136["bg"] = "#ff4500"
        ft = tkFont.Font(family='Times',size=28)
        GButton_136["font"] = ft
        GButton_136["fg"] = "#000000"
        GButton_136["justify"] = "center"
        GButton_136["text"] = "iPad"
        GButton_136.place(x=280,y=260,width=150,height=150)
        GButton_136["command"] = self.GButton_136_command

    def GButton_722_command(self):
        path = 'iPhone-Images'
        if not os.path.exists(path):
         os.makedirs(path)
        
        url = easygui.enterbox(msg="iPhone", title="BilawalM")
        Values = (url + "?platform=iphone")
        htmldata = urlopen(Values)
        soup = BeautifulSoup(htmldata, 'lxml')
        aas = soup.find_all("source", type="image/webp")
        imagelinks = []
        for item in aas:
            src = item.get("srcset")
            src4 = (src)
            src7 = re.findall("AppIcon", src4)

            if src7:
                None
            else:
                src5= (re.sub('626x0w.webp',"9999x0w.jpg", src4 ))
                src8 = re.findall("626x0w.webp", src4)
                if src8:
                    src5= (re.sub('626x0w.webp', "9999x0w.jpg", src4))
                    #print("H")
                else:
                    src5= (re.sub('460x0w.webp', "9999x0w.jpg", src4))
                    #print("V")
                src6= str(src5)
                a2 = src6.replace('[[' ,'').replace(']]', '').replace( " 626w", '\n').replace( " 460w", '\n')
                src14= str(a2)
                if re.findall("460x0w.webp",src4):
                    ch = '314w, '
                else:
                    ch = '434w, '
                pattern  = ".*" + ch 
                src14 = re.sub(pattern, '', src14)
                src15 = src14              
                from yarl import URL
                url1 = URL(src15)
                    #print ("got links")
                imagelinks.append(url1)
                for i, imagelink in enumerate(imagelinks):
                        response = requests.get(imagelink)
                        imagename = "iPhone-Images" + '/' + "data" + str(i+1) + '.jpg'
                        if response.status_code == 200:
                            with open(imagename, 'wb') as file:
                                file.write(response.content)
       


    def GButton_136_command(self):
        path = 'iPad-Images'
        if not os.path.exists(path):
         os.makedirs(path) 

        url = easygui.enterbox(msg="iPad", title="BilawalM")
        Values = (url + "?platform=ipad")
        htmldata = urlopen(Values)
        soup = BeautifulSoup(htmldata, 'lxml')
        aas = soup.find_all("source", type="image/webp")
        imagelinks = []
        for item in aas:
            src = item.get("srcset")
            src4 = (src)
            src7 = re.findall("AppIcon", src4)

            if src7:
                    None
            else:
            
                src5= (re.sub('626x0w.webp', "9999x0w.jpg", src4))
                src6= str(src5)
                a2 = src6.replace('[[' ,'').replace(']]', '').replace( " 626w", '\n')
                src14= str(a2)
                ch = '434w, '
                pattern  = ".*" + ch 

                src14 = re.sub(pattern, '', src14)
                src15 = src14
                from yarl import URL
                url1 = URL(src15)
                #print ("got links")
                imagelinks.append(url1)
                for i, imagelink in enumerate(imagelinks):
                    response = requests.get(imagelink)
                    imagename = "iPad-Images" + '/' + "data" + str(i+1) + '.jpg'
                    if response.status_code == 200:
                        with open(imagename, 'wb') as file:
                            file.write(response.content)
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
