from selenium import webdriver

# iframe, frameset, frame
driver = webdriver.Chrome(executable_path="C:\\Drivers\\chromedriver.exe")

driver.get("https://the-internet.herokuapp.com/iframe")
# you have to pass frame id or frame name or index value
driver.switch_to.frame("mce_0_ifr")
driver.find_element_by_css_selector("#tinymce").clear()
driver.find_element_by_css_selector("#tinymce").send_keys("I like trains!")
driver.switch_to.default_content()

print(driver.find_element_by_tag_name("h3").text)
