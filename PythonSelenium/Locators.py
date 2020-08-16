from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Drivers\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")

# driver.find_element_by_name("name").send_keys("Tasos")
driver.find_element_by_css_selector("input[name='name']").send_keys("Tasos")
driver.find_element_by_name("email").send_keys("mail@mail.com")
driver.find_element_by_xpath("//input[@type='submit']").click()
driver.find_element_by_id("exampleCheck1").click()

print(driver.find_element_by_class_name("alert-success").text)
print(driver.find_element_by_css_selector("[class*='alert-success']").text)
# //*[contains(@class,'alert-success')] -XPath Regex
# [class*='alert-success' -CSS Regex
