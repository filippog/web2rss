#!/usr/bin/env python

import re

import BeautifulSoup
from PyRSS2Gen import RSSItem, Guid
import ScrapeNFeed

from datetime import date

class Monty(ScrapeNFeed.ScrapedFeed):
    def HTML2RSS(self, headers, body):
        soup = BeautifulSoup.BeautifulSoup(body)
        today = soup('img', onload=re.compile("^STR.AttachZoomHover"), src=re.compile("^http://assets.comics.com/dyn/"))[0]

        title = today['alt']
        link = today['src']

        if not self.hasSeen(link):
            i = RSSItem(title=title,
                        description = '<img src="%s"/>' % link,
                        link=link)
            self.pushRSSItem(i)

Monty.load("Monty",
           'http://comics.com/monty/',
           "Monty by Jim Meddick",
           'monty.xml',
           'state/monty.pickle')

class Culdesac(ScrapeNFeed.ScrapedFeed):
    def HTML2RSS(self, headers, body):
        soup = BeautifulSoup.BeautifulSoup(body)

        title = soup.find('ul', attrs = {'class': 'feature-nav'}).li.string
        link = soup.find('link', attrs={'rel': 'image_src'})['href']
        description = '<img src="%s"/>' % link

        if not self.hasSeen(link):
            i = RSSItem(title=title,
                        description = description,
                        link=link)
            self.pushRSSItem(i)

Culdesac.load("Cul de sac",
              "http://www.gocomics.com/culdesac",
              "Cul de sac by Richard Thompson",
              'culdesac.xml',
              'state/culdesac.pickle',
              headers = [('User-agent', 'Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.0.3) Gecko/2008092414 Firefox/3.0.3')]
              )

class Maakies(ScrapeNFeed.ScrapedFeed):
    def HTML2RSS(self, headers, body):
        soup = BeautifulSoup.BeautifulSoup(body)
        today = soup('img', src=re.compile("^http://www.maakies.com/archive/m\d+.gif"))[0]

        link = today['src']

        # XXX fix title scraping

        if not self.hasSeen(link):
            i = RSSItem(title=date.today().strftime("Maakies - %d/%m/%Y"),
                        description = '<img src="%s"/>' % link,
                        link=link)
            self.pushRSSItem(i)

Maakies.load("Maakies",
           'http://www.maakies.com',
           "Maakies by Tony Millionaire",
           'maakies.xml',
           'state/maakies.pickle')
# vim:et
