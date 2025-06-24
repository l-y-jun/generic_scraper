from config import  _raiseErrorMsg
from urllib import parse
import json

def createURLs(domain, page_to, main_q = [], opt_q = {}, domain_data = None):
    """Create List of URLS to Scrap.

    - Errors:

        - main_q(Essential Query) validating Errors.
        - opt_q(Optional Query) validating Errors.

    - Returns:

        - List of Urls
    """
    urls = [];

    # Validate Input data
    if not domain_data:
        domain_data = getJsonData(domain);

    main_queries = domain_data["main_queries"];
    validateQueries(main_queries, main_q);

    # Create Single URL
    urls.append("?".join((domain_data["url"], createQueryStr(main_q))));

    # Create Page Variations
    page_key = domain_data["page_key"];
    page_from = int(getPageNumber(urls[0], page_key));
    while page_from < page_to:
        page_from += 1;
        urls.append(changePageNumber(urls[0], page_key, page_from));
        
    return (urls);

def getJsonData(domain):
    """Return dict-like domain Data from 'domains.json'

        - Errors:

            - domains.json file not found in current directory Error.
            - domain name not found in json file Error.

        - Returns:

            - Dict-like domain Data.(like in domains.json)
    """
    json_data = None;
    with open("domains.json", "r") as f:
        try:
            json_data = json.load(f);
        except Exception as e:
            _raiseErrorMsg("filename Open Error", "domains.json");

    avail_domains = json_data.keys();
    if domain not in avail_domains:
        _raiseErrorMsg("domain name Not Found Error", domain);

    return (json_data[domain]);

def changePageNumber(url, page_key, page):
    page_at, page_end = getPageNumberIdx(url, page_key);
    return f"{url[:page_at]}{page}{url[page_end:]}";

def getPageNumber(url, page_key):
    page_from, page_to = getPageNumberIdx(url, page_key);
    return (url[page_from:page_to]);

def getPageNumberIdx(url, page_key):
    key_at = url.find(page_key);
    page_at = key_at + len(page_key) + 1;
    page_end = page_at;
    while (page_end < len(url) and '0' <= url[page_end] and url[page_end] <= '9'):
        page_end += 1;
    return (page_at, page_end)

def validateQueries(origin, src):
    """check count of multiple queries"""
    query_cnt = len(origin);
    if query_cnt != len(src):
        _raiseErrorMsg("query count not match", f"expected {len(origin)}, used with:{len(src)}")

    while(query_cnt):
        query_cnt -= 1;
        validateQuery(origin[query_cnt], src[query_cnt]);
    return (True);

def validateQuery(origin, src):
    """check value and name of the single query"""
    if origin["name"] != src["name"]:
        _raiseErrorMsg("query name not match", f"expected name as:{origin['name']}, used with:{src['name']}");
    if not src["value"]:
        _raiseErrorMsg("query value not found", f"key name 'vlue' not found");

    avail_values = origin.get("values", None);
    if avail_values and (src["value"] not in avail_values):
        _raiseErrorMsg("query value unusable", f"value: {src['value']} is not usable on {src['name']}");

    return (True);

def createQueryStr(query_options):
    return ("&".join(list(map(lambda el:f"{el['name']}={el['value']}" ,query_options))));

if __name__ == "__main__":
    query_opts = [
        {"name":"q", "value":"pencil"},
        {"name":"listSize", "value":60},
        {"name":"sorter", "value":"saleCountDesc"},
        {"name":"page", "value":3},
    ];
    urls = createURLs("coupang", 5, query_opts,{});
    print(urls);
    urls = createURLs("coupang", 2, query_opts,{});
    print(urls);

#def createURL(domain, main_q = [], opt_q = {}):"""Create List of URLS to Scrap.
