import requests
import contextlib
import selenium.webdriver as webdriver
from bs4 import BeautifulSoup

class LovScraper(object):
    lovSearchUri = 'http://lov.okfn.org/dataset/lov/search/#s='
    def __init__(self):
        pass

    def getUrl(self, url):
        phantomjs = '/home/ivan/bin/phantomjs'
        with contextlib.closing(webdriver.PhantomJS(phantomjs)) as driver:
            driver.get(url)
            content = driver.page_source
            return BeautifulSoup(content)

    def search(self, term):
        url = self.lovSearchUri + term
        soup = self.getUrl(url)
        suggestions = []
        for div in soup.find_all(class_="gwt-HTML"): 
            uriContainer = div.find_all("td", width="100%", limit=1).pop()
            type = uriContainer.text.split()[1]
            uri = div.find_all('a').pop()
            shortUri = uri.get_text()
            fullUri = uri['href']
            score = div.find_all("tr", limit=1).pop()
            score = div.find_all("td")[1]
            score = score.get_text().split(":")[1]

            suggestion = {
                    "type": type,
                    "shortUri":shortUri,
                    "fullUri":fullUri,
                    "score":score
                    }

            suggestions.append(suggestion)
        return suggestions


if __name__ == "__main__":
    lovscraper = LovScraper()
    suggestions = lovscraper.search('Latitude')

    import pprint
    pprinter = pprint.PrettyPrinter()
    pprinter.pprint(suggestions)

