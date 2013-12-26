#this function gets info data from mdc json about wallet and puts it in
#passed dictionary /data/ under pools name
import urllib2
import json, estimate
import datetime, calendar

class UTC(datetime.tzinfo):
    """UTC"""

    def utcoffset(self, dt):
        return 0

    def tzname(self, dt):
        return "UTC"

    def dst(self, dt):
        return None

utc = UTC()

def update( pool_name, settings, data ):
#gettin json
    try:
        response = urllib2.urlopen(settings["adress"])
        mdc_json = json.loads(response.read())
        response.close()
    except:
        print "Ran into problem while trying to update %s info, will try again at next update interval" % pool_name
        return -1
#getting part with partical wallet info
    for k in mdc_json["report"]:
        if k[0] == settings["wallet"]:
            break
    data[pool_name] = k[1]
    timestamp = mdc_json["time"]
#converting our values to float    
    for x in data[pool_name].keys():
        data[pool_name][x] = float(data[pool_name][x])
        
    data[pool_name]["time"] = datetime.datetime.strptime(timestamp,"%Y-%m-%d %H:%M:%S")
    data[pool_name]["time"] = data[pool_name]["time"].replace(tzinfo=utc)
    data[pool_name]["time"] = datetime.datetime.fromtimestamp(calendar.timegm(data[pool_name]["time"].timetuple()))
    
#closing connection

#this one displays info from middlecoin webapi
#which is stored in dictionary /data/
def estimate_and_write( balance, settings, exchanges, exchange_info ):
    est = dict()
    for j in settings["estimates"]:
        est[j] = estimate.to_FIAT( balance, settings["currency"], j, exchanges, exchange_info)
    for j in est:
        for z in est[j]:
            print "\t\t\t= %.2f %s @%s %s" % ( est[j][z]["est"], j, z, est[j][z]["mode"])
  
def display( pool_name, settings, data, exchanges, exchange_info ):
    hashrate = data[pool_name].get("megahashesPerSecond",0)
    rejected = (data[pool_name].get("rejectedMegahashesPerSecond", 0) / data[pool_name].get("megahashesPerSecond", 0)* 100)
    paid =  data[pool_name].get("paidOut", 0)
    unpaid =  data[pool_name].get("immatureBalance", 0) + data[pool_name].get("unexchangedBalance", 0) + data[pool_name].get("bitcoinBalance", 0)
    exchanged = data[pool_name].get("bitcoinBalance", 0)
    unexchanged = data[pool_name].get("unexchangedBalance", 0)
    immature = data[pool_name].get("immatureBalance", 0)
    total = paid + unpaid
    shares = data[pool_name].get("lastHourShares",0)
    print pool_name
    print "Date: "+data[pool_name]["time"].strftime("%Y-%m-%d %H:%M:%S")
    print "Hashrate:\t %.2f Kh/s\tRejected:\t%.1f%%   Shares last h:  %d" % ((hashrate*1000), rejected, shares)
    print "Total paid:\t ", paid, settings["currency"]
    if ( "paid" in settings["estimates2"]):
         estimate_and_write( paid, settings, exchanges, exchange_info)
    print "Total unpaid:\t ", unpaid, settings["currency"]
    if ( "unpaid" in settings["estimates2"]):
         estimate_and_write( unpaid, settings, exchanges, exchange_info)
    print "Grand total:\t ", total, settings["currency"]
    if ( "total" in settings["estimates2"]):
         estimate_and_write( total, settings, exchanges, exchange_info)
    if settings["simple_info"] == False:
        print "Exchanged:\t ", exchanged, settings["currency"]
        if ( "exchanged" in settings["estimates2"]):
             estimate_and_write( exchanged, settings, exchanges, exchange_info)
        print "Unexchanged:\t ", unexchanged, settings["currency"]
        if ( "unexchanged" in settings["estimates2"]):
             estimate_and_write( unexchanged, settings, exchanges, exchange_info)
        print "Immature:\t  %f %s" % (immature, settings["currency"])
        if ( "immature" in settings["estimates2"]):
             estimate_and_write( immature, settings, exchanges, exchange_info)
        
