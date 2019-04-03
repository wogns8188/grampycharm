from libs.naverShopping.crawler import crawl
from libs.naverShopping.parser import parse
import json

def pageNumber():
    result=[]
    for pageIndex in range(1,3):
        result = result + parse(crawl(pageIndex))
    return result


res = pageNumber()
for item in res:
    print(item)
print(len(res))

file = open("./naverShopping.json", "w+")
file.write(json.dumps(res))
