import os
import time
import yaml

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait


def click_virtual_button(b, number):
    WebDriverWait(b, 5).until(
        EC.element_to_be_clickable((By.XPATH, f'//*[@aria-label="{number}"]'))
    ).click()


options = ChromeOptions()
'''options.add_argument('headless')
options.add_argument("disable-gpu")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")'''
options.add_argument("window-size=1920x1080")


def start(sido: str, type: str, scname: str, name: str, bd: str, pw: str):
    browser = webdriver.Chrome("./chromedriver.exe")

    browser.get('https://hcs.eduro.go.kr/')
    browser.find_element_by_id('btnConfirm2').click()
    browser.find_element_by_xpath('//*[@id="WriteInfoForm"]/table/tbody/tr[1]/td/button').click()
    selector = Select(browser.find_element_by_xpath('//*[@id="sidolabel"]'))
    selector.select_by_visible_text(sido)
    selector = Select(browser.find_element_by_xpath('//*[@id="crseScCode"]'))
    selector.select_by_visible_text(type)
    browser.find_element_by_xpath('//*[@id="orgname"]').send_keys(scname)
    browser.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[3]/td[2]/button').click()
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="softBoardListLayer"]/div[2]/div[1]/ul/li/a/p/a/em'))).click()
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="softBoardListLayer"]/div[2]/div[2]/input'))
    ).click()
    browser.find_element_by_xpath('//*[@id="user_name_input"]').send_keys(name)
    browser.find_element_by_xpath('//*[@id="birthday_input"]').send_keys(bd)

    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="btnConfirm"]'))
    ).click()

    time.sleep(0.1)

    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]'))
    ).click()

    num = list(pw)
    for i in range(len(pw)):
        click_virtual_button(browser, num[i])

    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="btnConfirm"]'))
    ).click()
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="container"]/div/section[2]/div[2]/ul/li/a/span[1]'))
    ).click()

    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="container"]/div/div[2]/div[2]/div[2]/dl[1]/dd/ul/li[1]/label'))
    ).click()
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="container"]/div/div[2]/div[2]/div[2]/dl[2]/dd/ul/li[1]/label'))
    ).click()
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="container"]/div/div[2]/div[2]/div[2]/dl[3]/dd/ul/li[1]/label'))
    ).click()
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="btnConfirm"]'))
    ).click()

    time.sleep(1)
    browser.quit()


with open('./config.yml', encoding='UTF8') as file:
    c = yaml.load(file, Loader=yaml.FullLoader)
    start(sido=c.get('sido'),
          type=c.get('type'),
          scname=c.get('scname'),
          name=c.get('name'),
          bd=c.get('bd'),
          pw=c.get('pw'))