
from twisted.internet import protocol,reactor

class arpserver(protocol.Protocol):
    def __init__(self,table):
        self.table = table
    def connectionMade(self):
        print('Client connected')

    def dataReceived(self, data):
        ip = data.decode()
        mac = self.table[ip]
        if mac is not None:
            reply = f'Mac addr of {ip} is {mac}'
            self.transport.write(reply.encode())
        else:
            self.transport.write(f'{ip} is not valid.'.encode())

class arpfactory(protocol.Factory):
    def __init__(self, table):
        self.table = table
    def buildProtocol(self, addr):
        return arpserver(self.tables)
    
table = {}
table["192.168.1.1"] = "00:11:22:33:44:55"
factory = arpfactory(table)
reactor.listenTCP(9104,arpfactory())
reactor.run()
