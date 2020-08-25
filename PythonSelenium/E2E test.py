
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\Drivers\\chromedriver.exe")
# driver = webdriver.Firefox(executable_path="C:\\Drivers\\geckodriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_css_selector("a[href*='shop']").click()
# Complicated Loop all products and catch from parent
# Simple
products = driver.find_elements_by_xpath("//div[@class='card h-100']")
for product in products:
    productName = product.find_element_by_xpath("div/h4/a").text
    if productName == "Blackberry":
        # Add item to cart
        product.find_element_by_xpath("div/button").click()
driver.find_element_by_css_selector("a[class*='btn-primary']").click()
driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
driver.find_element_by_id("country").send_keys("gre")
wait = WebDriverWait(driver,7)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Greece")))
driver.find_element_by_link_text("Greece").click()
driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
driver.find_element_by_css_selector("[value='Purchase']").click()
successText = driver.find_element_by_class_name("alert-success").text

assert "Success! Thank you!" in successText

driver.get_screenshot_as_file("screen.png")
