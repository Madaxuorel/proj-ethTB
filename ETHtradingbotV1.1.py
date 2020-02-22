import os
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException 
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from datetime import datetime
datetime.now().strftime('%Y-%m-%d %H:%M:%S')

options = Options()
options.headless = True
browser = webdriver.Chrome(executable_path=r"C:\Users\pc adam\Documents\EISTI\algoprog\perso\python\chromedriver\chromedriver.exe")

wait = WebDriverWait(browser, 20)
def removeprc(string): #removes the % from a string 
    string = str(string)
    list = string.split('%')
    string = " ".join(list)
    
    return string


def openpos():
    if buy_pos() or sell_pos():
        return 1
    else:
        return 0

    




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
    print("new buy pos created at ", date)
    
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
    print("new sell pos created at ", date)    
    
    
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
      print("position closed, profit on pos = ", profit)
      sleep(5)
            

def eth_buy(tag): #if a sell is open, closes it. if a buy is open, keeps it. if a buy is not open, opens one.
    
    if sell_pos():
        close_order()
    if buy_pos():
        print("keeping BUY pos")
    else:
        if tag == 1:
            new_buy_pos()
            
   
   
def eth_sell(tag):     #if a buy is open, closes it. if a sell is open, keeps it. if a sell is not open, opens one
    
    if buy_pos():
        close_order()
    if sell_pos():
        print("keeping SELL pos")
    else:
        if tag == 1:
            new_sell_pos()                        
            

def login():
    browser.get("https://trader.alvexo.fr/trading-area")
    timeout = 5
    email_log = browser.find_element_by_xpath('//*[@id="email"]')
    email_log.send_keys('adamleroux26@gmail.com')   
    passwd_log = browser.find_element_by_xpath('//*[@id="pass1"]')
    passwd_log.send_keys('Redstone16')
    btn_log = browser.find_element_by_xpath('/html/body/div[2]/section/div/div[1]/div/div/div/div[1]/form/div[4]/div')
    sleep(0.5)
    btn_log.click()
    sleep(20)
    print("loading page ...")
    print("page loaded")
    print("acquiering values ...")

def search_val():
    search_val = browser.find_element_by_xpath('//*[@id="search_markets_input"]').send_keys('eth')

    eth_eur_val = browser.find_element_by_xpath('//*[@id="tradeBoardResizable"]/section/section[3]/div[3]/ul/li[3]/div[2]/div').click()

    del_search = browser.find_element_by_xpath('/html/body/div[3]/section[16]/section[1]/section/section[1]/span').click()

    print("values acquired")            

    print("running eth trade")
    
    graph = browser.find_element_by_xpath('/html/body/div[3]/section[16]/section[1]/section/section[2]/div[2]/div[1]/ul/li[11]/div[1]/div[2]/span[2]').click()


login()

search_val()


while 1:
    date = datetime.now()
    refresh = browser.find_element_by_xpath('//*[@id="draggableNavRightResizable"]/section/section[1]/ul/li[4]').click()
    details = browser.find_element_by_xpath('//*[@id="draggableNavRightResizable"]/section/section[1]/ul/li[2]').click()
    old_values = float(wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='draggableNavRightResizable']/section/section[2]/section[1]/div[3]/ul/li[1]/div[2]/div[6]/span"))).text.split("%")[0])
    
    
    time = 0
    while time <= 60: #the loop lasts 10 minutes
        
        if openpos():
            try:
                profit = float(browser.find_element_by_xpath('//*[@id="equity-item-pnl"]/span[2]').text)
                
            except NoSuchElementException:
                print("can't reach element 'profit', default value = 0")
                profit = 0    
                
        else:
            pass
        
        
        if openpos() : # checks if the pos is good. if it loses money, it kills the position
            if profit <-0.30 and buy_pos() :
                close_order()
                eth_sell() #if the profit drops below -0.35,or the curve is inversing, close the order and breaks the loop
            elif profit < -0.30 and sell_pos():
                close_order()
                eth_buy()            
            else:
                time += 1
                sleep(10)    
        else:
            time += 1
            sleep(10)
            
    refresh = browser.find_element_by_xpath('//*[@id="draggableNavRightResizable"]/section/section[1]/ul/li[4]').click()
    details = browser.find_element_by_xpath('//*[@id="draggableNavRightResizable"]/section/section[1]/ul/li[2]').click()
    new_values = float(WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='draggableNavRightResizable']/section/section[2]/section[1]/div[3]/ul/li[1]/div[2]/div[6]/span"))).text.split("%")[0])
    
    values = new_values - old_values
    print(values,"%")
    if values > 0:
        eth_buy(1)
            

    elif  values < -0:
        eth_sell(1) 
    else:
        print("doing nothing lul")   



os.system("pause")            