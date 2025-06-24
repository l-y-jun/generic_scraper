from config import getDriver
from search import getPage
from scrape import scrapeItems
from urls import createURLs, getJsonData
from export import export_to_file

def getItemList(domain, page_to = 1, browser = "Chrome", main_queries = [], opt_queries = {}):
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
    # 1. set domain
    ## domain Should be in domains.json
    domain = "coupang"
    # 2. set the keyword to Search
    keyword = "pencil"
    # 3. set Page start
    page_from = 3
    # 4. set Page end
    page_to = 4

    # 5. Set QueryOptions
    ## Order of list Should be follow as in domains.json
    main_queries = [ 
        {"name": "q", "value": keyword}, # Search Item
        {"name": "listSize", "value": 60}, # Items Count
        {"name": "sorter", "value":"latestAsc"}, # Items Order
        {"name": "page", "value": page_from}, # Page Start
    ]
    # 6. future release feature
    opt_queries = {}

    # 7. get items list
    items = getItemList(domain, page_to, "Firefox", main_queries, opt_queries)
    # 8. export item list to csv
    export_to_file(domain, keyword, items)
