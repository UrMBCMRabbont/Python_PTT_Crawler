import urllib.request as req
import urllib
import urllib3
import requests
import bs4
from scraper_post import post_scraper
import pandas as pd 
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import re
from keyboard import press
import time


def send_request(url):
        #######establish an object for imitate a human brower
        request = req.Request(url, headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
            "cookie":"over18=1;"})
        with req.urlopen(request) as response:
            data = response.read().decode("utf-8")
            print(data)

def enter_feature(query):
        ######enter in the search_bar
        payload = {"q" : query}
        r = requests.post("https://www.ptt.cc/bbs/Gossiping/index.html", data=payload)
        print(r.text)
        print("----------------")
        return r.text

send_request("https://www.ptt.cc/ask/over18?from=%2Fbbs%2FGossiping%2Fsearch%3Fq%3D%25E6%25AD%25A3%25E5%25A6%25B9")
