from config import _BASEURL, BrowserLoadWaitWrapper, _raiseErrorMsg, _NEXT_BUTTON_SELECTOR 
from scrap import find_by_selector, find_by_tagname, find_by_linktext
from  selenium.webdriver.common.action_chains import ActionChains
import time

_MAX_RETRIES = 5

def _loadWait(driver):
    time.sleep(1.5)
    driver.implicitly_wait(4)
    time.sleep(1.5)

def _isLoaded(driver):
    el = find_by_tagname(driver, "footer")
    return True if el else False

def getPage(driver, url, retries = _MAX_RETRIES):
    driver.get(url)
    for i in range(retries):
        _loadWait(driver)
        if _isLoaded(driver):
            return True 
        print(f"Page Load retry for {i + 1} time(~{retries} retries)")
    return False

def navigateNextPage(driver, retries = _MAX_RETRIES):
    #el = find_by_selector(driver, ".btn-next > span")
    el = find_by_linktext(driver, "다음")
    if not el:
        print("NOT FOUND")
        return False
    if el and el.get_attribute("href"):
        print("FOUND EL!")
        return(el.get_attribute("href"))
    else:
        print("NOTFOUND EL")
        return False

def click(driver, el):
    action = ActionChains(driver)
    print("CLICKing...", el)
    action.move_to_element(el)
    action.pause(3)
    action.click(el)
    action.perform()
    time.sleep(4)
    #.pause(1)\
    
def scrapItems(driver):
    print(f"scrapPage")
    return []

