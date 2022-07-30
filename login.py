from getpass import getpass
from selenium import webdriver

username = input("Your Username:  ")
password = getpass("Your password:  ")

driver = webdriver.Chrome('C:\\Users\\hp\\Desktop\\SEM 2\\SCRIPTING REPOS\\chrome_driver\\chromedriver.exe')
url = ("https://manybooks.net/mnybks-login-form")
driver.get(url)

username_place = driver.find_element_by_name("email")
username_place.send_keys(username)

password_place = driver.find_element_by_name("pass")
password_place.send_keys(password)

login_button = driver.find_element_by_name("op")
login_button.submit()

driver.get("https://manybooks.net/titles/tzusun132132.html")

driver.find_element_by_link_text("download").submit()

