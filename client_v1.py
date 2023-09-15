import Pyro4

def main():
    
    server_uri = "PYRO:obj_4143c4562b2a4f16af396607ecc0e048@localhost:61174"

    
    remote_object = Pyro4.Proxy(server_uri)

    try:
        name = input("Enter your name: ")
        result = remote_object.say_hello(name)
        print("Server response:", result)
    except Pyro4.errors.CommunicationError as e:
        print("Error communicating with the server:", e)
    except Pyro4.errors.PyroError as e:
        print("Pyro4 error:", e)

if __name__ == "__main__":
    main()
