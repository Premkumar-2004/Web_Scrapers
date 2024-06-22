from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import random
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service



executable_path = "C:\\Users\\91765\\PycharmProjects\\chromedriver-win32\\chromedriver.exe"

# Use Service object to avoid deprecation warning


service = Service(executable_path)
driver = webdriver.Chrome(service=service)
driver.get("https://tutorialsninja.com/demo/")
driver.maximize_window()
time.sleep(10)

phone = driver.find_element(By.XPATH, '//a[text()="Phones & PDAs"]')
phone.click()
time.sleep(5)

iphone = driver.find_element(By.XPATH, '//a[text()="Palm Treo Pro"]')
iphone.click()
time.sleep(5)

firstpic=driver.find_element(By.XPATH,'//ul[@class="thumbnails"]/li[1]')
firstpic.click()
time.sleep(2)

nextclick=driver.find_element(By.XPATH,"//button[@title='Next (Right arrow key)']")

for i in range(2):
    nextclick.click()
    time.sleep(2)

driver.save_screenshot('screenshot#'+str(random.randint(0,101)) + '.png')


close =driver.find_element(By.XPATH,'//button[@title="Close (Esc)"]')
close.click()
time.sleep(2)

quantity=driver.find_element(By.ID,'input-quantity')
quantity.click()
time.sleep(2)
quantity.clear()
quantity.send_keys('2')

cart=driver.find_element(By.ID,'button-cart')
cart.click()
time.sleep(5)

#we dont want to click on the laptop menu we just want to move our curser there so for that we use action chains

laptops=driver.find_element(By.XPATH,'//a[text()="Laptops & Notebooks"]')
action=ActionChains(driver)
action.move_to_element(laptops).perform()

showlaptops=driver.find_element(By.XPATH,'//a[text()="Show AllLaptops & Notebooks"]')
showlaptops.click()

hp=driver.find_element(By.XPATH,'//a[text()="HP LP3065"]')
hp.click()
time.sleep(3)

#scrolling
addtocart=driver.find_element(By.XPATH,'//button[@id="button-cart"]')
addtocart.location_once_scrolled_into_view
dates=driver.find_element(By.XPATH,'//i[@class="fa fa-calendar"]')
calnext=driver.find_element(By.XPATH,'//th[@class="next"]')

dates.click()
month=driver.find_element(By.XPATH,'//th[@class="picker-switch"]')
while month.text!='December 2023':
    calnext.click()
time.sleep(3)

caldate=driver.find_element(By.XPATH,'//td[text()="12"]')
caldate.click()
addtocart.click()

time.sleep(3)
# oh god completed the product selection

# now lets finish the bill

goingtocart=driver.find_element(By.ID,'cart-total')
goingtocart.click()
time.sleep(2)

checkout=driver.find_element(By.XPATH,'//p[@class="text-right"]/a[2]')
checkout.click()
time.sleep(2)

guest=driver.find_element(By.XPATH,'//input[@value="guest"]')
guest.click()


countinue=driver.find_element(By.ID,'button-account')
countinue.click()
time.sleep(1)

countinue1=driver.find_element(By.XPATH,'//a[text()="Step 2: Billing Details "]')
countinue1.location_once_scrolled_into_view
time.sleep(3)


firstname=driver.find_element(By.ID,'input-payment-firstname')
firstname.click()
time.sleep(2)
firstname.send_keys('Prem')

lastname=driver.find_element(By.ID,'input-payment-lastname')
lastname.click()
time.sleep(2)
lastname.send_keys('kumar')

email=driver.find_element(By.ID,'input-payment-email')
email.click()
time.sleep(2)
email.send_keys("can@gmail.com")

telephone=driver.find_element(By.ID,'input-payment-telephone')
telephone.click()
time.sleep(2)
telephone.send_keys('0984827')


company=driver.find_element(By.ID,'input-payment-company')
company.click()
time.sleep(2)
company.send_keys('Bourbon pvt ltd')

address1=driver.find_element(By.ID,'input-payment-address-1')
address1.click()
time.sleep(2)
address1.send_keys('coimbatore')

address2=driver.find_element(By.ID,'input-payment-address-2')
address2.click()
time.sleep(2)
address2.send_keys('amrita viswa vidyapeetham')

city=driver.find_element(By.ID,'input-payment-city')
city.click()
time.sleep(2)
city.send_keys('FRankfurt')


postcode=driver.find_element(By.ID,'input-payment-postcode')
postcode.click()
time.sleep(2)
postcode.send_keys('641112')

country=driver.find_element(By.ID,'input-payment-country')
dropdown1=Select(country)
time.sleep(2)
dropdown1.select_by_index(87)
time.sleep(1)

state=driver.find_element(By.ID,'input-payment-zone')
dropdown2=Select(state)
time.sleep(1)
dropdown2.select_by_visible_text('Hessen')
time.sleep(1)




countinue2=driver.find_element(By.ID,'button-guest')
countinue2.click()
time.sleep(2)



countinue4=driver.find_element(By.ID,'button-shipping-method')
countinue4.click()
time.sleep(2)


checkbox1=driver.find_element(By.XPATH,'//input[@name="agree"]')
checkbox1.click()
time.sleep(2)

countinue5=driver.find_element(By.ID,'button-payment-method')
countinue5.click()
time.sleep(2)


#final price:
final_price=driver.find_element(By.XPATH,'//table[@class="table table-bordered table-hover"]/tfoot/tr[3]/td[2]')

print(f"the final price of products is {final_price}")

#confirm order
confirm=driver.find_element(By.ID,'button-confirm')
confirm.click()

#sucess text
sucess=driver.find_element(By.XPATH,'//div[@class="col-sm-12"]/h1')
print(sucess.text)
time.sleep(2)




driver.close()



































