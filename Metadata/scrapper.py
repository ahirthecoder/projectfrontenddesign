import requests
from bs4 import BeautifulSoup
import urllib
import regex as re

class Metadata:

    def __init__(self, URL):
        html_page = requests.get(URL)
        soup = BeautifulSoup(html_page.content, 'html.parser')
        self.title, self.image_link, self.discription = "", "", ""
        self.get_title(soup)
        self.get_image_link(soup)
        self.get_discription(soup)

    def get_title(self, soup):
        title = soup.find(class_ = "firstHeading")
        self.title = title.get_text()

    def get_image_link(self, soup):
        image_link = ""
        all_details = soup.find(class_ = "mw-parser-output")
        if (all_details is not None):
            image_tag = all_details.find('img')
            if (image_tag is not None):
                image_link = image_tag['src']
                self.image_link = image_link
                return
            right_thumbnail = soup.find(class_ = "thumbinner")
            if (right_thumbnail is not None):
                image_link = right_thumbnail.find('img')
                image_link = image_link['src']
                self.image_link = image_link
                return
        
        for raw_img in soup.find_all('img'):
            link = raw_img.get('src')
            if re.search('wikipedia/.*/thumb/', link) and not re.search('.svg', link):
                image_link = link
                break
        self.image_link = image_link

    def get_discription(self, soup):
        discription = ""
        all_details = soup.find(class_ = "mw-parser-output")
        if (all_details is None):
            self.discription = discription
            return

        discription = all_details.find(class_="shortdescription nomobile noexcerpt noprint searchaux")
        if ((discription is not None) and len(discription.get_text())!=0):
            self.discription = discription.get_text()
            return
        discription = all_details.find('p', class_=None)
        if ((discription is not None) and len(discription.get_text())!=0):
            self.discription = discription.get_text()
            return
        self.discription = ""

x = Metadata("https://en.wikipedia.org/wiki/Elon_Musk")
print("Title = " + x.title)
print("Image Link = " + x.image_link)
print("Discription = " + x.discription)