import urllib2, ssl
import json, estimate, datetime
def update( pool_name, settings, data ):
#gettin json
    adress = settings["adress"]+"index.php?page=api&action=getuserstatus&api_key="+settings["api_key"]+"&id="+settings["id"]
    hdr = {'User-Agent':'Mozilla/5.0'}
    try:
        req = urllib2.Request(adress,headers=hdr)
        response = urllib2.urlopen(req)
        alt_json = json.loads(response.read())
        response.close()
    except:
        print "Ran into problem while trying to update %s info, will try again at next update interval" % pool_name
        return -1
    data[pool_name] = alt_json["getuserstatus"]["data"]
    timestamp = datetime.datetime.now()
#time   
    data[pool_name]["time"] = timestamp

#this one displays info from alt webapi
#which is stored in dictionary /data/
def estimate_and_write( balance, settings, exchanges, exchange_info ):
    est = dict()
    for j in settings["estimates"]:
        est[j] = estimate.to_FIAT( balance, settings["currency"], j, exchanges, exchange_info)
    for j in est:
        for z in est[j]:
            print "\t\t\t= %.8f %s @%s %s" % ( est[j][z]["est"], j, z, est[j][z]["mode"])
  
def display( pool_name, settings, data, exchanges, exchange_info ):
    username = data[pool_name].get("username",0)
    hashrate = float(data[pool_name].get("hashrate",0))
    sharerate = float(data[pool_name].get("sharerate",0))
    paid_out =  float(data[pool_name]["transactions"].get("Debit_AP", 0))
    shares_valid = int(data[pool_name].get("valid",0))
    shares_invalid = float(data[pool_name].get("invalid",0))
    if (shares_valid+shares_invalid) > 0:
        efficiency = shares_valid/(shares_valid+shares_invalid)
    else:
        efficiency = 0
    print pool_name
    print "Date: "+data[pool_name]["time"].strftime("%Y-%m-%d %H:%M:%S")
    print "User: %s\tHashrate:\t %.2f kH/s\tSharerate: %.2f%%" % (username,(hashrate*1000), sharerate)
    print "Shares valid: %d\t invalid: %d\t Efficiency: %.2f" % ( shares_valid, shares_invalid, efficiency)
    print "Total paid:\t ", paid_out, settings["currency"]
    if ( "paid_out" in settings["estimates2"]):
         estimate_and_write( paid_out, settings, exchanges, exchange_info)
   
