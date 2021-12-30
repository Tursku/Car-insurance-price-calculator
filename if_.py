from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

def insuranceIf(reg, hetu, km):
    web=    webdriver.Chrome('/Users/eetuturakainen/Downloads/chromedriver')
    form_url=               ("https://www.if.fi/henkiloasiakkaat/vakuutukset/autovakuutus")
    web.get(form_url)
    time.sleep(1)

    web.find_element_by_xpath('/html/body/div[1]/div[2]/div[4]/div[2]/div/button').click()
    web.find_element_by_xpath('//*[@id="qst_11631_24c590b5-a868-4504-9612-6aaa08f75aa2"]').send_keys(reg) 
    web.find_element_by_xpath('//*[@id="qst_11630_9941162d-0136-4489-b0ab-adecca269141"]').send_keys(hetu) 
    web.find_element_by_xpath('//*[@id="entryFormSubmit"]').click()

    time.sleep(1)

    time.sleep(3)

    web.close()
    return
