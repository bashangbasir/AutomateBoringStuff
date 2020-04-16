import bs4
import requests

search_link = "https://www.imanshoppe.com/collections/new-arrival/products/hero-1-sudah-mati-edisi-kemas-kini"

def getPrice(productUrl):
    #header is put to prvent the page detect we using script, some still able to detect we use it.
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    res = requests.get(productUrl, headers=headers)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#ProductPrice-4601346261049')
    return elems[0].text.strip()

price = getPrice(search_link)
print("The price is : ",price)
