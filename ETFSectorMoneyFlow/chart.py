import json
from pprint import pprint

enriched = []
with open('BasicMaterials_XLB.json') as f:
    data = json.load(f)

for stock in data:
    print stock['close']
