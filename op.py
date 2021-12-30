from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
import time

def insuranceOp(reg, hetu, km):
    web1 = webdriver.Chrome('/Users/eetuturakainen/Downloads/chromedriver')
    form_url = "https://www.op.fi/henkiloasiakkaat/vakuutukset/ajoneuvovakuutus/autovakuutus-henkiloautolle"
    web1.get(form_url)
    time.sleep(1)
    web1.find_element_by_id('ocm-button.ocm-button--accept-all').click()

    web1.find_element_by_id('productCardRegNumber').send_keys(reg) 

    web1.find_element_by_id("productCardCalculateButton").click()
    time.sleep(1)
    web1.find_element_by_id('userInfoSSN').send_keys(hetu)

    web1.find_element_by_xpath('//*[@id="data-aff-price-form"]/div[1]/div[4]/div/div[1]/div/div/div[1]/label[2]').click()
    web1.find_element_by_xpath('//*[@id="data-aff-price-form"]/div[1]/div[4]/div/div[3]/div/div[1]/div[1]/label[1]').click()

    Select(web1.find_element_by_id('kilometresPerYear')).select_by_value(km)
    time.sleep(1)
    web1.find_element_by_id('jatka-data-aff').click()
    time.sleep(5)
    web1.find_element_by_xpath('//*[@id="options-list"]/li[1]/div[3]/div[1]/label/span/span[2]').click() #Kasko
             
    web1.find_element_by_xpath('//*[@id="t2k6b8mpth"]/div/div/label').click()
    web1.find_element_by_xpath('//*[@id="optional-covers-cover-1"]').click()
    time.sleep(3)  

    web1.quit()
    return




    