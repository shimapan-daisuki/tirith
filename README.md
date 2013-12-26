tirith
======

Python console program for monitoring statistics from cryptocurrency pools and exchanges.

Found this useful/helpful? You can donate here:

mardilv aka shimapan.daisuki:
- btc:    1PkCFatY7jgxY8BFaZe1YeL1baa8G7tVuR
- ltc:    LdSgAUcFed3szKGSmYQgFcFJvw9HJyAsHP


features
========
now:
- highly configurable,
- shows all available info in 2 display modes,
- displays balances and estimates in multiple currencies,
- can use average and last exchange rates from multiple exchanges for estimating your balances,
- shows exchange rates for multiple exchanges
- supported exchanges as of this moment: BTC-E, Bitstamp, Mt.Gox, Cryptsy
- supported pools as of this moment: 
  - http://middlecoin.com [ middlecoin ]
  - any pool with site of this type: examples: https://ftc.d2.cc/ or  http://lite.coin-pool.com/ [ common ]
  - any pool with site of this type: example: http://fst.zabmail.ru/ [ alt ]

planned:
- adding support for not yed added pools and exchanges
- notifications/alarms
- usb lcd displays support
- GUI

how to use 
==========

To use this program you need Python 2.7 installed. You can get it from here:  http://www.python.org/download/releases/2.7/

Set configs as described in next section and run tirith.py from terminal or just double-click it.

configuration
=============
EDIT CONFIGS FILES CAREFULLY AS MISSING EVEN ONE  > , < or > " < OR ADDING ONE TOO MUCH WILL MAKE IT UNREADABLE FOR PROGRAM
Between any element in any bracket list should  appear > , < however there can't be any after the last element in the list, just look at example configs. Also most of it is case-sensitive so take this into consideration too.

There are 3 configs files: config.cfg.txt, pools.cfg.txt and exchanges.cfg.txt

config
======

example:

    {
    "blink":	0.1,
    "clear":	true
    }

  blink - switches display between pools and exchanges every x minutes
          accepts float value or false ( to turn it off )
          
  clear - clears the terminal before every refresh, this DOESN'T WORK IN IDLE SHELL and will be annoying if used while            running program in the IDLE shell, accepts:  true or false
    
pools
=====
example:

    {
    "update_interval": 	5,
    "use": 		true,
    "pools":
        {
        "Middlecoin":
            {	
            "display":      true,
            "currency":     "BTC",
            "wallet":       "1PkCFatY7jgxY8BFaZe1YeL1baa8G7tVuR",
            "adress":       "http://middlecoin.com/json",
            "webapi":       "middlecoin",
            "simple_info":  false,
    	"estimates":	["USD", "EUR", "JPY" ],
    	"estimates2":	[ "paid", "total", "unpaid" ]
            },
        "ftc.d2.cc":
            {	
            "display":      true,
            "currency":     "FTC",
            "adress":       "https://ftc.d2.cc/",
            "webapi":       "common",
            "api_key":      "580f22610cd0971fd8c453ddd9be854379ea7a22b8f5a5ddf9e680f2f9151340",
            "simple_info":  false,
    	"estimates":	["USD"],
    	"estimates2":	["paid", "total", "round_estimate", "balance"]
            },
        "fst2": 
            {	
            "display":      true,
            "currency":     "FST",
            "id":       	"718",
            "adress":       "http://fst.zabmail.ru/",
            "webapi":       "alt",
            "api_key":      "12cb383e95ede387b1d60a0c3bd1f062edaaee10a2aafbf00d647b1ca48ae57c",
    	"estimates":	["USD", "BTC"],
    	"estimates2":	["paid_out"]
            }
        }
    }
    
  "update_interval" - program will try to get updated data from pool every x minutes, accepts float value
  
  "use" - this option lets you to completely disable monitoring data from pools, accepts true of false
  
  "pools" - here you can add pools which info you want to display, depending on type of pool api different options are              available, however most are shared
  
      "display" - toogle displaying stats from this pool, accepts true or false
    
      "currency" - pool's coin used in balances, only use captalised label such as "BTC", "XPM" etc, accepts string 
      
      "webapi" - webapi 'type' used by site, enter as string, to check which one is used by your pool look at examples in features section available values as of this moment: middlecoin, common, alt
    
      "adress" - pool's adress, accepts string
      
      "estimates" - list of currencies to estimate balances to, input as list of captalised labels as shown in example
      
      "estimates2" - list of values to be estimated, available values depends on pool's api type listed below, input as shown
        alt: paid_out
        middlecoin: paid, unpaid, total, exchanged, unexchanged, immature
        common: paid, total, balance, round_estimate
  
      "api_key" - used in every type of pool other than middlecoin, you can find it in you account's information on pool's site dashboard after logging in, input as string, available only for types: alt, common
      
      "id" - used for alt type pools, you can find it in you account's information on pool's site dashboard after logging in, input as string, available only for types: alt
      "wallet" - atm used only to display info from middlecoin, input your wallet adress which acts as your worker username
      
      "simple_info" - depending on this a little less info will be displayed, accepts true or false, available only for types: middlecoin, common
      

exchanges
=========

example:

    {
    "update_interval":	1,
    "use":			true,
    "exchangesFIAT":
        {
        "BTC-E":
            {	
            "display":          true,
            "simple_info":      true,
            "estimate_mode":    "last",
    	"FIAT":  [
    		"USD", "EUR"
    		],
            "coins": [
                "BTC", "LTC"
                	],
     	"webapi":           "BTC-E"
            },
        "Mt.Gox":
            {	
            "display":          true,
            "simple_info":      false,
    	"estimate_mode":    "average",
            "FIAT":  [
    		"JPY"
    		],
            "coins": [
                "BTC"
                	],
    	"webapi":           "Mt.Gox"
            },
        "Bitstamp":
            {	
            "display":          true,
            "simple_info":      true,
    	"estimate_mode":    "last",
            "FIAT":  [
    		"USD"
    		],
            "coins": [
                "BTC"
                	],
    	"webapi":           "Bitstamp"
            },
        
        "Cryptsy":
            {	
            "display":          true,
            "simple_info":      true,
    	"rates":  {
    		"FST":"BTC", "LTC":"BTC"
    		},
    	"webapi":           "Cryptsy",
    	"estimate_mode":    "last"
    
            }
        
        }  
      
    }
    
unlike pools, exchanges have distinct apis so you can't add any in this file unless module for its api has been added to program

"update\_interval", "use", "display" and "simple\_info" usage same as in pools cfg

aside from that only configurable things are:
  
  "estimate_mode" - which value will be used for estimating value in other currency, differs for exchanges
    Cryptsy: last
    BTC-E: average, last, low, high
    Bitstamp: average, last, low, high
    
    
      
      
