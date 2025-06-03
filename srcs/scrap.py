from selenium.webdriver.common.by import By

def find_by_selector(driver, selector):
    elem = driver.find_element(By.CSS_SELECTOR, selector)
    return (elem)

def find_by_tagname(driver, tagname):
    elem = driver.find_element(By.TAG_NAME, tagname)
    return (elem)

def find_by_linktext(driver, text):
    elem = driver.find_element(By.LINK_TEXT, text)
    return (elem)
        
