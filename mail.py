from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import requests

usr1 = input('Enter your email:')
pwd1 = input('Enter your password:')

outlookDriver = webdriver.Chrome()
outlookDriver.get('https://outlook.live.com/owa/')
print('outlook opened')

main_page = outlookDriver.current_window_handle

sleep(3)

sigining_box1 = outlookDriver.find_element_by_xpath(
    "//nav[@class='auxiliary-actions']//a[@data-task='signin']")
sigining_box1.click()
sleep(3)

outlookDriver.find_element_by_xpath("//input[@name='loginfmt']")

login_page = outlookDriver.current_window_handle
for handle in outlookDriver.window_handles:
    if handle != main_page:
        login_page = handle

outlookDriver.switch_to.window(login_page)

username_box1 = outlookDriver.find_element_by_xpath(
    "//input[@name='loginfmt']")
username_box1.clear()
username_box1.send_keys(usr1)

print('email id entered')
sleep(2)

outlookDriver.find_element_by_xpath("//input[@type='submit']").click()

pwd1_box = outlookDriver.find_element_by_xpath("//input[@type='password']")
pwd1_box.clear()
pwd1_box.send_keys(pwd1)

print('password entered')
sleep(3)


final_click = outlookDriver.find_element_by_xpath("//input[@type='submit']")
final_click.click()
sleep(6)


current_url = outlookDriver.current_url
print(current_url)

source = requests.get(current_url).text
soup = BeautifulSoup(source, 'lxml')
print(soup.prettify())
# driver.switch_to_defautlt_content()
# sleep(8)

# driver.find_element_by_id('AQAAAPBWCp4BAAAB9ZyiHQAAAAA=').click()

# outlookDriver.find_element_by_id('AQAAAPBWCp4BAAAB+QK1eQAAAAA=').click()
'''outlookDriver.find_element_by_xpath(
    "//div[@class='_1yIHkYLrqDZpAMQ3L2YILh _1E-ojjaYGhOxCgHp9Pe315 _5CGGutaz4d1vhT3GzbRJq _2Ht9U0YzzfQGXALqVdO2MN']//div[@class='_1hHMVrN7VV4d6Ylz-FsMuP _18LAllQi61d4a4XNAr9prg']").click()
my_value = outlookDriver.find_element_by_xpath(
    "//p[@class='x_text-center x_zn-fontbig x_zn-bold']")
new_value = my_value.text
print(new_value)'''
# outlookDriver.quit()
print('Finished!')


# print(my_value)
'''my_value = driver.find_element_by_class_name(
    'x_text-center x_zn-fontbig x_zn-bold')
my_value.text
print(my_value)'''

'''for elements in driver.find_element_by_tag_name('p'):
    print(elements.text)'''
