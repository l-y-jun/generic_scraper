from config import getDriver
from search import getPage, scrapItems, navigateNextPage
from urls import createURL

def searchList(domain, page_from, page_to, browser = "Chrome", options = {}):
    driver = getDriver(browser)
    items = []
    if not validate_options(domain, page_from, page_to, options):
        return ([])

    for i in range(page_from, page_to):
        options["page"] = i
        url = createURL(domain, options = options)
        print(url)
        with driver() as drv:
            try:
                print(f"START TO SCRAP PAGE {i}")
                if getPage(drv, url):
                    items.append(scrapItems(drv))
                else:
                    print("FAIL TO LOAD PAGE {i}")
                    return(items)
            except Exception as e:
                print(f"Uncaught Error, '{e}'. ends at {i} page.")
                return (items)
            print(f"END TO SCRAP PAGE {i}.")
    print("FINISHED TO SCRAP PAGES")
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
    page_to = 5
    options = {
        "keyword": keyword,
        "sorter":"latestAsc",
        "listSize": None
    }

    items = searchList("coupang", page_from, page_to, browser="Firefox", options = options)

