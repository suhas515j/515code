#suhas515

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install());
driver.get('https://web.whatsapp.com/')





input('Enter anything after scanning QR code')
name = input("enter name")

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

with open('words.txt','r') as file:
    for line in file:
        for word in line.split():
            msg_box.send_keys(word)
            button = driver.find_element_by_class_name('_1U1xa')
            button.click()
            