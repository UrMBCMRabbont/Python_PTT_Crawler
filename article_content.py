import urllib.request as req
import requests
import ssl
import bs4
ssl._create_default_https_context = ssl._create_unverified_context
import re

###grab the info only exist in the content

class post_scraper:

    def __init__(self, link_post):
        self.link_post = link_post
        self.data = []
        self.post_time = []
        self.locations = []
    
    def send_request(self):
        #######establish an object for imitate a human brower
        request = req.Request(self.link_post, headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
            "cookie":"over18=1;"})
        with req.urlopen(request) as response:
            self.data = response.read().decode("utf-8")
            return self.data

    def crawling_post(self):
        soup = bs4.BeautifulSoup(self.data, "html.parser")
        # for i in range(3):
        times = soup.find_all("div", class_="article-metaline")
        # soup.find_all('a', {'href': re.compile(r'crummy\.com/')})


        ####find exact time
        i = 0
        for time in times:
            if time.find("span", class_="article-meta-value") != None and len(time.find("span", class_="article-meta-value")) != 0:
                for item in time.find("span", class_="article-meta-value"):
                    if i == 2:
                        self.post_time.append(item.string)
            else:
                self.post_time.append("N/A")
            i = i + 1
        #####self.locations   
        
        return self.post_time
            

                