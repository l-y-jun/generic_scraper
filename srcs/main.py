from config import getDriver
from search import getPage, scrapItems, createUrl

PAGE_OPTIONS = {
    "from" : 1, # 검색 페이지 시작 
    "to" : 10,  # 검색 페이지 끝
    "size" : 60 # 36, 48, 60, 72
}

def searchList(url, page_range, browser = "Chrome"):
    driver = getDriver(browser)
    with driver() as drv:
        print("DRIVER STARTED, wait 8s for bootstrap...")
        getPage(drv, f"{url}{next(page_range)}")
        for page_number in page_range:
            print("start Search,")
            nav
            print("start scrap...")
            items = scrapItems(drv)
            print(items)

    print("END.")

if __name__ == "__main__":
    keyword = "pencil"

    for page_number in range(PAGE_OPTIONS["from"], PAGE_OPTIONS["to"] + 1):
        url = createUrl(keyword, sort_option = "latestAsc", page_size = PAGE_OPTIONS["size"])
        print(f"{url}{page_number}")

    page_range = range(PAGE_OPTIONS["from"], PAGE_OPTIONS["to"] + 1)
    searchList(url, page_range, browser = "Firefox")

