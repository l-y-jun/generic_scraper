from bs4 import BeautifulSoup as BS
from selenium.webdriver.common.by import By

def scrapeItems(driver, selector_data):
    html = BS(driver.page_source, "html.parser")
    selectors = selector_data["items"]
    for selector in selectors:
        items = html.select(selector)
        if items:
            print(f"item count: {len(items)}")
            for i, item in enumerate(items):
                try:
                    if i < 3:
                        print(item)
                    items[i] = _scrapeItem(item, selector_data["item"])
                except Exception as e:
                    print(f"scrape Error at {i}!!!")
                    items[i] = None
            return items
    return [];

def toNumeric(s):
    ret = "".join(filter(str.isnumeric, list(s)))
    return ret

def _scrapeItem(el, selector_data):
    product_info = {
            "image": None,
            "name" : el.select_one(selector_data["name"])["alt"],
            "price" : None,
            "rating": None,
            "reviews": None
    }

    try:
        image = el.select_one(selector_data["image"])["src"]
        if not image.startswith("https"):
            image = f"https:{image}"
        product_info["image"] = image
    except Exception as e:
        pass

    try:
        price_text = el.select_one(selector_data["price"]).text
        price = int(price_text) if price_text.isnumeric() else int(toNumeric(price_text))
        product_info["price"] = price
    except Exception as e:
        pass

    try:
        rating = el.select_one(selector_data["rating"]).text
        rating = int(rating)
        product_info["rating"] = rating
    except Exception as e:
        pass

    try:
        reviews = el.select_one(selector_data["reviews"]).text
        reviews = "".join(filter(lambda ch: ch >= '0' and ch <= '9', list(reviews)))
        reviews = int(reviews)
        product_info["reviews"] = reviews
    except Exception as e:
        pass

    return product_info

def find_by_tagname(driver, tagname, many = False):
    return driver.find_elements(By.TAG_NAME, tagname) if many else driver.find_element(By.TAG_NAME, tagname)

"""
def find_by_selector(driver, selector, many = False):
    return driver.find_elements(BY.CSS_SELECTOR, selector) if many else driver.find_element(BY.CSS_SELECTOR, selector)

def find_by_linktext(driver, text, many = False):
    return driver.find_elements(By.LINK_TEXT, text) if many else driver.find_element(By.LINK_TEXT, text)
"""
