# mqToElastic
A python module which reads from activeMQ and writes to ElasticSearch

##required python modules:

..json(to load password file)

..stomp (in our case to communicate with active MQ)
https://pypi.python.org/packages/source/s/stomp.py/stomp.py-4.1.9.tar.gz#md5=fe2ae033fbaf6541d8909ce7af5e45f4


..elasticSearch

##required password file <br />
```
{
  "stomp.ip" : "localhost",
  "stomp.port" : "61613",
  "elastic.ip" : "localhost",
  "elastic.port" : "9200"
}
```
