#this function gets info data from mdc json about wallet and puts it in
#passed dictionary /data/ under pools name
import urllib2, datetime
import json
btcef_pairs = [["btc", "usd"],["btc", "rur"],["btc", "eur"],["ltc", "usd"],["ltc", "rur"],["ltc", "eur"],["nmc", "usd"],["nvc", "usd"],["ppc", "usd"]]

def update( name, settings, data ):
#gettin json for every pair and adding it to dict /data/
    if (name in data) == False:
        data[name] = dict()
    for p in range(len(btcef_pairs)):
        currency_a = btcef_pairs[p][0]
        currency_b = btcef_pairs[p][1]
        currency_a = currency_a.upper()
        currency_b = currency_b.upper()
        if (currency_a in settings["coins"]) or (currency_b in settings["coins"]):
            adress = "https://btc-e.com/api/2/"+btcef_pairs[p][0]+"_"+btcef_pairs[p][1]+"/ticker/"
            try:
                response = urllib2.urlopen(adress)
                btcef = json.loads(response.read())
                response.close()
            except:
                print "Ran into problem while trying to update %s %s/%s info, will try again at next update interval" % (name,currency_a,currency_b)
                return -1                
            if (currency_b in settings["FIAT"]):
                if (currency_a in data["BTC-E"]) == False:
                    data["BTC-E"][currency_a] = dict()
                    
                if (currency_b in data["BTC-E"][currency_a]) == False:
                    data["BTC-E"][currency_a][currency_b] = dict()
                
                data["BTC-E"][currency_a][currency_b]["average"] = float(btcef["ticker"]["avg"])
                data["BTC-E"][currency_a][currency_b]["last"] = float(btcef["ticker"]["last"])
                data["BTC-E"][currency_a][currency_b]["high"] = float(btcef["ticker"]["high"])
                data["BTC-E"][currency_a][currency_b]["low"] = float(btcef["ticker"]["low"])
                data["BTC-E"][currency_a][currency_b]["timestamp"] = datetime.datetime.fromtimestamp( int(btcef["ticker"]["updated"]))
                data["BTC-E"][currency_a][currency_b]["volume"] = float(btcef["ticker"]["vol"])
                data["BTC-E"][currency_a][currency_b]["volume_currency"] = float(btcef["ticker"]["vol_cur"])
                

#closing connection
        

#this one displays info from middlecoin webapi
#which is stored in dictionary /data/
def display( exchange_name , data, simple ):
    print exchange_name
    for f in data[exchange_name]:
        for v in data[exchange_name][f]:
            print "\t\t%s/%s Date: %s" % (f,v,data[exchange_name][f][v]["timestamp"].strftime("%Y-%m-%d %H:%M:%S"))
            print "\tLast: \t%f\t\tAverage:\t%f" % (data[exchange_name][f][v]["last"],data[exchange_name][f][v]["average"])
            if simple == False:
                print "\tLow\t: %f\t\tHigh\t:\t%f" % (data[exchange_name][f][v]["low"],data[exchange_name][f][v]["high"])
                print "\tVolume\t: \t%f%s / %f%s" % (data[exchange_name][f][v]["volume"],v,data[exchange_name][f][v]["volume_currency"],f)
                
