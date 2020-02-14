from bs4 import BeautifulSoup
from util.RequestMaker import RequestMaker


class CryptoDataDownloader:
    def __init__(self):
        self.request = RequestMaker()
        self.url = 'https://coinmarketcap.com/'

    def getTokenData(self):
        response = self.request.get(self.url)

        return self.parseDataFromHtml(response.content)

    def parseDataFromHtml(self, html):
        tokenData = []
        soup = BeautifulSoup(html, 'html.parser')

        for row in soup.find_all('tr'):
            tds = list(row.find_all('td'))
            if (len(tds) > 0):
                data = {
                    "name": tds[1].find('a').text,
                    "price": tds[3].find('a').text,
                    "change": tds[6].find('div').text,
                    "volume": tds[4].find('a').text,
                    "marketCap": tds[2].find('div').text,
                }
                tokenData.append(data)

        return tokenData


# if __name__ == '__main__':
#     dataDownloader = CryptoDataDownloader()

#     print(dataDownloader.getTokenData())
