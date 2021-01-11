import time
from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

#INPUT URL HERE TO BUY
URL = 'https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440'
#URL = 'https://www.bestbuy.com/site/corsair-tm30-performance-thermal-paste/6318342.p?skuId=6318342'
fullFill = 'https://www.bestbuy.com/checkout/r/fulfillment'
fName =  
lName = 
address = "
city =  ""
state = 
zipcode =  "
email =  
phone = "

#Input Payment Method
creditCard = ''
expMonth = 
expMonth += 
expMonth= 
expYear = 
expYear += 
expYear = 
cvc = 
countTries = 0

def get_clear_browsing_button(driver):
    """Find the "CLEAR BROWSING BUTTON" on the Chrome settings page."""
    return driver.find_element_by_id('clearBrowsingDataConfirm')

def addToCart(driver):
    #STOP LOAD PAGE FOR FASTER ADD TO CART
    CartAvailable = ''
    myCart = ''

    try:
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "card-member__header"))
            )
    finally:
        while not CartAvailable:
            try:
                CartAvailable = driver.find_element_by_xpath(
                    "//div/button[contains(@class,'btn btn-primary btn-lg btn-block btn-leading-ficon add-to-cart-button')]")

            except:
                countTries = countTries + 1
                print("# of Tries: " + str(countTries) +" Add To Card Availablility : " + str(CartAvailable))
                driver.refresh()

    try:
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div/button[contains(@class,'btn btn-primary btn-lg btn-block btn-leading-ficon add-to-cart-button')]"))
        )
        print('Located Add To Cart Button')
    finally:
        driver.find_element_by_xpath(
            "//div/button[contains(@class,'btn btn-primary btn-lg btn-block btn-leading-ficon add-to-cart-button')]").click()
        driver.get('https://www.bestbuy.com/cart')


def getCheckout(driver):
    print('Cart Check')
    try:
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//fieldset/div[2]/div[1]/div/div/div/input[contains(@type,'radio')]"))
        )
        print('WAIT FOR SHIPPING DONE')
    finally:
        pickShipping = driver.find_element_by_xpath("//fieldset/div[2]/div[1]/div/div/div/input[contains(@type,'radio')]").click()

        driver.get('https://www.bestbuy.com/checkout/r/fulfillment')

def inputInformation(driver):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "consolidatedAddresses.ui_address_2.firstName")),
            EC.presence_of_element_located((By.ID, "consolidatedAddresses.ui_address_2.lastName"))
        )
    finally:
        firstName = driver.find_element_by_xpath(
            "//input[contains(@id,'consolidatedAddresses.ui_address_2.firstName')]")
        firstName.send_keys(fName)
        lastName = driver.find_element_by_xpath(
            "//input[contains(@id,'consolidatedAddresses.ui_address_2.lastName')]")
        lastName.send_keys(lName)
        billAddress = driver.find_element_by_xpath(
            "//input[contains(@id,'consolidatedAddresses.ui_address_2.street')]")
        billAddress.send_keys(address)
        cityName = driver.find_element_by_xpath(
            "//input[contains(@id,'consolidatedAddresses.ui_address_2.city')]")
        cityName.send_keys(city)
        postalCode = driver.find_element_by_xpath(
            "//input[contains(@id,'consolidatedAddresses.ui_address_2.zipcode')]")
        postalCode.send_keys(zipcode)
        selectState = driver.find_element_by_xpath('//option[9]').click()
        uncheckSaveAddress = driver.find_element_by_xpath("//section/label/div/input[contains(@type,'checkbox')]").click()
        emailAddress = driver.find_element_by_xpath("//input[contains(@id,'user.emailAddress')]")
        emailAddress.send_keys(email)
        phoneNumber = driver.find_element_by_xpath("//input[contains(@id,'user.phone')]")
        phoneNumber.send_keys(phone)
        continuePayment = driver.find_element_by_xpath("//button[contains(@class,'btn btn-lg btn-block btn-secondary')]").click()


def placeOrder(driver):
    #time.sleep(3)
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "payment.billingAddress.zipcode"))
        )
    finally:
        cCard = driver.find_element_by_xpath("//div[1]/input[contains(@id,'optimized-cc-card-number')]")
        cCard.send_keys(creditCard)
        try :
            e = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "expiration-month")),
                EC.presence_of_element_located((By.NAME, "expiration-year"))
            )

        finally:
            expM = driver.find_element_by_xpath("//div[1]/label/div/select/option[" + expMonth +"]").click()
            expY = driver.find_element_by_xpath("//div[2]/label/div/select/option[" + expYear +"]").click()
            securityCode = driver.find_element_by_xpath("//input[contains(@id,'credit-card-cvv')]")
            securityCode.send_keys(cvc)
            firstName = driver.find_element_by_xpath(
                "//input[contains(@id,'payment.billingAddress.firstName')]")
            firstName.send_keys(fName)

            lastName = driver.find_element_by_xpath(
                "//input[contains(@id,'payment.billingAddress.lastName')]")
            lastName.send_keys(lName)

            #/html/body/div[3]/div[2]/div/div/div[1]/div[1]/main/div[2]/div[3]/div/section/form/div/section/div[4]/label/div[2]/div/button
            driver.find_element_by_xpath(
                "//div[2]/div/button[contains(@class,'autocomplete__toggle')]").click()

            billAddress = driver.find_element_by_xpath(
                "//input[contains(@id,'payment.billingAddress.street')]")
            billAddress.send_keys(address)

            cityName = driver.find_element_by_xpath(
                "//input[contains(@id,'payment.billingAddress.city')]")
            #time.sleep(200 / 1000)
            cityName.send_keys(city)

            #time.sleep(200 / 1000)
            postalCode = driver.find_element_by_xpath(
                "//input[contains(@id,'payment.billingAddress.zipcode')]")
            postalCode.send_keys(zipcode)
            #time.sleep(200 / 1000)

            #/html/body/div[3]/div[2]/div/div/div[1]/div[1]/main/div[2]/div[3]/div/section/form/div/section/div[6]/div/div[2]/label/div/select/option[10]
            selectState = driver.find_element_by_xpath('//div[6]/div/div[2]/label/div/select/option[10]').click()
            #time.sleep(200 / 1000)
            driver.find_element_by_xpath('//div[6]/div/div[2]/label/div/select/option[10]').click()
            #time.sleep(3)


            placePayment = driver.find_element_by_xpath("//button[contains(@class,'btn btn-lg btn-block btn-primary')]").click()

def main():
        #INITIAL SET UP
    driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')  # Optional argument, if not specified will search path.
        #CLEAR CACHE AND COOKIES
    driver.delete_all_cookies()
        #Launch Website and BEGIN BOT
    driver.get(URL);
        #Add to cart
    AddToCart = addToCart(driver)
        #Clicked Checkout
    getToCheckout = getCheckout(driver)
        #Enter Information
    informationInput = inputInformation(driver)
        #FINAL ORDER
    pOrder = placeOrder(driver)

    time.sleep(10000)
    driver.quit()
if __name__ == "__main__":
    main()
