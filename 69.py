class ClientList(list):
    def search_email(self,value):
        result = [client for client in self if value in client.email]
        return result


class Client:
    all_clients = ClientList()

    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.all_clients.append(self)


    def __repr__(self):
        return f"Client(name='{self.name}',email='{self.email}')"


client1 = Client('Tom','sample@gmail.com')
client2 = Client('Donlad','sales@gmail.com')
client3 = Client('Mike','sales@gmail.com')
client4 = Client('Lisa','info@gmail.com')


result = [client.name for client in Client.all_clients.search_email('sales')]
print(result)
