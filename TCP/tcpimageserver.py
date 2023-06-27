from twisted.internet import protocol,reactor

class fileserver(protocol.Protocol):
    def connectionMade(self):
        print("Connected to client")
    
    def dataReceived(self,data):
        with open('receivedimage.jpg','wb') as f:
            f.write(data)

        txt = "File as been transferred and saved as 'receivedimage.jpg' "
        self.transport.write(txt.encode())

class fileserverfactory(protocol.Factory):
    def buildProtocol(self, addr):
        return fileserver()
    
reactor.listenTCP(8700,fileserverfactory())
reactor.run()