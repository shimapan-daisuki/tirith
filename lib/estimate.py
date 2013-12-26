def to_FIAT(value, a, b, exchanges, exchange_info ):
    estimates = dict()
    for o in exchange_info:
    
        mode = exchanges["exchangesFIAT"][o]["estimate_mode"]
        if a in exchange_info[o]:
        
            if b in exchange_info[o][a]:
                if (o in estimates) == False:
                    estimates[o] = dict()
                estimates[o]["est"] = float(exchange_info[o][a][b].get(mode,0)*value)
                estimates[o]["mode"] = mode
        #else:
           # estimates["Error:Not enough data to estimate."] = dict()
           # estimates["Error:Not enough data to estimate."]["est"] = 0
           # estimates["Error:Not enough data to estimate."]["mode"] = "Error."
    return estimates
