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
            currency_a = a
            currency_b = b
            adress = "http://data.mtgox.com/api/1/"+currency_a+currency_b+"/ticker"

            try:
                response = urllib2.urlopen(adress)
                mtg_json = json.loads(response.read())
                #closing connection
                response.close()
            except:
                print "Ran into problem while trying to update %s info, will try again at next update interval" % name
                return -1  
            mtg = mtg_json["return"]                
            data[name][currency_a][currency_b]["average"] = float(mtg["avg"]["value"])
            data[name][currency_a][currency_b]["last"] = float(mtg["last"]["value"])
            data[name][currency_a][currency_b]["high"] = float(mtg["high"]["value"])
            data[name][currency_a][currency_b]["low"] = float(mtg["low"]["value"])
            data[name][currency_a][currency_b]["timestamp"] = datetime.datetime.fromtimestamp( int(mtg["now"])/1e6)
            


#displays info from middlecoin webapi
#which is stored in dictionary /data/
def display( exchange_name , data, simple ):
    print exchange_name
    for f in data[exchange_name]:
        for v in data[exchange_name][f]:
            print "\t\t%s/%s Date: %s" % (f,v,data[exchange_name][f][v]["timestamp"].strftime("%Y-%m-%d %H:%M:%S"))
            print "\tLast: \t%f\t\tAverage:\t%f" % (data[exchange_name][f][v]["last"],data[exchange_name][f][v]["average"])
            if simple == False:
                print "\tLow: \t%f\t\tHigh:\t\t%f" % (data[exchange_name][f][v]["low"],data[exchange_name][f][v]["high"])
                
