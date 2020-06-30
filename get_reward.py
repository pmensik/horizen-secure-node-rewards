import requests

def get_reward():

    key = "178183dc6f485895635fb4affb118f429dafa499"
    
    data = requests.get("https://securenodes2.eu.zensystem.io/api/nodes/my/sumearnings?key=" + key).json()
    
    last_month = data["rows"][len(data["rows"]) - 2]

    reward = last_month["zen"]

    return reward
