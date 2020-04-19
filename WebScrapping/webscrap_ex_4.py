from selenium import webdriver

browser = webdriver.Chrome()

link = "https://automatetheboringstuff.com"
#open url 
browser.get(link)
#search element by css selector
# element can be select using id, class, name, tagname,partial link text,link text 
elem = browser.find_element_by_css_selector("body > div.main > div:nth-child(1) > ul:nth-child(20) > li:nth-child(1) > a")
#click element
elem.click()

about_author = browser.find_element_by_css_selector("#calibre_link-1609 > p")
author = about_author.text
print(author)

browser.get("https://google.com")

search_field = browser.find_element_by_css_selector("#tsf > div:nth-child(2) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input")

search_field.send_keys("Hello google!")
search_field.submit()

#can control the browser. 
# back&forward action, refresh , quit browser

browser.back()
browser.forward()
browser.refresh()
browser.quit()


