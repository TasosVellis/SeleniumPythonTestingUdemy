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


driver = webdriver.Chrome(executable_path="C:\\Drivers\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/")

validation_list = ["Cauliflower - 1 Kg", "Capsicum", "Carrot - 1 Kg", "Cashews - 1 Kg"]

driver.find_element_by_css_selector("input.search-keyword").send_keys("ca")
time.sleep(4)
count_assignment = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
assert count_assignment == 4
assignment_list = []
final_list = []
products = driver.find_elements_by_xpath("//div[@class='products']/div")
for product in products:
    assignment_list.append(product.find_element_by_xpath("h4").text)
sort_assignment_list = sorted(assignment_list)
print(sort_assignment_list)
step = 0
while step < count_assignment:
    for item in validation_list:
        if validation_list[step] in item:
            final_list.append(validation_list[step])
            break
    step += 1
sort_final_list = sorted(final_list)
print(sort_final_list)
assert sort_assignment_list == sort_final_list
driver.quit()
