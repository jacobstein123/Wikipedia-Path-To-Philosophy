import urllib2, re

def findFirstLink(article):
    url = 'http://en.wikipedia.org/w/index.php?title=%s&printable=yes'% '_'.join(article.split())
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent','Path to Philosophy Calc')]
    html = opener.open(url).read()
                                  #          link before bold                   |   link after the bold and no parens                |   link after bold with parens
    rawFirstLinkName = re.search(r'<p>[^<>]*?<a href="/wiki/([^#:]+?)".*?>.*?<b>|<p>.*?<b>.+?</b>[^\(]+?<a href="/wiki/([^#:]+?)".*?>|<p>.*?<b>.*?</b>.*?\(.*?\).*?<a href="/wiki/([^#:]+?)".*?>',html)
    firstLinkName = ''.join([rawFirstLinkName.group(i) for i in range(1,4) if rawFirstLinkName.group(i)])
    return firstLinkName
def pathToPhilosophy(article):
    path = []
    while article.lower() != 'philosophy':
        path.append(article)
        article = findFirstLink(article)
        print article
    path.append('philosophy')
    return path
