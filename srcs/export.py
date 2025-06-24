import time

def export_to_file(domain, keyword, items, filename=None):
    to_csv = to_csv_text(items)
    if not filename:
        t = time.localtime()
        filename = f"{domain}_{keyword}_{t.tm_hour}-{t.tm_min}-{t.tm_sec}.csv"
        with open(filename, "w") as f:
            f.write(f"image,name,price,rating,reviews\n{to_csv}");
    elif filename.endswith(".csv"):
        with open(filename, "a") as f:
            f.write(to_csv)
    else:
        print("ERROR WRITING FILE, only CSV file supported")
        return 0;
    print(f"DONE WRITING FILE {filename}")
        
def to_csv_text(items):
    ret = []
    for item in items:
        try:
            rating = item.get("rating", "")
            reviews = item.get("reviews", "")
            ret.append(f'{item["image"]},"{item["name"]}",{item["price"]},{rating},{reviews}\n')
        except:
            pass
    return "".join(ret)
