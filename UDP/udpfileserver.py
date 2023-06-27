from twisted.internet import protocol,reactor
import pickle
class echoserver(protocol.DatagramProtocol):

    def datagramReceived(self, datagram: bytes, addr):
        with open('receivedudpfile.txt','a+') as f:
            f.write(pickle.loads(datagram))

        print('File received')
        print('Connection lost')
        reactor.stop()

reactor.listenUDP(8045,echoserver())
reactor.run()
