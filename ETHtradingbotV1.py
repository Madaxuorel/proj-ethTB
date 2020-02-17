import os
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException 
from selenium.common.exceptions import ElementNotInteractableException


browser = webdriver.Chrome(executable_path=r"C:\Users\pc adam\Documents\EISTI\algoprog\perso\python\chromedriver\chromedriver.exe")

def removeprc(string): #removes the % from a string 
    string = str(string)
    list = string.split('%')
    string = " ".join(list)
    
    return string

def new_buy_pos():
    browser.find_element_by_xpath('//*[@id="market-watch"]/li[11]/div[2]/div[3]/span[1]').click()
    try:
        browser.find_element_by_xpath(' //*[@id="qtySelect"]/span').click()
    except ElementNotInteractableException :
        browser.find_element_by_xpath('//*[@id="app"]/section[1]/div/span[1]').click()
        browser.find_element_by_xpath('//*[@id="market-watch"]/li[11]/div[2]/div[3]/span[1]').click()
        browser.find_element_by_xpath(' //*[@id="qtySelect"]/span').click()
        
         
    browser.find_element_by_xpath('/html/body/div[3]/section[4]/div/div[2]/div[1]/div[3]/div[1]/ul/li[2]/div/div[1]/ul/li[4]').click()
    browser.find_element_by_xpath('//*[@id="new-order"]/div/div[2]/div[1]/div[3]/div[1]/ul/li[3]/div/span[1]').click()
    sleep(5)
    print("new buy pos created")
    
def new_sell_pos():
    browser.find_element_by_xpath('//*[@id="market-watch"]/li[11]/div[2]/div[1]').click()
    try: #try to open a new pos
        browser.find_element_by_xpath(' //*[@id="qtySelect"]/span').click()
    except ElementNotInteractableException : #close the popup 
        browser.find_element_by_xpath('//*[@id="app"]/section[1]/div/span[1]').click()
        browser.find_element_by_xpath('//*[@id="market-watch"]/li[11]/div[2]/div[3]/span[1]').click()
        browser.find_element_by_xpath('//*[@id="qtySelect"]/span').click()
    
    browser.find_element_by_xpath('/html/body/div[3]/section[4]/div/div[2]/div[1]/div[3]/div[1]/ul/li[2]/div/div[1]/ul/li[4]').click()
    browser.find_element_by_xpath('//*[@id="new-order"]/div/div[2]/div[1]/div[3]/div[1]/ul/li[1]/div/span[1]').click()
    sleep(5)
    print("new sell pos created")    
    
    
def sell_pos(): #returns 1 if a "sell" pos is open, 0 if not
    try:
        browser.find_element_by_xpath('/html/body/div[3]/section[16]/section[2]/section[2]/section[2]/div/div[1]/table/tbody/tr/td[3]/span')
    except  NoSuchElementException :
        return 0
    if str(browser.find_element_by_xpath('/html/body/div[3]/section[16]/section[2]/section[2]/section[2]/div/div[1]/table/tbody/tr/td[3]/span').text) == "SELL":
        return 1
    else:
        return 0
    
    
def buy_pos():  #idem
    try:
        browser.find_element_by_xpath('/html/body/div[3]/section[16]/section[2]/section[2]/section[2]/div/div[1]/table/tbody/tr/td[3]/span')
        
    except  NoSuchElementException :
        return 0
    if str(browser.find_element_by_xpath('/html/body/div[3]/section[16]/section[2]/section[2]/section[2]/div/div[1]/table/tbody/tr/td[3]/span').text) == "BUY":
        return 1
    else:
        return 0  
    
def close_order(): #closes an order
      browser.find_element_by_xpath('/html/body/div[3]/section[16]/section[2]/section[2]/section[2]/div/div[1]/table/tbody/tr').click()
      browser.find_element_by_xpath('//*[@id="modify-market-order"]/div/div[3]/div[1]/ul/li[3]/span').click()
      sleep(5)
            

def eth_buy(tag): #if a sell is open, closes it. if a buy is open, keeps it. if a buy is not open, opens one.
    
    if (sell_pos() == 1):
        close_order()
    if (buy_pos() == 1):
        print("keeping BUY pos")
    else:
        if tag == 1:
            new_buy_pos()
            
   
   
def eth_sell(tag):     #if a buy is open, closes it. if a sell is open, keeps it. if a sell is not open, opens one
    
    if buy_pos() == 1:
        close_order()
    if sell_pos() == 1:
        print("keeping SELL pos")
    else:
        if tag == 1:
            new_sell_pos()                        
            
browser.get("https://trader.alvexo.fr/trading-area")

timeout = 5

#login~~
email_log = browser.find_element_by_xpath('//*[@id="email"]')
email_log.send_keys('adamleroux26@gmail.com')   
passwd_log = browser.find_element_by_xpath('//*[@id="pass1"]')
passwd_log.send_keys('Redstone16')
btn_log = browser.find_element_by_xpath('/html/body/div[2]/section/div/div[1]/div/div/div/div[1]/form/div[4]/div')
sleep(0.5)
btn_log.click()
#~~

print("loading page ...")

sleep(10)
print("page loaded")
print("acquiering values ...")
#getting eth values ~~
search_val = browser.find_element_by_xpath('//*[@id="search_markets_input"]').send_keys('eth')

eth_eur_val = browser.find_element_by_xpath('//*[@id="tradeBoardResizable"]/section/section[3]/div[3]/ul/li[3]/div[2]/div').click()

del_search = browser.find_element_by_xpath('/html/body/div[3]/section[16]/section[1]/section/section[1]/span').click()
#~~
print("values acquired")            

print("running eth trade")

graph_icon = browser.find_element_by_xpath('//*[@id="market-watch"]/li[11]/div[1]/div[2]/span[2]').click()

while 1:

    refresh = browser.find_element_by_xpath('//*[@id="draggableNavRightResizable"]/section/section[1]/ul/li[4]').click()
    details = browser.find_element_by_xpath('//*[@id="draggableNavRightResizable"]/section/section[1]/ul/li[2]').click()
    old_values = float(removeprc(browser.find_element_by_xpath('//*[@id="draggableNavRightResizable"]/section/section[2]/section[1]/div[3]/ul/li[1]/div[2]/div[6]/span').text))
    
    sleep(300)
    
    refresh = browser.find_element_by_xpath('//*[@id="draggableNavRightResizable"]/section/section[1]/ul/li[4]').click()
    details = browser.find_element_by_xpath('//*[@id="draggableNavRightResizable"]/section/section[1]/ul/li[2]').click()
    new_values = float(removeprc(browser.find_element_by_xpath('//*[@id="draggableNavRightResizable"]/section/section[2]/section[1]/div[3]/ul/li[1]/div[2]/div[6]/span').text))
    
    values = new_values - old_values
    print(values,"%")
    if values > 0:
        eth_buy(1)
            

    elif  values < -0:
        eth_sell(1) 
    else:
        print("doing nothing lul")   



os.system("pause")            