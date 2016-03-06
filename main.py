import activeMQConnect
from elastic import elastic
el = elastic();

def getCredentials():
    import json
    from pprint import pprint

    with open('pass.json') as data_file:
      passPort = json.load(data_file)
    return passPort;

#activeMQConnect.start()
el.init()
