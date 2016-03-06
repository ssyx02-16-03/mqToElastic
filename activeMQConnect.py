def stompIt(ip,port,user,password):
    import time
    import stomp

    connecting = False
    connected = False

    class theListener(stomp.ConnectionListener):
        def on_error(self, headers, message):
            print('received an error "%s"' % message)
        def on_message(self, headers, message):
            connected = True;
            connecting = False;
            print('[stomp]:thats right! were online!')
            print('[stomp]:received a message "%s"' % message)

    def connect():
        conn = stomp.Connection([(ip,port)])
        conn.set_listener('', theListener())
        conn.start()
        conn.connect(user,password, wait=True)
        return conn;

    connecting = True
    conn = connect()
    conn.subscribe(destination='/topic/akutenpatients', id=1, ack='auto')
    conn.subscribe(destination='/topic/akutenevents', id=1, ack='auto')
    conn.subscribe(destination='/topic/ElvisSnapShot', id=1, ack='auto')


    conn.send(body='hello!', destination='/topic/ElvisSnapShot')

    while connecting:
        time.sleep(99)

    while connected:
        time.sleep(2)

    conn.disconnect()
    return;

def start():
    print("yey!")
    passPort = getCredentials()
    print(passPort)
    stompIt(passPort["stomp.ip"],passPort["stomp.port"],passPort["stomp.user"],passPort["stomp.pass"])
    return;
