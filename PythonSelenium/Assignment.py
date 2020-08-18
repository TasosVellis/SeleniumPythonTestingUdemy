# Explicit wait- Target to wait for specific object
# pause the test for few seconds using Time class

# 3 test cases
# 1. Validate whether products selected in Page 1
# are showing in Page 2 check page

# 2 Verify if Price Decreases on Discount

# 3 Verify if sum of products in checkout page matches with Total Amount
# 4 Verify if Search functionality in home page is working, put ca and see 4 products are x,y z

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\Drivers\\chromedriver.exe")
veg_list = []
items_list = []
driver.get("https://rahulshettyacademy.com/seleniumPractise/")

driver.find_element_by_css_selector("input.search-keyword").send_keys("ca")
time.sleep(4)
count_assignment = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
assert count_assignment == 4
assignment_list = []
products = driver.find_elements_by_xpath("//div[@class='products']/div")
for product in products:
    assignment_list.append(product.find_element_by_xpath("h4").text)
print(assignment_list)
assert assignment_list[0] == "Cauliflower - 1 Kg"
assert assignment_list[1] == 'Carrot - 1 Kg'
assert assignment_list[2] == 'Capsicum'
assert assignment_list[3] == 'Cashews - 1 Kg'


driver.find_element_by_css_selector("input.search-keyword").clear()
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(4)
count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
assert count == 3
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
# //div[@class='product-action']/button/parent::div/parent::div/h4
# we combine the previous xpath with one in the comment and in the loop
for button in buttons:
    items_list.append(button.find_element_by_xpath("parent::div/parent::div/h4").text)
    button.click()
print(items_list)

driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
wait = WebDriverWait(driver, 6)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoCode")))

veggies = driver.find_elements_by_css_selector("p.product-name")
for veg in veggies:
    veg_list.append(veg.text)

print(veg_list)

assert veg_list == items_list # Test Case number 1

originalAmount = driver.find_element_by_css_selector(".discountAmt").text
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()

wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "span.promoInfo")))
discountedAmount = driver.find_element_by_css_selector(".discountAmt").text
assert float(discountedAmount) < float(originalAmount) # Test Case Number 2

print(driver.find_element_by_css_selector("span.promoInfo").text)

amounts = driver.find_elements_by_xpath("//tr/td[5]/p")
total = 0
for amount in amounts:
    total = total + int(amount.text)

totalAmount = int(driver.find_element_by_css_selector(".totAmt").text)
assert total == totalAmount # Test Case Number 3
driver.close()