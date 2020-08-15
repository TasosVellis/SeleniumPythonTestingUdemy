from selenium import webdriver
# browser exposes an executable file
# Throught Selenium test we need to invoke the executable file
# which will thne invoke actual browser
# driver = webdriver.Chrome(executable_path="C:\\Drivers\\chromedriver.exe")
# driver = webdriver.Firefox(executable_path="C:\\Drivers\\geckodriver.exe")
driver = webdriver.Ie(executable_path="C:\\Drivers\\IEDriverServer.exe")
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/")  # Get Method to hit the url in browser

print(driver.title)
print(driver.current_url)
driver.get("https://sites.google.com/a/chromium.org/chromedriver/downloads/version-selection")
driver.minimize_window()
driver.back()
driver.refresh()
driver.close()  # Only current window get closed driver.quit() to close all
