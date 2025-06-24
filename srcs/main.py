from config import getDriver
from search import getPage
from scrape import scrapeItems
from urls import createURLs, getJsonData
from export import export_to_file

def searchList(domain, page_to = 1, browser = "Chrome", main_queries = [], opt_queries = {}):
    driver = getDriver(browser);
    items = [];
    domain_data = getJsonData(domain);

    urls = createURLs(domain, page_to, main_queries, opt_queries, domain_data)
    
    i = 1;
    for url in urls:
        print(f"scrape {url}...")
        with driver() as drv:
            print(f"START TO scrape PAGE: {i} times")
            ret = getPage(drv, url)
            if ret is True:
                print("HI", ret)
                items = items + scrapeItems(drv, domain_data["selector"])
            else:
                print("FAIL TO LOAD PAGE: at {i} times")
            """
            except Exception as e:
                print(f"Uncaught Error, '{e}'. ends at {i} times.")
                drv.close()
                drv.quit()
                return items;
            """
            print(f"END TO scrape PAGE: {i} times.")
        i += 1
    print("FINISHED TO scrape PAGES")
    return (items)

if __name__ == "__main__":
    domain = "coupang"
    keyword = "pencil"
    page_to = 3
    main_queries = [
        {"name": "q", "value":"pencil"},
        {"name": "listSize", "value": 60},
        {"name": "sorter", "value":"latestAsc"},
        {"name": "page", "value": 3},
    ]
    opt_queries = {}
    items = searchList(domain, page_to, "Firefox", main_queries, opt_queries)
    export_to_file(domain, keyword, items)
