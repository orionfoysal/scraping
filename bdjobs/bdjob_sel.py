from selenium import webdriver
from parsel import Selector
from time import sleep

driver = webdriver.Chrome('E:\scrapyTest\chromedriver_win32\chromedriver.exe')

driver.get('http://corporate3.bdjobs.com')
username = driver.find_element_by_id('NAME')
username.send_keys('orelco')
sleep(0.5)

password = driver.find_element_by_id('PASS')
password.send_keys('Login1#')
sleep(0.5)

submit = driver.find_element_by_xpath('//*[@type="submit"]')
submit.click()
sleep(5)

# driver.get('https://corporate3.bdjobs.com/view_resume.asp?Idn=23067562031ID1151331&key=dhaka&keytype=')

# sel = Selector(text=driver.page_source)

# download_pdf = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/ul/li[2]/a')

# download_pdf.click()

# applicantsName = sel.xpath('//*[@class="BDJApplicantsName"]//text()').extract()
# # applicantsAddress = sel.xpath('//*[@id="hid_MainCV"]/table[3]/tbody/tr/td/table/tbody/tr[2]/td/text()').extract()

# applicantsAddress = sel.xpath('//*[@class="BDJNormalText04"]/text()').extract()

# topics = sel.xpath('//*[@class="BDJHeadline01"]/u/text()').extract()


# main_cv = sel.xpath('//div[@id="hid_MainCV"]')

# ref = main_cv.xpath('.//table/tbody/tr[contains(.,"Reference")]')
# all_references = ref[0].xpath('.//tr//td/text()').extract()

# aca = main_cv.xpath('.//table/tbody[contains(.,"Academic")]')
# academic = academic.xpath('.//tr//text()').extract()

# bank = driver.find_element_by_xpath('//*[@id="bs-example-navbar-collapse-1"]/ul/li[2]/a')
# bank.click()

# keyword = driver.find_element_by_xpath('//*[@id="txtKeywordtmp"]')
# keyword.send_keys('University of Dhaka')
# search_button = driver.find_element_by_xpath('//*[@id="KeywordFrom"]/div/div/span/a')
# search_button.click()