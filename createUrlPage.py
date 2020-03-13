import bs4 as bs
import commentsHackingProject
import requests


class createUrlPage:
    def __init__(self):
        self.error = 0
        self.ssc = commentsHackingProject.securingCmmunicationsNetworksCourse()
        self.tmpArrayUrls = []

    def geturl(self, url):
        '''
        ### i will use a while loop until templistUrl is not empty and every time
        ### i will pop the first link and go into, i will put the data again in sauce and soup
        ### then i will try to manage it with a global variable to check that i dont go deep to much
        '''
        try:
            sauce = requests.get(url).text
            soup = bs.BeautifulSoup(sauce, 'lxml')
        except:
            print("Can't Connect To This Url")
            self.error = 1
            return None
        tempListUrls = []
        if self.error == 0:
            for url in soup.find_all('a'):
                if (url.get('href') is not None):
                    if 'https' in url.get('href'):  # filter to only links
                        if url.get('href') not in tempListUrls:
                            tempListUrls.append(url.get('href'))
        return tempListUrls

    def GoDeep(self, url, depth):
        '''
        arange list of full deep links from specific site
        :param url: link of site
        :param depth: how long depth you want to go
        '''
        if depth == 0:
            return
        print('Current: ' + url)
        tmpListOfData = self.ssc.getCommentsFromScripts(url)
        urls = self.geturl(url)
        self.tmpArrayUrls = list(set(urls) - set(self.tmpArrayUrls))
        urls = self.tmpArrayUrls
        if (urls is not None):
            urls = urls[:1]
            for currUrl in urls:
                DataFromSite = self.GoDeep(str(currUrl), depth - 1)
                if (DataFromSite is not None):
                    tmpListOfData.update(DataFromSite)
        return tmpListOfData
