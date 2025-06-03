from selenium import webdriver

_BROWSERS = {
    "Edge": webdriver.Edge,
    "Firefox": webdriver.Firefox,
    "Chrome": webdriver.Chrome,
    "Safari": webdriver.Safari,
}
_BASEURL = "https://www.coupang.com/np"
_GENERAL_WAITTIME = 6

_CUR_BUTTON_SELECTED_SELECTOR = ".Pagination_selected__r1eiC"
_NEXT_BUTTON_SELECTOR  = ".Pagination_nextBtn__TUY5t"

def _raiseErrorMsg(domain, value):
    raise ValueError(f"E: On {domain}, {value} is not Supported")

def getDriver(browserType):
    driver = None
    if browserType not in _BROWSERS:
        _raiseErrorMsg("browser Type", browserType)
    driver = _BROWSERS[browserType]
    return driver

def BrowserLoadWaitWrapper(func):
    def wrapper(*args, **kwargs):
        print("Before calling the function.")
        func(*args, **kwargs)
        print("After calling the function.")
    return wrapper
