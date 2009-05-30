#!/usr/bin/env python

import re

import BeautifulSoup
from PyRSS2Gen import RSSItem, Guid
import ScrapeNFeed

from datetime import date

class ManifestoPrima(ScrapeNFeed.ScrapedFeed):    
    def HTML2RSS(self, headers, body):
        import copy

        #massage = copy.copy(BeautifulSoup.BeautifulStoneSoup.MARKUP_MASSAGE)
        #script_massage = [(re.compile("sc'\+'ript"), lambda m: "script")] 
        #massage.extend(script_massage)
        #soup = BeautifulSoup.BeautifulSoup(body, markupMassage=massage)

        soup = BeautifulSoup.BeautifulSoup(body)

        #rellink = soup('img', src=re.compile("fileadmin/archivi/in_edicola/\d+prima.gif"))[0]['src']
        #link = "http://www.ilmanifesto.it/" + re.sub('prima.gif', 'primapagina.gif', rellink)

        rellink = soup('img', src=re.compile("fileadmin/archivi/in_edicola/\d+primapagina.gif"))[0]['src']
        link = "http://www.ilmanifesto.it/" + rellink

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

# vim:et
