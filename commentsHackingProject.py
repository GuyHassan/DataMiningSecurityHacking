import bs4 as bs
import requests
from bs4 import Comment
import re


class securingCmmunicationsNetworksCourse:
    def __init__(self):
        # --------------------- check all the options in username, credential and passowrd !! ---------------------
        self.optionPass = re.compile("(p|P)(a|A)(s|S)+[-,: _+]*(((w|W)(o|O)(r|R)(d|D))?)*")
        self.optionCredential = re.compile("(c|C)redential(s|S)*")
        self.optionUser = re.compile("(u|U)(s|S)(e|E)(r|R)*[-:, _\.&]*(n|N)(a|A)(m|M)(e|E)*")

        self.strComment, self.linksList = {}, []
        self.depth = 0

    def getCommentsFromScripts(self, linkSite):
        try:
            # linkSite = "https://guyhassan.github.io/Geo-Information-Project/"
            tmpStr = ''
            urlopen = requests.get(linkSite)
            soup = bs.BeautifulSoup(urlopen.text, 'lxml')

            # --------------------- get all comments from HTML page !! ---------------------

            comments = soup.find_all(string=lambda text: isinstance(text, Comment))
            print(comments)
            for comm in comments:
                if (self.optionUser.search(comm) or self.optionPass.search(comm) or self.optionCredential.search(comm)):
                    tmpStr += comm
            self.strComment[str(self.depth)] = {'linkSite': linkSite, 'Comment': tmpStr}
            self.depth += 1

            # -------------- get all link that ending in .css or .js ---------------------
            self.linksList = [link["href"] for link in soup.findAll('link') if
                              '.css' in link['href'] or '.js' in link['href']]
            self.linksList += [link["src"] for link in soup.findAll('script', {"src": True}) if
                               '.css' in link['src'] or '.js' in link['src']]

            # -- add the html link to the js or css link if them didnt include domain before.. (https:// and more) -----------------
            self.linksList = list(map(lambda link: linkSite + link if 'http' not in link else link, self.linksList))
            print(self.linksList)

            # -- for each link that include in the end .js or .css we search all the comments that include username or pass inside ---------
            for link in self.linksList:
                self.commentsFromJavaScript_CSS(link)
        except:
            pass
        return self.strComment

    def commentsFromJavaScript_CSS(self, link):
        tmpStr = ''
        # -- tell him try to open a link, if you get errors continue to the code ---------------------
        try:
            urlopen = requests.get(link)
            soup = bs.BeautifulSoup(urlopen.text, 'lxml')
            # --------------------- get all comments from javaScript and CSS links !! ---------------------
            reg = re.compile("/\*.*?\*/", re.DOTALL)
            matches = reg.findall(soup.text)
            for comm in matches:
                if ((self.optionUser.search(comm) or self.optionPass.search(comm) or self.optionCredential.search(
                        comm)) and not 'function' in comm):
                    tmpStr += comm
            # -- if this specific link didnt contain comment that suitable for that regex it is not comment that i want ------
            if (not tmpStr == ''):
                self.strComment[str(self.linksList.index(link) + 1)] = {'linkSite': link, 'Comment': tmpStr}
            # _________________________________________________________________________________________________
        except Exception:
            pass

# ssc = securingCmmunicationsNetworksCourse()
# print(ssc.getCommentsFromScripts('https://guyhassan.github.io/Geo-Information-Project/'))
