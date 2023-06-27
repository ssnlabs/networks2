from twisted.internet import protocol,reactor

class echoserver(protocol.Protocol):
    def dataReceived(self,data):
        print('Client connected')
        print('Message by client - ',data.decode())
        ack = f'{"Server recieved - " + data.decode()}'
        self.transport.write(ack.encode())
        
class echofactory(protocol.Factory):
    def buildProtocol(self,addr):
        return echoserver()
    
reactor.listenTCP(8000,echofactory())
reactor.run()        





















