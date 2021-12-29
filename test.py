from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome('/Users/eetuturakainen/Downloads/chromedriver')
form_url = "https://www.op.fi/henkiloasiakkaat/vakuutukset/ajoneuvovakuutus/autovakuutus-henkiloautolle"
driver.get(form_url)
time.sleep(3)
driver.find_element_by_id("ocm-button ocm-button--accept-all").click()
time.sleep(3)
time.sleep(3)
time.sleep(3)
time.sleep(3)
time.sleep(3)