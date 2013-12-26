import urllib2, ssl
import json, estimate, datetime
def update( pool_name, settings, data ):
#gettin json
    adress = settings["adress"]+"api.php?api_key="+settings["api_key"]
    hdr = {'User-Agent':'Mozilla/5.0'}
    try:
        req = urllib2.Request(adress,headers=hdr)
        response = urllib2.urlopen(req)
        c_json = json.loads(response.read())
        #closing connection
        response.close()
    except:
        print "Ran into problem while trying to update %s info, will try again at next update interval" % pool_name
        return -1
    data[pool_name] = c_json
    timestamp = datetime.datetime.now()
#time   
    data[pool_name]["time"] = timestamp


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
    username = data[pool_name].get("username",0)
    hashrate = float(data[pool_name].get("total_hashrate",0))
    paid =  float(data[pool_name].get("payout_history", 0))
    shares = int(data[pool_name].get("round_shares",0))
    round_est = float(data[pool_name].get("round_estimate",0))
    balance = float(data[pool_name].get("confirmed_rewards",0))
    total = paid + balance
    print pool_name
    print "Date: "+data[pool_name]["time"].strftime("%Y-%m-%d %H:%M:%S")
    print "User: %s\tHashrate:\t %.2f kH/s\tRound shares:%d" % (username,(hashrate*1000), shares)
    print "Total paid:\t ", paid, settings["currency"]
    if ( "paid" in settings["estimates2"]):
         estimate_and_write( paid, settings, exchanges, exchange_info)
    print "Balance:\t ", balance, settings["currency"]
    if ( "balance" in settings["estimates2"]):
         estimate_and_write( balance, settings, exchanges, exchange_info)
    print "Grand total:\t ", total, settings["currency"]
    if ( "total" in settings["estimates2"]):
         estimate_and_write( total, settings, exchanges, exchange_info)
    print "Round estimate:\t ", round_est, settings["currency"]
    if ( "round_estimate" in settings["estimates2"]):
         estimate_and_write( round_est, settings, exchanges, exchange_info)

    if settings["simple_info"] == False:
        print "Workers:"
        for w in data[pool_name].get("workers",0):
            alive = "Alive"
            if data[pool_name]["workers"][w].get("alive",0) == "0":
                alive = "Off"
            print "\t%s\n\tHashrate: %sKh/s\t Status: %s" % (w, data[pool_name]["workers"][w].get("hashrate",0),alive)
