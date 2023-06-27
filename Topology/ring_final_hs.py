from twisted.internet import protocol,reactor

class RingProtocol(protocol.Protocol):

    def __init__(self,factory):
        self.factory = factory #factory that stores the clients connected to the server 
        self.name = None       #name of the client that will connect to the server 
    def connectionMade(self):
        '''establishing a connection to the server'''

        print('New client connected: ',self.transport.getPeer())
        self.factory.clients.append(self)

    def connectionLost(self, reason):
        
        print("Client disconnected")
        index = self.factory.clients.index(self)  
        #getting the index of the client that is going to be removed 
        
        self.factory.clients[index]=None
        
    def dataReceived(self, data):
        message = data.decode().strip()

        if not self.name:
            self.name = message 
            print(self.name,' has connected to the server.')   
            #if the client has not connected to the server before 
            self.factory.names.append(self.name)

        else:
            if message.startswith('@'):                        
                '''one client will send message to another client '''
                recipient, private_message = message[1:].split(":", 1)
                receiver_index = self.factory.names.index(recipient)
                sender_index = self.factory.names.index(self.name)


                while sender_index != receiver_index:
                    sender_index += 1 
                    if sender_index == len(self.factory.names):
                        sender_index = 0
                    
                    if self.factory.clients[sender_index] is None:
                        '''the message can't be sent.'''
                        self.transport.write('link failure. message cannot be sent'.encode())
                        break 
                 
                    self.sendPrivateMessage(self.factory.names[sender_index], private_message)


            else:
                '''if destination not specified, the message is sent to the server.'''
                self.transport.write(message.encode())



    def sendPrivateMessage(self,recipient,message):
        for client in self.factory.clients:
            if client is not None:
                if client.name == recipient:
                    client.transport.write(f"(Private) {self.name}: {message}\n".encode())
                    break
        else:
            self.transport.write(f"Error: User {recipient} not found.\n".encode())


class RingFactory(protocol.Factory):

    def __init__(self):
        self.clients = []
        self.names = []
    def buildProtocol(self, addr):
        return RingProtocol(self)
    

if __name__ == "__main__":
    reactor.listenTCP(8080, RingFactory())
    print("Server started. Listening on port 8080...")
    print('''Enter client name to register. Enter @ before the starting of a message
          to send message to another client.''')
    reactor.run()
