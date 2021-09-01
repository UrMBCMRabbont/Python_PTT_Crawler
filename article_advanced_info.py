import urllib.request as req
import urllib
import urllib3
import requests
import bs4
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

prefix = "https://www.ptt.cc"

class feature_scraper():

    def __init__(self, page_url, writer_name, upvotes_num):
        self.page_url = page_url
        self.writer_name = writer_name
        self.upvotes_num = upvotes_num
        self.like_for_post = []
        self.dates_item = []
        self.data = []
        self.title_item = []
        self.link_for_post = []
        self.precise_times = []
        self.posters_item = []

        

    def send_request(self):
        #######establish an object for imitate a human brower
        request = req.Request(self.page_url, headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
            "cookie":"over18=1;"})
        with req.urlopen(request) as response:
            self.data = response.read().decode("utf-8")
            print(self.data)


    def crawling_feature(self):
        soup = bs4.BeautifulSoup(self.data, "html.parser")
        titles = soup.find_all("div", class_="title")  
        dates = soup.find_all("div", class_= "date")
        posters = soup.find_all("div", class_="author")
        likes = soup.find_all("div", class_="nrec")
        
        print(len(titles))
        for title in titles:
            if title.find("a") != None:
                if len(title.find("a")) != 0:
                    title = title.find("a").string
                    self.title_item.append(title)
            else:
                self.title_item.append("此文已被刪除")
                continue

        for like in likes:
            if like.find("span") != None:
                self.like_for_post.append(like.find("span").string)
            else:
                self.like_for_post.append(" ")

        for date in dates:
            if date != None:
                self.dates_item.append(date.string)
            else:
                self.dates_item.append("unknown")
                continue

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

        for poster in posters:
            if poster != None:
                self.posters_item.append(poster.string)

        try:
            nextpagelink = soup.find("a", string="‹ 上頁")   
            return nextpagelink["href"]
        except:
            pass
        

    def post_all(self):
        print(len(self.title_item))
        for i in range(len(self.title_item)):
            print(
                self.like_for_post[i],
                self.dates_item[i],
                self.precise_times[i], 
                self.title_item[i], 
                self.posters_item[i],
                self.link_for_post[i]
            )