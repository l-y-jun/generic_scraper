from config import getDriver
from search import getPage, scrapItems, navigateNextPage
from urls import createURL

def searchList(url, page_from, page_to, browser = "Chrome"):
    driver = getDriver(browser)
    pages = page_to - page_from

    with driver() as drv:
        print("DRIVER STARTED, wait 8s for bootstrap...")
        for i in range(pages):
            if getPage(drv, url):
                print("SUCCESS TO LOAD PAGE")
                items = scrapItems(drv)
                url = navigateNextPage(drv)
                if not url:
                    return (False)
            else:
                print("FAIL TO LOAD PAGE")

    print("END.")
    return (True)

if __name__ == "__main__":
    keyword = "pencil"
    page_from = 1
    page_to = 5

    url = createURL("coupang", {"keyword": "pencil", "sorter":"latestAsc", "listSize": None, "page": page_from})
    print(url)

    searchList(url, page_from, page_to, browser="Firefox")

