from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as BS
import json

def find_by_selector(driver, selector, many = False):
    return driver.find_elements(BY.CSS_SELECTOR, selector) if many else driver.find_element(BY.CSS_SELECTOR, selector)

def find_by_tagname(driver, tagname, many = False):
    return driver.find_elements(By.TAG_NAME, tagname) if many else driver.find_element(By.TAG_NAME, tagname)

def find_by_linktext(driver, text, many = False):
    return driver.find_elements(By.LINK_TEXT, text) if many else driver.find_element(By.LINK_TEXT, text)

def _scrapeItem(el, selector_data):
    product_info = {
            "image": el.select_one(selector_data["image"])["src"],
            "name" : el.select_one(selector_data["name"]).text,
            "price" : el.select_one(selector_data["price"]).text
    }
    try:
        product_info["rating"] = el.select_one(selector_data["rating"]).text,
    except:
        product_info["rating"] = None

    try:
        product_info["reviews"] = el.select_one(selector_data["price"]).text,
    except:
        product_info["reviews"] = None

    return product_info

def scrapeItems(driver, selector_data):
    html = BS(driver.page_source, "html.parser")
    selector = selector_data["items"]
    items = html.select(selector)
    for i, item in enumerate(items):
        try:
            items[i] = _scrapeItem(item, selector_data["item"])
        except Exception as e:
            items[i] = None
            print(f"scrape Error at {i}!!!")
            print(item)

    return (items)

