#!/usr/bin/python2
# -*- coding: cp1250 -*-
#this function gets info data from d2cc json about wallet and puts it in
#passed dictionary /data/ under pools name
import httplib, socket
from httplib import HTTPConnection, HTTPS_PORT
import ssl

class HTTPSConnection(HTTPConnection):
    "This class allows communication via SSL."
    default_port = HTTPS_PORT

    def __init__(self, host, port=None, key_file=None, cert_file=None,
            strict=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT,
            source_address=None):
        HTTPConnection.__init__(self, host, port, strict, timeout,
                source_address)
        self.key_file = key_file
        self.cert_file = cert_file

    def connect(self):
        "Connect to a host on a given (SSL) port."
        sock = socket.create_connection((self.host, self.port),
                self.timeout, self.source_address)
        if self._tunnel_host:
            self.sock = sock
            self._tunnel()
        # this is the only line we modified from the httplib.py file
        # we added the ssl_version variable
        self.sock = ssl.wrap_socket(sock, self.key_file, self.cert_file, ssl_version=ssl.PROTOCOL_TLSv1)

#now we override the one in httplib
httplib.HTTPSConnection = HTTPSConnection
# ssl_version corrections are done
import urllib2, json, datetime, os, time,traceback
from lib import middlecoin, btcef, common, alt, mtgox, bitstamp, cryptsy
from fractions import gcd
######################################################
#   Found this useful/helpful? Donate here:
#   mardilv
#   btc:    1PkCFatY7jgxY8BFaZe1YeL1baa8G7tVuR
#   ltc:    LdSgAUcFed3szKGSmYQgFcFJvw9HJyAsHP
######################################################
runningFlag = True
#dictionaries for storing info
exchange_info = dict() 
pool_info = dict()
#load configs:
try:
    pools = dict()
    pools = open("pools.cfg.txt", "r")
    pools = json.loads( pools.read() )
    exchanges = dict()
    exchanges = open("exchanges.cfg.txt", "r")
    exchanges = json.loads( exchanges.read() )
    config = dict()
    config = open("config.cfg.txt", "r")
    config = json.loads( config.read() )
except:
    print "Error in config files"
    runningFlag = False
    
    


#handling different webapis while updating and dsiplaying info
def update( name, webapi, what_do ):
    funcdict_p = {
        'middlecoin':middlecoin,
        'common':common,
        'alt':alt
        }
    funcdict_e = {
        'BTC-E':btcef,
        'Mt.Gox':mtgox,
        'Bitstamp':bitstamp,
        'Cryptsy':cryptsy
        }

    if ((webapi in funcdict_p) == False):
        if ((webapi in funcdict_e) == False):
            return -1
        else:
            if what_do == "data":
                funcdict_e[webapi].update( name, exchanges["exchangesFIAT"][name], exchange_info)
                return 1
            elif what_do == "display":
                if name in exchange_info:
                    if exchange_info[name].keys() > 0:
                        funcdict_e[webapi].display( name , exchange_info, exchanges["exchangesFIAT"][name]["simple_info"])
                        return 1
    else:    
        if what_do == "data":
            funcdict_p[webapi].update( name , pools["pools"][name], pool_info)
            return 1
        elif what_do == "display":
            if name in pool_info:
                if pool_info[name].keys() > 0:
                    funcdict_p[webapi].display( name ,pools["pools"][name], pool_info, exchanges, exchange_info )
                    return 1



pool_checktime_counter = float(0)
ex_checktime_counter = float(0)


sleeptime = float(gcd(float(pools["update_interval"]), float(exchanges["update_interval"])))
if (config["blink"] != False):
    blink_time = float(config["blink"])
    sleeptime = float(blink_time)
else:
    blink_time = 0
    
to_clear_or_not_to_clear = config["clear"]
display = "Exchanges"

while runningFlag:
    
    if (ex_checktime_counter <= 0):
        print "Updating exchanges data..."
        if (exchanges["use"] == True):
            #going trough all our exchanges in config checking if they're
            #set to be displayed
            for i in exchanges["exchangesFIAT"]:
                if exchanges["exchangesFIAT"][i]["display"]:
            #if it is, we update it
                    if update( i, exchanges["exchangesFIAT"][i]["webapi"], "data" ) == -1:
                        print "Error: webapi for %s not recognized x" % i
            ex_checktime_counter = float(exchanges["update_interval"])

    if (pool_checktime_counter <= 0):
        print "Updating pools data..."
        if(pools["use"] == True):
            #going trough all our pools in config checking if they're
            #set to be displayed
            for i in pools["pools"]:
                if pools["pools"][i]["display"]:
            #if it is, we update it
                    if update( i, pools["pools"][i]["webapi"], "data" ) == -1:
                        print "Error: webapi for %s not recognized p" % i
            pool_checktime_counter = float(pools["update_interval"])
            

    if to_clear_or_not_to_clear:
        os.system('cls' if os.name=='nt' else 'clear')
   
    #and then display updated info
    if (display == "Exchanges") or ( blink_time == 0):
        for i in exchanges["exchangesFIAT"]:                  
                if update( i, exchanges["exchangesFIAT"][i]["webapi"], "display" ) == -1:
                    print "Error: webapi for %s not recognized y" % i
                print "\n"
    if (display == "Pools") or ( blink_time == 0):
        for i in pools["pools"]:
                if update( i, pools["pools"][i]["webapi"], "display" ) == -1:
                    print "Error: webapi for %s not recognized q" % i
                print "\n"
                     
    pool_checktime_counter -= sleeptime
    ex_checktime_counter -= sleeptime
    if display == "Exchanges":
        display = "Pools"
    else:
        display = "Exchanges"
    time.sleep(sleeptime*60)
