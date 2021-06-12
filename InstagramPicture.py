from bs4 import BeautifulSoup as bs
import selenium.common.exceptions
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
 
print("enter username")
username = input()
 
print("enter password")
password = input()
 
print("enter the url")
url = input()


path()
time.sleep(1)
 
url_name(url)
 
login(username, password)
 
first_picture()
like_pic()
 
continue_liking()
chrome.close()


def login(username, your_password):
     
    # finds the login button
    log_but = chrome.find_element_by_class_name("L3NKy")
    time.sleep(2)
 
    # clicks the login button
    log_but.click()    
    time.sleep(4)
 
    # finds the username box
    usern = chrome.find_element_by_name("username")    
 
    # sends the entered username
    usern.send_keys(username)   
 
    # finds the password box
    passw = chrome.find_element_by_name("password")    
 
    # sends the entered password
    passw.send_keys(your_password)      
    passw.send_keys(Keys.RETURN)
    time.sleep(6)
    notn = chrome.find_element_by_class_name("yWX7d")# dont save info button
    notn.click()# click don't save button
    time.sleep(3)
    
    
def first_picture():
   
    # finds the first picture 
    pic = chrome.find_element_by_class_name("kIKUG")   
    pic.click()   # clicks on the first picture
    
    
 
def like_pic():
    time.sleep(2)
    like = chrome.find_element_by_class_name('fr66n')
    soup = bs(like.get_attribute('innerHTML'),'html.parser')
    if(soup.find('svg')['aria-label'] == 'Like'):
        like.click()
    time.sleep(2)


def next_picture():
    time.sleep(2)
    try:
        nex = chrome.find_element_by_class_name("coreSpriteRightPaginationArrow")
        time.sleep(1)
        return nex
    except selenium.common.exceptions.NoSuchElementException:
        return 0

def continue_liking():
    while(True):
        next_el = next_picture()
 
        # if next button is there then
        if next_el != False:
 
            # click the next button
            next_el.click()
            time.sleep(2)
 
            # like the picture
            like_pic()
            time.sleep(2)
        else:
            print("not found")
            break
            
def path():  
    global chrome
    print("enter the driver path")
    exe_path = input()
 
    # starts a new chrome session
    chrome = webdriver.Chrome() 



def url_name(url):  
    # the web page opens up
    chrome.get(url) 
    
    # webdriver will wait for 4 sec before throwing a  
    # NoSuchElement exception so that the element 
    # is detected and not skipped.
    time.sleep(4) 
    
#Ends    
