from twisted.internet import protocol,reactor

class fileserver(protocol.Protocol):
    def connectionMade(self):
        print("Connected to client")
    
    def dataReceived(self,data):
        with open('receivedfile.txt','w+') as f:
            f.write(data.decode())

        txt = "File as been transferred and saved as 'receivedfile.txt' "
        self.transport.write(txt.encode())

class fileserverfactory(protocol.Factory):
    def buildProtocol(self, addr):
        return fileserver()
    
reactor.listenTCP(8600,fileserverfactory())
reactor.run()