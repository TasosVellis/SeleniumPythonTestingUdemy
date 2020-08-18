from selenium import webdriver
validateText = "Tasos"
driver = webdriver.Chrome(executable_path="C:\\Drivers\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element_by_css_selector("#name").send_keys("Tasos")
driver.find_element_by_id("alertbtn").click()
alert = driver.switch_to.alert
alertText = alert.text
assert validateText in alertText
# alert.accept()
alert.dismiss()

# Remember alert.text to grab JS alerts
# alert.accept() positive scenario
# alert.dismiss() negative scenario