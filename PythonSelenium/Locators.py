

from selenium import webdriver
from selenium.webdriver.support.select import Select

# driver = webdriver.Chrome(executable_path="C:\\Drivers\\chromedriver.exe")
driver = webdriver.Firefox(executable_path="C:\\Drivers\\geckodriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")

# driver.find_element_by_name("name").send_keys("Tasos")
driver.find_element_by_css_selector("input[name='name']").send_keys("Tasos")
driver.find_element_by_name("email").send_keys("mail@mail.com")
driver.find_element_by_xpath("//input[@type='submit']").click()


driver.find_element_by_id("exampleCheck1").click()

# select class provides the method to handle the options in dropdown
dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)

print(driver.find_element_by_class_name("alert-success").text)
message = driver.find_element_by_css_selector("[class*='alert-success']").text
# //*[contains(@class,'alert-success')] -XPath Regex
# [class*='alert-success' -CSS Regex
assert "success" in message
driver.close()
