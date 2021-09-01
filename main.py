from article_content import post_scraper
from article_advanced_info import feature_scraper
from article_basic_info import title_scraper


URL = "https://www.ptt.cc/bbs/Gossiping/index.html"
URL_for_search = "https://www.ptt.cc/bbs/Gossiping/search?q="
prefix = "https://www.ptt.cc"
num_page = int(input("Enter the page number you want : "))
mode_value = 0

        
for i in range(num_page):

    if i == 0:
        scrape_title = title_scraper(URL)
        scrape_title.send_request()
        next_url = scrape_title.crawling_title()
        scrape_title.post_all()
    else:
        URL = prefix + next_url
        scrape_title = title_scraper(URL)
        scrape_title.send_request()
        next_url = scrape_title.crawling_title()
        scrape_title.post_all()