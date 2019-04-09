from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def login(driver, email,password):
    print("log in with {} {}".format(email,password))
    driver.get('https://mbasic.facebook.com/login/?ref=dbl&fl&refid=8')

    emailform = driver.find_element(By.ID,"m_login_email")
    emailform.clear()
    emailform.send_keys(email)
    passwordform = driver.find_element(By.XPATH, '//*[@id="login_form"]/ul/li[2]/div/input')
    passwordform.send_keys(password)
    passwordform.send_keys(Keys.ENTER)

    try:
        not_now = driver.find_element(By.XPATH,'//*[@id="root"]/table/tbody/tr/td/div/div[3]/a')
        print("login sukses")
        not_now.click()
        try:
            driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/table/tbody/tr/td[3]/a').click()
        except:
            pass
        driver.find_element(By.XPATH, '//*[@id="mbasic_logout_button"]').click()
        print("logout sukses")
        return True
    except Exception as e:
        print("login gagal")
        return False