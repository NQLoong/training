import urllib2,Beautifulsoup,re


def get_expiredate(domain):
  """
     抓取过期域名函数
     auth:nql
    :param domain:
    :return: datelist['registerdate','expiredate']
  """
  try:
      datelist = []
      url = "http://whois.chinaz.com/" + domain
      header = {'User-Agent': 'Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;WOW64;Trident/5.0)'}
      request = urllib2.Request(url, None, header)
      response = urllib2.urlopen(request, None, timeout=10).read()
      soup = BeautifulSoup(response, "html.parser", from_encoding='utf-8')
      content = soup.find_all('div', attrs={'class': 'fr WhLeList-right'})
      pattern = r'\d{4}\D\d{2}\D\d{2}\D'
      for div in content:
          for span in div.find_all('span'):
              if re.match(pattern, span.string):
                  datelist.append(span.string)
      print domain,datelist
      datelist = [datelist[-2], datelist[-1]]
      print datelist
      return (datelist)
  except:
      datelist=[]
      return datelist
