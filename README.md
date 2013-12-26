tirith
======

Python console program for monitoring statistics from cryptocurrency pools and exchanges.

Found this useful/helpful? You can donate here:
mardilv aka shimapan.daisuki
  btc:    1PkCFatY7jgxY8BFaZe1YeL1baa8G7tVuR
  ltc:    LdSgAUcFed3szKGSmYQgFcFJvw9HJyAsHP


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
  - middlecoin
  - any pool with site of this type: examples: https://ftc.d2.cc/ or  http://lite.coin-pool.com/
  - any pool with site of this type: example: http://fst.zabmail.ru/

planned:
- adding support for not yed added pools and exchanges
- notifications/alarms
- usb lcd displays support
- GUI
- 
how to use 
==========

To use this program you need Python 2.7 installed. You can get it from here:  http://www.python.org/download/releases/2.7/
Set configs as described in next section and run tirith.py from terminal or just double-click it.

configuration
=============
EDIT CONFIGS FILES CAREFULLY AS MISSING EVEN ONE , or " OR ADDING ONE TOO MUCH WILL MAKE IT UNREADABLE FOR PROGRAM
There are 3 configs files: config.cfg.txt, pools.cfg.txt and exchanges.cfg.txt

config.cfg
  options:
    blink - switches display between pools and exchanges every x minutes
            accepts:  float value  
                      false = to turn off
            default value 0.05
    clear - clears the terminal before every refresh, this DOESN'T WORK IN IDLE SHELL and will be annoying if used while             running program in the IDLE shell
            accepts:  true
                      false
  
