import telebot
from py5paisa import FivePaisaClient
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time


#Get your API keys from https://invest.5paisa.com/DeveloperAPI/APIKeys

cred={
    "APP_NAME":"APP_NAME",
    "APP_SOURCE":"APP_SOURCE",
    "USER_ID":"USER_ID",
    "PASSWORD":"PASSWORD",
    "USER_KEY":"USER_KEY",
    "ENCRYPTION_KEY":"ENCRYPTION_KEY"
    }


#This automation is to get 'Your Response Token'.

driver = uc.Chrome()


driver.get(f'https://dev-openapi.5paisa.com/WebVendorLogin/VLogin/Index?VendorKey="your USER_KEY"&ResponseURL=https://www.google.com/')


driver.implicitly_wait(10)
login_id = driver.find_element("xpath", '//*[@id="ObjVLoginModal_UserName"]')
login_id.send_keys("your email")
driver.implicitly_wait(10)
user_pwd = driver.find_element("xpath", '//*[@id="ObjVLoginModal_Password"]')
user_pwd.send_keys("your password")
driver.implicitly_wait(10)
user_DOB = driver.find_element("xpath", '//*[@id="ObjVLoginModal_DOB"]')
user_DOB.send_keys('your DOB')
driver.implicitly_wait(10)

submit = driver.find_element("xpath", '//*[@id="VLoginForm"]/button')
submit.click()




url = driver.current_url
initial_token = url.split('?RequestToken=')[1]
finalT = initial_token.split('&')[0]



client = FivePaisaClient(cred=cred)
client.get_access_token(finalT)

client.margin()


a = str(client.margin())
NetMargin = a.split(',')[2]
print(NetMargin)

#This part sends notification to your telegram via telegram Bot.

TOKEN = 'TOKEN'
tb = telebot.TeleBot(TOKEN)

user = tb.get_me()
tb.send_message(your_chat_ID, NetMargin)
