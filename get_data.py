import requests

def get_lastmonth():

    key = "178183dc6f485895635fb4affb118f429dafa499"
    
    data = requests.get("https://securenodes2.eu.zensystem.io/api/nodes/my/sumearnings?key=" + key).json()

    reward = round(float(data["rows"][len(data["rows"]) - 2]["zen"]), 2)

    return reward


def get_total():

    key = "178183dc6f485895635fb4affb118f429dafa499"
    
    data = requests.get("https://securenodes2.eu.zensystem.io/api/nodes/my/sumearnings?key=" + key).json()

    reward = round(float(data["totalzen"]), 2)

    return reward


def get_usdprice():
    
    zenbtc_price = requests.get("https://api.binance.com/api/v1/ticker/price?symbol=ZENBTC").json()["price"]
    btcusd_price = requests.get("https://api.binance.com/api/v1/ticker/price?symbol=BTCUSDT").json()["price"] 

    zenusd_price = float(zenbtc_price) * float(btcusd_price)

    return round(zenusd_price, 2)
