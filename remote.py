from selenium import webdriver
from selenium.webdriver.common.by import By
import string
import random

from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

N = 7

 
# using random.choices()
# generating random strings
res = ''.join(random.choices(string.ascii_lowercase +
                             'a', k=N))
letters = string.ascii_lowercase
options = FirefoxOptions()

    
print('[*] Starting Driver')
path_gecko = '/snap/bin/firefox.geckodriver' #replace with your gecko driver path
driver = webdriver.Firefox(service=Service(path_gecko)) 
# driver.install_addon('./adblocker_ultimate-3.7.28.xpi.1', temporary=True)
a=ActionChains(driver)
driver.get('https://mail.tm/en/')
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="accounts-menu"]').click()
time.sleep(5)
email=driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/div/div/div[2]/div[4]/div[3]/div/div[1]/p[2]').text
print(email)
window_before = driver.window_handles[0]
