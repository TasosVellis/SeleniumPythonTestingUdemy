# Explicit wait- Target to wait for specific object
# pause the test for few seconds using Time class
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\Drivers\\chromedriver.exe")
veg_list = []
items_list = []
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
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

assert veg_list == items_list

originalAmount = driver.find_element_by_css_selector(".discountAmt").text
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()

wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "span.promoInfo")))
discountedAmount = driver.find_element_by_css_selector(".discountAmt").text
assert float(discountedAmount) < float(originalAmount)

print(driver.find_element_by_css_selector("span.promoInfo").text)

amounts = driver.find_elements_by_xpath("//tr/td[5]/p")
total = 0
for amount in amounts:
    total = total + int(amount.text)

totalAmount = int(driver.find_element_by_css_selector(".totAmt").text)
assert total == totalAmount
driver.close()