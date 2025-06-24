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
        try:
            with driver() as drv:
                ret = getPage(drv, url)
                if ret is True:
                    items = items + scrapeItems(drv, domain_data["selector"])
        except Exception as e:
            print(f"Fail on {i} Time")
            # TODO 1: Failed Page Handling.
        #TODO 2: Duplicate Page Located Handling
        i += 1
    return (items)

if __name__ == "__main__":
    # domain Should be in domains.json
    domain = "coupang"
    # Set page of the End
    page_to = 4

    # Order Should be follwed as in domains.json
    main_queries = [ 
        {"name": "q", "value":"pencil"}, # Search Item
        {"name": "listSize", "value": 60}, # Items Count
        {"name": "sorter", "value":"latestAsc"}, # Items Order
        {"name": "page", "value": 3}, # Page Start
    ]
    opt_queries = {}

    items = searchList(domain, page_to, "Firefox", main_queries, opt_queries)
    export_to_file(domain, keyword, items)
