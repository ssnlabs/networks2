
from twisted.internet import protocol,reactor

class echoclient(protocol.Protocol):
    def connectionMade(self):
        msg = input("Enter message to be send to server - ")
        self.transport.write(msg.encode())
        
    def dataReceived(self,data):
        print(data.decode())
        self.transport.loseConnection()
        
class clientfactory(protocol.ClientFactory):
    def buildProtocol(self,addr):
        return echoclient()
    
    def clientConnectionFailed(self, connector, reason):
        print ("Connection failed.")
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print ("Connection lost.")
        reactor.stop()
    
    
reactor.connectTCP("localhost",8000,clientfactory())
reactor.run()





















