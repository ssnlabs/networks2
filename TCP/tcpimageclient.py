from twisted.internet import protocol,reactor

class fileclient(protocol.Protocol):
    def connectionMade(self):
        print('Connected to server')
        with open('/home/aasish/Documents/modelcodess/img.jpg','rb') as f:
            self.transport.write(f.read())

    def dataReceived(self,data):
    
        print(data.decode())

class fileclientfactory(protocol.ClientFactory):
    def buildProtocol(self,addr):
        return fileclient()

    def clientConnectionFailed(self, connector, reason):
        print ("Connection failed.")
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print ("Connection lost.")
        reactor.stop()

reactor.connectTCP("localhost",8700,fileclientfactory())
reactor.run()
