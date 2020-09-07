import bs4
import requests

def getAmazonPrice(productUrl):
    res = requests.get(productUrl, headers={'user-agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) "
                                                          "AppleWebKit/602.1.50 (KHTML, like Gecko) "
                                                          "CriOS/56.0.2924.75 Mobile/14E5239e "
                                                          "Safari/602.1 RuxitSynthetic/1.0 v1086965963 "
                                                          "t4690183951324214268 smf=0"})
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#newOfferAccordionRow .header-price')
    return elems


price = getAmazonPrice(
    'http://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994/ref=tmm_pap_swatch_0?_encoding=UTF8&amp;qid=&amp;sr=')
# print('The price is ' + price)