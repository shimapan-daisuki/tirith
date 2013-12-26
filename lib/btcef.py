#this function gets info data from mdc json about wallet and puts it in
#passed dictionary /data/ under pools name
import urllib2, datetime
import json

def update( name, settings, data ):
#gettin json for every pair and adding it to dict /data/
    if (name in data) == False:
        data[name] = dict()
        
        #for every rate set to be displayed
        for p in settings["rates"]:
            a = p
            for c in settings["rates"][p]:
                a = c
                b = settings["rates"][p][a]

            if (a in data[name]) == False:
                data[name][a] = dict()
            #then we look further for the second currency
            if (b in data[name][a]) == False:
                data[name][a][b] = dict()
            try:
                curr_a = str(a)
                curr_b = str(b)
                adress = "https://btc-e.com/api/2/"+curr_a.lower()+"_"+curr_b.lower()+"/ticker/"
                response = urllib2.urlopen(adress)
                btcef = json.loads(response.read())
                response.close()
                data[name][a][b]["average"] = float(btcef["ticker"]["avg"])
                data[name][a][b]["last"] = float(btcef["ticker"]["last"])
                data[name][a][b]["high"] = float(btcef["ticker"]["high"])
                data[name][a][b]["low"] = float(btcef["ticker"]["low"])
                data[name][a][b]["timestamp"] = datetime.datetime.fromtimestamp( int(btcef["ticker"]["updated"]))
                data[name][a][b]["volume"] = float(btcef["ticker"]["vol"])
                data[name][a][b]["volume_currency"] = float(btcef["ticker"]["vol_cur"])

            except:
                print "Ran into problem while trying to update %s %s/%s info, will try again at next update interval" % (name,a,b)
                return -1                
           
           
                              

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
                
