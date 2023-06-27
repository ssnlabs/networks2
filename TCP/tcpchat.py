from twisted.internet import reactor, protocol
from twisted.protocols.basic import LineOnlyReceiver

class ChatProtocol(LineOnlyReceiver):
    def __init__(self, factory):
        self.factory = factory
        self.name = None
        self.state = "GETNAME"

    def connectionMade(self):
        self.sendLine("What's your name?".encode())

    def connectionLost(self, reason):
        if self.name in self.factory.users:
            del self.factory.users[self.name]
            self.broadcastMessage(f"{self.name} has left the chat room.")

    def lineReceived(self, line):
        if self.state == "GETNAME":
            self.handle_GETNAME(line)
        else:
            self.handle_CHAT(line)

    def handle_GETNAME(self, name):
        if name in self.factory.users:
            self.sendLine("Name already taken, please choose another name.".encode())
            return
        self.sendLine(f"Welcome, {name}!".encode())
        self.broadcastMessage(f"{name} has joined the chat room.")
        self.name = name
        self.factory.users[name] = self
        self.state = "CHAT"

    def handle_CHAT(self, message):
        message = f"<{self.name}> {message}"
        self.broadcastMessage(message)

    def broadcastMessage(self, message):
        for name, protocol in self.factory.users.items():
            if protocol != self:
                protocol.sendLine(message.encode())

class ChatFactory(protocol.Factory):
    def __init__(self):
        self.users = {}

    def buildProtocol(self, addr):
        return ChatProtocol(self)

if __name__ == "__main__":
    reactor.listenTCP(8200, ChatFactory())
    reactor.run()