def stompIt(ip,port,user,password):
    import time
    import stomp

    connecting = False
    connected = False
    conn = stomp.Connection([(ip,port)])

    class theListener(stomp.ConnectionListener): #class(ancestor)

        def on_connected(self,headers,body):
            print('[stomp]:thats right! were online!')
            connected = True;
            connecting = False;
            conn.subscribe(destination='/topic/akutenpatients', id=1, ack='auto')
            conn.subscribe(destination='/topic/akutenevents', id=1, ack='auto')
        def on_disconnected(self):
            print("[stomp]: disconnected")
        def on_error(self, headers, message):
            print('[stomp]: received an error "%s"' % message)
        def on_message(self, headers, message):
            print('[stomp]: received a message "%s"' % message)

    def connect():
        connecting = True
        print("[stomp]: connecting")
        conn.set_listener('', theListener())
        conn.start()
        conn.connect(user,password, wait=True)

#the run:
    connect()

def start(passPort):
    stompIt(passPort["stomp.ip"],passPort["stomp.port"],passPort["stomp.user"],passPort["stomp.pass"])
    return;
