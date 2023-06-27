from twisted.internet import protocol,reactor

class echoserver(protocol.DatagramProtocol):
    def datagramReceived(self, datagram: bytes, addr):
        datagram = datagram.decode()
        if datagram=="CL":
            print('Connection lost')
            self.transport.stopListening()
        else:
            print('Message from client - ',datagram)

reactor.listenUDP(8038,echoserver())
reactor.run()
