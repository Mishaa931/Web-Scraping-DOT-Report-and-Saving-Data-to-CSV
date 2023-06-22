from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://dot.report/usdot/KS/Wichita")

roster_tbody = driver.find_elements(By.XPATH, "//table/tbody/tr")
#j = 1
links=[]
print(len(roster_tbody))
for i in range(2,len(roster_tbody)):
    element = driver.find_element(By.XPATH, f"(//table/tbody/tr/td/a)[{i}]")
    links.append(element.get_attribute('href'))
    #j = j + 1 

data=[]   
for link in links:
    driver.get(link)
    time.sleep(5)
    try:
        companyName = driver.find_element(
            By.XPATH, '//tbody/tr[2]/td[1]').text
    except:
        companyName = '-'
    try:
        Num = driver.find_element(
            By.XPATH, '///div[@ class="jumbotron"]/h1').text
    except:
        Num = '-'
    try:
        address = driver.find_element(
            By.XPATH, '').text
        #a=address.split(" ")
        add= address.strip().split('\n')[0]
        #print(add)    
    except:
        address = '-'
    try:
        li=address.strip().split('\n')[-1].split(',')[-1].split(' ')
        li=list(filter(None, li))
        state=li[0]
        #print(state)
    except:
        state='-'

    try:
        #zip= address.strip().split('\n')[-1].split(',')[-1].split(' ')[-1]
        code=li[-1]
        #print(code)
    except:
        code='-'
    
    try:
        city = address.strip().split('\n')[-1].split(',')[0]
        #print(city)
    except:
        city='-'

    
    try:
        phNum = driver.find_element(
            By.XPATH, '//tbody/tr[4]/td[2]').text
    except:
        phNum = '-'


    tempData={"Company Name": companyName,
        "Dot Number":Num,
        "Address":add,
        "Phone Number":phNum,
        "City":city,
        "State":state,
        "Zip":code}

    data.append(tempData)

df_data =pd.DataFrame(data)
print(df_data)
df_data.to_csv('Pleasehojabhai.csv', index=False)