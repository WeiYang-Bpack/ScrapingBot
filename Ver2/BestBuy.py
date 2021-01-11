import time
from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

#INPUT URL HERE TO BUY
#CURRENT GIGABYTE 3080
#KMAN
SKU = '6430621'
URL = 'https://api.bestbuy.com/click/5592e2b895800000/' +  SKU + '/pdp'
#URL = 'https://www.bestbuy.com/site/corsair-tm30-performance-thermal-paste/6318342.p?skuId=6318342'
fullFill = 'https://www.bestbuy.com/checkout/r/fulfillment'
cvc = ''



def get_clear_browsing_button(driver):
    """Find the "CLEAR BROWSING BUTTON" on the Chrome settings page."""
    return driver.find_element_by_id('clearBrowsingDataConfirm')



def getCheckout(driver):
    CheckOutChecker = ''
    countTries = 0
    #/html/body/div[1]/main/div/div[2]/div[1]/div/div/span/div/div[1]/div[1]/section[2]/div/div/div[3]/div/div[1]/button
    driver.get('https://api.bestbuy.com/click/5592e2b895800000/' + SKU + '/cart')
    while not CheckOutChecker:
        element = WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.CLASS_NAME, "order-summary__heading"))
        )
        try:
            CheckOutChecker = driver.find_element_by_xpath(
                "//button[contains(@class,'btn btn-lg btn-block btn-primary')]")
        except:
            countTries = countTries + 1
            print("# of Tries: " + str(countTries))
            driver.get('https://api.bestbuy.com/click/5592e2b895800000/' + SKU + '/cart')


    driver.get('https://www.bestbuy.com/checkout/r/payment')


def placeOrder(driver):
    try:
        # WebDriverWait(driver, 20).until((EC.visibility_of_element_located((By.CLASS_NAME, 'page-spinner page-spinner--out')))
        #     )
        element = WebDriverWait(driver, 100).until(
            EC.visibility_of_element_located((By.XPATH, "//input[contains(@id,'credit-card-cvv')]"))
            )

    finally:
        driver.find_element_by_xpath("//input[contains(@id,'credit-card-cvv')]").send_keys('661')
        placePayment = driver.find_element_by_xpath("//button[contains(@class,'btn btn-lg btn-block btn-primary')]").click()



def main():
        #INITIAL SET UP
    options = Options()
    options.page_load_strategy = 'eager'
    driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe', options= options)  # Optional argument, if not specified will search path.
        #CLEAR CACHE AND COOKIES
    driver.delete_all_cookies()
        #Launch Website and BEGIN BOT
    driver.get('https://www.bestbuy.com/identity/global/signin');
    time.sleep(20)
    start_time = time.time()
        #Clicked Checkout
    getToCheckout = getCheckout(driver)
        #Enter Information
    # informationInput = inputInformation(driver)
        #FINAL ORDER

    pOrder = placeOrder(driver)
    print("My program PLACE ORDER", time.time() - start_time, "to run")
    time.sleep(10000)
    driver.quit()
if __name__ == "__main__":
    main()
