from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

def insuranceIf(reg, hetu, km, address, post):
    web=    webdriver.Chrome('/Users/eetuturakainen/Downloads/chromedriver')
    form_url=               ("https://www.if.fi/henkiloasiakkaat/vakuutukset/autovakuutus")
    web.get(form_url)
    time.sleep(1)

    web.find_element_by_xpath('/html/body/div[1]/div[2]/div[4]/div[2]/div/button').click()
    web.find_element_by_xpath('//*[@id="qst_11631_24c590b5-a868-4504-9612-6aaa08f75aa2"]').send_keys(reg) 
    web.find_element_by_xpath('//*[@id="qst_11630_9941162d-0136-4489-b0ab-adecca269141"]').send_keys(hetu) 
    web.find_element_by_xpath('//*[@id="entryFormSubmit"]').click()

    time.sleep(5)

    Select(web.find_element_by_xpath('//*[@id="ctl06_ucProcess_ucTopQuestions_qst_15370"]')).select_by_value(km)
    web.find_element_by_xpath('//*[@id="ctl06_ucProcess_ucTopQuestions_qst_12535"]').send_keys(address) 
    web.find_element_by_xpath('//*[@id="ctl06_ucProcess_ucTopQuestions_qst_11634"]').send_keys(post) 
    web.find_element_by_xpath('//*[@id="ctl06_ucProcess_ucTopQuestions_btnMiddleStepPrice"]').click()

    time.sleep(8) # This needs the do when element available thing asap!

    web.find_element_by_xpath('//*[@id="quote-page-app"]/div[2]/div[1]/div[1]/div[4]/div[3]/div[1]/div[1]/div[2]/div[3]/div/label').click() # Selecting all of the extra shiet
    time.sleep(5)   
    web.find_element_by_xpath('//*[@id="quote-page-app"]/div[2]/div[1]/div[1]/div[4]/div[3]/div[2]/div[1]/div[2]/div[3]/div/label').click()
    time.sleep(5)
    web.find_element_by_xpath('//*[@id="quote-page-app"]/div[2]/div[1]/div[1]/div[4]/div[3]/div[3]/div[1]/div[2]/div[3]/div/label').click()
    time.sleep(5)    
    web.find_element_by_xpath('//*[@id="quote-page-app"]/div[2]/div[1]/div[2]/div/div/div/div[2]/ul/li[1]').click() # 200€
    time.sleep(5)

    amount = web.find_element_by_xpath('//*[@id="pnlPurchaseProductQuestions"]/div[2]/div/div[2]/div[2]/h6[2]')
    print("If : " + str(amount.text))

    time.sleep(10)

    web.close()
    return
