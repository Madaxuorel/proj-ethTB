#Developpé par Adam Le Roux
#Trading Bot V1
#Depuis le site alvexo.fr
#1°) login 
#2°) Mettre les valeures voulues en favori 


import os
from time import sleep
from selenium import webdriver


from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException 
from selenium.common.exceptions import ElementNotInteractableException
def removeprc(string): #removes the % from a string 
    string = str(string)
    list = string.split('%')
    string = " ".join(list)
    
    return string



    
def new_buy_pos():
    browser.find_element_by_xpath('//*[@id="market-watch"]/li[13]/div[2]/div[3]/span[1]').click()
    try:
        browser.find_element_by_xpath(' //*[@id="qtySelect"]/span').click()
    except ElementNotInteractableException :
        browser.find_element_by_xpath('//*[@id="app"]/section[1]/div/span[1]').click()
        browser.find_element_by_xpath('//*[@id="market-watch"]/li[13]/div[2]/div[3]/span[1]').click()
        browser.find_element_by_xpath(' //*[@id="qtySelect"]/span').click()
         
    browser.find_element_by_xpath('//*[@id="qtySelect"]/div/div[1]/ul/li[4]').click()
    browser.find_element_by_xpath('//*[@id="new-order"]/div/div[2]/div[1]/div[3]/div[1]/ul/li[3]/div/span[1]').click()
    sleep(5)
    
def new_sell_pos():
    browser.find_element_by_xpath('//*[@id="market-watch"]/li[13]/div[2]/div[1]/span[1]').click()
    try:
        browser.find_element_by_xpath(' //*[@id="qtySelect"]/span').click()
    except ElementNotInteractableException :
        browser.find_element_by_xpath('//*[@id="app"]/section[1]/div/span[1]').click()
        browser.find_element_by_xpath('//*[@id="market-watch"]/li[13]/div[2]/div[1]/span[1]').click()
        browser.find_element_by_xpath(' //*[@id="qtySelect"]/span').click()
    browser.find_element_by_xpath('//*[@id="qtySelect"]/div/div[1]/ul/li[4]').click()
    browser.find_element_by_xpath('//*[@id="new-order"]/div/div[2]/div[1]/div[3]/div[1]/ul/li[1]/div/span[1]').click()
    
    
    
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
      browser.find_element_by_xpath('//*[@id="item_749992"]/td[16]/button').click()


def removeprc(string): #removes the % from a string 
    string = str(string)
    list = string.split('%')
    string = " ".join(list)
    
    return string


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
        if tag == -1:
            new_sell_pos()
        elif tag == -2:
            print("c pas mal vend")
        elif tag == -3:
            print("vend putain")
        elif tag == -4:
            print("c chaud là")
            
            



browser = webdriver.Chrome(executable_path=r"C:\Users\pc adam\Documents\EISTI\algoprog\perso\python\chromedriver\chromedriver.exe")

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
sleep(15) #let the page load ...

#search markets and add them to favs~~
#here, tsla, btc, google, eth
print("page loaded")
print("acquiering values ...")
nb_of_values = 0
while nb_of_values <= 4:
    search_val = browser.find_element_by_xpath('//*[@id="search_markets_input"]')
    
    nb_of_values += 1
    if nb_of_values == 1:
        search_val.send_keys('btc') 
        btc_eur_val = browser.find_element_by_xpath('//*[@id="tradeBoardResizable"]/section/section[3]/div[3]/ul/li[3]/div[2]/div')
        btc_eur_val.click()
        del_search = browser.find_element_by_xpath('//*[@id="tradeBoardResizable"]/section/section[1]/span')
        del_search.click()    
    elif nb_of_values == 2:    
        search_val.send_keys('tsla')
        tsla_val = browser.find_element_by_xpath('//*[@id="tradeBoardResizable"]/section/section[3]/div[3]/ul/li/div[2]/div')
        tsla_val.click()
        del_search = browser.find_element_by_xpath('//*[@id="tradeBoardResizable"]/section/section[1]/span')
        del_search.click()    
    elif nb_of_values == 3:
        search_val.send_keys('eth')
        eth_eur_val = browser.find_element_by_xpath('//*[@id="tradeBoardResizable"]/section/section[3]/div[3]/ul/li[3]/div[2]/div')
        eth_eur_val.click()
        del_search = browser.find_element_by_xpath('//*[@id="tradeBoardResizable"]/section/section[1]/span')
        del_search.click()      
    elif nb_of_values == 4:
        search_val.send_keys('goog')
        eth_eur_val = browser.find_element_by_xpath('//*[@id="tradeBoardResizable"]/section/section[3]/div[3]/ul/li/div[2]/div')
        eth_eur_val.click()
        del_search = browser.find_element_by_xpath('//*[@id="tradeBoardResizable"]/section/section[1]/span')
        del_search.click()              
#~~                                                 
print("values acquired")
#testing by focusing on btc_eur
#first, getting buy and sell % from the website


eth_inv = 100
print("running eth trade")
graph_icon = browser.find_element_by_xpath('//*[@id="market-watch"]/li[13]/div[1]/div[2]/span[2]').click()


while 1:
    sleep(3)
    refresh = browser.find_element_by_xpath('//*[@id="draggableNavRightResizable"]/section/section[1]/ul/li[4]').click()
    details = browser.find_element_by_xpath('//*[@id="draggableNavRightResizable"]/section/section[1]/ul/li[2]').click()
    eth_values = browser.find_element_by_xpath('/html/body/div[3]/section[16]/section[3]/section/section[2]/section[1]/div[3]/ul/li[1]/div[2]/div[6]/span/text()')
    eth_values = eth_values.text
    eth_values = removeprc(eth_values)
    eth_values = float(eth_values)
    print(eth_values,"%")
    if eth_inv <= 200 and eth_values >= 0.5:
        eth_buy(1)
            

    elif eth_inv >= 0 and eth_values <= -0.5:
        eth_sell(1) 
       
    
    
    
       

    
      
   
        
        




os.system("pause")
