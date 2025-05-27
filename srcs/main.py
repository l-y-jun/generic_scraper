from config import getDriver
from search import newPage, scrapItems, createUrl, setUrl, navigatePage

PAGE_OPTIONS = {
    "from" : 1, # 검색 페이지 시작 
    "to" : 10,  # 검색 페이지 끝
    "size" : 60 # 36, 48, 60, 72
}

def searchList(base_url, page_range, browser = "Chrome"):
    driver = getDriver(browser)
    with driver() as drv:
        print("DRIVER STARTED, wait 8s for bootstrap...")
        page_number = next(page_range)
        target_url = setUrl(base_url, page_number)
        newPage(drv, target_url)
        for page_number in page_range:
            print("1. start Find")
            print("2. start scrap")
            items = scrapItems(drv)
            print("3. start Navigate")
            navigatePage(drv, page_number, page_number + 1)
            print(items)

    print("END.")

if __name__ == "__main__":
    keyword = "pencil"

    for page_number in range(PAGE_OPTIONS["from"], PAGE_OPTIONS["to"] + 1):
        url = createUrl(keyword, sort_option = "latestAsc", page_size = PAGE_OPTIONS["size"])
        print(f"{url}{page_number}")

    url = createUrl(keyword, sort_option = "latestAsc", page_size = PAGE_OPTIONS["size"])
    page_range = range(PAGE_OPTIONS["from"], PAGE_OPTIONS["to"] + 1)
    searchList(url, iter(page_range), browser = "Firefox")

