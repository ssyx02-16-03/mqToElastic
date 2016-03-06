from datetime import datetime
from elasticsearch import Elasticsearch

doc = {
    'author': 'kimchy',
    'text': 'Elasticsearch: cool. bonsai cool.',
    'timestamp': datetime.now(),
    }

class Elastic:
    def __init__(self,credentials):
        self.ip = credentials["elastic.ip"]
        self.port = credentials["elastic.port"]
        self.connecting = False
        self.connected = False

    def start(self):
        self.connect()
        self.refresh("_all")

    def connect(self):
         self.connecting = True
         print("[elastic] :connecting...")
         self.es = Elasticsearch(hosts=[{'host': self.ip, 'port': self.port}])

    def putIndex(self,putIndex,theBody):
        res = self.es.index(index=putIndex, doc_type='tweet', id=1, body=doc)
        print(res['created'])

    def getIndex(self,getIndex):
        res = self.es.get(index=getIndex, doc_type='tweet', id=1)
        print(res['_source'])

    def refresh(self,refIndex):
        self.es.indices.refresh(index=refIndex)
        print("[elastic] :connected!")
        print(self.es.info())
        self.connected = True

    def search(self,index,query):
        res = self.es.search(index="test-index",
                        body={
                            "query": {
                                "match_all": {}
                                }
                            })
        print("Got %d Hits:" % res['hits']['total'])
        for hit in res['hits']['hits']:
            print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])
        return res;
