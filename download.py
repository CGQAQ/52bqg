from requests import get

class Downloader:
    def __init__(self):
        self.counter = 0

    def download(self, url: str)->str:
        api = 'https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=all&ssl=all&anonymity=allr'
        proxies = get(api).text
        proxies = proxies.split('\r\n')
        while True:
            try:
                return get(url,headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0'}, proxies={'https_proxy': proxies[self.counter]}).content.decode('gbk')
            except:
                self.counter += 1
                print(f'counter changed')
