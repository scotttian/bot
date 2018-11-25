import json
from pprint import pprint

enriched = []
with open('spy.json') as f:
    data = json.load(f)

last = None
lastTwo = None
for stock in data:
    if last != None:
        PremarketChange = round(stock['open'] - last['close'],4)
        PremarketChangePercentage = PremarketChange/last['close']
        previousChange = last['changePercent']
        if lastTwo != None:
            previousTwoChange = lastTwo['changePercent']
        else:
            previousTwoChange = 0
    else:
        PremarketChange = stock['open']
        PremarketChangePercentage =0
        previousChange = 0
        if lastTwo != None:
            previousTwoChange = lastTwo['changePercent']
        else:
            previousTwoChange = 0
    stock['PremarketChange'] = PremarketChange
    stock['PremarketChangePercentage'] = PremarketChangePercentage * 100
    stock['previousChange'] = previousChange
    stock['previousTwoChange'] = previousTwoChange
    enriched.append(stock)
    lastTwo = last
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
        if abs(stock['PremarketChangePercentage'])<0.8:
            #print stock['PremarketChangePercentage']
            continue
        if abs(stock['previousTwoChange'])<2:
            continue
        if abs(stock['previousChange'])<1.8:
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
            #netdiff = float(stock['changePercent'])-float(stock['PremarketChangePercentage'])
            if realChangePercent > 0.0:
                print "----------UP-----------"
                print "open: " + str(stock['open'])
                print "close: " + str(stock['close'])
                print "premarket: "+str(stock['PremarketChangePercentage'])
                print "change percent: " + str(stock['changePercent'])
                print "real change precent: "+str(realChangePercent)
                #print "net diff: " + str(netdiff)
                print "\n"
                sameDirection =sameDirection+1
        else:
            print "----------DOWN-----------"
            diffDirection = diffDirection+1
            print stock['date']
            print "open: " + str(stock['open'])
            print "close: " + str(stock['close'])
            print "premarket: "+str(stock['PremarketChangePercentage'])
            print "real change precent: "+str(realChangePercent)
            print "\n"
            #print stock['PremarketChangePercentage']
            index = index+1
    print "same: "+str(sameDirection)
    print "diff: "+str(diffDirection)

Stats(enriched,70)
