#!/usr/bin/env python

import re

import BeautifulSoup
from PyRSS2Gen import RSSItem, Guid
import ScrapeNFeed

from datetime import date

class ManifestoPrima(ScrapeNFeed.ScrapedFeed):
    def HTML2RSS(self, headers, body):
        import copy

        soup = BeautifulSoup.BeautifulSoup(body)

        rellink = soup.find('a', attrs = {'href': re.compile('pagina/IMMAGINE/$')})
        if not rellink:
            return
        rellink = rellink['href']

        today = re.search("numero/(\d+)/pagina/", rellink).group(1)
        link = "http://www.ilmanifesto.it/fileadmin/archivi/in_edicola/%sprimapagina.gif" % today

        if not self.hasSeen(link):
            i = RSSItem(title = "il Manifesto prima pagina - %s" % today,
                        description = '<img src="%s"/>' % link,
                        link=link)
            self.pushRSSItem(i)

ManifestoPrima.load("il Manifesto",
                    "http://www.ilmanifesto.it/il-manifesto/in-edicola/",
                    "il Manifesto - prima pagina",
                    "manifesto_prima.xml",
                    "state/manifesto_prima.pickle")

class ManifestoVignetta(ScrapeNFeed.ScrapedFeed):
    def HTML2RSS(self, headers, body):
        import copy

        soup = BeautifulSoup.BeautifulSoup(body)

        rellink = soup.find('a', attrs = {'href': re.compile('pagina/VIGNETTA/$')})
        if not rellink:
            return
        rellink = rellink['href']

        today = re.search("numero/(\d+)/pagina/", rellink).group(1)
        link = "http://www.ilmanifesto.it/fileadmin/archivi/in_edicola/%svignetta.gif" % today

        if not self.hasSeen(link):
            i = RSSItem(title = "il Manifesto vignetta - %s" % today,
                        description = '<img src="%s"/>' % link,
                        link=link)
            self.pushRSSItem(i)

ManifestoVignetta.load("il Manifesto",
                    "http://www.ilmanifesto.it/il-manifesto/in-edicola/",
                    "il Manifesto - vignetta",
                    "manifesto_vignetta.xml",
                    "state/manifesto_vignetta.pickle")

# vim:et
