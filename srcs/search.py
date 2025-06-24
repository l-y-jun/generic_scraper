from config import BrowserLoadWaitWrapper, _raiseErrorMsg
from scrape import find_by_tagname
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import time

_MAX_RETRIES = 3

def _loadWait(driver):
    time.sleep(1)
    driver.implicitly_wait(3)
    time.sleep(1)

def _isLoaded(driver):
    try: 
        footer = find_by_tagname(driver, "footer")
        wait = WebDriverWait(driver, timeout=3)
        wait.until(lambda _ : footer.is_displayed())
    except NoSuchElementException:
        return False
    return True if footer else False

def getPage(driver, url, retries = _MAX_RETRIES):
    driver.get(url)
    _loadWait(driver)
    for _ in range(retries):
        if _isLoaded(driver):
            return True
    return _isLoaded(driver)

"""
from scrape import find_by_selector, find_by_linktext
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
    
def scrapeItems(driver):
    print(f"scrapePage")
    return []
"""
