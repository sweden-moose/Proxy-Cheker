from selenium import webdriver
from bs4 import BeautifulSoup
import time
import re
import check


proxies = []
driver = webdriver.Firefox()
driver.get("https://hidemy.name/ru/proxy-list/")
time.sleep(6)
fin = []
while True:
    print(driver.current_url)
    f = driver.find_element_by_tag_name('tbody')
    g = f.find_elements_by_tag_name('tr')
    for i in g:
        h = i.find_elements_by_tag_name('td')
        fin.append(h[0].text+':'+h[1].text)
    try:
        driver.find_element_by_class_name('mb1').click()
        driver.find_element_by_class_name('next_array').click()
    except:
        print('end')
        break
f = open('all_prox.txt','w')
f.write('\n'.join(fin))
f.close()
driver.close()

good_prox = []
for i in fin:
    print(i)
    good_prox.append(proxcheck.check_proxy(i))
good_prox = list(set(good_prox))
f = open('good_prox.txt','w')
f.write('\n'.join(fin))
f.close()

import remake2old
