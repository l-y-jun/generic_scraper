from config import  _raiseErrorMsg
from urllib import parse
import json

def _createQuery(query_options, options):
    urls = []
    for key in query_options:
        if key not in options:
            _raiseErrorMsg("search option not found in options", key)
        try:
            value = options[key] or query_options[key].get("values",[])[0]
            if query_options[key].get("values", None):
                if value not in query_options[key]["values"]:
                    _raiseErrorMsg(f"search option {key} value", value)
            urls.append(f"{key}={value}")
        except AttributeError as e:
            urls.append(f"{query_options[key]}={options[key]}")

    return "&".join(urls)

def createURL(domain, options = {}):
    urls = []

    with open("domains.json", "r") as f:
        data = json.load(f)
        avail_domains = data.keys()
        if domain not in avail_domains:
            _raiseErrorMsg("domain", domain)

        domain_options = data[domain]
        if options and options.get("keyword", None):
            urls.append(f'{domain_options["url"]}?')
        else:
            _raiseErrorMsg("query option", options["keyword"])

        urls.append(_createQuery(domain_options["query"], options))

    return ("".join(urls))
