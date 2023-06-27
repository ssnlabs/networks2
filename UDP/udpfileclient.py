from twisted.internet import protocol,reactor
import pickle
class echoclient(protocol.DatagramProtocol):
    def startProtocol(self):
        self.transport.connect('127.0.0.1',8045)
        self.sendDatagram()

    def sendDatagram(self):
        with open('file.txt','r+') as f:
            data = f.read()
            self.transport.write(pickle.dumps(data))
            print('File transferred')
            print('Connection lost')

reactor.listenUDP(0,echoclient())
reactor.run()