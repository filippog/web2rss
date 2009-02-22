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

        title = [ x.string[8:] for x in soup.findAll('dd') if x.string and x.string.startswith("Posted:") ][0]
        link = soup('img', alt=re.compile("^Cds\d+"), id=re.compile("^comic_\d+"))[0]['src']

        if not self.hasSeen(link):
            i = RSSItem(title=title,
                        description = '<img src="%s"/>' % link,
                        link=link)
            self.pushRSSItem(i)

Culdesac.load("Cul de sac",
              "http://www.gocomics.com/culdesac",
              "Cul de sac by Richard Thompson",
              'culdesac.xml', 
              'state/culdesac.pickle',
              headers = [('User-agent', 'Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.0.3) Gecko/2008092414 Firefox/3.0.3')]
              )

class ManifestoPrima(ScrapeNFeed.ScrapedFeed):    
    def HTML2RSS(self, headers, body):
        import copy

        massage = copy.copy(BeautifulSoup.BeautifulStoneSoup.MARKUP_MASSAGE)
        script_massage = [(re.compile("sc'\+'ript"), lambda m: "script")] 
        massage.extend(script_massage)

        soup = BeautifulSoup.BeautifulSoup(body, markupMassage=massage)

        rellink = soup('img', src=re.compile("fileadmin/archivi/in_edicola/\d+prima.gif"))[0]['src']
        link = "http://www.ilmanifesto.it/" + re.sub('prima.gif', 'primapagina.gif', rellink)

        if not self.hasSeen(link):
            i = RSSItem(title=date.today().strftime("il Manifesto prima pagina - %d/%m/%Y"),
                        description = '<img src="%s"/>' % link,
                        #description = "&lt;img src=&quot;%s&quot;/&gt;" % link,
                        link=link)
            self.pushRSSItem(i)

ManifestoPrima.load("il Manifesto",
                    "http://www.ilmanifesto.it/il-manifesto/in-edicola/numero/%s/pagina/IMMAGINE/" % date.today().strftime("%Y%m%d"),
                    "il Manifesto - prima pagina",
                    "manifesto_prima.xml",
                    "state/manifesto_prima.pickle")

#class ManifestoVignetta(ScrapeNFeed.ScrapedFeed):    
#    def HTML2RSS(self, headers, body):
#        import copy
#
#        massage = copy.copy(BeautifulSoup.BeautifulStoneSoup.MARKUP_MASSAGE)
#        script_massage = [(re.compile("sc'\+'ript"), lambda m: "script")] 
#        massage.extend(script_massage)
#
#        soup = BeautifulSoup.BeautifulSoup(body, markupMassage=massage)
#
#        rellink = soup('img', src=re.compile("fileadmin/archivi/in_edicola/\d+prima.gif"))[0]['src']
#        link = "http://www.ilmanifesto.it/" + re.sub('prima.gif', 'primapagina.gif', rellink)
#
#        if not self.hasSeen(link):
#            i = RSSItem(title=date.today().strftime("il Manifesto prima pagina - %d/%m/%Y"),
#                        description = "&lt;img src=&quot;%s&quot;/&gt;" % link,
#                        link=link)
#            self.pushRSSItem(i)
#
#ManifestoVignetta.load("il Manifesto",
#                    "http://www.ilmanifesto.it/il-manifesto/in-edicola/numero/%s/pagina/IMMAGINE/" % date.today().strftime("%Y%m%d"),
#                    "il Manifesto - vignetta",
#                    "manifesto_vignetta.xml",
#                    "manifesto_vignetta.pickle")
