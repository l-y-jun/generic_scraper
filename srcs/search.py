from urllib import parse
from config import _BASEURL, BrowserLoadWaitWrapper, _raiseErrorMsg
import time
_URLTypes = {
    "search": "search"
}

_OrderTypes = [ # items order from
    "scoreDesc", # 0 recommended items[DEFAULT]
    "latestAsc", # 1 latest items
    "salePriceAsc", # 2 low price items
    "salePriceDesc", # 3 high price items
    "saleCountDesc", # 4 high order count items 
]

_PAGE_SIZES = [ # items per page
    36, # 0
    48, # 1
    60, # 2
    72, # 3 max item count[DEFAULT]
] 

@BrowserLoadWaitWrapper
def newPage(driver, url):
    driver.get(url)
    driver.implicitly_wait(3)
    time.sleep(4)

def navigatePage(drviver, page_from, page_to):
    print(f"move page from {page_from} to {page_to}...")

def scrapItems(driver):
    print(f"scrapPage")
    return []

def createUrl(keyword, sort_option = "latestAsc", page_size = 72):
    if sort_option not in _OrderTypes:
        _raiseErrorMsg("sort Option", sort_option)

    if page_size not in _PAGE_SIZES:
        _raiseErrorMsg("page size", page_size)
        
    url_tokens = [_BASEURL, f"{_URLTypes["search"]}?q={keyword}&listSize={page_size}&sorter={sort_option}&page="]
    return ("/".join(url_tokens))

def setUrl(base_url, page_number):
    return (f"{base_url}{page_number}")

"""
def test_fails(driver):
    driver.get('https://www.selenium.dev/selenium/web/dynamic.html')
    driver.find_element(By.ID, "adder").click()

    with pytest.raises(NoSuchElementException):
        driver.find_element(By.ID, 'box0')


def test_sleep(driver):
    driver.get('https://www.selenium.dev/selenium/web/dynamic.html')
    driver.find_element(By.ID, "adder").click()

    time.sleep(2)
    added = driver.find_element(By.ID, "box0")

    assert added.get_dom_attribute('class') == "redbox"

def test_implicit(driver):
    driver.implicitly_wait(2)
    driver.get('https://www.selenium.dev/selenium/web/dynamic.html')
    driver.find_element(By.ID, "adder").click()

    added = driver.find_element(By.ID, "box0")

    assert added.get_dom_attribute('class') == "redbox"

def test_explicit(driver):
    driver.get('https://www.selenium.dev/selenium/web/dynamic.html')
    revealed = driver.find_element(By.ID, "revealed")
    driver.find_element(By.ID, "reveal").click()

    wait = WebDriverWait(driver, timeout=2)
    wait.until(lambda _ : revealed.is_displayed())

    revealed.send_keys("Displayed")
    assert revealed.get_property("value") == "Displayed"
"""
