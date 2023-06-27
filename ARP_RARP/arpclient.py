from twisted.internet import protocol,reactor

class arpclient(protocol.Protocol):
    def connectionMade(self):
        ip = input('Enter ip adddr :')
        self.transport.write(ip.encode())

    def dataReceived(self, data):
        macaddr = data.decode()
        if macaddr is not None:
            print('Mac addr :',macaddr)
        else:
            print('Invalid ip addr')

class arpfactory(protocol.ClientFactory):
    def buildProtocol(self,addr):
        return arpclient()
    
    def clientConnectionLost(self, connector, reason):
        print('Connection lost')
        reactor.stop()

    def clientConnectionFailed(self, connector, reason):
        print('Connection failed')
        reactor.stop()

reactor.connectTCP('localhost',8995,arpfactory())
reactor.run()

