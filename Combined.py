from os import link, name
from typing import final
import urllib  
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import requests
from urllib.request import urlopen
import easygui
import os
import urllib.request
import xurls

import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("BilawalM")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        

        GMessage_378=tk.Message(root)
        GMessage_378["bg"] = "#93c9ff"
        ft = tkFont.Font(family='Times',size=10)
        GMessage_378["font"] = ft
        GMessage_378["fg"] = "#333333"
        GMessage_378["justify"] = "center"
        GMessage_378["text"] = ""
        GMessage_378.place(x=0,y=0,width=600,height=496)

        GLabel_58=tk.Label(root)
        GLabel_58["bg"] = "#000000"
        ft = tkFont.Font(family='Times',size=34)
        GLabel_58["font"] = ft
        GLabel_58["fg"] = "#cc0000"
        GLabel_58["justify"] = "center"
        GLabel_58["text"] = "iOS Image Downloader"
        GLabel_58.place(x=0,y=50,width=598,height=137)

        GButton_966=tk.Button(root)
        GButton_966["bg"] = "#999999"
        ft = tkFont.Font(family='Times',size=28)
        GButton_966["font"] = ft
        GButton_966["fg"] = "#000000"
        GButton_966["justify"] = "center"
        GButton_966["text"] = "iPhone"
        GButton_966.place(x=70,y=250,width=173,height=150)
        GButton_966["command"] = self.GButton_966_command

        GButton_383=tk.Button(root)
        GButton_383["bg"] = "#999999"
        ft = tkFont.Font(family='Times',size=28)
        GButton_383["font"] = ft
        GButton_383["fg"] = "#000000"
        GButton_383["justify"] = "center"
        GButton_383["text"] = "iPad"
        GButton_383.place(x=360,y=250,width=173,height=150)
        GButton_383["command"] = self.GButton_383_command

    def GButton_966_command(self):
        
        path = 'iPhone-Images'
        if not os.path.exists(path):
         os.makedirs(path) 

        url = easygui.enterbox(msg="iPhone", title="BilawalM")
        Values = (url + "?platform=iphone")
        htmldata = urlopen(Values)
        soup = BeautifulSoup(htmldata, 'html.parser')
        aas = soup.find_all("source", class_="we-artwork__source", type="image/webp", media="(min-width: 1069px)")
        imagelinks = []
        for item in aas:
         src = item.get("srcset")
         src4 = (src)
         src7 = re.findall("AppIcon", src4)
         if src7:
          None
         else:
         # src5= (re.sub('460x0w.webp', "9999x0w.jpg", src4))
          src5= (re.sub('626x0w.webp',"9999x0w.jpg", src4 ))
          src8 = re.findall("626x0w.webp", src4)
          if src8:
           src5= (re.sub('626x0w.webp', "9999x0w.jpg", src4))
           #print("H")
          else:
           src5= (re.sub('460x0w.webp', "9999x0w.jpg", src4))
           #print("V")
          src6= str(src5)
          extractor = xurls.Strict()  
          urls = extractor.findall(src6)
          line1 = urls[1::2]
          line2 = ''.join(line1)
          imagelinks.append(line2)
          for i, imagelink in enumerate(imagelinks):
           response = requests.get(imagelink)
           imagename = "iPhone-Images" + '/' + "data" + str(i+1) + '.jpg'
           if response.status_code == 200:
            with open(imagename, 'wb') as file:
             file.write(response.content)
     
       


    def GButton_383_command(self):
        
        path = 'iPad-Images'
        if not os.path.exists(path):
         os.makedirs(path) 

        url = easygui.enterbox(msg="iPad", title="BilawalM")
        Values = (url + "?platform=ipad")
        htmldata = urlopen(Values)
        soup = BeautifulSoup(htmldata, 'html.parser')
        aas = soup.find_all("source", class_="we-artwork__source", type="image/webp", media="(min-width: 1069px)")
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
          extractor = xurls.Strict()  
          urls = extractor.findall(src6)
          line1 = urls[1::2]
          line2 = ''.join(line1)
          imagelinks.append(line2)
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
         

    


         


