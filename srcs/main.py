from config import getDriver
from search import getPage, navigateNextPage
from scrape import scrapeItems
from urls import createURL
from export import export_to_file
import json

def searchList(domain, page_from, page_to, browser = "Chrome", options = {}):
    driver = getDriver(browser)
    items = []
    json_data = None
    if not validate_options(domain, page_from, page_to, options):
        return ([])

    with open("domains.json", "r") as f:
        json_data = json.load(f)

    with driver() as drv:
        for i in range(page_from, page_to + 1):
            options["page"] = i
            url = createURL(domain, json_data, options = options)
            print(url)
            try:
                print(f"START TO scrape PAGE {i}")
                if getPage(drv, url):
                    items = items + scrapeItems(drv, json_data[domain]["selectorInfo"])
                else:
                    print("FAIL TO LOAD PAGE {i}")
                    drv.quit()
                    return(items)
            except Exception as e:
                print(f"Uncaught Error, '{e}'. ends at {i} page.")
                drv.quit()
                return (items)
            print(f"END TO scrape PAGE {i}.")
            drv.close()
        drv.quit()
    print("FINISHED TO scrape PAGES")
    return (items)

def validate_options(domain, page_from, page_to, options = {}):
    if page_from > page_to:
        return (False)

    if domain == "coupang":
        if not options.get("keyword", None):
            return (False)

    return (True)


if __name__ == "__main__":
    keyword = "pencil"
    page_from = 1
    page_to = 1
    options = {
        "keyword": keyword,
        "sorter":"latestAsc",
        "listSize": None
    }

    domain = "coupang"
    items = searchList(domain, page_from, page_to, browser="Firefox", options = options)
    print("SAVE TO FILES")
    export_to_file(domain, keyword, items)
