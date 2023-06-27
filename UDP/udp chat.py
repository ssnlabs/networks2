from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

class ChatServer(DatagramProtocol):
    def __init__(self):
        self.users = {} # maps user addresses to usernames

    def datagramReceived(self, data, addr):
        message = data.decode().strip()
        if addr in self.users:
            # if the user is already registered, broadcast the message to all other users
            username = self.users[addr]
            message = f"<{username}> {message}"
            for user_addr in self.users:
                if user_addr != addr:
                    self.transport.write(message.encode(), user_addr)
        else:
            # if the user is not registered, use the first message as their username
            self.users[addr] = message.split()[0]
            self.transport.write("Welcome to the chat!\n".encode(), addr)

if __name__ == "__main__":
    reactor.listenUDP(5008, ChatServer())
    print("Server started.")
    reactor.run()
