import Pyro4


@Pyro4.expose
class MyRemoteObject:
    def say_hello(self, name):
        return f"Hello, {name}!"

def main():
    
    remote_object = MyRemoteObject()

    
    with Pyro4.Daemon() as daemon:
        uri = daemon.register(remote_object)

        
        print("URI:", uri)

        
        daemon.requestLoop()

if __name__ == "__main__":
    main()
