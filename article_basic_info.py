import urllib.request as req
import urllib
import urllib3
import requests
import bs4 
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import re
import time
from article_content import post_scraper

prefix = "https://www.ptt.cc"

class title_scraper:

    def __init__(self, page_url):
        self.page_url = page_url
        self.dates_item = []
        self.posters_item = []
        self.precise_times = []
        self.title_item = []
        self.data = []
        self.link_for_post =  []
        self.like_for_post = []
        # self.IP_list = []



    def send_request(self):
        #######establish an object for imitate a human brower
        request = req.Request(self.page_url, headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
            "cookie":"over18=1;"})
        with req.urlopen(request) as response:
            self.data = response.read().decode("utf-8")

    def crawling_title(self):
        ######analyse the data we got
        soup = bs4.BeautifulSoup(self.data, "html.parser")
        titles = soup.find_all("div", class_="title")  
        dates = soup.find_all("div", class_= "date")
        posters = soup.find_all("div", class_="author")
        likes = soup.find_all("div", class_="nrec")
    

        ########find likes for each post
        for like in likes:
            if like.find("span") != None:
                self.like_for_post.append(like.find("span").string)
            else:
                self.like_for_post.append(" ")

        ########find the date of the post
        for date in dates:
            if date != None:
                self.dates_item.append(date.string)
            else:
                self.dates_item.append("unknown")
                continue

        ########find posters
        for poster in posters:
            if poster != None:
                self.posters_item.append(poster.string)

        ########find the title of the post
        for title in titles:
            if title.find("a") != None:
                if len(title.find("a")) != 0:
                    title = title.find("a").string
                    self.title_item.append(title)
            else:
                self.title_item.append("此文已被刪除")
                continue

        ########find url for each post
        for title in titles:
            if title.find("a") == None:
                self.link_for_post.append("N/A")
                self.precise_times.append("N/A")
            elif len(title.find("a")["href"]) != 0:
                link_for_post = title.find("a")["href"]
                self.link_for_post.append(prefix + link_for_post)
                link_post = prefix + link_for_post
                scrape_info = post_scraper(link_post)
                scrape_info.send_request()
                time = scrape_info.crawling_post()
                self.precise_times.append(time)
                # self.IP_list.append(locations)


        nextpagelink = soup.find("a", string="‹ 上頁")   
        return nextpagelink["href"]

    

    def post_all(self):

        for i in range(len(self.title_item)):
            print(
                self.like_for_post[i],
                self.dates_item[i],
                self.precise_times[i], 
                self.title_item[i], 
                self.posters_item[i],
                self.link_for_post[i],
                )