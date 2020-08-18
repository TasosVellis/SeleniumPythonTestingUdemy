from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Drivers\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# Checkboxes
checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")
print(len(checkboxes))
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()

# Radio Buttons
radiobuttons = driver.find_elements_by_name("radioButton")
radiobuttons[2].click()
assert radiobuttons[2].is_selected()

# Handling Javascript and Java Pop ups

