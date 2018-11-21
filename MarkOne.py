import json
from pprint import pprint

enriched = []
with open('spy.json') as f:
    data = json.load(f)

last = None
for stock in data:
    if last != None:
        PremarketChange = round(stock['open'] - last['close'],4)
        PremarketChangePercentage = PremarketChange/last['close']
        previousChange = last['changePercent']
    else:
        PremarketChange = stock['open']
        PremarketChangePercentage =0
        previousChange = 0
    stock['PremarketChange'] = PremarketChange
    stock['PremarketChangePercentage'] = PremarketChangePercentage * 100
    stock['previousChange'] = previousChange
    enriched.append(stock)
    last = stock


def Stats(data,month):
    sameDirection = 0
    diffDirection  =0
    offset = 1258 - month*22
    index = 0
    for stock in data:
        if index < offset:
            index = index+1
            continue
        if abs(stock['PremarketChangePercentage'])<1.4:
            #print stock['PremarketChangePercentage']
            continue
        if abs(stock['previousChange'])<1.4:
            continue
        # if abs(stock['previousChange'])<1.5 or abs(stock['previousChange'])>2:
        #     continue
        #print stock['date']
        realChangePercent = (stock['close'] - stock['open'])*100/stock['open']
        # if stock['previousChange'] * stock['PremarketChangePercentage'] <= 0:
        #     continue
        if realChangePercent * stock['PremarketChangePercentage']>=0:
            #sameDirection =sameDirection+1
            #print stock['date']
            netdiff = float(stock['changePercent'])-float(stock['PremarketChangePercentage'])
            if abs(netdiff) > 0.5:
                print stock['date']
                print "premarket: " + str(stock['PremarketChangePercentage'])
                print "open: " + str(stock['open'])
                print "close: " + str(stock['close'])
                print "change percent: " + str(stock['changePercent'])
                print "real change precent: "+str(realChangePercent)
                print "net diff: " + str(netdiff)
                print "\n"
                sameDirection =sameDirection+1
        else:
            diffDirection = diffDirection+1
            print stock['date']
            print "real change precent: "+str(realChangePercent)
            print "\n"
            #print stock['PremarketChangePercentage']
            index = index+1
    print "same: "+str(sameDirection)
    print "diff: "+str(diffDirection)

Stats(enriched,70)
