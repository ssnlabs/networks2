from twisted.internet import reactor, protocol
import time

class RTTClient(protocol.Protocol):
    def connectionMade(self):
        print("connected to server:")
        self.start=time.time()
        self.transport.write(b'hello')
    def dataReceived(self, data: bytes):
        print("recieved from server:",str(data))
        self.end=time.time()
        self.transport.loseConnection()
        print("tcp-rtt:",self.end-self.start)
    # def connectionLost(self, reason):
    #     print
class RTTC(protocol.ClientFactory):
    def buildProtocol(self, addr):
        return RTTClient()
    def clientConnectionFailed(self, connector, reason):
        print("connection failed")
        reactor.stop()
    def clientConnectionLost(self, connector, reason):
        print("connection lost")
        reactor.stop()
reactor.connectTCP("localhost",8000,RTTC())
reactor.run()