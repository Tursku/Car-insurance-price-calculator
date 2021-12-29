from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

def op(reg, hetu):
    web = webdriver.Chrome('/Users/eetuturakainen/Downloads/chromedriver')
    form_url = "https://www.op.fi/henkiloasiakkaat/vakuutukset/ajoneuvovakuutus/autovakuutus-henkiloautolle"
    web.get(form_url)
    time.sleep(1)
    web.find_element_by_id('ocm-button.ocm-button--accept-all').click()

    web.find_element_by_id('productCardRegNumber').send_keys(reg) 

    web.find_element_by_id("productCardCalculateButton").click()
    time.sleep(1)
    web.find_element_by_id('userInfoSSN').send_keys(hetu)

    web.find_element_by_xpath('//*[@id="data-aff-price-form"]/div[1]/div[4]/div/div[1]/div/div/div[1]/label[2]').click()
    web.find_element_by_xpath('//*[@id="data-aff-price-form"]/div[1]/div[4]/div/div[3]/div/div[1]/div[1]/label[1]').click()

    Select(web.find_element_by_id('kilometresPerYear')).select_by_index(6)
    time.sleep(1)
    web.find_element_by_id('jatka-data-aff').click()
    time.sleep(1)
    web.find_element_by_xpath('//*[@id="ins-option-1"]').click()

    return