#this function gets info data from mdc json about wallet and puts it in
#passed dictionary /data/ under pools name
import urllib2, datetime
import json
from decimal import *

markets = [["FRK", "BTC",  "33"], ["CGB", "BTC",  "70"], ["FRC", "BTC",  "39"], ["SBC", "BTC",  "51"], ["BTB", "BTC",  "23"], ["PPC", "LTC",  "125"], ["ANC", "BTC",  "66"], ["UNO", "BTC",  "133"], ["GLC", "BTC",  "76"], ["ASC", "XPM",  "112"], ["IXC", "BTC",  "38"], ["MEC", "BTC",  "45"], ["DOGE", "LTC",  "135"], ["YAC", "BTC",  "11"], ["WDC", "LTC",  "21"], ["MST", "LTC",  "62"], ["CMC", "BTC",  "74"], ["Points", "BTC",  "120"], ["XNC", "LTC",  "67"], ["CPR", "LTC",  "91"], ["NET", "BTC",  "134"], ["ADT", "LTC",  "94"], ["BTG", "BTC",  "50"], ["CRC", "BTC",  "58"], ["XJO", "BTC",  "115"], ["EMD", "BTC",  "69"], ["TAG", "BTC",  "117"], ["NVC", "BTC",  "13"], ["FTC", "BTC",  "5"], ["QRK", "BTC",  "71"], ["DBL", "LTC",  "46"], ["PHS", "BTC",  "86"], ["PTS", "BTC",  "119"], ["NEC", "BTC",  "90"], ["ZET", "BTC",  "85"], ["CAP", "BTC",  "53"], ["PPC", "BTC",  "28"], ["SPT", "BTC",  "81"], ["TRC", "BTC",  "27"], ["CENT", "LTC",  "97"], ["LTC", "BTC",  "3"], ["SRC", "BTC",  "88"], ["BUK", "BTC",  "102"], ["CSC", "BTC",  "68"], ["GLD", "BTC",  "30"], ["AMC", "BTC",  "43"], ["TIX", "LTC",  "107"], ["RYC", "LTC",  "37"], ["CNC", "BTC",  "8"], ["MEM", "LTC",  "56"], ["DGC", "BTC",  "26"], ["ORB", "BTC",  "75"], ["LKY", "BTC",  "34"], ["XPM", "BTC",  "63"], ["MNC", "BTC",  "7"], ["DVC", "LTC",  "52"], ["ADT", "XPM",  "113"], ["ARG", "BTC",  "48"], ["JKC", "LTC",  "35"], ["NRB", "BTC",  "54"], ["DEM", "BTC",  "131"], ["ELP", "LTC",  "93"], ["GLD", "LTC",  "36"], ["HBN", "BTC",  "80"], ["IFC", "LTC",  "60"], ["CGB", "LTC",  "123"], ["RED", "LTC",  "87"], ["WDC", "BTC",  "14"], ["ELC", "BTC",  "12"], ["XPM", "LTC",  "106"], ["DGC", "LTC",  "96"], ["DVC", "XPM",  "122"], ["GDC", "BTC",  "82"], ["COL", "LTC",  "109"], ["PXC", "LTC",  "101"], ["PYC", "BTC",  "92"], ["EZC", "LTC",  "55"], ["ANC", "LTC",  "121"], ["NET", "LTC",  "108"], ["CLR", "BTC",  "95"], ["ASC", "LTC",  "111"], ["FST", "BTC",  "44"], ["KGC", "BTC",  "65"], ["SBC", "LTC",  "128"], ["LK7", "BTC",  "116"], ["FST", "LTC",  "124"], ["ZET", "LTC",  "127"], ["TEK", "BTC",  "114"], ["MEC", "LTC",  "100"], ["BTE", "BTC",  "49"], ["CNC", "LTC",  "17"], ["TIX", "XPM",  "103"], ["SXC", "LTC",  "98"], ["QRK", "LTC",  "126"], ["NET", "XPM",  "104"], ["DMD", "BTC",  "72"], ["NMC", "BTC",  "29"], ["GME", "LTC",  "84"], ["COL", "XPM",  "110"], ["TGC", "BTC",  "130"], ["NBL", "BTC",  "32"], ["IFC", "XPM",  "105"], ["ALF", "BTC",  "57"], ["PXC", "BTC",  "31"], ["DOGE", "BTC",  "132"], ["FLO", "LTC",  "61"], ["BQC", "BTC",  "10"], ["YAC", "LTC",  "22"], ["CENT", "XPM",  "118"], ["GLX", "BTC",  "78"], ["BET", "BTC",  "129"]]

def update( name, settings, data ):
#gettin json for every pair and adding it to dict /data/
    if (name in data) == False:
        data[name] = dict()
        #for every rate set to be displayed
        for p in settings["rates"]:

            #we look through marketslist
            for z in range(len(markets)):
                #if we find it there we add it to dada if it isn't there already
                if markets[z][0] == p:
                    a = p
                    b = markets[z][1]
                    if (a in data[name]) == False:
                        data[name][a] = dict()
                        #then we look further for the second currency
                        if (b in data[name][a]) == False:
                            data[name][a][b] = dict()
                            try:
                                adress = "http://pubapi.cryptsy.com/api.php?method=singlemarketdata&marketid=%s" % markets[z][2]
                                response = urllib2.urlopen(adress)
                                cryptsy = json.loads(response.read())
                                response.close()  
                            except:
                                print "Ran into problem while trying to update %s %s/%s info, will try again at next update interval" % (name, a,b)
                                return -1
                            data[name][a][b]["last"] = float( cryptsy["return"]["markets"][a]["lasttradeprice"])
                            data[name][a][b]["timestamp"] = cryptsy["return"]["markets"][a]["lasttradetime"]
                                                 

#closing connection
        

#this one displays info from middlecoin webapi
#which is stored in dictionary /data/
def display( exchange_name , data, simple ):
    print exchange_name
    for f in data[exchange_name]:
        for v in data[exchange_name][f]:
            print "\tDate: %s\n%s\tLast: \t%.8f %s" % (data[exchange_name][f][v]["timestamp"],f,data[exchange_name][f][v]["last"],v)
            
