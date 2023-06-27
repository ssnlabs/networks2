from twisted.internet import reactor,protocol
import time
class RTTs(protocol.Protocol):
    def connectionMade(self):
        print("client connected")
    def dataReceived(self, data):
        print("recieved data:",data)
        self.transport.write(data)
    def connectionLost(self, reason):
        print("client removed")
        return

class RTT(protocol.Factory):
    def buildProtocol(self, addr):
        return RTTs()

reactor.listenTCP(8000,RTT())
reactor.run()