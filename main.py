import activeMQConnect
from elastic import Elastic

def getCredentials():
    import json
    from pprint import pprint

    with open('pass.json') as data_file:
      passPort = json.load(data_file)
    return passPort;

thePass = getCredentials()
el = Elastic(thePass)

activeMQConnect.start(thePass)
el.start()
el.getIndex("testing")
el.putIndex("testing","hey hallo")
el.getIndex("testing")
