def elastic():
    class elastic():
        from datetime import datetime
        from elasticsearch import Elasticsearch
        import main

        def __init__(self):
            self.es = undefined
            self.creds = getCredentials();
            self.connecting = false;

        def init(self):
            connect()
            refresh('_all')

        def connect(self):
             connecting = True
             es = Elasticsearch([('localhost',9200)])

        def putIndex(self,index,theBody):
            res = es.index(index="test-index", doc_type='tweet', id=1, body=theBody)
            print(res['created'])

        def getIndex(self,index):
            res = es.get(index="test-index", doc_type='tweet', id=1)
            print(res['_source'])

        def refresh(self,index):
            es.indices.refresh(index=index)

        def search(self,index,query):
            res = es.search(index="test-index",
                            body={
                                "query": {
                                    "match_all": {}
                                    }
                                })
            print("Got %d Hits:" % res['hits']['total'])
            for hit in res['hits']['hits']:
                print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])
            return res;
