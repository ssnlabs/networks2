from twisted.internet import protocol,reactor

class echoclient(protocol.DatagramProtocol):
    def startProtocol(self):
        self.transport.connect('127.0.0.1',8038)
        self.sendDatagram()

    def sendDatagram(self):
        flag = input('Do you want to send a message(y/n) :')
        if flag=='y':
            txt = input('Enter message :')
            self.transport.write(txt.encode())
            self.sendDatagram()     #if again wants to send txt
        else:
            self.transport.write('CL'.encode())
            self.transport.stopListening()

reactor.listenUDP(0,echoclient())
reactor.run()        