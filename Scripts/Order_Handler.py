from fastapi import FastAPI
import json
import datetime
#############################################################
# The API that handles incoming orders. Your code goes here #
#############################################################

'''
strategies.json - it contains data about strategies and corresponding instruments
stocks.json - it contains data about purchased stocks and not yet sold
orders.json - it contains order log i.e every buy/sell with date time
'''

def initialize_db():
    '''
    Creates jsons if does not exists.
    '''
    with open("../Jsons/user_profile.json") as f:
        user_profile = json.load(f)
    strategies = {}
    for strats in user_profile.values():
        for key,val in strats.items():
            strategies[key] = val
    with open("../Jsons/strategies.json",'w') as f:
        json.dump(strategies,f,indent=4)
        f.close()
    stocks = {}
    with open("../Jsons/stocks.json",'w') as f:
        json.dump(stocks,f,indent=4)
        f.close()
    orders = {}
    with open("../Jsons/orders.json",'w') as f:
        json.dump(orders,f,indent=4)
        f.close()
        
app = FastAPI()
initialize_db()

@app.post("/create_order")
def process_payload(payload: dict):
    '''
    Places order i.e buy/sell request
    '''
    # loading strategies, stocks, orders info
    with open("../Jsons/strategies.json") as f:
        strategies = json.load(f)
    with open("../Jsons/stocks.json") as f:
        stocks = json.load(f)
    with open("../Jsons/orders.json") as f:
        orders = json.load(f)
        
    strategy = payload["STRATEGY"]
    instrument = payload["INSTRUMENT"]
    position = payload["POSITION"]
    # validating instrument and strategy from payload
    try:
        if(instrument not in strategies[strategy]):
            return {"RESPONSE": "REJECTED"}
    except:
        return {"RESPONSE":"REJECTED"}
    # if sell request
    if(position=="SELL"):
        try:
            if(instrument in stocks[strategy]):
                stocks[strategy].remove(instrument)
                if(stocks[strategy]==[]):
                    del stocks[strategy]
                orders[len(orders)] = {"STRATEGY":strategy,"INSTRUMENT":instrument,"POSITION":position,"DATETIME":str(datetime.datetime.now())}
                # writes back to json file
                with open("../Jsons/stocks.json",'w') as f:
                    json.dump(stocks,f,indent=4)
                    f.close()
                with open("../Jsons/orders.json",'w') as f:
                    json.dump(orders,f,indent=4)
                    f.close()    
                return {"RESPONSE":"ACCEPTED"}
        except:
            pass
        return {"RESPONSE":"REJECTED"}
    # if sell request
    if(position=="BUY"):
        try:
            if(instrument in stocks[strategy]):
                return {"RESPONSE":"REJECTED"}
            stocks[strategy].append(instrument)
            orders[len(orders)] = {"STRATEGY":strategy,"INSTRUMENT":instrument,"POSITION":position,"DATETIME":str(datetime.datetime.now())}
            with open("../Jsons/stocks.json",'w') as f:
                json.dump(stocks,f,indent=4)
                f.close()
            with open("../Jsons/orders.json",'w') as f:
                json.dump(orders,f,indent=4)
                f.close()    
            return {"RESPONSE":"ACCEPTED"}
        except:
            stocks[strategy] = [instrument]
            orders[len(orders)] = {"STRATEGY":strategy,"INSTRUMENT":instrument,"POSITION":position,"DATETIME":str(datetime.datetime.now())}
            with open("../Jsons/stocks.json",'w') as f:
                json.dump(stocks,f,indent=4)
                f.close()
            with open("../Jsons/orders.json",'w') as f:
                json.dump(orders,f,indent=4)
                f.close()
            return {"RESPONSE":"ACCEPTED"}
    else:
        return {"RESPONSE":"ACCEPTED"}